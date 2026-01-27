import requests

id_user = 406189
# Assurez-vous que l'URL est exactement celle-ci (sans espaces, sans slash superflu)
url = f"http://localhost:8000/predict?user_id={id_user}"

try:
    response = requests.get(url)
    
    # 1. Vérifier le code de statut
    print(f"Status Code: {response.status_code}")
    
    # 2. Imprimer le texte BRUT avant de convertir en JSON
    print(f"Raw Response: '{response.text}'") 
    
    if response.status_code == 200:
        data = response.json()
        print("Succès :", data['prediction'])
    else:
        print("Erreur API détectée.")

except Exception as e:
    print(f"Erreur de script : {e}")