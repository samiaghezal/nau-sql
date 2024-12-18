class NauticalOrderLine(models.Model):
    id = models.ID()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    isLinePriceOverridden = models.Boolean()
    unitPriceOverriddenNote = models.String()
    note = models.String()
    productName = models.String()
    variantName = models.String()
    productSku = models.String()
    isShippingRequired = models.Boolean()
    digitalContentUrl = models.DigitalContentUrl()
    thumbnail = models.Image()
    unitPrice = models.TaxedMoney()
    totalPrice = models.TaxedMoney()
    variant = models.ProductVariant()
    translatedProductName = models.String()
    translatedVariantName = models.String()
    priceBook = models.PriceBook()
    sellerOrderline = models.OrderLine()
    quantityOrdered = models.Int()
    sale = models.Sale()
    saleDiscount = models.Money()
    voucherDiscount = models.Money()
    originalUnitPrice = models.TaxedMoney()
    discountedUnitPrice = models.TaxedMoney()

