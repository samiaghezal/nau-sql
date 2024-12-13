class VendorPayoutCountableEdge(models.Model):
    node = models.VendorPayout()
    cursor = models.String()

