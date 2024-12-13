class TypeformForm(models.Model):
    id = models.String()
    title = models.String()
    language = models.String()
    fields = models.TypeformFormFields()
    hidden = models.String()

