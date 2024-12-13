class PayoutDelete(models.Model):
    payoutErrors = models.PayoutError()
    payout = models.Payout()

