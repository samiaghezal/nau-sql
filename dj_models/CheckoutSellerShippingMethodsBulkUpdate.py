class CheckoutSellerShippingMethodsBulkUpdate(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

