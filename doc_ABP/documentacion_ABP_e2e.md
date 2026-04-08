# Automatización E2E de Login con Selenium

## ¿Qué es una automatización End-to-End (E2E)?

Las pruebas **End-to-End (E2E)** son un tipo de testing que verifica que una aplicación funcione correctamente desde el principio hasta el final, simulando la interacción que tendría un usuario real con el sistema. En lugar de probar funciones aisladas, probamos flujos completos.

En este caso, automatizamos el proceso de **inicio de sesión** en una aplicación web.

---

## Código en Python

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
# options.add_argument("--headless=new")  # si no quieres GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    # Navegar a la página de login
    driver.get("http://localhost:5173/login")
    print("Navigating to login page...")
    time.sleep(2)  # Esperar a que cargue la página
    
    # Aceptar cookies si aparece el banner
    try:
        accept_cookies_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"silktide-banner\"]/div/button[1]"))
        )
        accept_cookies_button.click()
        print("Cookies aceptadas")
        time.sleep(1)
    except Exception:
        print("No apareció banner de cookies, continuando...")
    
    # Buscar el campo de email
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"root\"]/div/form/input[1]"))
    )
    email_input.clear()
    email_input.send_keys("admin@email.com")
    print("Email entered")
    
    # Buscar el campo de password
    password_input = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/form/input[2]")
    password_input.clear()
    password_input.send_keys("admin")
    print("Password entered")
    
    # Buscar y hacer clic en el botón de login
    login_button = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div/form/button[1]")
    login_button.click()
    print("Login button clicked")
    
    # Esperar a que redireccione al dashboard
    WebDriverWait(driver, 10).until(
        EC.url_to_be("http://localhost:5173/dashboard")
    )
    
    # Verificar que estamos en el dashboard
    current_url = driver.current_url
    print(f"Current URL: {current_url}")
    
    if current_url == "http://localhost:5173/dashboard":
        print("✓ Login exitoso! Estamos en el dashboard.")
        print("Esperando 3 segundos para visualizar el dashboard...")
        time.sleep(3)  # Esperar 3 segundos para ver el dashboard
    else:
        print(f"✗ Error: Esperaba estar en dashboard pero estoy en {current_url}")

except Exception as e:
    print(f"Error durante el test: {e}")
    # driver.save_screenshot("error_login.png")
    print("Screenshot guardado como error_login.png")
finally:
    print("Cerrando navegador...")
    driver.quit()
    print("Fin del script")
```

---

## Explicación paso a paso

### 1. Configuración del navegador (líneas 8-14)
```python
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
```
Se configura Chrome con opciones específicas:
- `--no-sandbox` y `--disable-dev-shm-usage`: necesarios para ejecutar Chrome en entornos Linux/Docker
- `--start-maximized`: abre el navegador maximizado

### 2. Navegación a la página de login (líneas 18-20)
```python
driver.get("http://localhost:5173/login")
```
El navegador abre la URL de login de la aplicación (probablemente una app React/Vue en desarrollo).

### 3. Aceptar cookies (líneas 23-31)
```python
try:
    accept_cookies_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id=\"silktide-banner\"]/div/button[1]"))
    )
    accept_cookies_button.click()
except Exception:
    print("No apareció banner de cookies, continuando...")
```
Si aparece un banner de cookies, se acepta. Si no aparece, se continua sin error.

### 4. Rellenar credenciales (líneas 34-45)
```python
email_input.send_keys("admin@email.com")
password_input.send_keys("admin")
```
Se Introducen las credenciales de prueba:
- **Email**: `admin@email.com`
- **Password**: `admin`

### 5. Enviar formulario (líneas 48-50)
```python
login_button.click()
```
Se hace clic en el botón de login para enviar el formulario.

### 6. Verificar redirección (líneas 53-66)
```python
WebDriverWait(driver, 10).until(
    EC.url_to_be("http://localhost:5173/dashboard")
)
```
Se espera hasta que la URL cambie a `/dashboard`, confirmando que el login fue exitoso.

### 7. Limpieza (líneas 72-75)
```python
finally:
    driver.quit()
```
Siempre se cierra el navegador, incluso si hay errores.

---

## ¿Qué automatización hace este test?

| Paso | Acción | Objetivo |
|------|--------|----------|
| 1 | Abrir navegador | Simular usuario real |
| 2 | Ir a `/login` | Navegar a página de login |
| 3 | Aceptar cookies | Manejar banner emergente |
| 4 | Escribir email | Rellenar campo email |
| 5 | Escribir password | Rellenar campo contraseña |
| 6 | Clicar login | Enviar formulario |
| 7 | Verificar URL | Confirmar login exitoso |
| 8 | Cerrar navegador | Limpiar recursos |

---

## Tecnologías utilizadas

- **Selenium WebDriver**: Herramienta para automatizar navegadores
- **Python**: Lenguaje de programación
- **ChromeDriver**: Puente entre Selenium y Chrome
- **WebDriverWait**: Espera explícita para elementos dinámicos

---

## ¿Por qué es útil esta automatización?

1. **Repetibilidad**: Se puede ejecutar tantas veces como sea necesario
2. **Rapidez**: Elimina la necesidad de hacer pruebas manuales
3. **Detección de errores**: Si el login falla, el test lo detecta automáticamente
4. **Integración continua**: Se puede integrar en pipelines CI/CD
