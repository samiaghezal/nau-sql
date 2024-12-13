class PageBulkDelete(models.Model):
    count = models.Int()
    pageErrors = models.PageError()

