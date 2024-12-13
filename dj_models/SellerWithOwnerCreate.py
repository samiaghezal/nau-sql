class SellerWithOwnerCreate(models.Model):
    seller = models.Seller()
    sellerErrors = models.SellerError()

