class CustomerEvent(models.Model):
    id = models.ID()
    date = models.DateTime()
    type = models.CustomerEventsEnum()
    user = models.User()
    message = models.String()
    count = models.Int()
    order = models.Order()
    orderLine = models.OrderLine()
    nauticalOrder = models.NauticalOrder()

