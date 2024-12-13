class SellerCountableEdge(models.Model):
    node = models.Seller()
    cursor = models.String()

