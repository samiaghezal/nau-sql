class RefundUpdate(models.Model):
    refundErrors = models.RefundError()
    refund = models.Refund()

