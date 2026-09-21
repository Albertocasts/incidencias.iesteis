

# Manual de instalación de la aplicación web



## Decisiones de proyecto

|Elemento|Decisión·|Versión|Justificación|
|--------|-------|--------|-------------|
|Servidor web|Apache|2|Facidilidad de uso, popular|
|Base de datos|MySQL|8|Experiencia previa, popular|
|Lenguaje servidor|Python|3|Muy interesante para ASIR, uso extendido|
|Framework|Flask|3|Facilidad de uso, pensado especificamente para web, formularios y sesiones|
|Control de versiones|Git|8|Muy extendido|
|Documentación|Markdown|-|Muy utilizado con guthub

# # ¿Que hace un servidor web?

Almacena, procesa y entrega los componentes de un sitio web a los usuarios a traves de internet

## Proceso de instalación / puesta en marcha

1. Actualización del sistema
`sudo apt update && sudo apt upgrade -y`
2. Instalar git
`sudo apt install git`
3. Instalar VSCode + plugins
    - Markdown all in one
4. Instalar apache
 'sudo apt install apache2'
5. Cambiar permisos de la carpeta /var/www/html
``` bash
sudo chown -R $USER:$USER /var/www/html
sudo chmod -R u=rwX,go=rx /var/www/html
```
6. Instalar mysql server
``` bash
sudo apt install mysql-server
```
7. Configuracion mysql
``` mysql
create database incidencias;
create user 'incidencias'@'localhost' identified by 'incidencias';
grant all privileges on incidencias.* to 'incidencias'@'localhost';
flush privileges;
```
8. Creamos tablas y añadimos datos
```mysql
create table registro( id int auto_increment primary key, aula varchar(30), descripcion text, usuario varchar(20), estado varchar(30) );
insert into registro (aula, descripcion, usuario, estado) values ('Taller1', 'PC 24 no arranca', 'albertocast', 'ABIERTA'), ('Taller1', 'PC 24 no arranca', 'albertocast', 'ABIERTA'), ('Taller1', 'Iago no se calla', 'albertocast', 'ABIERTA');

```

## Configuración de github

1. Crear repositorio local, añadir archivos y commit
 ```bash
get init
git add .
git commit -n "comentario"
```

2. Crear cuenta github, crear repositorio github 


3. Conectar repositorio local en remoto
```bash
git remote add origin https://github.com/Albertocasts/incidencias.iesteis.git
git branch -M main
git push -u origin main
```


## Python
1. Instalar python
``` bash
sudo apt install python3-pip python3-venv -y
```

2. Conectamos y activamos el entorno virtual
``` bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar flask, conector de base de datos, comporbar y guardar las dependencias
``` bash
pip install flask
pip install mysql-connector-python
pip list
pip freeze > requirement.txt
```
4. Creamos un fichero app.py en la carpeta principal del proyecto
```bash
python3 app.py
```
 -Esto crea un servidor web alternativo lebavntado en localhost en el puerto 5000.Se podria poner Apache de intermediario utilzando un proxy
 -Habria que modificar etc/apache2/sites-available/incidencias.ies.teis.conf añadiendo esto dentro del virtualhost:
```
ProxxyPass / https://127.0.0.1:5000/
ProxxyPassReverse / https://127.0.0.1:5000/
```
-Y activar los modulos
```bash
sudo a2enmod proxy
sudo a2enmod proxy_http
sudo systemctl restart apache2
```

```
5. Comprobamos abriendo http://localhost:5000/
```


## Migración del formulario a Python/Flask

1. Creamos una carpeta templates y movemos ahi el index.html
2. Modificamos app.py
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

```
3. Comprobamos abriendo http://localhost:5000/ . El formulario lo devuelve flask

## Recibir los datos del formulario

1. Vamos a app.py y modificamos la primera línea añadiendo request:
```python
from flask import Flask, render_template, request
```
2. Añadimos una ruta en app.py para recibir los datos del formulario:
```python
@app.route("/incidencias", methods=["POST"])
def crear_incidencia():
    aula=request.form["Aula"]
    usuario=request.form["Usuario"]
    descripcion=request.form["Descripcion"]

    print("Aula:" + aula)
    print("Usuario:" + usuario)
    print("Descripcion:" + descripcion)
    return "Incidencia recibida"
´´´

