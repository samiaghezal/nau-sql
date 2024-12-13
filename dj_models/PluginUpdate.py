class PluginUpdate(models.Model):
    plugin = models.Plugin()
    pluginsErrors = models.PluginError()

