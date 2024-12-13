class SellerOnboardingChecklist(models.Model):
    id = models.ID()
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    tenant = models.Tenant()
    seller = models.Seller()
    position = models.Int()
    title = models.String()
    description = models.String()
    completeOn = models.SellerChecklistCompletionTriggersEnum()
    completedAt = models.DateTime()

