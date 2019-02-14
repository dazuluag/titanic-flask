titanic-flask
===
Modelado problema Titanic y publicación de servicios Flask para administración y utilización del modelo.

## Dependencias
> - pandas
> - scikit-learn
> - Flask

**Instalación de las dependencias:**
```
pip install -r requirements.txt
```


## Servicios
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
