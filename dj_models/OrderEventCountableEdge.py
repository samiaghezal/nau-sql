class OrderEventCountableEdge(models.Model):
    node = models.OrderEvent()
    cursor = models.String()

