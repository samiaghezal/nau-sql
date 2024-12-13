class PluginCountableEdge(models.Model):
    node = models.Plugin()
    cursor = models.String()

