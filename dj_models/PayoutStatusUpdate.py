class PayoutStatusUpdate(models.Model):
    payout = models.Payout()
    payoutErrors = models.PayoutError()

