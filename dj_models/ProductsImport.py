class ProductsImport(models.Model):
    importFile = models.ImportFile()
    importErrors = models.ImportError()

