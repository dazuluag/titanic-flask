# Importamos las librerías necesarias
import sys
import os
import traceback
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, request, jsonify

# Creamos la aplicación Flask para publicación de servicio
app = Flask(__name__)

# Cargamos el modelo entranado desde archivos pickle
model_directory = 'model'
model_file_name = '%s/model.pkl' % model_directory
model_columns_file_name = '%s/model_columns.pkl' % model_directory

# Variables para almacenar el modelo entrenado
model_columns = None
clf = None

# Función para realizar la predicción con método POST
@app.route('/titanic/predict', methods=['POST'])
def predict():
    if clf:
        try:
            json_ = request.json
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            prediction = list(clf.predict(query))
            return jsonify({'prediction': str(prediction)})
        except Exception as e:
            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print('Recomendamos que ejecute el entrenamiento')
        return 'No existe o no pudo ser cargado el modelo'

# Función main para lanzar el servicio Flask
if __name__ == '__main__':
    port = None
    try:
        port = os.environ['SURA_APP_PORT']
    except:
        port = 8000
    try:
        clf = joblib.load(model_file_name)
        print('Modelo cargado con éxito')
        model_columns = joblib.load(model_columns_file_name)
        print('Columnas del modelo cargadas con éxito')
    except Exception as e:
        print('No existe o no pudo ser cargado el modelo')
        print('Recomendamos que ejecute el entrenamiento')
        print(str(e))
        clf = None
    app.run(host='0.0.0.0', port=port, debug=True)