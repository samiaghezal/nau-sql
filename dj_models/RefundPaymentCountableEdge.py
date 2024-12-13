class RefundPaymentCountableEdge(models.Model):
    node = models.RefundPayment()
    cursor = models.String()

