class InstanceAttributeUnassign(models.Model):
    instance = models.CustomFieldInstance()
    attributeErrors = models.AttributeError()

