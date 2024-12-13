class VoucherBulkDelete(models.Model):
    count = models.Int()
    discountErrors = models.DiscountError()

