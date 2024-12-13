class DesignerDataType(models.Model):
    tenant = models.Tenant()
    id = models.ID()
    name = models.String()
    jsonContent = models.JSONString()

