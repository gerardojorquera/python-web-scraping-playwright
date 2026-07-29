import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()  # Carga las variables de entorno desde el archivo .env

url = os.getenv("URL")
username = os.getenv("APP_USERNAME")
password = os.getenv("APP_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    # time.sleep(5)
    #page.wait_for_selector('.product_pod')
    page.fill('input[name="Login"]', username)
    page.fill('input[name="Password"]', password)
    page.click('button[type="submit"]')
    print("Intentando iniciar sesión...")

    # Espera a que la página se cargue después del inicio de sesión
    page.wait_for_load_state('networkidle')
    print("Inicio de sesión completado. Puedes realizar acciones adicionales aquí.")

    """
    Esperar a que cargue el dashboard
    page.wait_for_selector('.tabla-precios')
    """

    input("Presiona Enter para finalizar el programa...")
    browser.close()