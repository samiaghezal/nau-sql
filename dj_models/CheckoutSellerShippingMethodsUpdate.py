class CheckoutSellerShippingMethodsUpdate(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()
