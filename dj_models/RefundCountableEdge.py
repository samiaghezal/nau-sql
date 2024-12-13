class RefundCountableEdge(models.Model):
    node = models.Refund()
    cursor = models.String()

