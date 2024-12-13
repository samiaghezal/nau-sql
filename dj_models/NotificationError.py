class NotificationError(models.Model):
    field = models.String()
    message = models.String()
    code = models.NotificationErrorCode()

