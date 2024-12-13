class Weight(models.Model):
    unit = models.WeightUnitsEnum()
    value = models.Float()

