class NauticalOrderPaymentCreate(models.Model):
    order = models.NauticalOrder()
    payment = models.Payment()
    paymentErrors = models.PaymentError()

