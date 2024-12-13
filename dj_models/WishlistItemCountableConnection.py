class WishlistItemCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.WishlistItemCountableEdge()
    totalCount = models.Int()

