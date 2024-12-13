class JournalEntryCorrect(models.Model):
    financialErrors = models.FinancialError()
    journalEntry = models.JournalEntry()

