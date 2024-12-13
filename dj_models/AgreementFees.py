class AgreementFees(models.Model):
    id = models.ID()
    tenant = models.Tenant()
    agreement = models.Agreement()
    feeType = models.FeeType()
    feeScope = models.FeeScope()
    feeValue = models.Decimal()
    feeName = models.String()

