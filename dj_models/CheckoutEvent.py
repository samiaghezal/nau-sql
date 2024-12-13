class CheckoutEvent(models.Model):
    tenant = models.Tenant()
    id = models.ID()
    createdAt = models.DateTime()
    type = models.CheckoutEventType()
    checkoutId = models.String()

