class DigitalContentCreate(models.Model):
    variant = models.ProductVariant()
    content = models.DigitalContent()
    productErrors = models.ProductError()

