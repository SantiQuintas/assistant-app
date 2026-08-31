# 🖐️ **Controlador Gestual para PC (Virtual Mouse)**
![Python](https://img.shields.io/badge/python-%233670A0.svg?style=for-the-badge&logo=python&logoColor=ffdd54)
> Nota: este proyecto esta en fase MVP.< 
Este proyecto es una interfaz de control natural (NUI) que permite manejar la computadora usando únicamente las manos y una cámara web, simulando una interfaz de ciencia ficción. Al ser un MVP, actualmente el programa solo sirve como una manera alternativa de usar el mouse, aunque el objetivo final de este proyecto seria lograr un metodo de entrada que no necesite del uso de las manos.

## Instalacion
### 1. Requisitos Previos
* Python 3.12 (Lo testee en esta version, si pasas de la version 3.13 podrias tener problemas de compatibilidad entre las dependencias)
* Contar con una camara web (Si usas droidcam, muy probablemente tengas que usar la camara virtual de OBS)
### 2. Clonar el repositorio
```bash
git clone https://github.com/SantiQuintas/synra-app.git \[nombre-de-tu-repo].git
cd [nombre-de-tu-repo]
```
### 3. Crear un entorno virtual
*Para evitar conflictos con las librerias*
* En Windows
```bash
python -m venv venv
venv\Scripts\activate
```
* En Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependencias
* pip install -r requirements.txt

### 4. Ejecutar
```bash
python3 -m venv venv
source venv/bin/activate
```
> Si estas en Linux, debes darle permisos al main, chmod +x main.py

## Caracteristicas
Al ejecutar el programa (python ./main.py), 
