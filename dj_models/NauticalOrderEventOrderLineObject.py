class NauticalOrderEventOrderLineObject(models.Model):
    quantity = models.Int()
    orderLine = models.NauticalOrderLine()
    itemName = models.String()

