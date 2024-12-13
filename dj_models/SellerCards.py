class SellerCards(models.Model):
    newSellers = models.Int()
    sellerOrders = models.Int()
    sellerCommissions = models.Money()

