# Hepha-CLI

Hepha-CLI (abreviatura de Hephaestus Command Line Interface), inspirado en Hephaestus, el legendario dios griego de la forja y el fuego, es una herramienta para simplificar y optimizar su interacción con AWS CLI v2. 

Justo como Hephaestus forjó las armas de los dioses y los héroes con su astucia y habilidad, Hepha-CLI está diseñado para ayudarte a "forjar" tus soluciones en AWS de la manera más eficiente posible.

## ¿Qué hace Hepha-CLI?

Hepha-CLI es una interfaz de línea de comandos que ayuda a los desarrolladores e ingenieros DevOps a manejar de manera eficiente una variedad de tareas en AWS CLI v2. Estas tareas incluyen:

- Crear y configurar una API Gateway.
- Crear y cargar funciones Lambda.
- Configurar las funciones Lambda.
- Configurar las capas (layers).

Estas son solo algunas de las operaciones que puedes realizar con Hepha-CLI. La herramienta está diseñada para ser extensible, por lo que puedes agregar nuevas funcionalidades según las necesidades de tu proyecto.

## ¿Por qué usar Hepha-CLI?

La inspiración en Hephaestus no es solo nominal. Así como Hephaestus era conocido por su habilidad para crear herramientas y armas de increíble poder y belleza, Hepha-CLI tiene como objetivo proporcionarte una herramienta poderosa y elegante para manejar tus tareas en AWS.

Hepha-CLI se creó para aliviar la complejidad de cargar comandos en AWS CLI v2, permitiéndote centrarte en lo que realmente importa: construir soluciones asombrosas en la nube. Al igual que Hephaestus forjó los escudos que protegieron a los héroes en sus aventuras, Hepha-CLI está aquí para protegerte de los intricados detalles de la administración de servicios de AWS.

Con Hepha-CLI, puedes trabajar con AWS de la manera más eficiente, segura y agradable posible. ¡Esperamos que te ayude en tu viaje de desarrollo y operaciones en la nube!

Bienvenido a Hepha-CLI, la herramienta que te ayudará a forjar tus propias soluciones increíbles en AWS. ¡Manos a la obra!

## Estructura
hepha-cli/
│
├── hepha/                 # Código fuente principal
│   ├── __init__.py        # Inicialización del paquete
│   ├── cli.py             # Punto de entrada principal del CLI
│   ├── api_gateway/       # Módulos para la API Gateway
│   │   ├── __init__.py
│   │   ├── create.py
│   │   ├── modify.py
│   │   ├── websocket.py
│   │   └── config.py
│   ├── lambda/            # Módulos para las funciones Lambda
│   │   ├── __init__.py
│   │   ├── create.py
│   │   ├── modify.py
│   │   └── config.py
│   └── utils/             # Módulos de utilidades
│       ├── __init__.py
│       └── templates.py
│
├── tests/                 # Pruebas unitarias
│   ├── __init__.py
│   ├── test_api_gateway.py
│   └── test_lambda.py
│
├── templates/             # Plantillas para las funciones Lambda
│   ├── lambda_template1.yml
│   └── lambda_template2.yml
│
├── .github/               # Configuraciones para GitHub Actions (CI/CD)
│   ├── workflows/
│   │   └── main.yml
│   └── actions/
│
├── .gitignore             # Archivos y directorios ignorados por Git
├── LICENSE                # Detalles de la licencia del proyecto
├── README.md              # Descripción detallada del proyecto
├── requirements.txt       # Dependencias del proyecto
└── setup.py               # Script de instalación


## Licencia

Hepha-CLI es un proyecto de código abierto bajo la licencia MIT.

