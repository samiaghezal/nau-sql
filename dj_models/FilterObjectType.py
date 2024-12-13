class FilterObjectType(models.Model):
    display = models.String()
    fieldType = models.String()
    name = models.String()
    placeholder = models.String()
    required = models.Boolean()
    value = models.String()

