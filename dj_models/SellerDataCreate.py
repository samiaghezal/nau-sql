class SellerDataCreate(models.Model):
    ok = models.Boolean()
    seller = models.Seller()
    sellerErrors = models.SellerError()
