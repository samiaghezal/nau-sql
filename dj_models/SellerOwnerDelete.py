class SellerOwnerDelete(models.Model):
    seller = models.Seller()
    sellerErrors = models.SellerError()

