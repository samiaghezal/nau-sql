class SellerNoteCreate(models.Model):
    ok = models.Boolean()
    note = models.String()
    sellerErrors = models.SellerError()

