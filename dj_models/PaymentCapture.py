class PaymentCapture(models.Model):
    payment = models.Payment()
    paymentErrors = models.PaymentError()

