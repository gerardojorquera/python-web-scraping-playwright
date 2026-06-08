from playwright.sync_api import sync_playwright
# import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://books.toscrape.com')
    #print(page.title())
    # time.sleep(5)
    page.wait_for_selector('.product_pod')
    elementos = page.locator(".product_pod").all()
    contador = 1
    for elemento in elementos:
        #texto = elemento.inner_text()
        #print(texto)
        enlace = elemento.locator("h3 a") # querySelector('h3 a')
        # 3. Extrae el valor del atributo 'title'
        titulo = enlace.get_attribute("title")
        enlace = enlace.get_attribute("href")

        precio_elemento = elemento.locator(".price_color") # querySelector('.price_color')
        precio = precio_elemento.inner_text()

        print(str(contador) + ") Titulo: " + titulo + " \nLink: " + enlace + 
              "\nPrecio: " + str(precio) + "\n")
        contador += 1

    input("Presiona Enter para finalizar el programa...")
    browser.close()