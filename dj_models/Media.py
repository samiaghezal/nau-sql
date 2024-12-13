class Media(models.Model):
    tenant = models.Tenant()
    id = models.ID()
    title = models.String()
    createdAt = models.String()
    image = models.Image()
    alt = models.String()

