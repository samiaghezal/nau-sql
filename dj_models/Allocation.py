class Allocation(models.Model):
    id = models.ID()
    quantity = models.Int()
    warehouse = models.Warehouse()

