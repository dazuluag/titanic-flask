# Importamos las librerías necesarias
import sys
import os
import time
import shutil
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

# Cargamos los archivos de entranamiento
training_data = 'data/train.csv'
include = ['Age', 'Sex', 'Embarked', 'Survived']
dependent_variable = include[-1]

# Cargamos el modelo entranado desde archivos pickle
model_directory = 'model'
model_file_name = '%s/model.pkl' % model_directory
model_columns_file_name = '%s/model_columns.pkl' % model_directory

# Variables para almacenar el modelo entrenado
model_columns = None
clf = None

# Función para realizar el entrenamiento con Randon Forest
def train():
    df = pd.read_csv(training_data)
    df_ = df[include]
    categoricals = []
    for col, col_type in df_.dtypes.iteritems():
        if col_type == 'O':
            categoricals.append(col)
        else:
            # Reemplazaos los valores nulos con 0s
            df_[col].fillna(0, inplace=True)

    # Creamos los atributos dummies para las categoricas
    df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)
    x = df_ohe[df_ohe.columns.difference([dependent_variable])]
    y = df_ohe[dependent_variable]
    # Obtenemos las columnas que serán usadas en el entrenamiento
    global model_columns
    model_columns = list(x.columns)
    joblib.dump(model_columns, model_columns_file_name)
    global clf
    clf = RandomForestClassifier()
    start = time.time()
    # Realizamos el entrenamiento del modelo
    clf.fit(x, y)
    print('Entrenamiento en %.1f segundos' % (time.time() - start))
    print('Score del modelo entrenado: %s' % clf.score(x, y))
    joblib.dump(clf, model_file_name)
    return 'Success'

# Función para limpiar el entrenamiento del modelo
def wipe():
    try:
        shutil.rmtree('model')
        os.makedirs(model_directory)
        return 'Success'
    except Exception as e:
        print(str(e))
        return 'No fue posible eliminar y re-crear el directorio del modelo'
