class NauticalOrderCountableEdge(models.Model):
    node = models.NauticalOrder()
    cursor = models.String()

