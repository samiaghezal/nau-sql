class Flow(models.Model):
    id = models.ID()
    tenant = models.Tenant()
    identifier = models.String()
    seller = models.Seller()
    process = models.FlowProcess()
    mapping = models.JSONString()
    formId = models.String()

