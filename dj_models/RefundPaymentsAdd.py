class RefundPaymentsAdd(models.Model):
    refund = models.Refund()
    refundErrors = models.RefundError()

