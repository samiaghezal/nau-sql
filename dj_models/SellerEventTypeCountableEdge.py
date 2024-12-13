class SellerEventTypeCountableEdge(models.Model):
    node = models.SellerEventType()
    cursor = models.String()

