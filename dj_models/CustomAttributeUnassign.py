class CustomAttributeUnassign(models.Model):
    customFieldTemplate = models.CustomFieldTemplate()
    attributeErrors = models.ProductError()

