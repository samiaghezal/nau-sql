class CatalogImportProcessCountableEdge(models.Model):
    node = models.CatalogImportProcess()
    cursor = models.String()

