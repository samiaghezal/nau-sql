class TypeformForms(models.Model):
    totalItems = models.Int()
    pageCount = models.Int()
    items = models.TypeformFormsItem()

