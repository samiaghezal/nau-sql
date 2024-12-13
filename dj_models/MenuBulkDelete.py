class MenuBulkDelete(models.Model):
    count = models.Int()
    menuErrors = models.MenuError()

