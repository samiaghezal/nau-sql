class CheckoutCountableEdge(models.Model):
    node = models.Checkout()
    cursor = models.String()

