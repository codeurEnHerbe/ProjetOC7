import dash
from dash import html, dcc, Input, Output, State
import dash_daq as daq
import requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)
server = app.server
app.title = "Credit Scoring Dashboard"


API_URL = "https://projetoc6.onrender.com"

try:
    ref = pd.read_csv("Auriac_Rafael_1_referentiel_022026.csv", encoding="ISO-8859-1")
    ref_dict = dict(zip(ref["Row"], ref["Description"]))
except:
    ref_dict = {}

def wrap_text(text, max_len=60):
    if not isinstance(text, str):
        return text
    words = text.split()
    lines = []
    current = ""
    for w in words:
        if len(current) + len(w) <= max_len:
            current += (" " if current else "") + w
        else:
            lines.append(current)
            current = w
    lines.append(current)
    return "<br>".join(lines)

available_features = []
default_feat1 = None
default_feat2 = None

try:
    resp_feat = requests.get(f"{API_URL}/features_list", timeout=5)
    if resp_feat.status_code == 200:
        available_features = resp_feat.json().get("features", [])
        if available_features:
            default_feat1 = available_features[0]
            default_feat2 = available_features[1] if len(available_features) > 1 else available_features[0]
except:
    pass

app.layout = html.Div(

    style={
        "backgroundColor": "#f5f6fa",
        "minHeight": "100vh",
        "fontFamily": "Inter, Arial, sans-serif",
        "padding": "20px"
    },

    children=[

        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px 30px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                "marginBottom": "25px"
            },
            children=[
                html.H1("Credit Scoring Dashboard", style={"margin": 0}),
                html.P("Analyse individuelle du risque client", style={"color": "#7f8c8d"})
            ]
        ),

        html.Div(
            style={
                "display": "flex",
                "gap": "20px",
                "marginBottom": "25px"
            },
            children=[

                html.Div(
                    style={
                        "flex": "1",
                        "backgroundColor": "white",
                        "padding": "20px",
                        "borderRadius": "12px",
                        "boxShadow": "0 4px 12px rgba(0,0,0,0.08)"
                    },
                    children=[
                        html.Label("ID Client", style={"fontWeight": "600"}),
                        dcc.Input(
                            id="user-id-input",
                            type="number",
                            value=406189,
                            style={
                                "width": "96%",
                                "padding": "10px",
                                "marginTop": "8px",
                                "marginBottom": "12px"
                            }
                        ),
                        html.Button(
                            "Analyser",
                            id="predict-button",
                            n_clicks=0,
                            style={
                                "width": "100%",
                                "padding": "12px",
                                "backgroundColor": "#3498db",
                                "color": "white",
                                "border": "none",
                                "borderRadius": "8px",
                                "fontWeight": "600",
                                "cursor": "pointer"
                            }
                        )
                    ]
                ),

                html.Div(
                    style={
                        "flex": "2",
                        "display": "flex",
                        "gap": "20px"
                    },
                    children=[

                        html.Div(
                            style={
                                "flex": "1",
                                "backgroundColor": "white",
                                "padding": "20px",
                                "borderRadius": "12px",
                                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                                "textAlign": "center"
                            },
                            children=[
                                html.H4("Décision modèle"),
                                html.Div(id="output-prediction")
                            ]
                        ),

                        html.Div(
                            style={
                                "flex": "1",
                                "backgroundColor": "white",
                                "padding": "20px",
                                "borderRadius": "12px",
                                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                                "textAlign": "center"
                            },
                            children=[
                                daq.Gauge(
                                    id="probability-gauge",
                                    min=0,
                                    max=1,
                                    value=0,
                                    showCurrentValue=True,
                                    color={
                                        "gradient": True,
                                        "ranges": {
                                            "green": [0, 0.4],
                                            "yellow": [0.4, 0.7],
                                            "red": [0.7, 1]
                                        }
                                    }
                                )
                            ]
                        )
                    ]
                )
            ]
        ),

        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                "marginBottom": "25px"
            },
            children=[
                html.H3("Facteurs d'influence (Local vs Global)"),
                dcc.Graph(id="feature-importance-graph")
            ]
        ),

        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)"
            },
            children=[

                html.H3("Analyse comparative"),

                html.Div(
                    style={"display": "flex", "gap": "20px", "marginBottom": "20px"},
                    children=[
                        html.Div(
                            style={"flex": 1},
                            children=[
                                html.Label("Feature 1"),
                                dcc.Dropdown(
                                    id="feat1-dropdown",
                                    options=[{"label": i, "value": i} for i in available_features],
                                    value=default_feat1
                                )
                            ]
                        ),
                        html.Div(
                            style={"flex": 1},
                            children=[
                                html.Label("Feature 2"),
                                dcc.Dropdown(
                                    id="feat2-dropdown",
                                    options=[{"label": i, "value": i} for i in available_features],
                                    value=default_feat2
                                )
                            ]
                        )
                    ]
                ),

                html.Div(
                    style={"display": "flex", "gap": "20px"},
                    children=[
                        html.Div(style={"flex": 1}, children=[dcc.Graph(id="dist-plot-1")]),
                        html.Div(style={"flex": 1}, children=[dcc.Graph(id="dist-plot-2")])
                    ]
                ),

                html.Div(
                    style={"marginTop": "20px"},
                    children=[dcc.Graph(id="bivariate-plot")]
                )
            ]
        )
    ]
)


