class WebhookEvent(models.Model):
    eventType = models.WebhookEventTypeEnum()
    name = models.String()

