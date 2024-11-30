import pytest
from pages.urban_routes_page import UrbanRoutesPage
from utils.config import get_driver
from data import BASE_URL

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_taxi_order_flow(driver):
    driver.get(BASE_URL)
    page = UrbanRoutesPage(driver)

    # Flujo completo de pedido de taxi
    page.set_address("123 Main St")
    page.select_tariff_comfort()
    page.set_phone_number("1234567890")
    page.add_credit_card("123")
    page.send_message("Por favor, venga rápido.")
    page.wait_for_search_modal()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.urban_routes_page import UrbanRoutesPage
from utils.config import BASE_URL
from utils.helper import retrieve_phone_code

@pytest.fixture
def setup():
    # Configura el driver de Selenium
    driver = webdriver.Chrome(executable_path="/path/to/chromedriver")
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_request_taxi(setup):
    driver = setup
    urban_routes_page = UrbanRoutesPage(driver)

    # Configurar la dirección
    urban_routes_page.configure_address("123 Main St, City, Country")

    # Seleccionar la tarifa Comfort
    urban_routes_page.select_tarifa_comfort()

    # Ingresar número de teléfono
    urban_routes_page.enter_phone_number("+1234567890")

    # Agregar tarjeta de crédito
    urban_routes_page.add_credit_card("4111111111111111", "12/24", "123")
    
    # Interceptar código de confirmación
    phone_code = retrieve_phone_code()
    urban_routes_page.enter_phone_code(phone_code)

    # Escribir un mensaje para el conductor
    urban_routes_page.write_message("Please arrive quickly!")

    # Pedir manta y pañuelos
    urban_routes_page.request_blanket_and_tissues()

    # Solicitar 2 helados
    urban_routes_page.request_ice_cream(2)

    # Verificar que se haya abierto el modal de búsqueda de automóvil
    assert urban_routes_page.is_searching_for_taxi_modal_displayed()

    # Esperar y verificar la información del conductor en el modal
    assert urban_routes_page.is_driver_info_displayed()

