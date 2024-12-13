class CheckoutConvertToNauticalQuoteOrder(models.Model):
    order = models.NauticalOrder()
    checkoutErrors = models.CheckoutError()

