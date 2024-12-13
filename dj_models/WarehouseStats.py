class WarehouseStats(models.Model):
    warehouseId = models.ID()
    quantity = models.Int()
    quantityAllocated = models.Int()
    quantityAvailable = models.Int()

