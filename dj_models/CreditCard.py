class CreditCard(models.Model):
    brand = models.String()
    firstDigits = models.String()
    lastDigits = models.String()
    expMonth = models.Int()
    expYear = models.Int()

