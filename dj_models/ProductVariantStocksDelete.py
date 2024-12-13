class ProductVariantStocksDelete(models.Model):
    productVariant = models.ProductVariant()
    stockErrors = models.StockError()

