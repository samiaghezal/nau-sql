class DefaultSellerChecklist(models.Model):
    title = models.String()
    description = models.String()
    completeOn = models.SellerChecklistCompletionTriggersEnum()
    isEnabled = models.Boolean()

