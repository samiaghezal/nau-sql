class EmailTemplateCountableEdge(models.Model):
    node = models.EmailTemplate()
    cursor = models.String()

