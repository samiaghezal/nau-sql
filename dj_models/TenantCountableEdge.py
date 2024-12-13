class TenantCountableEdge(models.Model):
    node = models.Tenant()
    cursor = models.String()

