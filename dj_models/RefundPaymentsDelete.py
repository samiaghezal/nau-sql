class RefundPaymentsDelete(models.Model):
    count = models.Int()
    refundErrors = models.RefundError()

