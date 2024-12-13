class PayoutUpdate(models.Model):
    payout = models.Payout()
    payoutErrors = models.PayoutError()

