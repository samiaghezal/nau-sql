class CustomFieldTemplate(models.Model):
    id = models.ID()
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    contentType = models.CustomFieldTemplateEnum()
    customAttributes = models.Attribute()

