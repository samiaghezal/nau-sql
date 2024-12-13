class SellerBannerUpdate(models.Model):
    seller = models.Seller()
    sellerErrors = models.SellerError()

