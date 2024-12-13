class MicrositeCountableEdge(models.Model):
    node = models.Microsite()
    cursor = models.String()

