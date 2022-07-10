# Intro
Desarrollo de API REST de proveedor de servicios de pagos con DJANGO y MONGO.
## Installations
Probado en MongoDB 5.0.8
+ Hay que instalar mongo.
+ Hay que crear la base de datos payments 
```[json]
use payments 
```
+ Hay que crear un usuario
```[json]
db.createUser(
		{
	user: "newCombin",
	pwd:  passwordPrompt(),   
	roles: [ { role: "readWrite", db: "payments"  }
	}
)
```
Probado en Pyhton 3.10.2 venv en WSL
```[python]
pip install -r requirements.txt
```
```[python]
python manage.py runserver 
```
## EndPoint
+ En nuesto panel de administracion tenemos que conectarnos para poder crear las boletas [localhost](http://localhost:8000/admin)
```[bash]
UserName: newCombin
Password: newcombin1
```

+ Una vez creada nuestra boleta de servicios podemos acceder a ella con el siguiente comando desde Linux.
```[bash]
curl -X GET http://localhost:8000/api/boletas/<pending/paid>/<nameServices>

pending: En lista las boletas pendientes : en base al punto3 del reto
paid: En lista todas las boletas pagadas : en base al punto4 del reto

Ejemplo:
curl -X GET http://localhost:8000/api/boletas/pending/luz

```
## Models
Existen tres colecciones en Mongo: 
+ **api_boletas:** Tiene toda la informacion de las boletas creadas.
+ **api_transactions:** Tiene toda la informacion referente a transacciones.
+ **api_cliente:** Tiene la informacion del cliente y su referencia de con que pago, etc.

## Nota
Existe un archivo .env que contiene las credeneciales de la base de datos (esto nunca lo subo es una excepcion)
