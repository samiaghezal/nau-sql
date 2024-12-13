class NauticalOrderEventCountableEdge(models.Model):
    node = models.NauticalOrderEvent()
    cursor = models.String()

