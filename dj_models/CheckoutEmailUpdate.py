class CheckoutEmailUpdate(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

