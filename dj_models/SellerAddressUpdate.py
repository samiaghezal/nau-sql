class SellerAddressUpdate(models.Model):
    seller = models.Seller()
    sellerErrors = models.SellerError()
    address = models.Address()

