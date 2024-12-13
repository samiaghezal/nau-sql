class PayoutCountableEdge(models.Model):
    node = models.Payout()
    cursor = models.String()

