class WebhookDelete(models.Model):
    webhookErrors = models.WebhookError()
    webhook = models.Webhook()

