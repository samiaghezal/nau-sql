class SellerAddressSetDefault(models.Model):
    seller = models.Seller()
    sellerErrors = models.SellerError()

