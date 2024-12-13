class SellerLogoUpdate(models.Model):
    seller = models.Seller()
    sellerErrors = models.SellerError()

