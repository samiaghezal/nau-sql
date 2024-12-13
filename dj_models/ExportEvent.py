class ExportEvent(models.Model):
    id = models.ID()
    date = models.DateTime()
    type = models.ExportEventsEnum()
    user = models.User()
    app = models.App()
    message = models.String()

