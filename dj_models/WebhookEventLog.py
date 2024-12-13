class WebhookEventLog(models.Model):
    id = models.ID()
    tenant = models.Tenant()
    date = models.DateTime()
    targetUrl = models.String()
    eventType = models.String()
    webhookId = models.String()
    transactionId = models.String()
    appId = models.String()
    pluginId = models.String()
    payload = models.JSONString()
    error = models.String()
    direction = models.WebhookDirectionEnum()

