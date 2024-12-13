class InReportMarketplaceTaxesByCountryType(models.Model):
    category = models.String()
    title = models.String()
    columns = models.ColumnObjectType()
    filters = models.FilterObjectType()
    summary = models.AbstractOrderSellerReportType()
    report = models.MarketplaceTaxReportByLocaleType()

