class VendorPayoutOnboardingLinkRequest(models.Model):
    link = models.String()
    vendor = models.Vendor()
    pluginsErrors = models.PluginError()

