class WebhookUpdate(models.Model):
    webhookErrors = models.WebhookError()
    webhook = models.Webhook()

