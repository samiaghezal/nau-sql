class NauticalOrderUpdateApplyVoucherCode(models.Model):
    nauticalOrder = models.NauticalOrder()
    orderErrors = models.OrderError()

