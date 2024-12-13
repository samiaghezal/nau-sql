class RefundPaymentCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.RefundPaymentCountableEdge()
    totalCount = models.Int()

