class CheckoutSetTransactionCurrency(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

