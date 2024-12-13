class EmailTemplateCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.EmailTemplateCountableEdge()
    totalCount = models.Int()

