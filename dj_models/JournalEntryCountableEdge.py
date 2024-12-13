class JournalEntryCountableEdge(models.Model):
    node = models.JournalEntry()
    cursor = models.String()

