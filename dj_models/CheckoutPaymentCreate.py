class CheckoutPaymentCreate(models.Model):
    checkout = models.Checkout()
    payment = models.Payment()
    paymentErrors = models.PaymentError()

