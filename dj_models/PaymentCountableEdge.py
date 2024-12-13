class PaymentCountableEdge(models.Model):
    node = models.Payment()
    cursor = models.String()

