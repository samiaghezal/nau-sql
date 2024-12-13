class ProductVariantBulkCreate(models.Model):
    count = models.Int()
    productVariants = models.ProductVariant()
    bulkProductErrors = models.BulkProductError()

