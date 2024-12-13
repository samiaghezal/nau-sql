class CheckoutComplete(models.Model):
    order = models.NauticalOrder()
    confirmationNeeded = models.Boolean()
    confirmationData = models.JSONString()
    checkoutErrors = models.CheckoutError()

