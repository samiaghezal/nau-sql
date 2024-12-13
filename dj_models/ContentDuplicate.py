class ContentDuplicate(models.Model):
    content = models.Content()
    shopErrors = models.ShopError()

