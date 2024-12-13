class AbstractOrderSellerReportType(models.Model):
    gross = models.Float()
    orders = models.Int()
    net = models.Float()
    shipping = models.Float()
    average = models.Float()
    taxes = models.Float()
    discounts = models.Float()
    volumeDiscounts = models.Float()
    revenue = models.Float()
    totals = models.Int()
    commission = models.Float()
    payout = models.Float()

