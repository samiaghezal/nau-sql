class ProductImage(models.Model):
    id = models.ID()
    sortOrder = models.Int()
    externalId = models.String()
    externalSource = models.String()
    alt = models.String()
    url = models.String()

