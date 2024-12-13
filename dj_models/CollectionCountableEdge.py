class CollectionCountableEdge(models.Model):
    node = models.Collection()
    cursor = models.String()

