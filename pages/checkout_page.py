class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"

        self.continue_button = "#continue"
        self.finish_button = "#finish"

        self.success_message = ".complete-header"

    def complete_checkout(self):

        self.page.fill(self.first_name, "Shubham")
        self.page.fill(self.last_name, "Mirani")
        self.page.fill(self.postal_code, "364001")

        self.page.click(self.continue_button)
        self.page.click(self.finish_button)

    def get_success_message(self):

        return self.page.locator(
            self.success_message
        ).inner_text()