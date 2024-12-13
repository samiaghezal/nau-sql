class TaxExemptCode(models.Model):
    code = models.String()
    name = models.String()
    description = models.String()
    validCountries = models.String()

