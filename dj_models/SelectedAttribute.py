class SelectedAttribute(models.Model):
    attribute = models.Attribute()
    values = models.AttributeValue()
    templated = models.Boolean()

