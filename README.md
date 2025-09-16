[README.md](https://github.com/user-attachments/files/22372084/README.md)
Framework de Automatización de Pruebas para API RESTful
Este proyecto implementa un framework de automatización de pruebas robusto y escalable para APIs RESTful, utilizando Python, pytest y la librería requests. El objetivo es verificar la funcionalidad, la integridad y el rendimiento de las APIs mediante pruebas automatizadas.

Descripción
El framework está diseñado para facilitar la creación, ejecución y reporte de pruebas para APIs RESTful. Utiliza la API pública de JSONPlaceholder como entorno de pruebas objetivo, cubriendo operaciones comunes como GET, POST, PUT y DELETE.

Características Principales
Automatización de Pruebas: Permite la creación de casos de prueba automatizados para endpoints de API.
Validación Integral: Verifica códigos de estado HTTP, la estructura y el contenido de las respuestas JSON.
Organización Modular: Estructura clara del proyecto para facilitar la escalabilidad y el mantenimiento.
Reportes Detallados: Generación de reportes HTML interactivos de los resultados de las pruebas utilizando pytest-html.
Reutilización de Código: Uso de fixtures de pytest y un cliente API modular para evitar la duplicación de código.
Tecnologías Utilizadas
Lenguaje: Python
Framework de Pruebas: pytest
Librería HTTP: requests
Generación de Reportes: pytest-html
Entorno Virtual: venv (para gestión de dependencias)
Instrucciones de Configuración
Clonar el Repositorio:

git clone https://github.com/javivela422.git
cd tu_repositorio
Crear y Activar un Entorno Virtual:

python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
Instalar Dependencias:

pip install -r requirements.txt
2. Ejecución de Pruebas:

Para ejecutar todas las pruebas definidas en el framework, abre la terminal (asegúrate de que tu entorno virtual esté activado) y ejecuta:

pytest
Pytest descubrirá automáticamente todos los archivos de prueba que comienzan con test_ y ejecutará las funciones de prueba que comienzan con test_.

3. Generación de Reportes de Pruebas:

Para generar un reporte HTML detallado de los resultados de la ejecución de las pruebas, utiliza el siguiente comando:

pytest --html=reports/report.html
Esto creará un archivo report.html dentro de la carpeta reports/, que podrás abrir en tu navegador para ver un resumen visual de las pruebas pasadas y fallidas.

Estructura del Proyecto
api_testing_framework/
├── venv/
├── tests/
│   ├── __init__.py
│   ├── test_posts.py
│   ├── test_users.py
│   └── ...
├── utils/
│   ├── __init__.py
│   └── api_client.py
├── conftest.py
├── requirements.txt
└── README.md
