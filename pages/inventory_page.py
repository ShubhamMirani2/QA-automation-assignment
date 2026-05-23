class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.sort_dropdown = ".product_sort_container"
        self.inventory_prices = ".inventory_item_price"
        self.add_to_cart_buttons = "button.btn_inventory"
        self.cart_icon = ".shopping_cart_link"

    def sort_high_to_low(self):

        self.page.select_option(
            self.sort_dropdown,
            "hilo"
        )

    def get_all_prices(self):

        prices = self.page.locator(
            self.inventory_prices
        ).all_inner_texts()

        return [
            float(price.replace("$", ""))
            for price in prices
        ]

    def add_top_two_products(self):

        buttons = self.page.locator(
            self.add_to_cart_buttons
        )

        buttons.nth(0).click()
        buttons.nth(1).click()

    def go_to_cart(self):

        self.page.click(self.cart_icon)