class PageBulkPublish(models.Model):
    count = models.Int()
    pageErrors = models.PageError()

