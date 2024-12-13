class ProductVariantStocksUpdate(models.Model):
    productVariant = models.ProductVariant()
    bulkStockErrors = models.BulkStockError()

