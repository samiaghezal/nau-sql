class CheckoutNoteUpdate(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

