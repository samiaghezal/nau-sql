class CheckoutRemovePONumbers(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()
