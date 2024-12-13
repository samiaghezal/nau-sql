class TypeformFormFields(models.Model):
    attachment = models.TypeformFormAttachment()
    fieldType = models.String()
    id = models.String()
    layout = models.TypeformFormLayout()
    name = models.String()
    options = models.TypeformFormOption()
    ref = models.String()
    required = models.Boolean()
    title = models.String()
    properties = models.TypeformFormProperties()
    type = models.String()