@app.callback(
    [
        Output("output-prediction", "children"),
        Output("probability-gauge", "value"),
        Output("feature-importance-graph", "figure"),
        Output("dist-plot-1", "figure"),
        Output("dist-plot-2", "figure"),
        Output("bivariate-plot", "figure")
    ],
    [Input("predict-button", "n_clicks"),
     Input("feat1-dropdown", "value"),
     Input("feat2-dropdown", "value")],
    State("user-id-input", "value")
)
def update_dashboard(n_clicks, feat1, feat2, user_id):

    empty_fig = go.Figure()
    if n_clicks == 0 or user_id is None:
        return "", 0, empty_fig, empty_fig, empty_fig, empty_fig

    resp_pred = requests.get(f"{API_URL}/predict?user_id={user_id}")
    data_pred = resp_pred.json()

    if "error" in data_pred:
        return html.Div(data_pred["error"], style={'color': 'red'}), 0, empty_fig, empty_fig, empty_fig, empty_fig

    prediction_flag = data_pred["prediction"]
    probability = data_pred["probability"]
    local_imp = data_pred["feature_importance"]

    pred_text = "Client à Risque" if prediction_flag == 1 else "Client Fiable"
    pred_color = "red" if prediction_flag == 1 else "green"

    pred_div = html.Div([
        html.P(pred_text, style={'color': pred_color}),
        html.P(f"Probabilité : {probability:.2%}")
    ])

    resp_glob = requests.get(f"{API_URL}/global_importance")
    global_imp = resp_glob.json().get("global_feature_importance", {})

    df_imp = pd.DataFrame(list(local_imp.items()), columns=["feature", "local"])
    df_imp["abs"] = df_imp["local"].abs()
    df_imp = df_imp.sort_values("abs", ascending=False).head(10)
    df_imp["global"] = df_imp["feature"].map(global_imp).fillna(0)
    df_imp["desc"] = df_imp["feature"].map(ref_dict).fillna("").apply(wrap_text)

    fig_imp = go.Figure()
    fig_imp.add_bar(y=df_imp["feature"], x=df_imp["local"], orientation="h",
                    name="Local", customdata=df_imp["desc"],
                    hovertemplate="%{y}<br>%{x:.4f}<br>%{customdata}")
    fig_imp.add_trace(go.Bar(
        y=df_imp["feature"],
        x=df_imp["global"],
        orientation="h",
        name="Global",
        opacity=0.5,
        customdata=df_imp["desc"],
        hovertemplate="%{y}<br>Global: %{x:.4f}<br>%{customdata}<extra></extra>"
    ))

    fig_imp.update_layout(barmode="group", yaxis=dict(autorange="reversed"))

    if not feat1 or not feat2:
        return pred_div, probability, fig_imp, empty_fig, empty_fig, empty_fig

    resp_plot = requests.get(
        f"{API_URL}/plot_data?user_id={user_id}&feature1={feat1}&feature2={feat2}",
        timeout=10
    )

    if resp_plot.status_code != 200:
        return pred_div, probability, fig_imp, empty_fig, empty_fig, empty_fig

    try:
        plot_data = resp_plot.json()
    except ValueError:
        return pred_div, probability, fig_imp, empty_fig, empty_fig, empty_fig


    if "error" in plot_data:
        return pred_div, probability, fig_imp, empty_fig, empty_fig, empty_fig

    df_sample = pd.DataFrame(plot_data["data"])
    client = plot_data["client"]

    fig1 = px.histogram(df_sample, x=feat1, color="PREDICTION")
    fig1.add_vline(x=client[feat1])

    fig2 = px.histogram(df_sample, x=feat2, color="PREDICTION")
    fig2.add_vline(x=client[feat2])

    fig3 = px.scatter(df_sample, x=feat1, y=feat2, color="SCORE_PROBA")
    fig3.add_scatter(x=[client[feat1]], y=[client[feat2]],
                     mode="markers", marker=dict(size=14, color="black"))

    return pred_div, round(probability, 2), fig_imp, fig1, fig2, fig3


if __name__ == "__main__":
    app.run(debug=True)
