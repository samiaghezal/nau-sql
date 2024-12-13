class ShopDomainUpdate(models.Model):
    shop = models.Shop()
    shopErrors = models.ShopError()

