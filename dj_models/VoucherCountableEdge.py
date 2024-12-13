class VoucherCountableEdge(models.Model):
    node = models.Voucher()
    cursor = models.String()

