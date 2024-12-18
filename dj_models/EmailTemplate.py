class EmailTemplate(models.Model):
    id = models.ID()
    title = models.String()
    subject = models.String()
    senderEmailAddress = models.String()
    content = models.String()
    defaultContent = models.String()
    renderedContent = models.String()
    description = models.String()
    isCustom = models.Boolean()
    isActive = models.Boolean()
    isEditable = models.Boolean()
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    recipientType = models.RecipientTypeEnum()
    eventType = models.EventTypeEnum()

