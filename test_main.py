import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.smoke
@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Menu Item Navigation')
@allure.description('Verifies that each menu item on the homepage navigates to the correct page and displays the correct heading.')
@allure.severity(allure.severity_level.CRITICAL)
def test_menu_item(driver):

    with allure.step("Opening the homepage"):
        driver.get("https://tutorialsninja.com/demo/")


    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs",  "Cameras", "MP3 Players"]

    with allure.step(f"Clicking on menu item: {expected_menu_items[0]}"):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[1]}"):
        menu_item2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item2.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[2]}"):
        menu_item3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item3.click()

    with allure.step(f"Clicking on menu item: {expected_menu_items[3]}"):
        menu_item4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item4.click()


    with allure.step(f"Verifying the page heading for {expected_menu_items[4]}"):
        menu_item5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_item5.click()
    assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4]

    with allure.step(f"Verifying the page heading for {expected_menu_items[5]}"):

        menu_item6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_item6.click()

    assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5]

    with allure.step(f"Verifying the page heading for {expected_menu_items[6]}"):
        menu_item7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item7.click()

    assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6]

    with allure.step(f"Verifying the page heading for {expected_menu_items[7]}"):
        menu_item8 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_item8.click()








@pytest.mark.parametrize("menu_locator, submenu_locator, result_text", [
    (
            (By.PARTIAL_LINK_TEXT, 'Desktops'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Desktop'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, 'Laptops & Notebooks'),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )
])

@pytest.mark.regression
@pytest.mark.smoke
@allure.feature('Menu Navigation')
@allure.suite('UI Tests')
@allure.title('Test Nested Menu Item Navigation')
@allure.description('Verifies that each nested menu item on the homepage navigates to the correct page and displays the correct heading.')
@allure.severity(allure.severity_level.CRITICAL)
def test_nested_menu(driver, menu_locator, submenu_locator, result_text):
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step(f'Navigating to submenu: {submenu_locator} under menu: {menu_locator}'):
        menu = driver.find_element(*menu_locator)
        submenu = driver.find_element(*submenu_locator)
        ActionChains(driver).move_to_element(menu).click(submenu).perform()

    with allure.step(f'Verifying the page heading is: {result_text}'):
        heading_text = driver.find_element(By.TAG_NAME, 'h2').text
        assert heading_text == result_text, f"Expected heading '{result_text}', but got '{heading_text}'"

@pytest.mark.regression
@pytest.mark.smoke
@allure.feature('Search Functionality')
@allure.suite('UI Tests')
@allure.title('Test Product Search')
@allure.description('Verifies that searching for "MacBook" returns relevant products.')
@allure.severity(allure.severity_level.CRITICAL)
def test_search_product(driver):
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Searching for the product "MacBook"'):
        search = driver.find_element(By.NAME, 'search')
        search.send_keys('MacBook')
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
        button.click()

    with allure.step('Verifying that all displayed products contain "MacBook"'):
        products = driver.find_elements(By.TAG_NAME, 'h4')
        new_list = [elem.text for elem in products if 'MacBook' in elem.text]
        assert len(products) == len(
            new_list), f"Some products do not contain 'MacBook'. Found: {[elem.text for elem in products]}"


@pytest.mark.regression
@allure.feature('Cart Functionality')
@allure.suite('UI Tests')
@allure.title('Test Adding Product to Cart')
@allure.description('Verifies that a product can be successfully added to the cart and appears in the cart dropdown.')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart(driver):
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")
        time.sleep(2)

    with allure.step('Adding the first product (MacBook) to the cart'):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
        product.click()

    with allure.step('Verifying the success message for adding the product'):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )
        assert "Success: You have added" in success_message.text, "Product not added successfully."

    with allure.step('Verifying the cart total shows 1 item'):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )

    with allure.step('Opening the cart dropdown'):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart"))
        )
        cart_button.click()

    with allure.step('Verifying the product is in the cart'):
        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.pull-right"))
        )
        assert "MacBook" in cart_contents.text, f"Expected 'MacBook' in cart, but got {cart_contents.text}"




@pytest.mark.smoke
@allure.feature('Homepage Slideshow')
@allure.suite('UI Tests')
@allure.title('Test Slider Functionality')
@allure.description('Verifies that the homepage slider is visible and the next button works to navigate to the next image.')
@allure.severity(allure.severity_level.NORMAL)
def test_slider_functionality(driver):
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Checking if the slider is visible'):
        slider = driver.find_element(By.CLASS_NAME, "swiper-container")
        assert slider.is_displayed(), "Slider is not visible on the page."


    with allure.step('Capturing the first slide image'):
        first_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        first_slide_src = first_slide.get_attribute("src")

    with allure.step('Clicking the next arrow on the slider'):
        next_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-next')
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

    # Step to verify the slide has changed
    with allure.step('Verifying that the slider moves to the next image'):
        WebDriverWait(driver, 15).until_not(
            EC.element_to_be_clickable(first_slide)
        )
        new_slide = driver.find_element(By.CSS_SELECTOR, ".swiper-slide-active img")
        new_slide_src = new_slide.get_attribute("src")
        assert first_slide_src != new_slide_src, "Slider did not move to the next image."


@pytest.mark.regression
@allure.feature('Wishlist Functionality')
@allure.suite('UI Tests')
@allure.title('Test Adding Product to Wishlist')
@allure.description('Verifies that a product can be successfully added to the wishlist and appears in the wishlist page.')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_wishlist(driver, login):
    with allure.step('Logging in and opening the homepage'):

        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Adding the first product (MacBook) to the wishlist'):
        wishlist_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]'))
        )
        wishlist_button.click()

    with allure.step('Verifying the success message for adding to wishlist'):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )
        assert "Success: You have added" in success_message.text, "Wishlist add failed"

    with allure.step('Navigating to the wishlist page'):
        wishlist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="wishlist-total"]'))
        )
        wishlist_link.click()

    with allure.step('Verifying the product is in the wishlist'):
        wishlist_contents = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr[2]/td[2]/a'))
        )
        assert "MacBook" in wishlist_contents.text, "MacBook not found in wishlist"



@pytest.mark.parametrize("button, header, expected_text", [
    (
        (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "About Us"

    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Contact Us"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Product Returns"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Find Your Favorite Brand"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Purchase a Gift Certificate"
    )
])
@pytest.mark.regression
@pytest.mark.smoke
@allure.feature('Footer Navigation')
@allure.suite('UI Tests')
@allure.title('Test Footer Links')
@allure.description('Verifies that clicking on a footer link navigates to the correct page and displays the expected header.')
@allure.severity(allure.severity_level.NORMAL)
def test_footer(driver, button, header, expected_text):
    # Step to open the homepage
    with allure.step('Opening the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    # Step to click on the footer link
    with allure.step('Clicking on the specified footer link'):
        footer_button = driver.find_element(*button)
        footer_button.click()

    # Step to verify the header text on the navigated page
    with allure.step(f'Verifying the header text is "{expected_text}"'):
        footer_header_text = driver.find_element(*header).text
        assert footer_header_text == expected_text, f"Expected '{expected_text}' but got '{footer_header_text}'"












