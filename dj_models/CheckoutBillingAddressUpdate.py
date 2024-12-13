class CheckoutBillingAddressUpdate(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

