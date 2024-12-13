class SellerDetailCards(models.Model):
    sellerOrders = models.Int()
    sellerCommissions = models.Money()
    sellerSales = models.TaxedMoney()

