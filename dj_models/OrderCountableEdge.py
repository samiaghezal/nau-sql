class OrderCountableEdge(models.Model):
    node = models.Order()
    cursor = models.String()

