class JournalEntry(models.Model):
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    id = models.ID()
    description = models.String()
    fulfillmentLine = models.FulfillmentLine()
    nauticalOrder = models.NauticalOrder()
    order = models.Order()
    orderLine = models.OrderLine()
    payment = models.Payment()
    refund = models.Refund()
    refundLine = models.RefundLine()
    vendorPayout = models.VendorPayout()
    type = models.JournalEntryTypeEnum()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    ledgerEntries = models.LedgerEntry()

