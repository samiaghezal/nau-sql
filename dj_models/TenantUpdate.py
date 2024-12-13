class TenantUpdate(models.Model):
    tenant = models.Tenant()
    tenantErrors = models.TenantError()

