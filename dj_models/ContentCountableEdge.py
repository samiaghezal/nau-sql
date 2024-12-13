class ContentCountableEdge(models.Model):
    node = models.Content()
    cursor = models.String()

