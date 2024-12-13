class PageUpdate(models.Model):
    pageErrors = models.PageError()
    page = models.Page()

