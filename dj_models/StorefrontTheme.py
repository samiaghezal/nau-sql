class StorefrontTheme(models.Model):
    id = models.ID()
    primaryColor = models.String()
    backgroundColor = models.String()
    logo = models.Image()
    faviconImage = models.Image()
    faviconUrl = models.String()
    font = models.Font()
    fontColor = models.String()

