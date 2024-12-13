class SellerUserTypeCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.SellerUserTypeCountableEdge()
    totalCount = models.Int()

