from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_saucedemo_flow(page):


    # Open Website
    page.goto("https://www.saucedemo.com/")

    # Login
    login_page = LoginPage(page)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Inventory Page
    inventory_page = InventoryPage(page)

    # Sort Products High To Low
    inventory_page.sort_high_to_low()

    # Verify Sorting
    prices = inventory_page.get_all_prices()

    assert prices == sorted(
        prices,
        reverse=True
    )

    # Add Top Two Products
    inventory_page.add_top_two_products()

    # Go To Cart
    inventory_page.go_to_cart()

    # Cart Page
    cart_page = CartPage(page)

    cart_page.click_checkout()

    # Checkout Page
    checkout_page = CheckoutPage(page)

    checkout_page.complete_checkout()

    # Verify Success Message
    success_text = checkout_page.get_success_message()

    assert success_text == "Thank you for your order!"