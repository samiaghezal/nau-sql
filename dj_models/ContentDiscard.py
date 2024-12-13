class ContentDiscard(models.Model):
    content = models.Content()
    shopErrors = models.ShopError()

