class InReportMarketplaceTaxSummaryType(models.Model):
    category = models.String()
    title = models.String()
    columns = models.ColumnObjectType()
    filters = models.FilterObjectType()
    summary = models.AbstractOrderSellerReportType()
    report = models.MarketplaceTaxReportType()

