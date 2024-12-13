class DesignerDataCreate(models.Model):
    ok = models.Boolean()
    designerdata = models.DesignerDataType()
    designerErrors = models.MarketplaceConfigurationError()

