class StockEvent(models.Model):
    id = models.ID()
    date = models.DateTime()
    type = models.StockEventType()
    stock = models.Stock()
    parameters = models.JSONString()
    user = models.User()

