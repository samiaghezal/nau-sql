class ProductsExport(models.Model):
    exportFile = models.ExportFile()
    exportErrors = models.ExportError()

