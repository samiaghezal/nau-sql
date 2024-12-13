class WebhookJobCountableEdge(models.Model):
    node = models.WebhookJob()
    cursor = models.String()

