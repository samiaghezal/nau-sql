class Tenant(models.Model):
    id = models.ID()
    name = models.String()
    isActive = models.Boolean()

