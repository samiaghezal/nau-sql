class FinancialError(models.Model):
    field = models.String()
    message = models.String()
    code = models.FinancialErrorCode()

