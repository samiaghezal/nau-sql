class RefundPaymentsUpdate(models.Model):
    refund = models.Refund()
    refundErrors = models.RefundError()

