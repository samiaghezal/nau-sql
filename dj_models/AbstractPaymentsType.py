class AbstractPaymentsType(models.Model):
    payments = models.Int()
    totalAuthorized = models.Float()
    captured = models.Float()
    average = models.Float()

