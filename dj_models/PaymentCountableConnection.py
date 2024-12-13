class PaymentCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.PaymentCountableEdge()
    totalCount = models.Int()

