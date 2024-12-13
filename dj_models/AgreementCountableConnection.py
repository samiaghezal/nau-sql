class AgreementCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.AgreementCountableEdge()
    totalCount = models.Int()

