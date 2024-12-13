class AbstractPercentReportType(models.Model):
    gross = models.Float()
    orders = models.Float()
    net = models.Float()
    shipping = models.Float()
    average = models.Float()
    taxes = models.Float()
    discounts = models.Float()
    volumeDiscounts = models.Float()
    revenue = models.Float()
    totals = models.Float()

