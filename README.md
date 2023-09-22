# Pasos para configurar el ambiente local.

Clonar el repo: 
```sh
git clone https://github.com/hernan-dagata/py-backend.git
```

Crear el ambiente local:
```sh
python3 -m venv env
```

Activar el ambiente local:
```sh
source env/bin/activate
```

Instalar las librerías necesarias:
```sh
pip3 install -r requirements.txt
```

Subir el ambiente local por el puerto 5000:
```sh
uvicorn main:app --reload --port 5000
```
----
## Para ver la documentación swagger en local:
Abrir la url: 
````sh
http://127.0.0.1:5000/docs#/Movies/get_movies_movies_get
```