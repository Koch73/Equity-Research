from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc


# Webdriver Settings
options = Options()
options.add_argument("--headless")  # Sesion without UI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-images")

# Driver sesion initialization
driver = uc.Chrome(options=options)
# setting the sleep times to 0 when not necessary
driver.implicitly_wait(0)

URL = 'https://www.macrotrends.net/stocks/charts/WDAY/workday/operating-margin'

# Abrir la página
driver.get(URL)

# Obtener el HTML completo de la página
html = driver.page_source

# Cerrar el navegador
driver.quit()

# Imprimir o utilizar el HTML
print(html)
