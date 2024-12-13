class PublicSeller(models.Model):
    id = models.ID()
    companyName = models.String()
    slug = models.String()
    logo = models.Image()
    status = models.SellerStatus()
    banner = models.Image()
    storeDescription = models.String()
    products = models.ProductCountableConnection()
    variants = models.ProductVariantCountableConnection()

