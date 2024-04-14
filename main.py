import time
import pytest
from playwright.sync_api import sync_playwright
import data

# Доступ к переменным осуществляется через data
data.minus_1_json
data.zero_json
data.one_json
data.handred_1_json
data.handred_2_json
data.thousand_1_json

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()

#################### locators ####################
co2_counter = '//*[@class="desktop-impact-item-eeQO3"][2]'
water_counter = '//*[@class="desktop-impact-item-eeQO3"][4]'
energy_counter = '//*[@class="desktop-impact-item-eeQO3"][6]'

###################### data.json ######################
main_url = 'https://www.avito.ru/avito-care/eco-impact'
mock_url = 'https://www.avito.ru/web/1/charity/ecoImpact/init'

def run_test(page, data, output_path):
    page.route(mock_url, lambda route: route.fulfill(json=data))
    page.goto(main_url)
    time.sleep(4)
    page.locator(co2_counter).screenshot(path=f'{output_path}-CO2.png')
    page.locator(water_counter).screenshot(path=f'{output_path}-water.png')
    page.locator(energy_counter).screenshot(path=f'{output_path}-energy.png')
    page.close()

def test_minus_1(page):
    run_test(page, minus_1_json, './output/test1')

def test_zero(page):
    run_test(page, zero_json, './output/test2')

def test_one(page):
    run_test(page, one_json, './output/test3')

def test_handred_1(page):
    run_test(page, handred_1_json, './output/test4')

def test_handred_2(page):
    run_test(page, handred_2_json, './output/test5')

def test_thousand_1(page):
    run_test(page, thousand_1_json, './output/test6')
