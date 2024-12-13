class UserAvatarDelete(models.Model):
    user = models.User()
    accountErrors = models.AccountError()

