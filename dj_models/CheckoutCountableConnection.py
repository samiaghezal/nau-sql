class CheckoutCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.CheckoutCountableEdge()
    totalCount = models.Int()

