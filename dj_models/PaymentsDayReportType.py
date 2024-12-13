class PaymentsDayReportType(models.Model):
    payments = models.Int()
    totalAuthorized = models.Float()
    captured = models.Float()
    average = models.Float()
    dimension = models.Date()
    chargeStatus = models.String()

