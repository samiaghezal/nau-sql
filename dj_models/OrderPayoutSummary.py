class OrderPayoutSummary(models.Model):
    commissions = models.Money()
    discounts = models.Money()
    fees = models.Money()
    refunds = models.Money()
    refundsCommission = models.Money()
    sales = models.Money()
    shipping = models.Money()
    total = models.Money()
    vendorPayout = models.VendorPayout()

