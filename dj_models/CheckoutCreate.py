class CheckoutCreate(models.Model):
    created = models.Boolean()
    checkoutErrors = models.CheckoutError()
    checkout = models.Checkout()

