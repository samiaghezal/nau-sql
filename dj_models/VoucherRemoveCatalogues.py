class VoucherRemoveCatalogues(models.Model):
    voucher = models.Voucher()
    discountErrors = models.DiscountError()

