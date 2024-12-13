class SellerOnboardingSettingsCreate(models.Model):
    shop = models.Shop()
    shopErrors = models.ShopError()

