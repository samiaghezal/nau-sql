class PaymentSource(models.Model):
    id = models.String()
    gateway = models.String()
    creditCardInfo = models.CreditCard()

