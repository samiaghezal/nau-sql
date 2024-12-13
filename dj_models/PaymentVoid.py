class PaymentVoid(models.Model):
    payment = models.Payment()
    paymentErrors = models.PaymentError()

