# 🧪 API Testing - Creación de Kits para Urban Grocers

## 📌 Descripción del proyecto

Este proyecto consiste en la automatización de pruebas para el endpoint **Crear un kit** de la API de Urban Grocers utilizando **Python**, **Pytest** y la librería **Requests**.

El objetivo es validar el correcto funcionamiento del servicio encargado de crear kits personales para un usuario autenticado, verificando tanto escenarios positivos como negativos mediante pruebas automatizadas.

Para ejecutar las pruebas, primero se crea un usuario mediante la API, se obtiene el **authToken** de autenticación y posteriormente se realizan las solicitudes al endpoint **POST /api/v1/kits** enviando el encabezado **Authorization Bearer Token** requerido por el servicio.

---

# 🎯 Objetivos

- Automatizar pruebas funcionales para el endpoint de creación de kits.
- Validar reglas de negocio relacionadas con el campo **name**.
- Verificar códigos de respuesta HTTP esperados.
- Confirmar que la respuesta de la API corresponde con la información enviada.
- Aplicar buenas prácticas de organización de proyectos de automatización en Python.

---

# 🛠 Tecnologías utilizadas

- Python 3
- Pytest
- Requests
- Selenium WebDriver (configuración del entorno)
- Git
- GitHub
- PyCharm

---

# 📁 Estructura del proyecto

```
qa_project
│
├── configuration.py
├── data.py
├── sender_stand_request.py
├── create_kit_name_test.py
└── README.md
```

### configuration.py  -  Contiene la configuración del proyecto:

- URL base del servicio.
- Endpoints utilizados por la API.

---

### data.py  -  Almacena los datos utilizados durante las pruebas, incluyendo:

- Datos para la creación del usuario.
- Datos utilizados para la creación de kits.

---

### sender_stand_request.py  -  Contiene las funciones responsables de enviar las solicitudes HTTP a la API.

Funciones implementadas:

- Crear usuario.
- Crear kit personal.
- Envío del encabezado Authorization Bearer Token.

---

### create_kit_name_test.py  -  Contiene todos los casos de prueba automatizados desarrollados con Pytest.

---

# ✅ Casos de prueba implementados

| Nº | Escenario | Resultado esperado |
|----|-----------|-------------------|
|1|Nombre con 1 carácter|201 Created|
|2|Nombre con 511 caracteres|201 Created|
|3|Nombre vacío|400 Bad Request|
|4|Nombre con 512 caracteres|400 Bad Request|
|5|Caracteres especiales|201 Created|
|6|Espacios|201 Created|
|7|Números como texto|201 Created|
|8|Campo **name** ausente|400 Bad Request|
|9|Campo **name** como número|400 Bad Request|

---

# 🔍 Validaciones realizadas

Cada prueba verifica:

- Código de estado HTTP.
- Campo **name** devuelto por la API.
- Coincidencia entre el valor enviado y el recibido.
- Manejo correcto de errores para entradas inválidas.

---

# 🔐 Flujo de las pruebas

1. Crear un usuario mediante la API.
2. Obtener el **authToken**.
3. Enviar el encabezado:

```
Authorization: Bearer <authToken>
```

4. Crear el kit personal.
5. Validar la respuesta del servidor.

---

# ▶️ Ejecución del proyecto

## Instalar dependencias

```bash
pip install requests
pip install pytest
pip install selenium
```

También es posible instalar todas las dependencias mediante:

```bash
pip install -r requirements.txt
```

---

## Ejecutar todas las pruebas

```bash
pytest -v
```

Para visualizar los resultados detallados:

```bash
pytest -s -v
```

---

# 📊 Resultados esperados

Al ejecutar el proyecto se obtiene un reporte indicando el estado de cada caso de prueba.

Ejemplo:

```
test_create_kit_1_character PASSED
test_create_kit_511_characters PASSED
test_create_kit_empty_name PASSED
test_create_kit_512_characters PASSED
test_create_kit_special_characters PASSED
test_create_kit_spaces PASSED
test_create_kit_numbers PASSED
test_create_kit_no_name_parameter PASSED
test_create_kit_name_number_type PASSED
```

---

# 🚀 Competencias desarrolladas

Durante este proyecto se aplicaron conocimientos relacionados con:

- Diseño de casos de prueba.
- Automatización de pruebas de API.
- Validación de respuestas HTTP.
- Manejo de autenticación mediante Bearer Token.
- Organización de proyectos en Python.
- Uso de Pytest para pruebas automatizadas.
- Control de versiones con Git y GitHub.

---

# 👩‍💻 Autor

QA Junior Mery Baracaldo

Fundamentos de Automatización: 

- Python
- Pytest
- Requests
- Selenium
- Git & GitHub
- API Testing
- SQL
- Postman
