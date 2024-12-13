class MoneyRange(models.Model):
    start = models.Money()
    stop = models.Money()

