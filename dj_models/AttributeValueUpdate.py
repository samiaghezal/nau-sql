class AttributeValueUpdate(models.Model):
    attribute = models.Attribute()
    productErrors = models.ProductError()
    attributeValue = models.AttributeValue()

