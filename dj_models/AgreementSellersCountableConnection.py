class AgreementSellersCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.AgreementSellersCountableEdge()
    totalCount = models.Int()

