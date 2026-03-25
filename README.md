# Testing - Cerrajeria Solidària

Este proyecto contiene los tests automatizados para la aplicación web de **Cerrajeria Solidària**, una plataforma de cerrajería comunitaria. Los tests están desarrollados en **Python** utilizando **Selenium** para la automatización del navegador.

## Autores

- **Alejandro Buenaventura Tarrillo**
- **Ruben Gallardo Mancha**

## 🛠 Librerías Utilizadas

### Dependencias Principales

| Librería | Versión | Descripción |
|----------|---------|-------------|
| **selenium** | 4.41.0 | Framework principal para automatización de navegadores web. Permite controlar Chrome, Firefox, Edge y otros navegadores programáticamente. |


### Creacción Entorno Virtual Python
```bash
python3 -m venv venv
```

### Activación Entorno Virtual Python
```bash
source venv/bin/activate
```

### Instalación

```bash
pip install -r requirements.txt
```

## 📋 Tests con Selenium

Los tests automatizados utilizan Selenium WebDriver para controlar el navegador Chrome en modo automático. A continuación se describen los diferentes tipos de tests implementados y planificados para la aplicación Cerrajeria Solidària.

### Tests Existentes

#### 1. Test de Login (`01_testing_loggin.py`)

Este test verifica el flujo de autenticación de usuarios en la aplicación:

- **Navegación**: Accede a la página de login (`http://localhost:5173/login`)
- **Gestión de cookies**: Acepta el banner de cookies si aparece
- **Autenticación**: 
  - Introduce credenciales de email (`admin@email.com`)
  - Introduce contraseña (`admin`)
  - Hace clic en el botón de login
- **Verificación**: Confirma que la redirección al dashboard es exitosa (`http://localhost:5173/dashboard`)

### Tests Planificados

Para la aplicación Cerrajeria Solidària, se deberían implementar los siguientes tests:

#### 2. Test de Registro de Usuario
- Verificar que un nuevo usuario puede registrarse
- Validar campos obligatorios
- Verificar confirmación de email

#### 3. Test de Cierre de Sesión
- Verificar que el usuario puede cerrar sesión correctamente
- Confirmar redirección a la página de login

#### 4. Test de Navegación por el Dashboard
- Verificar que todos los elementos del dashboard cargan correctamente
- Comprobar las opciones del menú

## 🚀 Ejecución de Tests

### Requisitos Previos

1. Python 3.8+
2. Google Chrome instalado
3. ChromeDriver compatible (incluido automáticamente con Selenium 4)

### Ejecutar un Test de ejemplo

```bash
python 01_testing_loggin.py
```

## 🔧 Tecnologías

- **Lenguaje**: Python
- **Framework de Testing**: Selenium WebDriver
- **Navegador**: Google Chrome
- **Servidor Local**: Vite (puerto 5173)

## 📝 Notas

- Los tests están diseñados para ejecutarse contra un servidor local en `http://localhost:5173`
- Se utiliza WebDriverWait para esperar elementos dinámicos
- Los localizadores XPath se usan para encontrar elementos en el DOM
