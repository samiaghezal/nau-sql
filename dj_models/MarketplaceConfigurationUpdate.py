class MarketplaceConfigurationUpdate(models.Model):
    marketplaceConfiguration = models.MarketplaceConfiguration()
    marketplaceConfigurationErrors = models.MarketplaceConfigurationError()

