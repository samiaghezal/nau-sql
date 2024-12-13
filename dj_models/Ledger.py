class Ledger(models.Model):
    id = models.ID()
    accountType = models.LedgerAccountTypeEnum()
    balance = models.Money()
    seller = models.Seller()
    type = models.LedgerTypeEnum()
    version = models.BigInt()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    buyer = models.User()

