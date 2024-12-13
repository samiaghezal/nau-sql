class AttributeValueBulkCreate(models.Model):
    count = models.Int()
    attributeValues = models.AttributeValue()
    attributeErrors = models.AttributeError()

