class VoucherUpdate(models.Model):
    discountErrors = models.DiscountError()
    voucher = models.Voucher()

