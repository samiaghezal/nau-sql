class DigitalContentCountableEdge(models.Model):
    node = models.DigitalContent()
    cursor = models.String()

