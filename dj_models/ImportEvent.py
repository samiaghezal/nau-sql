class ImportEvent(models.Model):
    id = models.ID()
    date = models.DateTime()
    type = models.ImportEventsEnum()
    user = models.User()
    app = models.App()
    message = models.String()

