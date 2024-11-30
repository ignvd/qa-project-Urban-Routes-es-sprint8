import pytest
from selenium import webdriver
from pages.urban_routes_page import UrbanRoutesPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Puedes usar cualquier otro navegador como Firefox
    driver.get("https://urbanroutes.com")  # Asegúrate de que esta sea la URL correcta
    yield driver
    driver.quit()

def test_configure_address(setup):
    page = UrbanRoutesPage(setup)
    page.configure_address("1234 Main St, Ciudad, País")
    assert "1234 Main St" in setup.page_source

def test_select_comfort_tariff(setup):
    page = UrbanRoutesPage(setup)
    page.select_tarifa_comfort()
    comfort_selected = setup.find_element(*page.TARIFA_COMFORT).is_selected()
    assert comfort_selected

def test_enter_phone_number(setup):
    page = UrbanRoutesPage(setup)
    page.enter_phone_number("1234567890")
    phone_value = setup.find_element(*page.PHONE_INPUT).get_attribute("value")
    assert phone_value == "1234567890"

def test_add_credit_card(setup):
    page = UrbanRoutesPage(setup)
    page.add_credit_card("4111111111111111", "12/25", "123")
    assert page.driver.find_element(*page.LINK_CARD_BUTTON).is_enabled()

def test_write_message(setup):
    page = UrbanRoutesPage(setup)
    page.write_message("Estoy listo para mi viaje")
    message_value = setup.find_element(*page.MESSAGE_INPUT).get_attribute("value")
    assert message_value == "Estoy listo para mi viaje"

def test_request_blanket_and_tissues(setup):
    page = UrbanRoutesPage(setup)
    page.request_blanket_and_tissues()
    # Verifica que se haya hecho clic en los botones correspondientes
    assert setup.find_element(*page.BLANKET_BUTTON).is_displayed()
    assert setup.find_element(*page.TISSUES_BUTTON).is_displayed()

def test_request_ice_cream(setup):
    page = UrbanRoutesPage(setup)
    page.request_ice_cream(2)
    # Asegúrate de que los botones de helado se hayan presionado
    assert setup.find_element(*page.ICE_CREAM_BUTTON).is_displayed()

def test_searching_for_taxi_modal(setup):
    page = UrbanRoutesPage(setup)
    page.is_searching_for_taxi_modal_displayed()
    assert setup.find_element(*page.SEARCH_MODAL).is_displayed()

def test_driver_info_displayed(setup):
    page = UrbanRoutesPage(setup)
    page.is_driver_info_displayed()
    assert setup.find_element(*page.DRIVER_INFO).is_displayed()
