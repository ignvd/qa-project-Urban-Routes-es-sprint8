from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    """Configura y devuelve un controlador de Selenium."""
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(executable_path="path/to/chromedriver")  # Cambia a la ruta correcta de tu chromedriver
    return webdriver.Chrome(service=service, options=options)
