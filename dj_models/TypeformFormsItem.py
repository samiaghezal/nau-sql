class TypeformFormsItem(models.Model):
    Links = models.TypeformFormsItemLink()
    id = models.String()
    lastUpdatedAt = models.String()
    self = models.TypeformFormsItemSelf()
    theme = models.TypeformFormsItemSelf()
    title = models.String()

