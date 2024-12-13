class ShippingZoneCountryArea(models.Model):
    id = models.ID()
    country = models.CountryDisplay()
    countryArea = models.CountryArea()

