class ExportFileCountableEdge(models.Model):
    node = models.ExportFile()
    cursor = models.String()

