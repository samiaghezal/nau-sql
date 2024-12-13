class ShopAddressUpdate(models.Model):
    shop = models.Shop()
    shopErrors = models.ShopError()

