class ShippingError(models.Model):
    field = models.String()
    message = models.String()
    code = models.ShippingErrorCode()
    warehouses = models.ID()

