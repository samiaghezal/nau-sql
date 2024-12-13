class WebhookJobCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.WebhookJobCountableEdge()
    totalCount = models.Int()

