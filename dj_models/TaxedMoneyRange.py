class TaxedMoneyRange(models.Model):
    start = models.TaxedMoney()
    stop = models.TaxedMoney()

