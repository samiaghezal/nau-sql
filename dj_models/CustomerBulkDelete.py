class CustomerBulkDelete(models.Model):
    count = models.Int()
    accountErrors = models.AccountError()

