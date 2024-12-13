class Category(models.Model):
    id = models.ID()
    description = models.String()
    descriptionHtml = models.String()
    externalId = models.String()
    externalSource = models.String()
    seoTitle = models.String()
    seoDescription = models.String()
    name = models.String()
    slug = models.String()
    parent = models.Category()
    allowProductAssignment = models.Boolean()
    level = models.Int()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    ancestors = models.CategoryCountableConnection()
    products = models.ProductCountableConnection()
    children = models.CategoryCountableConnection()
    backgroundImage = models.Image()
    trailingBreadcrumbs = models.Category()
    customFields = models.SelectedAttribute()
