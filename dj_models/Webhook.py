class Webhook(models.Model):
    name = models.String()
    targetUrl = models.String()
    isActive = models.Boolean()
    secretKey = models.String()
    connectionString = models.String()
    queueName = models.String()
    id = models.ID()
    events = models.WebhookEvent()
    app = models.App()

