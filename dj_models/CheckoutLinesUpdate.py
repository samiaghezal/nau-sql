class CheckoutLinesUpdate(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

