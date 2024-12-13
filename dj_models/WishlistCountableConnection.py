class WishlistCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.WishlistCountableEdge()
    totalCount = models.Int()

