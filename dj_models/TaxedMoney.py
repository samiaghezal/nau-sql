class TaxedMoney(models.Model):
    currency = models.String()
    gross = models.Money()
    net = models.Money()
    tax = models.Money()

