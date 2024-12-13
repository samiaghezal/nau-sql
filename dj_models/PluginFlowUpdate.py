class PluginFlowUpdate(models.Model):
    flow = models.Flow()
    pluginsErrors = models.PluginError()

