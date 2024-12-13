class SellerOnboardingChecklistError(models.Model):
    field = models.String()
    message = models.String()
    code = models.SellerOnboardingChecklistErrorCode()

