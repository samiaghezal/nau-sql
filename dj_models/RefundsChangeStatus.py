class RefundsChangeStatus(models.Model):
    count = models.Int()
    refundErrors = models.RefundError()

