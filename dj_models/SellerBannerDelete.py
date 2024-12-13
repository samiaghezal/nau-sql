class SellerBannerDelete(models.Model):
    seller = models.Seller()
    sellerErrors = models.SellerError()

