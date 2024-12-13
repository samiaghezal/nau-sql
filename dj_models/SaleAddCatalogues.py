class SaleAddCatalogues(models.Model):
    sale = models.Sale()
    discountErrors = models.DiscountError()

