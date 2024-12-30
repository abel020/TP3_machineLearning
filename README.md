# Predicción de Diabetes con KNN

## Descripción

Este proyecto implementa un modelo predictivo basado en el algoritmo K-Nearest Neighbors (KNN) para predecir la probabilidad de diabetes a partir de datos ingresados por el usuario en un formulario web. El modelo fue entrenado utilizando un dataset balanceado al 50% entre casos con y sin diabetes, almacenado en el archivo modelo_knn_diabetes5050.pkl. El desarrollo se realizó con el framework Django, ofreciendo una interfaz web funcional y amigable, y se desplegó en la plataforma Railway para garantizar su disponibilidad y fácil acceso.

## Autor

Gomez Nuñez Abel Anderson

## Tecnologías Utilizadas

- **Django**: Framework web para desarrollar aplicaciones.
- **Scikit-learn**: Biblioteca de Python para Machine Learning.
- **Pandas**: Biblioteca para manipulación de datos.
- **NumPy**: Biblioteca para computación numérica.
- **Railway**: Plataforma para el despliegue de aplicaciones.

## Dataset Utilizado

El modelo fue entrenado utilizando un dataset de indicadores de salud relacionado con la diabetes, disponible en Kaggle. Este dataset incluye información recopilada a partir de la encuesta BRFSS 2015, equilibrada al 50% entre individuos con y sin diabetes.  

Puedes encontrar más detalles sobre el dataset en el siguiente enlace:  
[Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)


## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/abel020/TP3_machineLearning.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd TP3_machineLearning
   ```

3. Crea un entorno virtual e instálalo:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`
   pip install -r requirements.txt
   ```

4. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

## Uso

1. Abre tu navegador y ve a `http://127.0.0.1:8000`.
2. Completa el formulario con los datos necesarios.
3. Envía el formulario para obtener la predicción de diabetes.

## Capturas de Pantalla

### Menú Principal
![Menú Principal](Api/static/imagenes/Menu.jpeg)

### Formulario de Entrada
![Formulario de Entrada](Api/static/imagenes/Formulario.jpeg)

### Predicción de Diabetes
![Predicción de Diabetes](Api/static/imagenes/Prediccion.jpeg)

## Despliegue

Este proyecto está desplegado en Railway. Puedes acceder a la aplicación en el siguiente enlace:

[Enlace a la aplicación desplegada](https://tp3machinelearning-production.up.railway.app)

### Archivos importantes para el despliegue

- **Procfile**: Este archivo es necesario para que Railway sepa cómo ejecutar la aplicación.
- **runtime.txt**: Este archivo especifica la versión de Python que se utilizará en el entorno de Railway.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz un commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.


