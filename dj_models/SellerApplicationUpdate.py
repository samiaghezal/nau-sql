class SellerApplicationUpdate(models.Model):
    seller = models.Seller()
    sellerErrors = models.SellerError()

