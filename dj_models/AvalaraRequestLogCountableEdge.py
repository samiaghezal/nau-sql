class AvalaraRequestLogCountableEdge(models.Model):
    node = models.AvalaraRequestLog()
    cursor = models.String()

