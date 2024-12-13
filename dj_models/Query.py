class Query(models.Model):
    emailTemplate = models.EmailTemplate()
    emailTemplatePreview = models.EmailTemplatePreview()
    emailTemplates = models.EmailTemplateCountableConnection()
    wishlistItemsByName = models.WishlistItemCountableConnection()
    webhook = models.Webhook()
    webhookEvents = models.WebhookEvent()
    webhookSamplePayload = models.JSONString()
    webhookEventLogs = models.WebhookEventLogCountableConnection()
    webhookJobs = models.WebhookJobCountableConnection()
    warehouse = models.Warehouse()
    warehouses = models.WarehouseCountableConnection()
    stock = models.Stock()
    stocks = models.StockCountableConnection()
    content = models.Content()
    contentDraft = models.Content()
    contentList = models.ContentCountableConnection()
    media = models.Media()
    mediaList = models.MediaCountableConnection()
    tenant = models.Tenant()
    tenants = models.TenantCountableConnection()
    shop = models.Shop()
    analyticsId = models.String()
    customStorefrontDomain = models.CustomDomain()
    shippingZone = models.ShippingZone()
    shippingZones = models.ShippingZoneCountableConnection()
    seller = models.Seller()
    sellerBySlug = models.PublicSeller()
    sellers = models.SellerCountableConnection()
    sellerUser = models.SellerUserType()
    sellerUsers = models.SellerUserTypeCountableConnection()
    userSellers = models.SellerUserType()
    sellerEvents = models.SellerEventTypeCountableConnection()
    allowedOwners = models.UserCountableConnection()
    availablePlans = models.AgreementCountableConnection()
    sellerListCards = models.SellerCards()
    sellerDetailCards = models.SellerDetailCards()
    newSellers = models.Int()
    sellerOrders = models.Int()
    sellerCommissions = models.Money()
    refund = models.Refund()
    refunds = models.RefundCountableConnection()
    digitalContent = models.DigitalContent()
    digitalContents = models.DigitalContentCountableConnection()
    allCategories = models.Category()
    categories = models.CategoryCountableConnection()
    category = models.Category()
    collection = models.Collection()
    collections = models.CollectionCountableConnection()
    product = models.Product()
    products = models.ProductCountableConnection()
    productType = models.ProductType()
    productTypes = models.ProductTypeCountableConnection()
    productVariant = models.ProductVariant()
    productVariants = models.ProductVariantCountableConnection()
    reportProductSales = models.ProductVariantCountableConnection()
    priceBook = models.PriceBook()
    priceBooks = models.PriceBookCountableConnection()
    priceBookVariants = models.PriceBookVariantCountableConnection()
    priceBookProducts = models.PriceBookProductCountableConnection()
    priceBookProductTypes = models.PriceBookProductTypeCountableConnection()
    priceBookVariantsHistory = models.PriceBookVariantHistoryCountableConnection()
    priceBookProductsHistory = models.PriceBookProductHistoryCountableConnection()
    priceBookProductTypesHistory = models.PriceBookProductTypeHistoryCountableConnection()
    priceBookUsers = models.UserCountableConnection()
    plugin = models.Plugin()
    plugins = models.PluginCountableConnection()
    customerTaxCertificates = models.TaxCertificate()
    thirdPartyProducts = models.GenericScalar()
    importThirdPartyProduct = models.GenericScalar()
    availableImportSources = models.Plugin()
    catalogImportProcess = models.CatalogImportProcess()
    catalogImportProcesses = models.CatalogImportProcessCountableConnection()
    taxExemptCodes = models.TaxExemptCode()
    typeformForms = models.TypeformForms()
    typeformForm = models.TypeformForm()
    pluginFlows = models.Flow()
    getClientSecret = models.GenericScalar()
    getPayoutGateways = models.PaymentGateway()
    avalaraRequestLogs = models.AvalaraRequestLogCountableConnection()
    checkoutEvents = models.CheckoutEventCountableConnection()
    payout = models.Payout()
    payouts = models.PayoutCountableConnection()
    vendorPayout = models.VendorPayout()
    vendorPayouts = models.VendorPayoutReport()
    vendorPayoutList = models.SingleVendorPayoutReport()
    payment = models.Payment()
    payments = models.PaymentCountableConnection()
    page = models.Page()
    pages = models.PageCountableConnection()
    homepageEvents = models.OrderEventCountableConnection()
    marketplaceHomepageEvents = models.NauticalOrderEventCountableConnection()
    order = models.Order()
    nauticalOrder = models.NauticalOrder()
    orders = models.OrderCountableConnection()
    nauticalOrders = models.NauticalOrderCountableConnection()
    draftOrders = models.OrderCountableConnection()
    nauticalDraftOrders = models.NauticalOrderCountableConnection()
    nauticalQuoteOrders = models.NauticalOrderCountableConnection()
    nauticalQuoteOrderByToken = models.NauticalOrder()
    quoteOrders = models.OrderCountableConnection()
    ordersTotal = models.TaxedMoney()
    nauticalOrdersTotal = models.TaxedMoney()
    orderByToken = models.Order()
    nauticalOrderByToken = models.NauticalOrder()
    returns = models.FulfillmentCountableConnection()
    optimizedHome = models.OptimizedHome()
    nauticalConfiguration = models.NauticalConfiguration()
    nauticalConfigurationList = models.NauticalConfiguration()
    microsite = models.Microsite()
    microsites = models.MicrositeCountableConnection()
    vendorMicrosite = models.Microsite()
    menu = models.Menu()
    menus = models.MenuCountableConnection()
    menuItem = models.MenuItem()
    menuItems = models.MenuItemCountableConnection()
    marketplaceConfiguration = models.MarketplaceConfiguration()
    currencies = models.NauticalCurrency()
    countries = models.CountryDisplay()
    emailLogs = models.EmailEventCountableConnection()
    locationSearch = models.LocationSuggestion()
    locationGeocode = models.Coordinates()
    insightsOrdersCustomerSummary = models.InReportOrderCustomerSummaryType()
    insightsOrdersSellerSummary = models.InReportOrderSellerSummaryType()
    insightsOrdersMarketplaceSummary = models.InReportOrderMarketplaceSummaryType()
    insightsMarketplacePayoutsSummary = models.InReportMarketplacePayoutsSummaryType()
    insightsMarketplaceTaxSummary = models.InReportMarketplaceTaxSummaryType()
    insightsMarketplaceTaxesByCountry = models.InReportMarketplaceTaxesByCountryType()
    insightsMarketplaceTaxesByCountryArea = models.InReportMarketplaceTaxesByCountryType()
    insightsTopPerformingProducts = models.InReportTopPerformingProductsType()
    insightsTopPerformingCategories = models.InReportTopPerformingCategoriesType()
    insightsMarketplacePaymentsSummary = models.InReportMarketplacePaymentsSummaryType()
    dashboardOrdersSummary = models.DashboardOrdersSummaryType()
    dashboardTopSellerPerformance = models.DashboardTopSellerPerformanceType()
    dashboardGraph = models.DashboardGraphType()
    fontList = models.FontCountableConnection()
    journalEntries = models.JournalEntryCountableConnection()
    ledgers = models.LedgerCountableConnection()
    sale = models.Sale()
    sales = models.SaleCountableConnection()
    voucher = models.Voucher()
    vouchers = models.VoucherCountableConnection()
    designerdata = models.DesignerDataType()
    designerdatalist = models.DesignerDataType()
    integrationEmbeddingToken = models.String()
    exportFile = models.ExportFile()
    exportFiles = models.ExportFileCountableConnection()
    taxTypes = models.TaxType()
    checkout = models.Checkout()
    checkouts = models.CheckoutCountableConnection()
    checkoutLine = models.CheckoutLine()
    checkoutLines = models.CheckoutLineCountableConnection()
    attributes = models.AttributeCountableConnection()
    attribute = models.Attribute()
    customFieldTemplates = models.CustomFieldTemplate()
    customFieldTemplate = models.CustomFieldTemplate()
    appsInstallations = models.AppInstallation()
    apps = models.AppCountableConnection()
    app = models.App()
    agreement = models.Agreement()
    agreements = models.AgreementCountableConnection()
    sellerAgreement = models.AgreementSellers()
    sellerAgreements = models.AgreementSellers()
    addressValidationRules = models.AddressValidationData()
    address = models.Address()
    customers = models.UserCountableConnection()
    permissionGroups = models.GroupCountableConnection()
    permissionGroup = models.Group()
    me = models.User()
    staffUsers = models.UserCountableConnection()
    user = models.User()
    userByEmail = models.User()
    _entities = models._Entity()
    _service = models._Service()
