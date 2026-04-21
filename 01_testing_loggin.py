import time

from selenium_helpers import BASE_URL, create_driver, login

driver = create_driver()

try:
    login(driver)

    if driver.current_url != f"{BASE_URL}/login":
        print("✓ Login exitoso!")
        print("Esperando 3 segundos para visualizar la pagina...")
        time.sleep(3)  # Esperar 3 segundos para ver el dashboard
    else:
        print(f"✗ Error: Seguimos en login: {driver.current_url}")

except Exception as e:
    print(f"Error durante el test: {e}")
    # driver.save_screenshot("error_login.png")
    print("Screenshot guardado como error_login.png")
finally:
    print("Cerrando navegador...")
    driver.quit()
    print("Fin del script")
