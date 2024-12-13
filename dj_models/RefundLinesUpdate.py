class RefundLinesUpdate(models.Model):
    refund = models.Refund()
    refundErrors = models.RefundError()

