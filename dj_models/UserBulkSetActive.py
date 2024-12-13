class UserBulkSetActive(models.Model):
    count = models.Int()
    accountErrors = models.AccountError()

