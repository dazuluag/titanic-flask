titanic-flask
===
Modelado problema Titanic y publicación de servicios Flask para administración y utilización del modelo.

## Dependencias del servicio
> - pandas
> - scikit-learn
> - Flask

**Instalación de las dependencias:**
```
pip install -r requirements.txt
```

## Endpoints del servicio
### /titanic/predict (POST)
**Input:**
```
[
    {"Age": 85, "Sex": "male", "Embarked": "S"},
    {"Age": 60, "Sex": "female", "Embarked": "C"},
    {"Age": 38, "Sex": "male", "Embarked": "C"},
    {"Age": 21, "Sex": "male", "Embarked": "S"}
]
```
**Output:**
```
{
    "prediction": "[1, 1, 0, 0]"
}
```

## Miscelaneos
### Variable de ambiente *FLASK_ENV*
Por defecto, la librería de Flask presenta un mensaje de advertencia recomendando que no se utilice un servidor de desarrollo en ambiente de producción:
> WARNING: Do not use the development server in a production environment.

Para evitar que se presente este mensaje debe crear la variable de ambiente *FLASK_ENV* en su ambiente local de la siguiente manera:
#### Linux
```
export FLASK_ENV=development
```
#### Windows
```
set FLASK_ENV=development
```

## Instalación con Docker
### Construyendo la imagen docker
```
docker build -t titanic-docker:latest .
```
### Ejecutando la imagen docker
```
docker run -d -p 7000:7000 titanic-docker:latest
```
