class AgreementCountableEdge(models.Model):
    node = models.Agreement()
    cursor = models.String()

