class MenuItemBulkDelete(models.Model):
    count = models.Int()
    menuErrors = models.MenuError()

