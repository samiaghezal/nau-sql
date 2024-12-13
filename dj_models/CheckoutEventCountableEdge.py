class CheckoutEventCountableEdge(models.Model):
    node = models.CheckoutEvent()
    cursor = models.String()

