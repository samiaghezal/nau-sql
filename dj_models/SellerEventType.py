class SellerEventType(models.Model):
    id = models.ID()
    date = models.DateTime()
    type = models.SellerEventsEnum()
    user = models.User()
    parameters = models.JSONString()
    status = models.String()
    message = models.String()
    seller = models.Seller()

