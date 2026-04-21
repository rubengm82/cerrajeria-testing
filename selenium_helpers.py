from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "http://localhost:5173"
DEFAULT_EMAIL = "admin@email.com"
DEFAULT_PASSWORD = "admin"


def create_chrome_options(headless=False):
    options = Options()

    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")

    return options


def create_driver(headless=False):
    return webdriver.Chrome(options=create_chrome_options(headless=headless))


def accept_cookies_if_visible(driver, timeout=5):
    try:
        accept_cookies_button = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="silktide-banner"]/div/button[1]')
            )
        )
        accept_cookies_button.click()
        print("Cookies aceptadas")
    except Exception:
        print("No aparecio banner de cookies, continuando...")


def login(driver, email=DEFAULT_EMAIL, password=DEFAULT_PASSWORD):
    driver.get(f"{BASE_URL}/login")
    print("Navigating to login page...")

    accept_cookies_if_visible(driver)

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/form/input[1]'))
    )
    email_input.clear()
    email_input.send_keys(email)
    print("Email entered")

    password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/input[2]')
    password_input.clear()
    password_input.send_keys(password)
    print("Password entered")

    login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/form/button[1]')
    login_button.click()
    print("Login button clicked")

    WebDriverWait(driver, 10).until(EC.url_changes(f"{BASE_URL}/login"))
    WebDriverWait(driver, 10).until(
        lambda current_driver: current_driver.execute_script(
            "return window.localStorage.getItem('token') !== null"
        )
    )
    print(f"Current URL: {driver.current_url}")

    return driver
