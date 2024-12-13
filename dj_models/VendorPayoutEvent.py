class VendorPayoutEvent(models.Model):
    id = models.ID()
    parameters = models.JSONString()
    date = models.DateTime()
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    type = models.VendorPayoutEventsEnum()
    user = models.User()
    message = models.String()

