class Money(models.Model):
    currency = models.String()
    baseAmount = models.BigInt()

