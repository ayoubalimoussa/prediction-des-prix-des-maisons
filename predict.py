from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Charger le modèle entraîné
with open('rf.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Récupérer les noms des colonnes utilisés lors de l'entraînement
model_columns = model.feature_names_in_


@app.route('/')
def home():
    return render_template('index2.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Récupérer les valeurs du formulaire
    form_data = {key: float(value) for key, value in request.form.items()}

    # Créer un DataFrame avec les données utilisateur
    user_data = pd.DataFrame([form_data])

    # Ajouter les colonnes manquantes avec une valeur par défaut (par ex., 0)
    for col in model_columns:
        if col not in user_data.columns:
            user_data[col] = 0

    # Réorganiser les colonnes dans le même ordre que celles utilisées par le modèle
    user_data = user_data[model_columns]

    # Effectuer la prédiction
    prediction = model.predict(user_data)

    return render_template(
        'index2.html',
        prediction_text='Predicted House Price: ${:.2f}'.format(prediction[0])
    )


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
