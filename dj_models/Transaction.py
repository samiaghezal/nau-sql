class Transaction(models.Model):
    id = models.ID()
    created = models.DateTime()
    payment = models.Payment()
    token = models.String()
    kind = models.TransactionKind()
    isSuccess = models.Boolean()
    error = models.String()
    amount = models.Money()

