class CheckoutLineCountableEdge(models.Model):
    node = models.CheckoutLine()
    cursor = models.String()

