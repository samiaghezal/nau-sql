class VendorPayout(models.Model):
    id = models.ID()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    tenant = models.Tenant()
    created = models.DateTime()
    updated = models.DateTime()
    gateway = models.String()
    payout = models.Payout()
    seller = models.Seller()
    currency = models.String()
    average = models.Decimal()
    discounts = models.Decimal()
    net = models.Decimal()
    shipping = models.Decimal()
    volumeDiscounts = models.Decimal()
    commission = models.Decimal()
    feeAmount = models.Decimal()
    fees = models.Money()
    payoutAmount = models.Decimal()
    payable = models.Money()
    included = models.Boolean()
    status = models.VendorPayoutStatus()
    statusMessage = models.String()
    adjustmentAmount = models.Decimal()
    adjustment = models.Money()
    refundAmount = models.Decimal()
    refund = models.Money()
    ledgerVersion = models.BigInt()
    events = models.VendorPayoutEvent()
    orders = models.OrderCountableConnection()
    refundLines = models.RefundLineCountableConnection()
    commissionMoney = models.Money()
    discountsMoney = models.Money()
    netSales = models.Money()
    shippingMoney = models.Money()
    subtotal = models.Money()
    total = models.Money()

