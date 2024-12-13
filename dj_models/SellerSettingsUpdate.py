class SellerSettingsUpdate(models.Model):
    seller = models.Seller()
    sellerErrors = models.SellerError()

