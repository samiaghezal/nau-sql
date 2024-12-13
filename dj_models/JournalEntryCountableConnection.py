class JournalEntryCountableConnection(models.Model):
    pageInfo = models.PageInfo()
    edges = models.JournalEntryCountableEdge()
    totalCount = models.Int()

