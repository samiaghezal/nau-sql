class SellerVolumeDiscount(models.Model):
    seller = models.Int()
    volumeDiscount = models.Money()

