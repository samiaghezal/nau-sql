class CheckoutDelete(models.Model):
    checkoutErrors = models.CheckoutError()
    checkout = models.Checkout()

