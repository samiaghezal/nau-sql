class RefundBulkDelete(models.Model):
    count = models.Int()
    refundErrors = models.RefundError()

