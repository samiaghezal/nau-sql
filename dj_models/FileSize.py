class FileSize(models.Model):
    bytes = models.BigInt()
    kilobytes = models.Decimal()
    megabytes = models.Decimal()

