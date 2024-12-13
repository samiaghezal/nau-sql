class CheckoutLineCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.CheckoutLineCountableEdge()
    totalCount = models.Int()

