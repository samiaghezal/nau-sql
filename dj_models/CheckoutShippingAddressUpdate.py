class CheckoutShippingAddressUpdate(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

