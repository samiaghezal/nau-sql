class CheckoutCustomerAttach(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

