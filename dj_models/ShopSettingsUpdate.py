class ShopSettingsUpdate(models.Model):
    shop = models.Shop()
    shopErrors = models.ShopError()

