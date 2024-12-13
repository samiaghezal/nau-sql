class ProductVariantStocksCreate(models.Model):
    productVariant = models.ProductVariant()
    bulkStockErrors = models.BulkStockError()

