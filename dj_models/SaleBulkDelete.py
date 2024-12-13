class SaleBulkDelete(models.Model):
    count = models.Int()
    discountErrors = models.DiscountError()

