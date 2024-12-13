class DigitalContentUrl(models.Model):
    content = models.DigitalContent()
    created = models.DateTime()
    downloadNum = models.Int()
    id = models.ID()
    url = models.String()
    token = models.NauticalUUID()

