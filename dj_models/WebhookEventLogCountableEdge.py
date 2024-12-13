class WebhookEventLogCountableEdge(models.Model):
    node = models.WebhookEventLog()
    cursor = models.String()

