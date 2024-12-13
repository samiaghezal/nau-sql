class SaleRemoveCatalogues(models.Model):
    sale = models.Sale()
    discountErrors = models.DiscountError()

