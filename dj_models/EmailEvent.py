class EmailEvent(models.Model):
    id = models.ID()
    tenant = models.Tenant()
    date = models.DateTime()
    fromEmail = models.String()
    toEmails = models.String()
    bccEmails = models.String()
    ccEmails = models.String()
    messageType = models.EmailEventMessageType()
    emailPluginId = models.String()
    template = models.String()
    payload = models.JSONString()
    error = models.String()

