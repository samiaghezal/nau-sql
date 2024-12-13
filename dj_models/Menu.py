class Menu(models.Model):
    id = models.ID()
    name = models.String()
    slug = models.String()
    items = models.MenuItem()

