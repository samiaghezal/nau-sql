class EmailTemplatePreview(models.Model):
    id = models.ID()
    renderedContent = models.String()

