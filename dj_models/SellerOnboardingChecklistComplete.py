class SellerOnboardingChecklistComplete(models.Model):
    checklist = models.SellerOnboardingChecklist()
    checklistErrors = models.SellerOnboardingChecklistError()

