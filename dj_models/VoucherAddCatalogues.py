class VoucherAddCatalogues(models.Model):
    voucher = models.Voucher()
    discountErrors = models.DiscountError()

