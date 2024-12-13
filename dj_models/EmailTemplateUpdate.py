class EmailTemplateUpdate(models.Model):
    emailTemplate = models.EmailTemplate()
    notificationErrors = models.NotificationError()

