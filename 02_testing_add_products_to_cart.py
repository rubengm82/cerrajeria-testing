import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium_helpers import BASE_URL, create_driver, login

driver = create_driver()
product_name = "Cilindre 30x30 Níquel Securemme K1"

try:
    login(driver, email="user@email.com", password="user")

    # Se navega a la pagina de productos
    driver.get(f"{BASE_URL}/products")
    WebDriverWait(driver, 10).until(EC.url_contains("/products"))

    # Se abre el modal del producto
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            f"//div[@role='button' and contains(@aria-label, '{product_name}')]"
        ))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "product-view-modal"))
    )

    # Se añade el producto al carrito
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(normalize-space(), 'Afegir al carret')]"
        ))
    ).click()

    # Se navega al carrito
    time.sleep(2)
    driver.get(f"{BASE_URL}/cart")
    WebDriverWait(driver, 10).until(EC.url_contains("/cart"))

    driver.save_screenshot("cart_after_add_product.png")
    time.sleep(3)

except Exception as e:
    print(f"Error durante el test: {e}")
finally:
    print("Cerrando navegador...")
    driver.quit()
    print("Fin del script")
