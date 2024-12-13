class CustomDomain(models.Model):
    id = models.ID()
    domain = models.String()
    status = models.DomainStatusEnum()
    errorDetails = models.String()
    sslCertName = models.String()

