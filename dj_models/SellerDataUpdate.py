class SellerDataUpdate(models.Model):
    ok = models.Boolean()
    seller = models.Seller()
    sellerErrors = models.SellerError()

