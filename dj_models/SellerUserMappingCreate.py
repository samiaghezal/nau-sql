class SellerUserMappingCreate(models.Model):
    ok = models.Boolean()
    sellerUser = models.SellerUserType()
    sellerErrors = models.SellerError()

