class Shop(models.Model):
    availablePaymentGateways = models.PaymentGateway()
    geolocalization = models.Geolocalization()
    countries = models.CountryDisplay()
    supportedCurrencies = models.NauticalCurrency()
    defaultCountry = models.CountryDisplay()
    defaultMailSenderName = models.String()
    defaultMailSenderAddress = models.String()
    defaultMailSupportAddress = models.String()
    description = models.String()
    domain = models.Domain()
    apiUrl = models.String()
    dashboardUrl = models.String()
    enableQuoteOrders = models.Boolean()
    enableOfferOrders = models.Boolean()
    name = models.String()
    permissions = models.Permission()
    phonePrefixes = models.String()
    includeTaxesInPrices = models.Boolean()
    chargeTaxesOnShipping = models.Boolean()
    trackInventoryByDefault = models.Boolean()
    defaultWeightUnit = models.WeightUnitsEnum()
    automaticFulfillmentDigitalProducts = models.Boolean()
    defaultDigitalMaxDownloads = models.Int()
    defaultDigitalUrlValidDays = models.Int()
    companyAddress = models.Address()
    customerSetPasswordUrl = models.String()
    loginForCheckout = models.Boolean()
    loginForPrice = models.Boolean()
    activePlugins = models.Plugin()
    crispWebsiteId = models.String()
    geolocationEnabled = models.Boolean()
    requireProductApproval = models.Boolean()
    timezone = models.String()
    checkoutTheme = models.CheckoutTheme()
    storefrontTheme = models.StorefrontTheme()
    sellerOnboardingSettings = models.SellerOnboardingSettings()

