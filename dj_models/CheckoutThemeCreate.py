class CheckoutThemeCreate(models.Model):
    shop = models.Shop()
    shopErrors = models.ShopError()

