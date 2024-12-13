class DashboardTopSellerPerformanceType(models.Model):
    filters = models.FilterObjectType()
    current = models.DashboardSellerOrderPerformanceType()
    previous = models.DashboardSellerOrderPerformanceType()

