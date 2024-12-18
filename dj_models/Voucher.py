class Voucher(models.Model):
    id = models.ID()
    type = models.VoucherTypeEnum()
    name = models.String()
    code = models.String()
    usageLimit = models.Int()
    used = models.Int()
    startDate = models.DateTime()
    endDate = models.DateTime()
    applyOncePerOrder = models.Boolean()
    applyOncePerCustomer = models.Boolean()
    discountValueType = models.DiscountValueTypeEnum()
    discountValue = models.Decimal()
    currency = models.String()
    minSpent = models.Money()
    minCheckoutItemsQuantity = models.Int()
    categories = models.CategoryCountableConnection()
    collections = models.CollectionCountableConnection()
    products = models.ProductCountableConnection()
    variants = models.ProductVariantCountableConnection()
    countries = models.CountryDisplay()

