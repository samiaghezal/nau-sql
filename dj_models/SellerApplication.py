class SellerApplication(models.Model):
    createdAt = models.DateTime()
    updatedAt = models.DateTime()
    checkpoint = models.SellerApplicationCheckpoint()
    formData = models.JSONString()
    seller = models.Seller()
    submittedAt = models.DateTime()
    id = models.ID()

