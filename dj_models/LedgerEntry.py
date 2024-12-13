class LedgerEntry(models.Model):
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    id = models.ID()
    journalEntry = models.JournalEntry()
    ledger = models.Ledger()
    ledgerVersion = models.BigInt()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    amount = models.Money()
    ledgerBalance = models.Money()

