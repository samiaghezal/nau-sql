class SellerUserType(models.Model):
    id = models.ID()
    tenant = models.Tenant()
    seller = models.Seller()
    user = models.User()
    isDefault = models.Boolean()

