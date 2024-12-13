class SellerOnboardingSettings(models.Model):
    id = models.ID()
    isAcceptingNewSellers = models.Boolean()
    summary = models.String()
    welcomeMessage = models.String()
    fulfillmentModel = models.String()
    requiredDocuments = models.String()
    notAcceptingSellersMessage = models.String()
    isProductImportAllowed = models.Boolean()

