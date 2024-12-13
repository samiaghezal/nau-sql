class OrderEventOrderLineObject(models.Model):
    quantity = models.Int()
    orderLine = models.OrderLine()
    itemName = models.String()

