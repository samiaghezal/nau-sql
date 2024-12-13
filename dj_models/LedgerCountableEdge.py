class LedgerCountableEdge(models.Model):
    node = models.Ledger()
    cursor = models.String()

