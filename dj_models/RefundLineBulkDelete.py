class RefundLineBulkDelete(models.Model):
    count = models.Int()
    refundErrors = models.RefundError()

