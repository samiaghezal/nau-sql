class CustomersExport(models.Model):
    ok = models.Boolean()
    plugin = models.ID()
    pluginsErrors = models.PluginError()

