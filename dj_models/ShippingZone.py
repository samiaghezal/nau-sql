class ShippingZone(models.Model):
    id = models.ID()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    name = models.String()
    seller = models.Seller()
    warehouses = models.Warehouse()
    priceRange = models.MoneyRange()
    countries = models.CountryDisplay()
    shippingMethods = models.ShippingMethod()
    countryAreas = models.ShippingZoneCountryArea()

