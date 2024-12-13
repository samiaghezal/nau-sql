class CheckoutAddPONumbers(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

