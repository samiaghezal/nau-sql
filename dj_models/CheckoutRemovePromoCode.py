class CheckoutRemovePromoCode(models.Model):
    checkout = models.Checkout()
    checkoutErrors = models.CheckoutError()

