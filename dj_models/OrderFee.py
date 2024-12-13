class OrderFee(models.Model):
    id = models.ID()
    tenant = models.Tenant()
    order = models.Order()
    currency = models.NauticalCurrency()
    transactionAmount = models.Decimal()
    transactionCurrency = models.NauticalCurrency()
    transactionFee = models.Money()
    domiciledAmount = models.Decimal()
    domiciledFee = models.Money()
    source = models.SourceFeeEnum()
    name = models.String()
    notes = models.String()
    data = models.JSONString()
