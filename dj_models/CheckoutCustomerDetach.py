class CheckoutCustomerDetach(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

