class PageCountableEdge(models.Model):
    node = models.Page()
    cursor = models.String()

