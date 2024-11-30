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
