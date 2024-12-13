class RefundLineCountableEdge(models.Model):
    node = models.RefundLine()
    cursor = models.String()

