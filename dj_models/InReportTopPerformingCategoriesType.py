class InReportTopPerformingCategoriesType(models.Model):
    category = models.String()
    title = models.String()
    columns = models.ColumnObjectType()
    filters = models.FilterObjectType()
    summary = models.AbstractProductVariantType()
    report = models.ProductCategoryReportType()

