class WarehouseUpdate(models.Model):
    warehouseErrors = models.WarehouseError()
    warehouse = models.Warehouse()

