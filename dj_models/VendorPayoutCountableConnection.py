class VendorPayoutCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.VendorPayoutCountableEdge()
    totalCount = models.Int()

