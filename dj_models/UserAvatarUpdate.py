class UserAvatarUpdate(models.Model):
    user = models.User()
    accountErrors = models.AccountError()

