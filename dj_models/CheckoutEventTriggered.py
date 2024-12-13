class CheckoutEventTriggered(models.Model):
    checkoutEvent = models.CheckoutEvent()
    pluginsErrors = models.PluginError()

