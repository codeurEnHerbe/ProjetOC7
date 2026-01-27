```python
pip install dash dash-daq
```

    Note: you may need to restart the kernel to use updated packages.Requirement already satisfied: dash in c:\users\rafael\anaconda3\lib\site-packages (3.2.0)
    Requirement already satisfied: dash-daq in c:\users\rafael\anaconda3\lib\site-packages (0.6.0)
    Requirement already satisfied: Flask<3.2,>=1.0.4 in c:\users\rafael\anaconda3\lib\site-packages (from dash) (2.2.5)
    Requirement already satisfied: Werkzeug<3.2 in c:\users\rafael\anaconda3\lib\site-packages (from dash) (2.2.3)
    Requirement already satisfied: plotly>=5.0.0 in c:\users\rafael\anaconda3\lib\site-packages (from dash) (5.24.1)
    Requirement already satisfied: importlib-metadata in c:\users\rafael\anaconda3\lib\site-packages (from dash) (7.0.1)
    Requirement already satisfied: typing-extensions>=4.1.1 in c:\users\rafael\anaconda3\lib\site-packages (from dash) (4.15.0)
    Requirement already satisfied: requests in c:\users\rafael\anaconda3\lib\site-packages (from dash) (2.32.5)
    Requirement already satisfied: retrying in c:\users\rafael\anaconda3\lib\site-packages (from dash) (1.4.2)
    Requirement already satisfied: nest-asyncio in c:\users\rafael\anaconda3\lib\site-packages (from dash) (1.6.0)
    Requirement already satisfied: setuptools in c:\users\rafael\anaconda3\lib\site-packages (from dash) (68.2.2)
    Requirement already satisfied: Jinja2>=3.0 in c:\users\rafael\anaconda3\lib\site-packages (from Flask<3.2,>=1.0.4->dash) (3.1.3)
    Requirement already satisfied: itsdangerous>=2.0 in c:\users\rafael\anaconda3\lib\site-packages (from Flask<3.2,>=1.0.4->dash) (2.0.1)
    Requirement already satisfied: click>=8.0 in c:\users\rafael\anaconda3\lib\site-packages (from Flask<3.2,>=1.0.4->dash) (8.1.7)
    Requirement already satisfied: MarkupSafe>=2.1.1 in c:\users\rafael\anaconda3\lib\site-packages (from Werkzeug<3.2->dash) (2.1.3)
    Requirement already satisfied: colorama in c:\users\rafael\anaconda3\lib\site-packages (from click>=8.0->Flask<3.2,>=1.0.4->dash) (0.4.6)
    Requirement already satisfied: tenacity>=6.2.0 in c:\users\rafael\anaconda3\lib\site-packages (from plotly>=5.0.0->dash) (8.2.2)
    Requirement already satisfied: packaging in c:\users\rafael\anaconda3\lib\site-packages (from plotly>=5.0.0->dash) (23.1)
    Requirement already satisfied: zipp>=0.5 in c:\users\rafael\anaconda3\lib\site-packages (from importlib-metadata->dash) (3.17.0)
    Requirement already satisfied: charset_normalizer<4,>=2 in c:\users\rafael\anaconda3\lib\site-packages (from requests->dash) (2.0.4)
    Requirement already satisfied: idna<4,>=2.5 in c:\users\rafael\anaconda3\lib\site-packages (from requests->dash) (3.4)
    Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\rafael\anaconda3\lib\site-packages (from requests->dash) (2.5.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\rafael\anaconda3\lib\site-packages (from requests->dash) (2025.10.5)
    
    

    
    [notice] A new release of pip is available: 25.2 -> 25.3
    [notice] To update, run: python.exe -m pip install --upgrade pip
    


```python
import dash
from dash import html, dcc, Input, Output, State
import requests
import dash_daq as daq

```


```python
import pandas as pd
ref = pd.read_csv('referentiel.csv', encoding = "ISO-8859-1")
ref.drop(columns=['Unnamed: 0'])[['Row', 'Description']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>SK_ID_CURR</td>
      <td>ID of loan in our sample</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TARGET</td>
      <td>Target variable (1 - client with payment diffi...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NAME_CONTRACT_TYPE</td>
      <td>Identification if loan is cash or revolving</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CODE_GENDER</td>
      <td>Gender of the client</td>
    </tr>
    <tr>
      <th>4</th>
      <td>FLAG_OWN_CAR</td>
      <td>Flag if the client owns a car</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>214</th>
      <td>NUM_INSTALMENT_NUMBER</td>
      <td>On which installment we observe payment</td>
    </tr>
    <tr>
      <th>215</th>
      <td>DAYS_INSTALMENT</td>
      <td>When the installment of previous credit was su...</td>
    </tr>
    <tr>
      <th>216</th>
      <td>DAYS_ENTRY_PAYMENT</td>
      <td>When was the installments of previous credit p...</td>
    </tr>
    <tr>
      <th>217</th>
      <td>AMT_INSTALMENT</td>
      <td>What was the prescribed installment amount of ...</td>
    </tr>
    <tr>
      <th>218</th>
      <td>AMT_PAYMENT</td>
      <td>What the client actually paid on previous cred...</td>
    </tr>
  </tbody>
</table>
<p>219 rows × 2 columns</p>
</div>




```python
ref
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Table</th>
      <th>Row</th>
      <th>Description</th>
      <th>Special</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>application_{train|test}.csv</td>
      <td>SK_ID_CURR</td>
      <td>ID of loan in our sample</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>application_{train|test}.csv</td>
      <td>TARGET</td>
      <td>Target variable (1 - client with payment diffi...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>application_{train|test}.csv</td>
      <td>NAME_CONTRACT_TYPE</td>
      <td>Identification if loan is cash or revolving</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>application_{train|test}.csv</td>
      <td>CODE_GENDER</td>
      <td>Gender of the client</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>application_{train|test}.csv</td>
      <td>FLAG_OWN_CAR</td>
      <td>Flag if the client owns a car</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>214</th>
      <td>installments_payments.csv</td>
      <td>NUM_INSTALMENT_NUMBER</td>
      <td>On which installment we observe payment</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>215</th>
      <td>installments_payments.csv</td>
      <td>DAYS_INSTALMENT</td>
      <td>When the installment of previous credit was su...</td>
      <td>time only relative to the application</td>
    </tr>
    <tr>
      <th>216</th>
      <td>installments_payments.csv</td>
      <td>DAYS_ENTRY_PAYMENT</td>
      <td>When was the installments of previous credit p...</td>
      <td>time only relative to the application</td>
    </tr>
    <tr>
      <th>217</th>
      <td>installments_payments.csv</td>
      <td>AMT_INSTALMENT</td>
      <td>What was the prescribed installment amount of ...</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>218</th>
      <td>installments_payments.csv</td>
      <td>AMT_PAYMENT</td>
      <td>What the client actually paid on previous cred...</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>219 rows × 4 columns</p>
</div>




```python
import dash
from dash import html, dcc, Input, Output, State
import dash_daq as daq
import requests
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)
app.title = "Dashboard de prédiction"

app.layout = html.Div([

    html.H2("Prédiction utilisateur"),

    html.Div([
        dcc.Input(
            id="user-id-input",
            type="number",
            placeholder="Entrer un ID utilisateur",
            style={"marginRight": "10px"}
        ),
        html.Button("Prédire", id="predict-button", n_clicks=0)
    ], style={"marginBottom": "20px"}),

    html.Div(id="output-prediction", style={"fontSize": "18px", "marginTop": "20px"}),

    html.Div(
        daq.Gauge(
            id="probability-gauge",
            label="Probabilité",
            value=0,
            min=0,
            max=1,
            size=200,
            color={"gradient": True, "ranges": {"green": [0, 0.3], "yellow": [0.3, 0.7], "red": [0.7, 1]}}
        ),
        style={"marginTop": "40px", "textAlign": "center"}
    ),

    html.H3("Feature Importance (Top 10)", style={"marginTop": "50px"}),
    dcc.Graph(id="feature-importance-graph")

])


@app.callback(
    [
        Output("output-prediction", "children"),
        Output("probability-gauge", "value"),
        Output("feature-importance-graph", "figure")
    ],
    Input("predict-button", "n_clicks"),
    State("user-id-input", "value")
)
def get_prediction(n_clicks, user_id):
    if n_clicks == 0 or user_id is None:
        return "Veuillez entrer un ID utilisateur et cliquer sur 'Prédire'.", 0, px.scatter()

    try:
        url = f"http://127.0.0.1:8000/predict?user_id={user_id}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        prediction = data.get("prediction", "N/A")
        probability = data.get("probability", 0)
        feat_imp = data.get("feature_importance", {})

        probability = min(max(float(probability), 0), 1)

        # --- Construction du graph ---
        if feat_imp:
            df = pd.DataFrame(list(feat_imp.items()), columns=["feature", "importance"])
            df["abs_importance"] = df["importance"].abs()
            df = df.sort_values("abs_importance", ascending=False).head(10)

            fig = px.bar(
                df,
                x="importance",
                y="feature",
                orientation="h",
                title="Top 10 Feature Importances",
            )
            fig.update_layout(height=500)
        else:
            fig = px.scatter(title="Aucune information disponible")

        return [
            html.P(f"Prédiction : {prediction}"),
            html.P(f"Probabilité : {probability:.4f}")
        ], probability, fig

    except Exception as e:
        fig = px.scatter(title="Erreur lors de la création du graphique")
        return f"Erreur lors de la requête : {e}", 0, fig


if __name__ == "__main__":
    app.run(debug=True)

```



<iframe
    width="100%"
    height="650"
    src="http://127.0.0.1:8050/"
    frameborder="0"
    allowfullscreen

></iframe>


