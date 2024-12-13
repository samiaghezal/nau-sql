class CountryDisplay(models.Model):
    code = models.String()
    country = models.String()
    requiredFields = models.String()
    allowedCountryAreas = models.String()
    detailedAllowedCountryAreas = models.CountryArea()

