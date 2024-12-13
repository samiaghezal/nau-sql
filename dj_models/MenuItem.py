class MenuItem(models.Model):
    id = models.ID()
    menu = models.Menu()
    name = models.String()
    parent = models.MenuItem()
    category = models.Category()
    collection = models.Collection()
    page = models.Page()
    level = models.Int()
    children = models.MenuItem()
    url = models.String()

