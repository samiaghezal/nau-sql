class CheckoutLineAddNote(models.Model):
    checkoutErrors = models.CheckoutError()
    checkoutLine = models.CheckoutLine()

