class WebhookEventLogCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.WebhookEventLogCountableEdge()
    totalCount = models.Int()

