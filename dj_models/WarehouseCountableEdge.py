class WarehouseCountableEdge(models.Model):
    node = models.Warehouse()
    cursor = models.String()

