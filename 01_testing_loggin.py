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
        print("No appearedció banner de cookies, continuando...")
    
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