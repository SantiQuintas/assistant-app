# **Controlador Gestual para PC (Virtual Mouse)**

> Nota: Este proyecto está en fase MVP.

Este proyecto es una interfaz de control natural (NUI) que permite manejar la computadora usando únicamente las manos y una cámara web, simulando una interfaz de ciencia ficción. Al ser un MVP, actualmente el programa solo sirve como una manera alternativa de usar el mouse, aunque el objetivo final de este proyecto sería lograr un método de entrada que permita al usuario manejar su computadora por medio de sus manos, ojos y voz.

## Instalación

### 1. Requisitos previos

* Python 3.12 (Lo testeé en esta versión; si pasás de la versión 3.13 podrías tener problemas de compatibilidad entre las dependencias).
* Contar con una cámara web (si usás DroidCam, muy probablemente tengas que usar la cámara virtual de OBS).

### 2. Clonar el repositorio

```bash
git clone https://github.com/SantiQuintas/synra-app.git
cd synra-app

```

### 3. Crear un entorno virtual

> Para evitar conflictos con las librerías.

* En Windows:

```bash
python -m venv venv
venv\Scripts\activate

```

* En Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate

```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt

```

### 5. Ejecutar

```bash
python main.py

```

> Si estás en Linux, primero debés darle permisos de ejecución al archivo principal:

```bash
chmod +x main.py
./main.py

```

## Características

El programa cuenta con un menú de inicio por consola y dos modos de uso principales:

### Clásico (2D):

* Movés el cursor del mouse apuntando con tu dedo índice.
* Si juntás el índice y el pulgar, apretás el clic izquierdo (hasta que no separes tus dedos, el clic seguirá apretado, lo que permite arrastrar ventanas y archivos).
* Si juntás el meñique con el pulgar, apretás el clic derecho; funciona igual al clic izquierdo.
* Al erguir el índice y el dedo del medio al mismo tiempo (formando un dos o el símbolo de la paz) entrarás en modo scroll. Tu índice deja de mover el cursor, y el programa decidirá si scrollear para abajo o para arriba dependiendo de si movés tu mano en esa dirección (dependiendo de qué tanto muevas la mano, aumentará o disminuirá la velocidad del scroll).

### Holográfico (3D / Air-Tap):

* **Paredes virtuales:** Utiliza estimación de profundidad (fusionando el tamaño 2D de tu mano con el eje Z espacial) para dividir tu entorno en capas.
* **Zona de interacción:** Mantenés la mano a una distancia cómoda para mover el cursor por la pantalla sin riesgo de cliquear sin querer.
* **Clic por profundidad:** Para accionar el clic, simplemente empujás tu dedo índice hacia adelante atravesando la pared virtual invisible, tal como si tocaras un botón suspendido en el aire.
