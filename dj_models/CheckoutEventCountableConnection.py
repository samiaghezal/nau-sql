class CheckoutEventCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.CheckoutEventCountableEdge()
    totalCount = models.Int()

