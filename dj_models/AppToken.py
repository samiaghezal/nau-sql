class AppToken(models.Model):
    name = models.String()
    authToken = models.String()
    id = models.ID()

