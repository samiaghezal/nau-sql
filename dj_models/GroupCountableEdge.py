class GroupCountableEdge(models.Model):
    node = models.Group()
    cursor = models.String()

