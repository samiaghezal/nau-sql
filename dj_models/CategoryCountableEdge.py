class CategoryCountableEdge(models.Model):
    node = models.Category()
    cursor = models.String()

