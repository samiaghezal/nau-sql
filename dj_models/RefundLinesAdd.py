class RefundLinesAdd(models.Model):
    refund = models.Refund()
    refundErrors = models.RefundError()

