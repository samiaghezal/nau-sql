class VariantSize(models.Model):
    length = models.Decimal()
    width = models.Decimal()
    height = models.Decimal()
    sizeUnits = models.DistanceUnitsEnum()

