# Generated Pydantic models from GraphQL schema

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PageInfo(BaseModel):
    has_next_page: bool = Field(..., alias="hasNextPage")
    has_previous_page: bool = Field(..., alias="hasPreviousPage")
    start_cursor: Optional[str] = Field(..., alias="startCursor")
    end_cursor: Optional[str] = Field(..., alias="endCursor")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any
from uuid import UUID


class Query(BaseModel):
    id: str
    content: str
    filter: Optional[StaffUserInput]
    sort_by: Optional[UserSortingInput] = Field(..., alias="sortBy")
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    wishlist_name: str = Field(..., alias="wishlistName")
    webhook_events: WebhookEvent = Field(..., alias="webhookEvents")
    event_type: WebhookSampleEventTypeEnum = Field(..., alias="eventType")
    identifier: Optional[str]
    slug: Optional[str]
    shop: Shop
    analytics_id: Optional[str] = Field(..., alias="analyticsId")
    custom_storefront_domain: Optional[CustomDomain] = Field(..., alias="customStorefrontDomain")
    number: Optional[str]
    tax_id: Optional[str] = Field(..., alias="taxId")
    email: str
    seller: Optional[str]
    query: Optional[str]
    period: Optional[ReportingPeriod]
    all_categories: List[Category] = Field(..., alias="allCategories")
    level: Optional[int]
    microsite: Optional[str]
    nsn: Optional[str]
    price_book_id: str = Field(..., alias="priceBookId")
    variant_id: Optional[str] = Field(..., alias="variantId")
    product_id: Optional[str] = Field(..., alias="productId")
    product_type_id: str = Field(..., alias="productTypeId")
    source: str
    available_import_sources: List[Plugin] = Field(..., alias="availableImportSources")
    tax_exempt_codes: List[TaxExemptCode] = Field(..., alias="taxExemptCodes")
    page: Optional[int]
    search: Optional[str]
    gateway: str
    payment_information: StripeClientPaymentData = Field(..., alias="paymentInformation")
    get_payout_gateways: List[PaymentGateway] = Field(..., alias="getPayoutGateways")
    end_date: date = Field(..., alias="endDate")
    payout_id: Optional[str] = Field(..., alias="payoutId")
    vendor_type: Optional[str] = Field(..., alias="vendorType")
    vendor_id: Optional[str] = Field(..., alias="vendorId")
    token: Optional[UUID]
    is_marketplace: bool = Field(..., alias="isMarketplace")
    start_date: date = Field(..., alias="startDate")
    configuration_name: str = Field(..., alias="configurationName")
    nautical_configuration_list: List[NauticalConfiguration] = Field(..., alias="nauticalConfigurationList")
    name: Optional[str]
    marketplace_configuration: MarketplaceConfiguration = Field(..., alias="marketplaceConfiguration")
    currencies: NauticalCurrency
    countries: CountryDisplay
    search_data: str = Field(..., alias="searchData")
    location_data: Optional[str] = Field(..., alias="locationData")
    perspective: PerformancePerspective
    dimension: Optional[str]
    designerdatalist: DesignerDataType
    integration_embedding_token: Optional[str] = Field(..., alias="integrationEmbeddingToken")
    tax_types: TaxType = Field(..., alias="taxTypes")
    custom_field_templates: CustomFieldTemplate = Field(..., alias="customFieldTemplates")
    content_type: Optional[CustomFieldTemplateEnum] = Field(..., alias="contentType")
    apps_installations: AppInstallation = Field(..., alias="appsInstallations")
    country_code: CountryCode = Field(..., alias="countryCode")
    country_area: Optional[str] = Field(..., alias="countryArea")
    city: Optional[str]
    city_area: Optional[str] = Field(..., alias="cityArea")
    me: Optional[User]
    service: _Service = Field(..., alias="_service")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class EmailTemplate(BaseModel):
    id: str
    title: str
    subject: str
    sender_email_address: Optional[str] = Field(..., alias="senderEmailAddress")
    content: Optional[str]
    default_content: Optional[str] = Field(..., alias="defaultContent")
    rendered_content: Optional[str] = Field(..., alias="renderedContent")
    description: Optional[str]
    is_custom: bool = Field(..., alias="isCustom")
    is_active: bool = Field(..., alias="isActive")
    is_editable: bool = Field(..., alias="isEditable")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    recipient_type: RecipientTypeEnum = Field(..., alias="recipientType")
    event_type: EventTypeEnum = Field(..., alias="eventType")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class EmailTemplatePreview(BaseModel):
    id: Optional[str]
    rendered_content: Optional[str] = Field(..., alias="renderedContent")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class EmailTemplateCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: EmailTemplateCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class EmailTemplateCountableEdge(BaseModel):
    node: EmailTemplate
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistItemCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: WishlistItemCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class WishlistItemCountableEdge(BaseModel):
    node: WishlistItem
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistItem(BaseModel):
    id: str
    wishlist: Wishlist
    product: Optional[Product]
    variant: Optional[ProductVariant]
    note: Optional[str]
    expiry_date: Optional[datetime] = Field(..., alias="expiryDate")
    quantity: int
    requested_price: Optional[Money] = Field(..., alias="requestedPrice")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Wishlist(BaseModel):
    id: str
    created_at: datetime = Field(..., alias="createdAt")
    name: str
    is_default: bool = Field(..., alias="isDefault")
    user: Optional[User]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class User(BaseModel):
    id: str
    last_login: Optional[datetime] = Field(..., alias="lastLogin")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    external_payout_account_id: Optional[str] = Field(..., alias="externalPayoutAccountId")
    external_payout_source: Optional[UserExternalPayoutSource] = Field(..., alias="externalPayoutSource")
    external_payout_onboarding_url: Optional[str] = Field(..., alias="externalPayoutOnboardingUrl")
    company_name: str = Field(..., alias="companyName")
    email: str
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    is_staff: bool = Field(..., alias="isStaff")
    is_active: bool = Field(..., alias="isActive")
    note: Optional[str]
    date_joined: datetime = Field(..., alias="dateJoined")
    last_status_changed_at: Optional[datetime] = Field(..., alias="lastStatusChangedAt")
    default_shipping_address: Optional[Address] = Field(..., alias="defaultShippingAddress")
    default_billing_address: Optional[Address] = Field(..., alias="defaultBillingAddress")
    personal_phone: Optional[str] = Field(..., alias="personalPhone")
    tax_exempt_code: Optional[str] = Field(..., alias="taxExemptCode")
    vat_identification_number: Optional[str] = Field(..., alias="vatIdentificationNumber")
    addresses: Address
    checkout: Optional[Checkout]
    filter: Optional[CustomerNauticalOrderFilterInput]
    sort_by: Optional[OrderSortingInput] = Field(..., alias="sortBy")
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    num_orders: Optional[int] = Field(..., alias="numOrders")
    user_permissions: UserPermission = Field(..., alias="userPermissions")
    permission_groups: Group = Field(..., alias="permissionGroups")
    editable_groups: Group = Field(..., alias="editableGroups")
    size: Optional[int]
    events: CustomerEvent
    stored_payment_sources: PaymentSource = Field(..., alias="storedPaymentSources")
    seller: Optional[Seller]
    is_assignable: Optional[bool] = Field(..., alias="isAssignable")
    documents: Document
    price_book: Optional[PriceBook] = Field(..., alias="priceBook")
    dashboard_embedding_token: Optional[str] = Field(..., alias="dashboardEmbeddingToken")
    custom_fields: SelectedAttribute = Field(..., alias="customFields")

from pydantic import BaseModel, Field


class MetadataItem(BaseModel):
    key: str
    value: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Address(BaseModel):
    id: str
    first_name: str = Field(..., alias="firstName")
    last_name: str = Field(..., alias="lastName")
    company_name: str = Field(..., alias="companyName")
    street_address1: str = Field(..., alias="streetAddress1")
    street_address2: str = Field(..., alias="streetAddress2")
    city: str
    city_area: str = Field(..., alias="cityArea")
    postal_code: str = Field(..., alias="postalCode")
    country: CountryDisplay
    country_area: str = Field(..., alias="countryArea")
    phone: Optional[str]
    is_default_shipping_address: Optional[bool] = Field(..., alias="isDefaultShippingAddress")
    is_default_billing_address: Optional[bool] = Field(..., alias="isDefaultBillingAddress")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class CountryDisplay(BaseModel):
    code: str
    country: str
    required_fields: List[str] = Field(..., alias="requiredFields")
    allowed_country_areas: List[str] = Field(..., alias="allowedCountryAreas")
    detailed_allowed_country_areas: CountryArea = Field(..., alias="detailedAllowedCountryAreas")

from pydantic import BaseModel, Field


class CountryArea(BaseModel):
    code: str
    name: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any
from uuid import UUID


class Checkout(BaseModel):
    created: datetime
    last_change: datetime = Field(..., alias="lastChange")
    user: Optional[User]
    quantity: int
    billing_address: Optional[Address] = Field(..., alias="billingAddress")
    shipping_address: Optional[Address] = Field(..., alias="shippingAddress")
    note: str
    currency: str
    discount: Optional[Money]
    discount_name: Optional[str] = Field(..., alias="discountName")
    translated_discount_name: Optional[str] = Field(..., alias="translatedDiscountName")
    voucher_code: Optional[str] = Field(..., alias="voucherCode")
    po_numbers: List[str] = Field(..., alias="poNumbers")
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    available_marketplace_shipping_methods: ShippingMethod = Field(..., alias="availableMarketplaceShippingMethods")
    available_shipping_methods_by_seller: MultiSellerShippingMethod = Field(..., alias="availableShippingMethodsBySeller")
    applicable_volume_discounts: Optional[Money] = Field(..., alias="applicableVolumeDiscounts")
    applicable_volume_discounts_by_seller: SellerVolumeDiscount = Field(..., alias="applicableVolumeDiscountsBySeller")
    available_payment_gateways: PaymentGateway = Field(..., alias="availablePaymentGateways")
    email: str
    is_shipping_required: bool = Field(..., alias="isShippingRequired")
    lines: CheckoutLine
    shipping_price: TaxedMoney = Field(..., alias="shippingPrice")
    subtotal_price: TaxedMoney = Field(..., alias="subtotalPrice")
    token: UUID
    total_price: TaxedMoney = Field(..., alias="totalPrice")
    discount_type: Optional[VoucherTypeEnum] = Field(..., alias="discountType")
    shipping_methods: CheckoutSellerShipping = Field(..., alias="shippingMethods")
    shipping_sale_discount: Money = Field(..., alias="shippingSaleDiscount")
    marketplace_shipping_method: Optional[ShippingMethod] = Field(..., alias="marketplaceShippingMethod")
    marketplace_shipping_price: TaxedMoney = Field(..., alias="marketplaceShippingPrice")

from pydantic import BaseModel, Field


class Money(BaseModel):
    currency: str
    base_amount: int = Field(..., alias="baseAmount")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShippingMethod(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    name: str
    price: Optional[Money]
    minimum_order_price: Optional[Money] = Field(..., alias="minimumOrderPrice")
    maximum_order_price: Optional[Money] = Field(..., alias="maximumOrderPrice")
    minimum_order_weight: Optional[Weight] = Field(..., alias="minimumOrderWeight")
    maximum_order_weight: Optional[Weight] = Field(..., alias="maximumOrderWeight")
    type: Optional[ShippingMethodTypeEnum]
    requires_secondary_address: Optional[bool] = Field(..., alias="requiresSecondaryAddress")

from pydantic import BaseModel, Field


class Weight(BaseModel):
    unit: WeightUnitsEnum
    value: float

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MultiSellerShippingMethod(BaseModel):
    seller: Optional[int]
    seller_id: str = Field(..., alias="sellerId")
    seller_name: str = Field(..., alias="sellerName")
    value: ShippingMethod

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerVolumeDiscount(BaseModel):
    seller: Optional[int]
    volume_discount: Optional[Money] = Field(..., alias="volumeDiscount")

from pydantic import BaseModel, Field


class PaymentGateway(BaseModel):
    name: str
    id: str
    config: GatewayConfigLine
    currencies: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class GatewayConfigLine(BaseModel):
    field: str
    value: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutLine(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    is_line_price_overridden: bool = Field(..., alias="isLinePriceOverridden")
    unit_price_overridden_note: Optional[str] = Field(..., alias="unitPriceOverriddenNote")
    note: Optional[str]
    variant: ProductVariant
    quantity: int
    sale: Optional[Sale]
    total_price: TaxedMoney = Field(..., alias="totalPrice")
    requires_shipping: Optional[bool] = Field(..., alias="requiresShipping")
    seller: Optional[SellerType]
    discounted_unit_price: TaxedMoney = Field(..., alias="discountedUnitPrice")
    original_unit_price: TaxedMoney = Field(..., alias="originalUnitPrice")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class ProductVariant(BaseModel):
    id: str
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    description: str
    description_html: str = Field(..., alias="descriptionHtml")
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    seo_title: Optional[str] = Field(..., alias="seoTitle")
    seo_description: Optional[str] = Field(..., alias="seoDescription")
    sku: Optional[str]
    name: str
    nautical_stock_number: str = Field(..., alias="nauticalStockNumber")
    status: ProductVariantStatus
    sub_status: ProductVariantSubStatus = Field(..., alias="subStatus")
    currency: Optional[str]
    product: Product
    track_inventory: bool = Field(..., alias="trackInventory")
    weight: Optional[Weight]
    seller: Optional[Seller]
    published_at: Optional[datetime] = Field(..., alias="publishedAt")
    is_published: bool = Field(..., alias="isPublished")
    override_currency: bool = Field(..., alias="overrideCurrency")
    requires_quote: bool = Field(..., alias="requiresQuote")
    allow_backorders: Optional[bool] = Field(..., alias="allowBackorders")
    is_price_override_allowed: bool = Field(..., alias="isPriceOverrideAllowed")
    is_shipping_required: bool = Field(..., alias="isShippingRequired")
    is_digital: bool = Field(..., alias="isDigital")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    price: Optional[Money]
    pricing: Optional[VariantPricingInfo]
    is_visible: bool = Field(..., alias="isVisible")
    size: Optional[VariantSize]
    attributes: SelectedAttribute
    custom_fields: SelectedAttribute = Field(..., alias="customFields")
    cost_price: Optional[Money] = Field(..., alias="costPrice")
    margin: Optional[int]
    quantity_ordered: Optional[int] = Field(..., alias="quantityOrdered")
    features: List[VariantFeature]
    images: List[ProductImage]
    available_images: List[ProductImage] = Field(..., alias="availableImages")
    digital_content: Optional[DigitalContent] = Field(..., alias="digitalContent")
    country_code: Optional[CountryCode] = Field(..., alias="countryCode")
    net_revenue: Optional[float] = Field(..., alias="netRevenue")
    gross_revenue: Optional[float] = Field(..., alias="grossRevenue")
    sort_order_in_collection: Optional[int] = Field(..., alias="sortOrderInCollection")
    documents: List[Document]
    stock_events: List[StockEvent] = Field(..., alias="stockEvents")
    sales: Sale
    vouchers: Voucher

from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class Product(BaseModel):
    id: Optional[str]
    publication_date: Optional[date] = Field(..., alias="publicationDate")
    description: str
    description_html: str = Field(..., alias="descriptionHtml")
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    seller: Optional[Seller]
    mpn: Optional[str]
    brand: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    seo_title: Optional[str] = Field(..., alias="seoTitle")
    seo_description: Optional[str] = Field(..., alias="seoDescription")
    product_type: Optional[ProductType] = Field(..., alias="productType")
    name: str
    slug: str
    category: Optional[Category]
    currency: str
    updated_at: Optional[datetime] = Field(..., alias="updatedAt")
    created_at: datetime = Field(..., alias="createdAt")
    charge_taxes: bool = Field(..., alias="chargeTaxes")
    weight: Optional[Weight]
    available_for_purchase: Optional[date] = Field(..., alias="availableForPurchase")
    visible_in_listings: bool = Field(..., alias="visibleInListings")
    default_variant: Optional[ProductVariant] = Field(..., alias="defaultVariant")
    override_price: bool = Field(..., alias="overridePrice")
    override_currency: bool = Field(..., alias="overrideCurrency")
    status: ProductStatus
    sub_status: ProductSubStatus = Field(..., alias="subStatus")
    is_price_override_allowed: bool = Field(..., alias="isPriceOverrideAllowed")
    is_shipping_required: bool = Field(..., alias="isShippingRequired")
    is_digital: bool = Field(..., alias="isDigital")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    size: Optional[int]
    pricing: Optional[ProductPricingInfo]
    is_available: Optional[bool] = Field(..., alias="isAvailable")
    minimal_variant_price: Optional[Money] = Field(..., alias="minimalVariantPrice")
    tax_type: Optional[TaxType] = Field(..., alias="taxType")
    attributes: SelectedAttribute
    custom_fields: SelectedAttribute = Field(..., alias="customFields")
    purchase_cost: Optional[MoneyRange] = Field(..., alias="purchaseCost")
    margin: Optional[Margin]
    variants: List[ProductVariant]
    images: List[ProductImage]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    collections: List[Collection]
    is_available_for_purchase: Optional[bool] = Field(..., alias="isAvailableForPurchase")
    sort_order: Optional[int] = Field(..., alias="sortOrder")
    is_published: bool = Field(..., alias="isPublished")
    features: List[ProductFeature]
    locations: List[Location]
    origin_location: Optional[Location] = Field(..., alias="originLocation")
    destination_location: Optional[Location] = Field(..., alias="destinationLocation")
    primary_location: Optional[Location] = Field(..., alias="primaryLocation")
    warehouses_stats: List[WarehouseStats] = Field(..., alias="warehousesStats")
    actions: List[ProductAction]
    documents: Document
    sales: Sale
    vouchers: Voucher
    sort_priority_weight: Optional[Decimal] = Field(..., alias="sortPriorityWeight")
    product_status_logs: List[ProductStatusLog] = Field(..., alias="productStatusLogs")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class Seller(BaseModel):
    id: str
    company_name: str = Field(..., alias="companyName")
    slug: str
    size: Optional[int]
    status: SellerStatus
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    external_payout_account_id: Optional[str] = Field(..., alias="externalPayoutAccountId")
    external_payout_source: Optional[SellerExternalPayoutSource] = Field(..., alias="externalPayoutSource")
    external_payout_onboarding_url: Optional[str] = Field(..., alias="externalPayoutOnboardingUrl")
    is_marketplace_seller: bool = Field(..., alias="isMarketplaceSeller")
    identification: List[str]
    addresses: List[Address]
    default_shipping_address: Optional[Address] = Field(..., alias="defaultShippingAddress")
    default_billing_address: Optional[Address] = Field(..., alias="defaultBillingAddress")
    owner: Optional[User]
    default_currency: str = Field(..., alias="defaultCurrency")
    fulfilled_by_marketplace: bool = Field(..., alias="fulfilledByMarketplace")
    checklists: List[SellerOnboardingChecklist]
    application: Optional[SellerApplication]
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    agreement: Optional[Agreement]
    agreement_acknowledged: Optional[datetime] = Field(..., alias="agreementAcknowledged")
    can_use_in_storefront: Optional[bool] = Field(..., alias="canUseInStorefront")
    microsite: Optional[Microsite]
    pk: Optional[int]
    external_payout_status: Optional[bool] = Field(..., alias="externalPayoutStatus")
    external_payout_schedule: Optional[str] = Field(..., alias="externalPayoutSchedule")
    agreement_decision_reason: Optional[str] = Field(..., alias="agreementDecisionReason")
    store_description: Optional[str] = Field(..., alias="storeDescription")
    documents: List[Document]
    approved_date: Optional[datetime] = Field(..., alias="approvedDate")
    first_product_created_date: Optional[datetime] = Field(..., alias="firstProductCreatedDate")
    first_order_placed_date: Optional[datetime] = Field(..., alias="firstOrderPlacedDate")
    created: datetime
    updated: datetime
    account_setup_tasks_are_done: Optional[bool] = Field(..., alias="accountSetupTasksAreDone")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Image(BaseModel):
    url: str
    alt: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: ProductCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class ProductCountableEdge(BaseModel):
    node: Product
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: ProductVariantCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class ProductVariantCountableEdge(BaseModel):
    node: ProductVariant
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerUserTypeCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: SellerUserTypeCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class SellerUserTypeCountableEdge(BaseModel):
    node: SellerUserType
    cursor: str

from pydantic import BaseModel, Field


class SellerUserType(BaseModel):
    id: str
    tenant: Tenant
    seller: Seller
    user: User
    is_default: bool = Field(..., alias="isDefault")

from pydantic import BaseModel, Field


class Tenant(BaseModel):
    id: str
    name: str
    is_active: bool = Field(..., alias="isActive")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerEventTypeCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: SellerEventTypeCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class SellerEventTypeCountableEdge(BaseModel):
    node: SellerEventType
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerEventType(BaseModel):
    id: str
    date: Optional[datetime]
    type: Optional[SellerEventsEnum]
    user: Optional[User]
    parameters: Optional[Dict[str, Any]]
    status: Optional[str]
    message: Optional[str]
    seller: Optional[Seller]

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerOnboardingChecklist(BaseModel):
    id: str
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    tenant: Tenant
    seller: Seller
    position: int
    title: str
    description: str
    complete_on: Optional[SellerChecklistCompletionTriggersEnum] = Field(..., alias="completeOn")
    completed_at: Optional[datetime] = Field(..., alias="completedAt")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerApplication(BaseModel):
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    checkpoint: SellerApplicationCheckpoint
    form_data: Dict[str, Any] = Field(..., alias="formData")
    seller: Seller
    submitted_at: Optional[datetime] = Field(..., alias="submittedAt")
    id: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VendorPayoutCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: VendorPayoutCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class VendorPayoutCountableEdge(BaseModel):
    node: VendorPayout
    cursor: str

from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class VendorPayout(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    tenant: Tenant
    created: datetime
    updated: datetime
    gateway: str
    payout: Payout
    seller: Optional[Seller]
    currency: str
    average: Decimal
    discounts: Decimal
    net: Decimal
    shipping: Decimal
    volume_discounts: Decimal = Field(..., alias="volumeDiscounts")
    commission: Decimal
    fee_amount: Decimal = Field(..., alias="feeAmount")
    fees: Money
    payout_amount: Decimal = Field(..., alias="payoutAmount")
    payable: Money
    included: bool
    status: VendorPayoutStatus
    status_message: Optional[str] = Field(..., alias="statusMessage")
    adjustment_amount: Decimal = Field(..., alias="adjustmentAmount")
    adjustment: Money
    refund_amount: Decimal = Field(..., alias="refundAmount")
    refund: Money
    ledger_version: int = Field(..., alias="ledgerVersion")
    event_types: List[VendorPayoutEventsEnum] = Field(..., alias="eventTypes")
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    commission_money: Money = Field(..., alias="commissionMoney")
    discounts_money: Money = Field(..., alias="discountsMoney")
    net_sales: Money = Field(..., alias="netSales")
    shipping_money: Money = Field(..., alias="shippingMoney")
    subtotal: Money
    total: Money

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Payout(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    tenant: Tenant
    created: str
    updated: datetime
    start_date: Optional[date] = Field(..., alias="startDate")
    end_date: str = Field(..., alias="endDate")
    status: PayoutStatus
    name: Optional[str]
    currency: str
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    vendors: int
    net_sales: Money = Field(..., alias="netSales")
    discounts: Money
    shipping: Money
    commission: Money
    fees: Money
    refunds: Money
    adjustments: Money
    payout: Money

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VendorPayoutEvent(BaseModel):
    id: str
    parameters: Dict[str, Any]
    date: datetime
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    type: VendorPayoutEventsEnum
    user: Optional[User]
    message: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: OrderCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class OrderCountableEdge(BaseModel):
    node: Order
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class Order(BaseModel):
    id: str
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    order_source: OrderOrderSource = Field(..., alias="orderSource")
    seller: Optional[Seller]
    created: datetime
    updated: Optional[datetime]
    status: OrderStatus
    sub_status: Optional[OrderSubStatus] = Field(..., alias="subStatus")
    user: Optional[User]
    language_code: str = Field(..., alias="languageCode")
    tracking_client_id: str = Field(..., alias="trackingClientId")
    billing_address: Optional[Address] = Field(..., alias="billingAddress")
    shipping_address: Optional[Address] = Field(..., alias="shippingAddress")
    vat_code: str = Field(..., alias="vatCode")
    eu_invoice_messaging: Optional[str] = Field(..., alias="euInvoiceMessaging")
    vat_identification_number: Optional[str] = Field(..., alias="vatIdentificationNumber")
    mp_vat_identification_number: Optional[str] = Field(..., alias="mpVatIdentificationNumber")
    currency: str
    shipping_method: Optional[ShippingMethod] = Field(..., alias="shippingMethod")
    shipping_method_name: Optional[str] = Field(..., alias="shippingMethodName")
    shipping_price: Optional[TaxedMoney] = Field(..., alias="shippingPrice")
    is_shipping_price_overridden: bool = Field(..., alias="isShippingPriceOverridden")
    token: str
    voucher: Optional[Voucher]
    discount: Optional[Money]
    discount_name: Optional[str] = Field(..., alias="discountName")
    translated_discount_name: Optional[str] = Field(..., alias="translatedDiscountName")
    display_gross_prices: bool = Field(..., alias="displayGrossPrices")
    customer_note: str = Field(..., alias="customerNote")
    weight: Optional[Weight]
    imported_at: Optional[datetime] = Field(..., alias="importedAt")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    fulfillments: Fulfillment
    fees: List[OrderFee]
    lines: OrderLine
    allowed_sub_statuses: List[OrderSubStatusEnum] = Field(..., alias="allowedSubStatuses")
    available_shipping_methods: List[ShippingMethod] = Field(..., alias="availableShippingMethods")
    invoices: List[Invoice]
    number: Optional[str]
    marketplace_order_number: Optional[str] = Field(..., alias="marketplaceOrderNumber")
    is_paid: Optional[bool] = Field(..., alias="isPaid")
    payment_status: PaymentChargeStatusEnum = Field(..., alias="paymentStatus")
    payment_status_display: str = Field(..., alias="paymentStatusDisplay")
    total: Optional[TaxedMoney]
    original_total: Optional[TaxedMoney] = Field(..., alias="originalTotal")
    subtotal: Optional[TaxedMoney]
    status_display: Optional[str] = Field(..., alias="statusDisplay")
    can_finalize: bool = Field(..., alias="canFinalize")
    events: List[OrderEvent]
    user_email: Optional[str] = Field(..., alias="userEmail")
    is_shipping_required: bool = Field(..., alias="isShippingRequired")
    payout_status: Optional[PayoutStatusEnum] = Field(..., alias="payoutStatus")
    available_payout_balance: Optional[Money] = Field(..., alias="availablePayoutBalance")
    seller_commission: Optional[Money] = Field(..., alias="sellerCommission")
    volume_discount: Optional[TaxedMoney] = Field(..., alias="volumeDiscount")
    validation_status: List[ValidationStatus] = Field(..., alias="validationStatus")
    is_only_seller_on_nautical_order: Optional[bool] = Field(..., alias="isOnlySellerOnNauticalOrder")
    marketplace_order: Optional[NauticalOrder] = Field(..., alias="marketplaceOrder")
    vendor_payout: Optional[VendorPayout] = Field(..., alias="vendorPayout")
    vendor_payouts: List[VendorPayout] = Field(..., alias="vendorPayouts")

from pydantic import BaseModel, Field


class TaxedMoney(BaseModel):
    currency: str
    gross: Money
    net: Money
    tax: Money

from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Voucher(BaseModel):
    id: str
    type: VoucherTypeEnum
    name: Optional[str]
    code: str
    usage_limit: Optional[int] = Field(..., alias="usageLimit")
    used: int
    start_date: datetime = Field(..., alias="startDate")
    end_date: Optional[datetime] = Field(..., alias="endDate")
    apply_once_per_order: bool = Field(..., alias="applyOncePerOrder")
    apply_once_per_customer: bool = Field(..., alias="applyOncePerCustomer")
    discount_value_type: DiscountValueTypeEnum = Field(..., alias="discountValueType")
    discount_value: Decimal = Field(..., alias="discountValue")
    currency: str
    min_spent: Optional[Money] = Field(..., alias="minSpent")
    min_checkout_items_quantity: Optional[int] = Field(..., alias="minCheckoutItemsQuantity")
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    countries: CountryDisplay

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CategoryCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: CategoryCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class CategoryCountableEdge(BaseModel):
    node: Category
    cursor: str

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class Category(BaseModel):
    id: str
    description: str
    description_html: str = Field(..., alias="descriptionHtml")
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    seo_title: Optional[str] = Field(..., alias="seoTitle")
    seo_description: Optional[str] = Field(..., alias="seoDescription")
    name: str
    slug: str
    parent: Optional[Category]
    allow_product_assignment: bool = Field(..., alias="allowProductAssignment")
    level: int
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    filter: Optional[ProductFilterInput]
    sort_by: Optional[ProductOrder] = Field(..., alias="sortBy")
    size: Optional[int]
    trailing_breadcrumbs: List[Category] = Field(..., alias="trailingBreadcrumbs")
    custom_fields: SelectedAttribute = Field(..., alias="customFields")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SelectedAttribute(BaseModel):
    attribute: Attribute
    values: AttributeValue
    templated: Optional[bool]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Attribute(BaseModel):
    id: str
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    input_type: AttributeInputTypeEnum = Field(..., alias="inputType")
    name: str
    slug: str
    all_product_types: ProductType = Field(..., alias="allProductTypes")
    values: AttributeValue
    value_required: bool = Field(..., alias="valueRequired")
    visible_in_storefront: bool = Field(..., alias="visibleInStorefront")
    filterable_in_storefront: bool = Field(..., alias="filterableInStorefront")
    filterable_in_dashboard: bool = Field(..., alias="filterableInDashboard")
    available_in_grid: bool = Field(..., alias="availableInGrid")
    storefront_search_position: int = Field(..., alias="storefrontSearchPosition")
    created_by: Optional[Seller] = Field(..., alias="createdBy")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductTypeCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: ProductTypeCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class ProductTypeCountableEdge(BaseModel):
    node: ProductType
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductType(BaseModel):
    id: str
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    name: str
    slug: str
    is_shipping_required: bool = Field(..., alias="isShippingRequired")
    is_digital: bool = Field(..., alias="isDigital")
    weight: Optional[Weight]
    is_price_override_allowed: bool = Field(..., alias="isPriceOverrideAllowed")
    created_by: Optional[Seller] = Field(..., alias="createdBy")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    tax_type: Optional[TaxType] = Field(..., alias="taxType")
    variant_attributes: Attribute = Field(..., alias="variantAttributes")
    has_variants: Optional[bool] = Field(..., alias="hasVariants")
    product_attributes: Attribute = Field(..., alias="productAttributes")
    filter: Optional[AttributeFilterInput]
    product_features: ProductTypeProductFeature = Field(..., alias="productFeatures")
    variant_features: ProductTypeVariantFeature = Field(..., alias="variantFeatures")
    model: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TaxType(BaseModel):
    description: Optional[str]
    tax_code: Optional[str] = Field(..., alias="taxCode")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: AttributeCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class AttributeCountableEdge(BaseModel):
    node: Attribute
    cursor: str

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class ProductTypeProductFeature(BaseModel):
    id: str
    sort_order: Optional[int] = Field(..., alias="sortOrder")
    tenant: Tenant
    feature_type: FeatureTypeEnum = Field(..., alias="featureType")
    name: str
    description: str
    options: List[str]
    product_type: ProductType = Field(..., alias="productType")
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductFeatureCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: ProductFeatureCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class ProductFeatureCountableEdge(BaseModel):
    node: ProductFeature
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any
from uuid import UUID


class ProductFeature(BaseModel):
    id: str
    sort_order: Optional[int] = Field(..., alias="sortOrder")
    deleted_at: Optional[datetime] = Field(..., alias="deletedAt")
    deleted_by_user: Optional[User] = Field(..., alias="deletedByUser")
    deleted_by_app: Optional[App] = Field(..., alias="deletedByApp")
    deletion_batch_uuid: Optional[UUID] = Field(..., alias="deletionBatchUuid")
    tenant: Tenant
    feature_type: FeatureTypeEnum = Field(..., alias="featureType")
    name: str
    description: str
    options: List[str]
    product: Product
    product_type_feature: Optional[ProductTypeProductFeature] = Field(..., alias="productTypeFeature")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class App(BaseModel):
    id: str
    name: Optional[str]
    created: Optional[datetime]
    is_active: Optional[bool] = Field(..., alias="isActive")
    permissions: List[Permission]
    user: Optional[User]
    tokens: List[AppToken]
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    type: Optional[AppTypeEnum]
    webhooks: List[Webhook]
    about_app: Optional[str] = Field(..., alias="aboutApp")
    data_privacy: Optional[str] = Field(..., alias="dataPrivacy")
    data_privacy_url: Optional[str] = Field(..., alias="dataPrivacyUrl")
    homepage_url: Optional[str] = Field(..., alias="homepageUrl")
    support_url: Optional[str] = Field(..., alias="supportUrl")
    configuration_url: Optional[str] = Field(..., alias="configurationUrl")
    app_url: Optional[str] = Field(..., alias="appUrl")
    version: Optional[str]
    access_token: Optional[str] = Field(..., alias="accessToken")

from pydantic import BaseModel, Field


class Permission(BaseModel):
    code: PermissionEnum
    name: str

from pydantic import BaseModel, Field


class AppToken(BaseModel):
    name: str
    auth_token: str = Field(..., alias="authToken")
    id: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Webhook(BaseModel):
    name: str
    target_url: str = Field(..., alias="targetUrl")
    is_active: bool = Field(..., alias="isActive")
    secret_key: Optional[str] = Field(..., alias="secretKey")
    connection_string: Optional[str] = Field(..., alias="connectionString")
    queue_name: Optional[str] = Field(..., alias="queueName")
    id: str
    events: WebhookEvent
    app: App

from pydantic import BaseModel, Field


class WebhookEvent(BaseModel):
    event_type: WebhookEventTypeEnum = Field(..., alias="eventType")
    name: str

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class ProductTypeVariantFeature(BaseModel):
    id: str
    sort_order: Optional[int] = Field(..., alias="sortOrder")
    tenant: Tenant
    feature_type: FeatureTypeEnum = Field(..., alias="featureType")
    name: str
    description: str
    options: List[str]
    product_type: ProductType = Field(..., alias="productType")
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VariantFeatureCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: VariantFeatureCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class VariantFeatureCountableEdge(BaseModel):
    node: VariantFeature
    cursor: str

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class VariantFeature(BaseModel):
    id: str
    sort_order: Optional[int] = Field(..., alias="sortOrder")
    tenant: Tenant
    feature_type: FeatureTypeEnum = Field(..., alias="featureType")
    name: str
    description: str
    options: List[str]
    variant: ProductVariant
    product_type_feature: Optional[ProductTypeVariantFeature] = Field(..., alias="productTypeFeature")

from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeValue(BaseModel):
    id: str
    sort_order: Optional[int] = Field(..., alias="sortOrder")
    tenant: Tenant
    name: str
    value: str
    slug: str
    attribute: Attribute
    date_time: Optional[datetime] = Field(..., alias="dateTime")
    plain_text: str = Field(..., alias="plainText")
    rich_text: str = Field(..., alias="richText")
    currency: str
    amount: Decimal
    money: Optional[Money]
    reference: str
    boolean: bool
    file: Optional[File]
    file_url: Optional[str] = Field(..., alias="fileUrl")
    date: Optional[date]
    type: Optional[AttributeValueType]
    input_type: AttributeInputTypeEnum = Field(..., alias="inputType")

from pydantic import BaseModel, Field


class File(BaseModel):
    url: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CollectionCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: CollectionCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class CollectionCountableEdge(BaseModel):
    node: Collection
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Collection(BaseModel):
    id: str
    publication_date: Optional[date] = Field(..., alias="publicationDate")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    description: str
    description_html: str = Field(..., alias="descriptionHtml")
    seo_title: Optional[str] = Field(..., alias="seoTitle")
    seo_description: Optional[str] = Field(..., alias="seoDescription")
    is_visible: bool = Field(..., alias="isVisible")
    name: str
    slug: str
    filter: Optional[ProductVariantFilterInput]
    sort_by: Optional[VariantSortingInput] = Field(..., alias="sortBy")
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    size: Optional[int]
    is_published: bool = Field(..., alias="isPublished")
    type: Optional[CollectionTypeEnum]
    custom_fields: SelectedAttribute = Field(..., alias="customFields")
    sales: Sale
    vouchers: Voucher
    on_sale: Optional[bool] = Field(..., alias="onSale")

from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Sale(BaseModel):
    id: str
    name: str
    type: DiscountValueTypeEnum
    value: Decimal
    start_date: datetime = Field(..., alias="startDate")
    end_date: Optional[datetime] = Field(..., alias="endDate")
    currency: str
    min_spent: Optional[Money] = Field(..., alias="minSpent")
    min_checkout_items_quantity: int = Field(..., alias="minCheckoutItemsQuantity")
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    sale_type: SaleTypeEnum = Field(..., alias="saleType")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class Fulfillment(BaseModel):
    id: str
    fulfillment_order: int = Field(..., alias="fulfillmentOrder")
    related_to: Optional[Fulfillment] = Field(..., alias="relatedTo")
    order: Order
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    status: FulfillmentStatus
    tracking_company: Optional[str] = Field(..., alias="trackingCompany")
    tracking_number: Optional[str] = Field(..., alias="trackingNumber")
    tracking_url: Optional[str] = Field(..., alias="trackingUrl")
    shipping_label_url: Optional[str] = Field(..., alias="shippingLabelUrl")
    created: datetime
    updated: datetime
    user: Optional[User]
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    lines: List[FulfillmentLine]
    seller: Optional[Seller]
    status_display: Optional[str] = Field(..., alias="statusDisplay")
    warehouse: Optional[Warehouse]
    total_lines_quantity: Optional[int] = Field(..., alias="totalLinesQuantity")
    total_lines_money: Money = Field(..., alias="totalLinesMoney")
    custom_fields: SelectedAttribute = Field(..., alias="customFields")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class NauticalOrder(BaseModel):
    id: str
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    order_source: NauticalOrderOrderSource = Field(..., alias="orderSource")
    created: datetime
    updated: Optional[datetime]
    status: NauticalOrderStatus
    sub_status: Optional[NauticalOrderSubStatus] = Field(..., alias="subStatus")
    user: Optional[User]
    language_code: str = Field(..., alias="languageCode")
    tracking_client_id: str = Field(..., alias="trackingClientId")
    billing_address: Optional[Address] = Field(..., alias="billingAddress")
    shipping_address: Optional[Address] = Field(..., alias="shippingAddress")
    currency: str
    is_marketplace_shipping_price_overridden: bool = Field(..., alias="isMarketplaceShippingPriceOverridden")
    shipping_price: Optional[TaxedMoney] = Field(..., alias="shippingPrice")
    eu_invoice_messaging: Optional[str] = Field(..., alias="euInvoiceMessaging")
    vat_identification_number: Optional[str] = Field(..., alias="vatIdentificationNumber")
    mp_vat_identification_number: Optional[str] = Field(..., alias="mpVatIdentificationNumber")
    token: str
    voucher: Optional[Voucher]
    shipping_discount: Optional[Money] = Field(..., alias="shippingDiscount")
    discount: Optional[Money]
    discount_name: Optional[str] = Field(..., alias="discountName")
    translated_discount_name: Optional[str] = Field(..., alias="translatedDiscountName")
    display_gross_prices: bool = Field(..., alias="displayGrossPrices")
    customer_note: str = Field(..., alias="customerNote")
    weight: Optional[Weight]
    imported_at: Optional[datetime] = Field(..., alias="importedAt")
    po_numbers: List[str] = Field(..., alias="poNumbers")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    available_marketplace_shipping_methods: List[ShippingMethod] = Field(..., alias="availableMarketplaceShippingMethods")
    seller_fulfillments: Fulfillment = Field(..., alias="sellerFulfillments")
    allowed_sub_statuses: List[OrderSubStatusEnum] = Field(..., alias="allowedSubStatuses")
    seller_unfulfilled: OrderLine = Field(..., alias="sellerUnfulfilled")
    lines: NauticalOrderLine
    actions: OrderAction
    available_shipping_methods_by_seller: List[MultiSellerShippingMethod] = Field(..., alias="availableShippingMethodsBySeller")
    invoices: List[Invoice]
    number: Optional[str]
    is_paid: Optional[bool] = Field(..., alias="isPaid")
    payment_status: PaymentChargeStatusEnum = Field(..., alias="paymentStatus")
    payment_status_display: str = Field(..., alias="paymentStatusDisplay")
    payments: List[Payment]
    total: Optional[TaxedMoney]
    subtotal: Optional[TaxedMoney]
    status_display: Optional[str] = Field(..., alias="statusDisplay")
    can_finalize: bool = Field(..., alias="canFinalize")
    validation_status: List[ValidationStatus] = Field(..., alias="validationStatus")
    total_authorized: Optional[Money] = Field(..., alias="totalAuthorized")
    total_captured: Optional[Money] = Field(..., alias="totalCaptured")
    total_refunded: Optional[Money] = Field(..., alias="totalRefunded")
    events: List[NauticalOrderEvent]
    positive: Optional[bool]
    user_email: Optional[str] = Field(..., alias="userEmail")
    is_shipping_required: bool = Field(..., alias="isShippingRequired")
    volume_discount: Optional[TaxedMoney] = Field(..., alias="volumeDiscount")
    shipping_method_name: str = Field(..., alias="shippingMethodName")
    sub_orders: List[Order] = Field(..., alias="subOrders")
    refunds: List[Refund]
    marketplace_shipping_price: TaxedMoney = Field(..., alias="marketplaceShippingPrice")
    marketplace_shipping_method: Optional[ShippingMethod] = Field(..., alias="marketplaceShippingMethod")
    marketplace_shipping_method_name: Optional[str] = Field(..., alias="marketplaceShippingMethodName")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class OrderLine(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    is_line_price_overridden: bool = Field(..., alias="isLinePriceOverridden")
    unit_price_overridden_note: Optional[str] = Field(..., alias="unitPriceOverriddenNote")
    note: Optional[str]
    product_name: str = Field(..., alias="productName")
    variant_name: str = Field(..., alias="variantName")
    product_sku: Optional[str] = Field(..., alias="productSku")
    is_shipping_required: bool = Field(..., alias="isShippingRequired")
    quantity_fulfilled: int = Field(..., alias="quantityFulfilled")
    quantity_declined: int = Field(..., alias="quantityDeclined")
    digital_content_url: Optional[DigitalContentUrl] = Field(..., alias="digitalContentUrl")
    order: Order
    nautical_order_line: NauticalOrderLine = Field(..., alias="nauticalOrderLine")
    size: Optional[int]
    unit_price: Optional[TaxedMoney] = Field(..., alias="unitPrice")
    total_price: Optional[TaxedMoney] = Field(..., alias="totalPrice")
    variant: Optional[ProductVariant]
    translated_product_name: str = Field(..., alias="translatedProductName")
    translated_variant_name: str = Field(..., alias="translatedVariantName")
    allocations: List[Allocation]
    price_book: Optional[PriceBook] = Field(..., alias="priceBook")
    quantity_ordered: int = Field(..., alias="quantityOrdered")
    unfulfilled_quantity_refunded: int = Field(..., alias="unfulfilledQuantityRefunded")
    fulfilled_quantity_refunded: int = Field(..., alias="fulfilledQuantityRefunded")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from uuid import UUID


class DigitalContentUrl(BaseModel):
    content: DigitalContent
    created: datetime
    download_num: int = Field(..., alias="downloadNum")
    id: str
    url: Optional[str]
    token: UUID

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class DigitalContent(BaseModel):
    use_default_settings: bool = Field(..., alias="useDefaultSettings")
    automatic_fulfillment: bool = Field(..., alias="automaticFulfillment")
    product_variant: ProductVariant = Field(..., alias="productVariant")
    content_file: Optional[str] = Field(..., alias="contentFile")
    max_downloads: Optional[int] = Field(..., alias="maxDownloads")
    url_valid_days: Optional[int] = Field(..., alias="urlValidDays")
    urls: List[DigitalContentUrl]
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderLine(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    is_line_price_overridden: bool = Field(..., alias="isLinePriceOverridden")
    unit_price_overridden_note: Optional[str] = Field(..., alias="unitPriceOverriddenNote")
    note: Optional[str]
    product_name: str = Field(..., alias="productName")
    variant_name: str = Field(..., alias="variantName")
    product_sku: Optional[str] = Field(..., alias="productSku")
    is_shipping_required: bool = Field(..., alias="isShippingRequired")
    digital_content_url: Optional[DigitalContentUrl] = Field(..., alias="digitalContentUrl")
    size: Optional[int]
    unit_price: Optional[TaxedMoney] = Field(..., alias="unitPrice")
    total_price: Optional[TaxedMoney] = Field(..., alias="totalPrice")
    variant: Optional[ProductVariant]
    translated_product_name: str = Field(..., alias="translatedProductName")
    translated_variant_name: str = Field(..., alias="translatedVariantName")
    price_book: Optional[PriceBook] = Field(..., alias="priceBook")
    seller_orderline: Optional[OrderLine] = Field(..., alias="sellerOrderline")
    quantity_ordered: int = Field(..., alias="quantityOrdered")
    sale: Optional[Sale]
    sale_discount: Optional[Money] = Field(..., alias="saleDiscount")
    voucher_discount: Optional[Money] = Field(..., alias="voucherDiscount")
    original_unit_price: Optional[TaxedMoney] = Field(..., alias="originalUnitPrice")
    discounted_unit_price: Optional[TaxedMoney] = Field(..., alias="discountedUnitPrice")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class PriceBook(BaseModel):
    description: str
    description_html: str = Field(..., alias="descriptionHtml")
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    name: str
    deleted: bool
    price_book_variants: List[PriceBookVariant] = Field(..., alias="priceBookVariants")
    price_book_products: List[PriceBookProduct] = Field(..., alias="priceBookProducts")
    price_book_product_types: List[PriceBookProductType] = Field(..., alias="priceBookProductTypes")
    number_of_products: int = Field(..., alias="numberOfProducts")
    number_of_product_types: int = Field(..., alias="numberOfProductTypes")
    number_of_variants: int = Field(..., alias="numberOfVariants")

from pydantic import BaseModel, Field


class PriceBookVariant(BaseModel):
    id: str
    price_book: PriceBook = Field(..., alias="priceBook")
    variant: ProductVariant
    value_type: PriceBookVariantValueType = Field(..., alias="valueType")
    currency: str
    price: Money
    percentage: float

from pydantic import BaseModel, Field


class PriceBookProduct(BaseModel):
    id: str
    price_book: PriceBook = Field(..., alias="priceBook")
    product: Product
    value_type: PriceBookProductValueType = Field(..., alias="valueType")
    currency: str
    price: Money
    percentage: float

from pydantic import BaseModel, Field


class PriceBookProductType(BaseModel):
    id: str
    price_book: PriceBook = Field(..., alias="priceBook")
    product_type: ProductType = Field(..., alias="productType")
    value_type: PriceBookProductTypeValueType = Field(..., alias="valueType")
    currency: str
    price: Money
    percentage: float

from pydantic import BaseModel, Field


class Allocation(BaseModel):
    id: str
    quantity: int
    warehouse: Warehouse

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Warehouse(BaseModel):
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    id: str
    name: str
    slug: str
    company_name: str = Field(..., alias="companyName")
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    address: Address
    email: str
    seller: Seller
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShippingZoneCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: ShippingZoneCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class ShippingZoneCountableEdge(BaseModel):
    node: ShippingZone
    cursor: str

from pydantic import BaseModel, Field


class ShippingZone(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    name: str
    seller: Seller
    warehouses: Warehouse
    price_range: MoneyRange = Field(..., alias="priceRange")
    countries: CountryDisplay
    shipping_methods: ShippingMethod = Field(..., alias="shippingMethods")
    country_areas: ShippingZoneCountryArea = Field(..., alias="countryAreas")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MoneyRange(BaseModel):
    start: Optional[Money]
    stop: Optional[Money]

from pydantic import BaseModel, Field


class ShippingZoneCountryArea(BaseModel):
    id: str
    country: CountryDisplay
    country_area: CountryArea = Field(..., alias="countryArea")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Invoice(BaseModel):
    id: str
    metadata: MetadataItem
    status: JobStatusEnum
    number: str
    external_url: Optional[str] = Field(..., alias="externalUrl")
    is_valid: bool = Field(..., alias="isValid")
    is_editable: bool = Field(..., alias="isEditable")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    message: Optional[str]
    url: Optional[str]

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class Payment(BaseModel):
    id: str
    gateway: str
    is_active: bool = Field(..., alias="isActive")
    created: datetime
    modified: datetime
    token: str
    checkout: Optional[Checkout]
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    payment_method_type: str = Field(..., alias="paymentMethodType")
    payment_method_token: Optional[str] = Field(..., alias="paymentMethodToken")
    customer_ip_address: Optional[str] = Field(..., alias="customerIpAddress")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    charge_status: PaymentChargeStatusEnum = Field(..., alias="chargeStatus")
    actions: OrderAction
    total: Optional[Money]
    captured_amount: Optional[Money] = Field(..., alias="capturedAmount")
    transactions: List[Transaction]
    available_capture_amount: Optional[Money] = Field(..., alias="availableCaptureAmount")
    available_refund_amount: Optional[Money] = Field(..., alias="availableRefundAmount")
    credit_card: Optional[CreditCard] = Field(..., alias="creditCard")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Transaction(BaseModel):
    id: str
    created: datetime
    payment: Payment
    token: str
    kind: TransactionKind
    is_success: bool = Field(..., alias="isSuccess")
    error: Optional[str]
    amount: Optional[Money]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CreditCard(BaseModel):
    brand: str
    first_digits: Optional[str] = Field(..., alias="firstDigits")
    last_digits: str = Field(..., alias="lastDigits")
    exp_month: Optional[int] = Field(..., alias="expMonth")
    exp_year: Optional[int] = Field(..., alias="expYear")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ValidationStatus(BaseModel):
    message: Optional[str]
    code: Optional[str]
    variant: Optional[str]

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class NauticalOrderEvent(BaseModel):
    id: str
    date: datetime
    type: OrderEventsEnum
    user: Optional[User]
    message: Optional[str]
    email: Optional[str]
    email_type: Optional[OrderEventsEmailsEnum] = Field(..., alias="emailType")
    amount: Optional[float]
    payment_id: Optional[str] = Field(..., alias="paymentId")
    payment_gateway: Optional[str] = Field(..., alias="paymentGateway")
    quantity: Optional[int]
    composed_id: Optional[str] = Field(..., alias="composedId")
    order_number: Optional[str] = Field(..., alias="orderNumber")
    invoice_number: Optional[str] = Field(..., alias="invoiceNumber")
    oversold_items: List[str] = Field(..., alias="oversoldItems")
    lines: List[NauticalOrderEventOrderLineObject]
    warehouse: Optional[Warehouse]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderEventOrderLineObject(BaseModel):
    quantity: Optional[int]
    order_line: Optional[NauticalOrderLine] = Field(..., alias="orderLine")
    item_name: Optional[str] = Field(..., alias="itemName")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Refund(BaseModel):
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    description: str
    description_html: str = Field(..., alias="descriptionHtml")
    id: str
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    buyer: Optional[User]
    external_id: Optional[str] = Field(..., alias="externalId")
    name: str
    order: NauticalOrder
    status: RefundStatusEnum
    token: str
    refund_type: RefundTypeEnum = Field(..., alias="refundType")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundLineCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: RefundLineCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class RefundLineCountableEdge(BaseModel):
    node: RefundLine
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field


class RefundLine(BaseModel):
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    id: str
    charged_to: RefundChargeToEnum = Field(..., alias="chargedTo")
    currency: str
    line_scope: RefundLineScopeEnum = Field(..., alias="lineScope")
    line_type: RefundLineTypeEnum = Field(..., alias="lineType")
    percentage: float
    quantity_fulfilled: int = Field(..., alias="quantityFulfilled")
    quantity_unfulfilled: int = Field(..., alias="quantityUnfulfilled")
    refund: Refund
    refund_scope: RefundScope = Field(..., alias="refundScope")
    total: TaxedMoney

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundPaymentCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: RefundPaymentCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class RefundPaymentCountableEdge(BaseModel):
    node: RefundPayment
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field


class RefundPayment(BaseModel):
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    id: str
    payment_type: RefundPaymentTypeEnum = Field(..., alias="paymentType")
    refund: Refund
    refund_method: RefundMethod = Field(..., alias="refundMethod")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FulfillmentLine(BaseModel):
    id: str
    quantity: int
    order_line: Optional[OrderLine] = Field(..., alias="orderLine")
    return_reason: Optional[str] = Field(..., alias="returnReason")

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderFee(BaseModel):
    id: str
    tenant: Tenant
    order: Optional[Order]
    currency: NauticalCurrency
    transaction_amount: Decimal = Field(..., alias="transactionAmount")
    transaction_currency: NauticalCurrency = Field(..., alias="transactionCurrency")
    transaction_fee: Optional[Money] = Field(..., alias="transactionFee")
    domiciled_amount: Decimal = Field(..., alias="domiciledAmount")
    domiciled_fee: Optional[Money] = Field(..., alias="domiciledFee")
    source: Optional[SourceFeeEnum]
    name: str
    notes: str
    data: Dict[str, Any]

from pydantic import BaseModel, Field


class NauticalCurrency(BaseModel):
    code: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class OrderEvent(BaseModel):
    id: str
    date: datetime
    type: Optional[OrderEventsEnum]
    user: Optional[User]
    message: Optional[str]
    email: Optional[str]
    email_type: Optional[OrderEventsEmailsEnum] = Field(..., alias="emailType")
    amount: Optional[float]
    payment_id: Optional[str] = Field(..., alias="paymentId")
    payment_gateway: Optional[str] = Field(..., alias="paymentGateway")
    quantity: Optional[int]
    composed_id: Optional[str] = Field(..., alias="composedId")
    order_number: Optional[str] = Field(..., alias="orderNumber")
    invoice_number: Optional[str] = Field(..., alias="invoiceNumber")
    oversold_items: List[str] = Field(..., alias="oversoldItems")
    lines: List[OrderEventOrderLineObject]
    fulfilled_items: List[FulfillmentLine] = Field(..., alias="fulfilledItems")
    warehouse: Optional[Warehouse]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderEventOrderLineObject(BaseModel):
    quantity: Optional[int]
    order_line: Optional[OrderLine] = Field(..., alias="orderLine")
    item_name: Optional[str] = Field(..., alias="itemName")

from pydantic import BaseModel, Field


class OrderPayoutSummary(BaseModel):
    commissions: Money
    discounts: Money
    fees: Money
    refunds: Money
    refunds_commission: Money = Field(..., alias="refundsCommission")
    sales: Money
    shipping: Money
    total: Money
    vendor_payout: VendorPayout = Field(..., alias="vendorPayout")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementSellersCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: AgreementSellersCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class AgreementSellersCountableEdge(BaseModel):
    node: AgreementSellers
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementSellers(BaseModel):
    id: str
    tenant: Tenant
    seller: Seller
    acknowledged_on: Optional[datetime] = Field(..., alias="acknowledgedOn")
    plan: Optional[Agreement]
    effective_at: datetime = Field(..., alias="effectiveAt")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem

from datetime import datetime, date
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Agreement(BaseModel):
    id: str
    publication_date: Optional[date] = Field(..., alias="publicationDate")
    is_published: bool = Field(..., alias="isPublished")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    content: str
    content_html: str = Field(..., alias="contentHtml")
    tenant: Tenant
    seo_title: Optional[str] = Field(..., alias="seoTitle")
    seo_description: Optional[str] = Field(..., alias="seoDescription")
    slug: str
    title: str
    commission_type: CommissionTypeEnum = Field(..., alias="commissionType")
    default_commission: Decimal = Field(..., alias="defaultCommission")
    markup_commission_type: MarkupCommissionTypeEnum = Field(..., alias="markupCommissionType")
    markup_commission_value: Optional[Decimal] = Field(..., alias="markupCommissionValue")
    is_active: Optional[bool] = Field(..., alias="isActive")
    granular_commissions: AgreementCommission = Field(..., alias="granularCommissions")
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    fees: AgreementFees
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementCommission(BaseModel):
    id: str
    tenant: Tenant
    commission: Decimal
    agreement: Agreement
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    instance: Optional[Category]

from decimal import Decimal
from pydantic import BaseModel, Field


class AgreementFees(BaseModel):
    id: str
    tenant: Tenant
    agreement: Agreement
    fee_type: FeeType = Field(..., alias="feeType")
    fee_scope: FeeScope = Field(..., alias="feeScope")
    fee_value: Decimal = Field(..., alias="feeValue")
    fee_name: str = Field(..., alias="feeName")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WarehouseCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: WarehouseCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class WarehouseCountableEdge(BaseModel):
    node: Warehouse
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Microsite(BaseModel):
    id: str
    publication_date: Optional[date] = Field(..., alias="publicationDate")
    description: str
    description_html: str = Field(..., alias="descriptionHtml")
    seo_title: Optional[str] = Field(..., alias="seoTitle")
    seo_description: Optional[str] = Field(..., alias="seoDescription")
    name: str
    slug: str
    footer_text: Optional[str] = Field(..., alias="footerText")
    seller: Optional[Seller]
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    filter: Optional[ProductFilterInput]
    sort_by: Optional[ProductOrder] = Field(..., alias="sortBy")
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    size: Optional[int]
    is_published: bool = Field(..., alias="isPublished")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Document(BaseModel):
    id: str
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    tenant: Tenant
    file: str
    name: str
    description: str
    file_extension: str = Field(..., alias="fileExtension")
    file_content_type: Optional[str] = Field(..., alias="fileContentType")
    file_size: Optional[FileSize] = Field(..., alias="fileSize")
    url: Optional[str]

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FileSize(BaseModel):
    bytes: Optional[int]
    kilobytes: Optional[Decimal]
    megabytes: Optional[Decimal]

from pydantic import BaseModel, Field


class ProductPricingInfo(BaseModel):
    on_sale: bool = Field(..., alias="onSale")
    discount: TaxedMoney
    discount_local_currency: TaxedMoney = Field(..., alias="discountLocalCurrency")
    price_range: TaxedMoneyRange = Field(..., alias="priceRange")
    price_range_undiscounted: TaxedMoneyRange = Field(..., alias="priceRangeUndiscounted")
    price_range_local_currency: TaxedMoneyRange = Field(..., alias="priceRangeLocalCurrency")
    price_range_undiscounted_local_currency: TaxedMoneyRange = Field(..., alias="priceRangeUndiscountedLocalCurrency")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TaxedMoneyRange(BaseModel):
    start: Optional[TaxedMoney]
    stop: Optional[TaxedMoney]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Margin(BaseModel):
    start: Optional[int]
    stop: Optional[int]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductImage(BaseModel):
    id: str
    sort_order: Optional[int] = Field(..., alias="sortOrder")
    external_id: Optional[str] = Field(..., alias="externalId")
    external_source: Optional[str] = Field(..., alias="externalSource")
    alt: str
    size: Optional[int]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductImageCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: ProductImageCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class ProductImageCountableEdge(BaseModel):
    node: ProductImage
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Location(BaseModel):
    id: str
    lon: Optional[float]
    lat: Optional[float]
    location_type: Optional[LocationTypeEnum] = Field(..., alias="locationType")
    location_kind: Optional[LocationKindEnum] = Field(..., alias="locationKind")
    company_name: str = Field(..., alias="companyName")
    street_address1: str = Field(..., alias="streetAddress1")
    street_address2: str = Field(..., alias="streetAddress2")
    city: str
    city_area: str = Field(..., alias="cityArea")
    postal_code: str = Field(..., alias="postalCode")
    country: CountryDisplay
    country_area: str = Field(..., alias="countryArea")
    phone: Optional[str]

from pydantic import BaseModel, Field


class WarehouseStats(BaseModel):
    warehouse_id: str = Field(..., alias="warehouseId")
    quantity: int
    quantity_allocated: int = Field(..., alias="quantityAllocated")
    quantity_available: int = Field(..., alias="quantityAvailable")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductStatusLog(BaseModel):
    user: Optional[User]
    sub_status: Optional[ProductSubStatusEnum] = Field(..., alias="subStatus")
    sub_status_reason: Optional[str] = Field(..., alias="subStatusReason")
    created_at: Optional[datetime] = Field(..., alias="createdAt")
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem

from pydantic import BaseModel, Field


class VariantPricingInfo(BaseModel):
    on_sale: bool = Field(..., alias="onSale")
    discount: TaxedMoney
    discount_local_currency: TaxedMoney = Field(..., alias="discountLocalCurrency")
    price: TaxedMoney
    price_undiscounted: TaxedMoney = Field(..., alias="priceUndiscounted")
    price_local_currency: TaxedMoney = Field(..., alias="priceLocalCurrency")
    price_undiscounted_local_currency: TaxedMoney = Field(..., alias="priceUndiscountedLocalCurrency")

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VariantSize(BaseModel):
    length: Optional[Decimal]
    width: Optional[Decimal]
    height: Optional[Decimal]
    size_units: Optional[DistanceUnitsEnum] = Field(..., alias="sizeUnits")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Stock(BaseModel):
    warehouse: Warehouse
    product_variant: ProductVariant = Field(..., alias="productVariant")
    quantity: int
    out_of_stock_threshold: Optional[int] = Field(..., alias="outOfStockThreshold")
    quantity_allocated: int = Field(..., alias="quantityAllocated")
    id: str
    quantity_available: int = Field(..., alias="quantityAvailable")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class StockEvent(BaseModel):
    id: str
    date: datetime
    type: StockEventType
    stock: Optional[Stock]
    parameters: Dict[str, Any]
    user: Optional[User]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerType(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    pk: Optional[int]
    company_name: Optional[str] = Field(..., alias="companyName")
    owner: Optional[UserType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class UserType(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    first_name: Optional[str] = Field(..., alias="firstName")
    last_name: Optional[str] = Field(..., alias="lastName")
    email: Optional[str]
    default_shipping_address: Optional[AddressType] = Field(..., alias="defaultShippingAddress")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AddressType(BaseModel):
    id: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    first_name: Optional[str] = Field(..., alias="firstName")
    last_name: Optional[str] = Field(..., alias="lastName")
    street_address1: Optional[str] = Field(..., alias="streetAddress1")
    street_address2: Optional[str] = Field(..., alias="streetAddress2")
    city: Optional[str]
    postal_code: Optional[str] = Field(..., alias="postalCode")
    country: Optional[str]
    country_area: Optional[str] = Field(..., alias="countryArea")
    phone: Optional[str]

from decimal import Decimal
from pydantic import BaseModel, Field


class CheckoutSellerShipping(BaseModel):
    tenant: Tenant
    id: str
    seller: Seller
    shipping_method: ShippingMethod = Field(..., alias="shippingMethod")
    is_price_overridden: bool = Field(..., alias="isPriceOverridden")
    price_override_amount: Decimal = Field(..., alias="priceOverrideAmount")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: NauticalOrderCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class NauticalOrderCountableEdge(BaseModel):
    node: NauticalOrder
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class UserPermission(BaseModel):
    code: PermissionEnum
    name: str
    user_id: Optional[str] = Field(..., alias="userId")

from pydantic import BaseModel, Field


class Group(BaseModel):
    id: str
    name: str
    permissions: Permission
    users: User
    user_can_manage: bool = Field(..., alias="userCanManage")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomerEvent(BaseModel):
    id: str
    date: Optional[datetime]
    type: Optional[CustomerEventsEnum]
    user: Optional[User]
    message: Optional[str]
    count: Optional[int]
    order: Optional[Order]
    order_line: Optional[OrderLine] = Field(..., alias="orderLine")
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PaymentSource(BaseModel):
    id: str
    gateway: str
    credit_card_info: Optional[CreditCard] = Field(..., alias="creditCardInfo")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: WishlistCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class WishlistCountableEdge(BaseModel):
    node: Wishlist
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WebhookEventLogCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: WebhookEventLogCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class WebhookEventLogCountableEdge(BaseModel):
    node: WebhookEventLog
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WebhookEventLog(BaseModel):
    id: str
    tenant: Tenant
    date: datetime
    target_url: Optional[str] = Field(..., alias="targetUrl")
    event_type: str = Field(..., alias="eventType")
    webhook_id: Optional[str] = Field(..., alias="webhookId")
    transaction_id: Optional[str] = Field(..., alias="transactionId")
    app_id: Optional[str] = Field(..., alias="appId")
    plugin_id: Optional[str] = Field(..., alias="pluginId")
    payload: Dict[str, Any]
    error: Optional[str]
    direction: Optional[WebhookDirectionEnum]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WebhookJobCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: WebhookJobCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class WebhookJobCountableEdge(BaseModel):
    node: WebhookJob
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WebhookJob(BaseModel):
    id: str
    status: JobStatusEnum
    message: Optional[str]
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    tenant: Tenant
    body: Optional[Dict[str, Any]]
    request_meta: Optional[Dict[str, Any]] = Field(..., alias="requestMeta")
    source: Optional[str]
    type: Optional[GenericWebhookTransactionType]
    vendor_entity_link: Optional[str] = Field(..., alias="vendorEntityLink")
    marketplace_entity_link: Optional[str] = Field(..., alias="marketplaceEntityLink")
    seller: Optional[Seller]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class StockCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: StockCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class StockCountableEdge(BaseModel):
    node: Stock
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Content(BaseModel):
    publication_date: Optional[date] = Field(..., alias="publicationDate")
    is_published: bool = Field(..., alias="isPublished")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    id: str
    slug: str
    is_page: bool = Field(..., alias="isPage")
    locked_by: Optional[User] = Field(..., alias="lockedBy")
    lock_expiry: Optional[datetime] = Field(..., alias="lockExpiry")
    data: Dict[str, Any]
    draft_data: Dict[str, Any] = Field(..., alias="draftData")
    revision: int
    has_active_draft: Optional[bool] = Field(..., alias="hasActiveDraft")
    content_page_data: Optional[ContentPageData] = Field(..., alias="contentPageData")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentPageData(BaseModel):
    seo_title: Optional[str] = Field(..., alias="seoTitle")
    seo_description: Optional[str] = Field(..., alias="seoDescription")
    id: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: ContentCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class ContentCountableEdge(BaseModel):
    node: Content
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Media(BaseModel):
    tenant: Tenant
    id: str
    title: str
    created_at: str = Field(..., alias="createdAt")
    image: Optional[Image]
    alt: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MediaCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: MediaCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class MediaCountableEdge(BaseModel):
    node: Media
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TenantCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: TenantCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class TenantCountableEdge(BaseModel):
    node: Tenant
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Shop(BaseModel):
    currency: Optional[str]
    geolocalization: Optional[Geolocalization]
    language_code: Optional[LanguageCodeEnum] = Field(..., alias="languageCode")
    supported_currencies: NauticalCurrency = Field(..., alias="supportedCurrencies")
    default_country: Optional[CountryDisplay] = Field(..., alias="defaultCountry")
    default_mail_sender_name: Optional[str] = Field(..., alias="defaultMailSenderName")
    default_mail_sender_address: Optional[str] = Field(..., alias="defaultMailSenderAddress")
    default_mail_support_address: Optional[str] = Field(..., alias="defaultMailSupportAddress")
    description: Optional[str]
    domain: Domain
    api_url: Optional[str] = Field(..., alias="apiUrl")
    dashboard_url: Optional[str] = Field(..., alias="dashboardUrl")
    enable_quote_orders: Optional[bool] = Field(..., alias="enableQuoteOrders")
    enable_offer_orders: Optional[bool] = Field(..., alias="enableOfferOrders")
    name: str
    permissions: Permission
    phone_prefixes: str = Field(..., alias="phonePrefixes")
    include_taxes_in_prices: bool = Field(..., alias="includeTaxesInPrices")
    charge_taxes_on_shipping: bool = Field(..., alias="chargeTaxesOnShipping")
    track_inventory_by_default: Optional[bool] = Field(..., alias="trackInventoryByDefault")
    default_weight_unit: Optional[WeightUnitsEnum] = Field(..., alias="defaultWeightUnit")
    automatic_fulfillment_digital_products: Optional[bool] = Field(..., alias="automaticFulfillmentDigitalProducts")
    default_digital_max_downloads: Optional[int] = Field(..., alias="defaultDigitalMaxDownloads")
    default_digital_url_valid_days: Optional[int] = Field(..., alias="defaultDigitalUrlValidDays")
    company_address: Optional[Address] = Field(..., alias="companyAddress")
    customer_set_password_url: Optional[str] = Field(..., alias="customerSetPasswordUrl")
    login_for_checkout: Optional[bool] = Field(..., alias="loginForCheckout")
    login_for_price: Optional[bool] = Field(..., alias="loginForPrice")
    active_plugins: Plugin = Field(..., alias="activePlugins")
    crisp_website_id: Optional[str] = Field(..., alias="crispWebsiteId")
    geolocation_enabled: Optional[bool] = Field(..., alias="geolocationEnabled")
    require_product_approval: Optional[bool] = Field(..., alias="requireProductApproval")
    timezone: str
    checkout_theme: Optional[CheckoutTheme] = Field(..., alias="checkoutTheme")
    storefront_theme: Optional[StorefrontTheme] = Field(..., alias="storefrontTheme")
    seller_onboarding_settings: Optional[SellerOnboardingSettings] = Field(..., alias="sellerOnboardingSettings")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Geolocalization(BaseModel):
    country: Optional[CountryDisplay]

from pydantic import BaseModel, Field


class Domain(BaseModel):
    host: str
    url: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class Plugin(BaseModel):
    id: str
    private_metadata: Dict[str, Any] = Field(..., alias="privateMetadata")
    metadata: Dict[str, Any]
    company: Optional[str]
    category: Optional[PluginConfigurationCategory]
    description_short: str = Field(..., alias="descriptionShort")
    logo_url: Optional[str] = Field(..., alias="logoUrl")
    created: datetime
    external_url: Optional[str] = Field(..., alias="externalUrl")
    support_url: Optional[str] = Field(..., alias="supportUrl")
    allow_sellers: Optional[bool] = Field(..., alias="allowSellers")
    allow_many_active_plugins_in_category: bool = Field(..., alias="allowManyActivePluginsInCategory")
    tenant: Tenant
    identifier: str
    name: str
    description: str
    active: bool
    configuration: List[ConfigurationItem]
    default_configuration: List[ConfigurationItem] = Field(..., alias="defaultConfiguration")
    support_seller_configuration: Optional[bool] = Field(..., alias="supportSellerConfiguration")
    version: str

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class ConfigurationItem(BaseModel):
    name: str
    value: Optional[str]
    type: Optional[ConfigurationTypeFieldEnum]
    help_text: Optional[str] = Field(..., alias="helpText")
    label: Optional[str]
    options: List[str]

from pydantic import BaseModel, Field


class CheckoutTheme(BaseModel):
    id: str
    confirmation_url: str = Field(..., alias="confirmationUrl")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class StorefrontTheme(BaseModel):
    id: str
    primary_color: Optional[str] = Field(..., alias="primaryColor")
    background_color: Optional[str] = Field(..., alias="backgroundColor")
    logo: Optional[Image]
    favicon_image: Optional[Image] = Field(..., alias="faviconImage")
    favicon_url: Optional[str] = Field(..., alias="faviconUrl")
    font: Optional[Font]
    font_color: Optional[str] = Field(..., alias="fontColor")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Font(BaseModel):
    id: str
    name: Optional[str]
    slug: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerOnboardingSettings(BaseModel):
    id: str
    is_accepting_new_sellers: Optional[bool] = Field(..., alias="isAcceptingNewSellers")
    summary: Optional[str]
    welcome_message: Optional[str] = Field(..., alias="welcomeMessage")
    fulfillment_model: Optional[str] = Field(..., alias="fulfillmentModel")
    required_documents: Optional[str] = Field(..., alias="requiredDocuments")
    not_accepting_sellers_message: Optional[str] = Field(..., alias="notAcceptingSellersMessage")
    is_product_import_allowed: Optional[bool] = Field(..., alias="isProductImportAllowed")

from pydantic import BaseModel, Field


class CustomDomain(BaseModel):
    id: str
    domain: str
    status: DomainStatusEnum
    error_details: str = Field(..., alias="errorDetails")
    ssl_cert_name: str = Field(..., alias="sslCertName")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PublicSeller(BaseModel):
    id: str
    company_name: str = Field(..., alias="companyName")
    slug: str
    size: Optional[int]
    status: SellerStatus
    store_description: str = Field(..., alias="storeDescription")
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: SellerCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class SellerCountableEdge(BaseModel):
    node: Seller
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class UserCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: UserCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class UserCountableEdge(BaseModel):
    node: User
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: AgreementCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class AgreementCountableEdge(BaseModel):
    node: Agreement
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerCards(BaseModel):
    new_sellers: Optional[int] = Field(..., alias="newSellers")
    seller_orders: Optional[int] = Field(..., alias="sellerOrders")
    seller_commissions: Optional[Money] = Field(..., alias="sellerCommissions")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerDetailCards(BaseModel):
    seller_orders: Optional[int] = Field(..., alias="sellerOrders")
    seller_commissions: Optional[Money] = Field(..., alias="sellerCommissions")
    seller_sales: Optional[TaxedMoney] = Field(..., alias="sellerSales")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: RefundCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class RefundCountableEdge(BaseModel):
    node: Refund
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DigitalContentCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: DigitalContentCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class DigitalContentCountableEdge(BaseModel):
    node: DigitalContent
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PriceBookCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PriceBookCountableEdge(BaseModel):
    node: PriceBook
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookVariantCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PriceBookVariantCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PriceBookVariantCountableEdge(BaseModel):
    node: PriceBookVariant
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PriceBookProductCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PriceBookProductCountableEdge(BaseModel):
    node: PriceBookProduct
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductTypeCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PriceBookProductTypeCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PriceBookProductTypeCountableEdge(BaseModel):
    node: PriceBookProductType
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookVariantHistoryCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PriceBookVariantHistoryCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PriceBookVariantHistoryCountableEdge(BaseModel):
    node: PriceBookVariantHistory
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookVariantHistory(BaseModel):
    id: str
    price_book: Optional[PriceBook] = Field(..., alias="priceBook")
    variant_id: int = Field(..., alias="variantId")
    value_type: PriceBookVariantHistoryValueType = Field(..., alias="valueType")
    currency: str
    created_at: date = Field(..., alias="createdAt")
    price: Money
    percentage: float
    deleted: bool

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductHistoryCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PriceBookProductHistoryCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PriceBookProductHistoryCountableEdge(BaseModel):
    node: PriceBookProductHistory
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductHistory(BaseModel):
    id: str
    price_book: Optional[PriceBook] = Field(..., alias="priceBook")
    product_id: int = Field(..., alias="productId")
    value_type: PriceBookProductHistoryValueType = Field(..., alias="valueType")
    currency: str
    created_at: date = Field(..., alias="createdAt")
    price: Money
    percentage: float
    deleted: bool

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductTypeHistoryCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PriceBookProductTypeHistoryCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PriceBookProductTypeHistoryCountableEdge(BaseModel):
    node: PriceBookProductTypeHistory
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductTypeHistory(BaseModel):
    id: str
    price_book: Optional[PriceBook] = Field(..., alias="priceBook")
    product_type_id: int = Field(..., alias="productTypeId")
    value_type: PriceBookProductTypeHistoryValueType = Field(..., alias="valueType")
    currency: str
    created_at: date = Field(..., alias="createdAt")
    price: Money
    percentage: float
    deleted: bool

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PluginCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PluginCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PluginCountableEdge(BaseModel):
    node: Plugin
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TaxCertificate(BaseModel):
    id: Optional[int]
    company_id: Optional[str] = Field(..., alias="companyId")
    signed_date: Optional[str] = Field(..., alias="signedDate")
    expiration_date: Optional[str] = Field(..., alias="expirationDate")
    filename: Optional[str]
    document_exists: Optional[bool] = Field(..., alias="documentExists")
    download_url: Optional[str] = Field(..., alias="downloadUrl")
    valid: Optional[bool]
    verified: Optional[bool]
    exempt_percentage: Optional[str] = Field(..., alias="exemptPercentage")
    is_single_certificate: Optional[bool] = Field(..., alias="isSingleCertificate")
    exemption_number: Optional[str] = Field(..., alias="exemptionNumber")
    exemption_reason_name: Optional[str] = Field(..., alias="exemptionReasonName")
    exemption_reason_id: Optional[int] = Field(..., alias="exemptionReasonId")
    status: Optional[str]
    created_date: Optional[str] = Field(..., alias="createdDate")
    modified_date: Optional[str] = Field(..., alias="modifiedDate")
    tax_number_type: Optional[str] = Field(..., alias="taxNumberType")
    business_number_type: Optional[str] = Field(..., alias="businessNumberType")
    exposure_zone_name: Optional[str] = Field(..., alias="exposureZoneName")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CatalogImportProcess(BaseModel):
    status: CatalogImportProcessStatus
    message: Optional[str]
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    task_id: Optional[str] = Field(..., alias="taskId")
    external_source: str = Field(..., alias="externalSource")
    finished_at: Optional[datetime] = Field(..., alias="finishedAt")
    created_by: Optional[User] = Field(..., alias="createdBy")
    seller: Optional[Seller]
    internal_notes: Optional[str] = Field(..., alias="internalNotes")
    id: str
    filter: Optional[CatalogImportProcessLogRecordFilterInput]
    sort_by: Optional[CatalogImportProcessLogRecordSortInput] = Field(..., alias="sortBy")
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CatalogImportProcessLogRecordCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: CatalogImportProcessLogRecordCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class CatalogImportProcessLogRecordCountableEdge(BaseModel):
    node: CatalogImportProcessLogRecord
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CatalogImportProcessLogRecord(BaseModel):
    id: str
    created_at: datetime = Field(..., alias="createdAt")
    task_id: Optional[str] = Field(..., alias="taskId")
    object_id: Optional[str] = Field(..., alias="objectId")
    operation: CatalogImportProcessLogRecordOperation
    related_object_name: Optional[str] = Field(..., alias="relatedObjectName")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CatalogImportProcessCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: CatalogImportProcessCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class CatalogImportProcessCountableEdge(BaseModel):
    node: CatalogImportProcess
    cursor: str

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class TaxExemptCode(BaseModel):
    code: str
    name: str
    description: str
    valid_countries: List[str] = Field(..., alias="validCountries")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class TypeformForms(BaseModel):
    total_items: Optional[int] = Field(..., alias="totalItems")
    page_count: Optional[int] = Field(..., alias="pageCount")
    items: List[TypeformFormsItem]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TypeformFormsItem(BaseModel):
    links: Optional[TypeformFormsItemLink] = Field(..., alias="Links")
    id: Optional[str]
    last_updated_at: Optional[str] = Field(..., alias="lastUpdatedAt")
    self: Optional[TypeformFormsItemSelf]
    theme: Optional[TypeformFormsItemSelf]
    title: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TypeformFormsItemLink(BaseModel):
    display: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TypeformFormsItemSelf(BaseModel):
    href: Optional[str]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class TypeformForm(BaseModel):
    id: Optional[str]
    title: Optional[str]
    language: Optional[str]
    fields: List[TypeformFormFields]
    hidden: List[str]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class TypeformFormFields(BaseModel):
    attachment: Optional[TypeformFormAttachment]
    field_type: Optional[str] = Field(..., alias="fieldType")
    id: Optional[str]
    layout: Optional[TypeformFormLayout]
    name: Optional[str]
    options: List[TypeformFormOption]
    ref: Optional[str]
    required: Optional[bool]
    title: Optional[str]
    properties: Optional[TypeformFormProperties]
    type: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TypeformFormAttachment(BaseModel):
    type: Optional[str]
    href: Optional[str]
    properties: Optional[TypeformFormProperties]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class TypeformFormProperties(BaseModel):
    description: Optional[str]
    fields: List[TypeformGroupProperties]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TypeformGroupProperties(BaseModel):
    id: Optional[str]
    title: Optional[str]
    ref: Optional[str]
    type: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TypeformFormLayout(BaseModel):
    type: Optional[str]
    placement: Optional[str]
    attachment: Optional[TypeformFormAttachment]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TypeformFormOption(BaseModel):
    label: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Flow(BaseModel):
    id: str
    tenant: Tenant
    identifier: str
    seller: Optional[Seller]
    process: FlowProcess
    mapping: Dict[str, Any]
    form_id: str = Field(..., alias="formId")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AvalaraRequestLogCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: AvalaraRequestLogCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class AvalaraRequestLogCountableEdge(BaseModel):
    node: AvalaraRequestLog
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AvalaraRequestLog(BaseModel):
    created_at: datetime = Field(..., alias="createdAt")
    request_url: Optional[str] = Field(..., alias="requestUrl")
    request_data: Dict[str, Any] = Field(..., alias="requestData")
    response_data: Dict[str, Any] = Field(..., alias="responseData")
    error: Optional[str]
    id: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutEventCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: CheckoutEventCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class CheckoutEventCountableEdge(BaseModel):
    node: CheckoutEvent
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field


class CheckoutEvent(BaseModel):
    tenant: Tenant
    id: str
    created_at: datetime = Field(..., alias="createdAt")
    type: CheckoutEventType
    checkout_id: str = Field(..., alias="checkoutId")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PayoutCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PayoutCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PayoutCountableEdge(BaseModel):
    node: Payout
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VendorPayoutReport(BaseModel):
    included: Optional[VendorPayoutReportSubset]
    excluded: Optional[VendorPayoutReportSubset]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class VendorPayoutReportSubset(BaseModel):
    category: Optional[str]
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: Optional[OrderVendorSummaryType]
    report: List[OrderVendorReportType]
    title: Optional[str]

from pydantic import BaseModel, Field


class ColumnObjectType(BaseModel):
    display: str
    field_type: str = Field(..., alias="fieldType")
    name: str
    order: int

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FilterObjectType(BaseModel):
    display: str
    field_type: str = Field(..., alias="fieldType")
    name: str
    placeholder: str
    required: bool
    value: Optional[str]

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderVendorSummaryType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    vendors: Optional[int]
    adjustments: Optional[Decimal]
    penalties: Optional[Decimal]
    refunds: Optional[Decimal]
    fees: Optional[Decimal]

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderVendorReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    vendor_id: Optional[int] = Field(..., alias="vendorId")
    vendor: Optional[Vendor]
    vendor_payout: Optional[VendorPayout] = Field(..., alias="vendorPayout")
    adjustments: Optional[Decimal]
    penalties: Optional[Decimal]
    refunds: Optional[Decimal]
    fees: Optional[Decimal]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class SingleVendorPayoutReport(BaseModel):
    payouts: List[SingleVendorReportType]
    summary: Optional[SingleVendorSummaryType]

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SingleVendorReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[Decimal]
    adjustments: Optional[Decimal]
    penalties: Optional[Decimal]
    refunds: Optional[Decimal]
    fees: Optional[Decimal]
    start_date: Optional[str] = Field(..., alias="startDate")
    end_date: Optional[str] = Field(..., alias="endDate")
    payout_end_date: Optional[str] = Field(..., alias="payoutEndDate")
    status: Optional[str]
    vendor_payout: Optional[VendorPayout] = Field(..., alias="vendorPayout")

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SingleVendorSummaryType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    adjustments: Optional[Decimal]
    penalties: Optional[Decimal]
    refunds: Optional[Decimal]
    fees: Optional[Decimal]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PaymentCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PaymentCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PaymentCountableEdge(BaseModel):
    node: Payment
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Page(BaseModel):
    id: str
    publication_date: Optional[date] = Field(..., alias="publicationDate")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    content: str
    content_html: str = Field(..., alias="contentHtml")
    seo_title: Optional[str] = Field(..., alias="seoTitle")
    seo_description: Optional[str] = Field(..., alias="seoDescription")
    slug: str
    title: str
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    is_published: bool = Field(..., alias="isPublished")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PageCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: PageCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class PageCountableEdge(BaseModel):
    node: Page
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderEventCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: OrderEventCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class OrderEventCountableEdge(BaseModel):
    node: OrderEvent
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderEventCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: NauticalOrderEventCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class NauticalOrderEventCountableEdge(BaseModel):
    node: NauticalOrderEvent
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FulfillmentCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: FulfillmentCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class FulfillmentCountableEdge(BaseModel):
    node: Fulfillment
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OptimizedHome(BaseModel):
    sales: Optional[TaxedMoney]
    orders: Optional[int]
    to_fulfill: Optional[int] = Field(..., alias="toFulfill")
    to_capture: Optional[int] = Field(..., alias="toCapture")
    out_of_stock: Optional[int] = Field(..., alias="outOfStock")
    top_products: ProductVariant = Field(..., alias="topProducts")
    seller_activities: OrderEvent = Field(..., alias="sellerActivities")
    marketplace_activities: NauticalOrderEvent = Field(..., alias="marketplaceActivities")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalConfiguration(BaseModel):
    configuration_name: Optional[str] = Field(..., alias="configurationName")
    configuration_value: Optional[bool] = Field(..., alias="configurationValue")
    configuration_value_datetime: Optional[datetime] = Field(..., alias="configurationValueDatetime")
    configuration_value_string: Optional[str] = Field(..., alias="configurationValueString")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MicrositeCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: MicrositeCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class MicrositeCountableEdge(BaseModel):
    node: Microsite
    cursor: str

from pydantic import BaseModel, Field


class Menu(BaseModel):
    id: str
    name: str
    slug: str
    items: MenuItem

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuItem(BaseModel):
    id: str
    menu: Menu
    name: str
    parent: Optional[MenuItem]
    category: Optional[Category]
    collection: Optional[Collection]
    page: Optional[Page]
    level: int
    children: MenuItem
    url: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: MenuCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class MenuCountableEdge(BaseModel):
    node: Menu
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuItemCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: MenuItemCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class MenuItemCountableEdge(BaseModel):
    node: MenuItem
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from uuid import UUID


class MarketplaceConfiguration(BaseModel):
    tenant: Tenant
    id: UUID
    marketplace_name: str = Field(..., alias="marketplaceName")
    require_product_approval: bool = Field(..., alias="requireProductApproval")
    require_product_types: bool = Field(..., alias="requireProductTypes")
    payout_automation_strategy: Optional[MarketplaceConfigurationPayoutAutomationStrategyEnum] = Field(..., alias="payoutAutomationStrategy")
    domiciled_currency: MarketplaceConfigurationCurrencyEnum = Field(..., alias="domiciledCurrency")
    supported_currencies: str = Field(..., alias="supportedCurrencies")
    default_country: str = Field(..., alias="defaultCountry")
    supported_countries: str = Field(..., alias="supportedCountries")
    seller_can_send_quote: bool = Field(..., alias="sellerCanSendQuote")
    variant_uniqueness: Optional[VariantUniquenessEnum] = Field(..., alias="variantUniqueness")
    default_seller_checklists: DefaultSellerChecklist = Field(..., alias="defaultSellerChecklists")
    enable_stock_allocation_for_quotes: bool = Field(..., alias="enableStockAllocationForQuotes")
    enable_stock_allocation_for_offers: Optional[bool] = Field(..., alias="enableStockAllocationForOffers")
    enable_stock_allocation_for_drafts: bool = Field(..., alias="enableStockAllocationForDrafts")
    validate_stock_on_order_payment_creation: bool = Field(..., alias="validateStockOnOrderPaymentCreation")
    timezone: str
    enable_backorders: bool = Field(..., alias="enableBackorders")
    revenue_accrual_strategy: Optional[RevenueAccrualStrategyEnum] = Field(..., alias="revenueAccrualStrategy")
    available_shipping_strategy: Optional[AvailableShippingStrategyEnum] = Field(..., alias="availableShippingStrategy")
    attribute_template_strategy: MarketplaceConfigurationAttributeTemplateStrategy = Field(..., alias="attributeTemplateStrategy")
    fulfillment_model: FulfillmentModelEnum = Field(..., alias="fulfillmentModel")
    default_weight_unit: Optional[WeightUnitsEnum] = Field(..., alias="defaultWeightUnit")
    automatic_fulfillment_digital_products: bool = Field(..., alias="automaticFulfillmentDigitalProducts")
    default_digital_max_downloads: Optional[int] = Field(..., alias="defaultDigitalMaxDownloads")
    default_digital_url_valid_days: Optional[int] = Field(..., alias="defaultDigitalUrlValidDays")
    track_inventory_by_default: bool = Field(..., alias="trackInventoryByDefault")
    description: str
    name: str
    company_address: Optional[Address] = Field(..., alias="companyAddress")
    default_mail_sender_name: Optional[str] = Field(..., alias="defaultMailSenderName")
    default_mail_sender_address: Optional[str] = Field(..., alias="defaultMailSenderAddress")
    default_mail_support_address: Optional[str] = Field(..., alias="defaultMailSupportAddress")
    customer_set_password_url: Optional[str] = Field(..., alias="customerSetPasswordUrl")
    include_taxes_in_prices: bool = Field(..., alias="includeTaxesInPrices")
    charge_taxes_on_shipping: bool = Field(..., alias="chargeTaxesOnShipping")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DefaultSellerChecklist(BaseModel):
    title: str
    description: str
    complete_on: Optional[SellerChecklistCompletionTriggersEnum] = Field(..., alias="completeOn")
    is_enabled: bool = Field(..., alias="isEnabled")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class EmailEventCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: EmailEventCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class EmailEventCountableEdge(BaseModel):
    node: EmailEvent
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class EmailEvent(BaseModel):
    id: str
    tenant: Tenant
    date: datetime
    from_email: str = Field(..., alias="fromEmail")
    to_emails: List[str] = Field(..., alias="toEmails")
    bcc_emails: List[str] = Field(..., alias="bccEmails")
    cc_emails: List[str] = Field(..., alias="ccEmails")
    message_type: EmailEventMessageType = Field(..., alias="messageType")
    email_plugin_id: str = Field(..., alias="emailPluginId")
    template: Optional[str]
    payload: Dict[str, Any]
    error: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class LocationSuggestion(BaseModel):
    label: str
    address: Optional[Address]

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Coordinates(BaseModel):
    label: Optional[str]
    latitude: Optional[Decimal]
    longitude: Optional[Decimal]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class InReportOrderCustomerSummaryType(BaseModel):
    category: str
    title: str
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: OrderSellerSummaryType
    report: List[OrderCustomerReportType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderSellerSummaryType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    sellers: Optional[float]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderCustomerReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    user_id: Optional[int] = Field(..., alias="userId")
    user: Optional[User]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class InReportOrderSellerSummaryType(BaseModel):
    category: str
    title: str
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: OrderSellerSummaryType
    report: List[OrderSellerReportType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderSellerReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    seller_id: Optional[int] = Field(..., alias="sellerId")
    seller: Optional[Seller]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class InReportOrderMarketplaceSummaryType(BaseModel):
    category: str
    title: str
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: OrderSellerSummaryType
    report: List[OrderMarketplaceReportType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderMarketplaceReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    dimension: Optional[date]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class InReportMarketplacePayoutsSummaryType(BaseModel):
    category: str
    title: str
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: OrderSellerSummaryType
    report: List[OrderSellerReportType]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class InReportMarketplaceTaxSummaryType(BaseModel):
    category: str
    title: str
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: AbstractOrderSellerReportType
    report: List[MarketplaceTaxReportType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AbstractOrderSellerReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MarketplaceTaxReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    dimension: Optional[date]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class InReportMarketplaceTaxesByCountryType(BaseModel):
    category: str
    title: str
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: AbstractOrderSellerReportType
    report: List[MarketplaceTaxReportByLocaleType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MarketplaceTaxReportByLocaleType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    billing_address__country: Optional[str] = Field(..., alias="billingAddress_Country")
    billing_address__country_area: Optional[str] = Field(..., alias="billingAddress_CountryArea")
    country_area: Optional[str] = Field(..., alias="countryArea")
    country: Optional[str]
    country_name: Optional[str] = Field(..., alias="countryName")
    country_area_name: Optional[str] = Field(..., alias="countryAreaName")
    country_state: Optional[CountryState] = Field(..., alias="countryState")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CountryState(BaseModel):
    area: Optional[str]
    area_name: Optional[str] = Field(..., alias="areaName")
    country: Optional[str]
    country_name: Optional[str] = Field(..., alias="countryName")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class InReportTopPerformingProductsType(BaseModel):
    category: str
    title: str
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: AbstractProductVariantType
    report: List[ProductVariantReportType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AbstractProductVariantType(BaseModel):
    totals: Optional[int]
    gross_revenue: Optional[float] = Field(..., alias="grossRevenue")
    quantity_ordered: Optional[int] = Field(..., alias="quantityOrdered")
    avg_price_gross_amount: Optional[float] = Field(..., alias="avgPriceGrossAmount")
    max_price_gross_amount: Optional[float] = Field(..., alias="maxPriceGrossAmount")
    min_price_gross_amount: Optional[float] = Field(..., alias="minPriceGrossAmount")
    revenue: Optional[float]
    avg_price: Optional[float] = Field(..., alias="avgPrice")
    max_price: Optional[float] = Field(..., alias="maxPrice")
    min_price: Optional[float] = Field(..., alias="minPrice")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantReportType(BaseModel):
    totals: Optional[int]
    gross_revenue: Optional[float] = Field(..., alias="grossRevenue")
    quantity_ordered: Optional[int] = Field(..., alias="quantityOrdered")
    avg_price_gross_amount: Optional[float] = Field(..., alias="avgPriceGrossAmount")
    max_price_gross_amount: Optional[float] = Field(..., alias="maxPriceGrossAmount")
    min_price_gross_amount: Optional[float] = Field(..., alias="minPriceGrossAmount")
    revenue: Optional[float]
    avg_price: Optional[float] = Field(..., alias="avgPrice")
    max_price: Optional[float] = Field(..., alias="maxPrice")
    min_price: Optional[float] = Field(..., alias="minPrice")
    product_id: int = Field(..., alias="productId")
    product: Product
    name: str
    id: str

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class InReportTopPerformingCategoriesType(BaseModel):
    category: str
    title: str
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: AbstractProductVariantType
    report: List[ProductCategoryReportType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductCategoryReportType(BaseModel):
    totals: Optional[int]
    gross_revenue: Optional[float] = Field(..., alias="grossRevenue")
    quantity_ordered: Optional[int] = Field(..., alias="quantityOrdered")
    avg_price_gross_amount: Optional[float] = Field(..., alias="avgPriceGrossAmount")
    max_price_gross_amount: Optional[float] = Field(..., alias="maxPriceGrossAmount")
    min_price_gross_amount: Optional[float] = Field(..., alias="minPriceGrossAmount")
    revenue: Optional[float]
    avg_price: Optional[float] = Field(..., alias="avgPrice")
    max_price: Optional[float] = Field(..., alias="maxPrice")
    min_price: Optional[float] = Field(..., alias="minPrice")
    product__category_id: Optional[int] = Field(..., alias="product_CategoryId")
    category: Optional[Category]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class InReportMarketplacePaymentsSummaryType(BaseModel):
    category: str
    title: str
    columns: List[ColumnObjectType]
    filters: List[FilterObjectType]
    summary: AbstractPaymentsType
    report: List[PaymentsDayReportType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AbstractPaymentsType(BaseModel):
    payments: Optional[int]
    total_authorized: Optional[float] = Field(..., alias="totalAuthorized")
    captured: Optional[float]
    average: Optional[float]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PaymentsDayReportType(BaseModel):
    payments: Optional[int]
    total_authorized: Optional[float] = Field(..., alias="totalAuthorized")
    captured: Optional[float]
    average: Optional[float]
    dimension: Optional[date]
    charge_status: Optional[str] = Field(..., alias="chargeStatus")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class DashboardOrdersSummaryType(BaseModel):
    filters: List[FilterObjectType]
    current: Optional[AbstractOrderSellerReportType]
    previous: Optional[AbstractOrderSellerReportType]
    deltas: Optional[OrderSummaryDeltaDataType]
    orders_to_fulfill: Optional[int] = Field(..., alias="ordersToFulfill")
    payments_to_process: Optional[int] = Field(..., alias="paymentsToProcess")
    returns_to_process: Optional[int] = Field(..., alias="returnsToProcess")
    pending_reviews: Optional[int] = Field(..., alias="pendingReviews")
    pending_payouts: Optional[int] = Field(..., alias="pendingPayouts")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderSummaryDeltaDataType(BaseModel):
    percent: Optional[AbstractPercentReportType]
    values: Optional[AbstractOrderSellerReportType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AbstractPercentReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[float]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[float]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class DashboardTopSellerPerformanceType(BaseModel):
    filters: List[FilterObjectType]
    current: List[DashboardSellerOrderPerformanceType]
    previous: List[DashboardSellerOrderPerformanceType]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DashboardSellerOrderPerformanceType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    seller_id: Optional[int] = Field(..., alias="sellerId")
    seller: Optional[Seller]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class DashboardGraphType(BaseModel):
    filters: List[FilterObjectType]
    graph: List[GraphDataType]

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class GraphDataType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volume_discounts: Optional[float] = Field(..., alias="volumeDiscounts")
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    dimension: Optional[datetime]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FontCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: FontCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class FontCountableEdge(BaseModel):
    node: Font
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class JournalEntryCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: JournalEntryCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class JournalEntryCountableEdge(BaseModel):
    node: JournalEntry
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class JournalEntry(BaseModel):
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    id: str
    description: str
    fulfillment_line: Optional[FulfillmentLine] = Field(..., alias="fulfillmentLine")
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    order: Optional[Order]
    order_line: Optional[OrderLine] = Field(..., alias="orderLine")
    payment: Optional[Payment]
    refund: Optional[Refund]
    refund_line: Optional[RefundLine] = Field(..., alias="refundLine")
    vendor_payout: Optional[VendorPayout] = Field(..., alias="vendorPayout")
    type: JournalEntryTypeEnum
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    ledger_entries: LedgerEntry = Field(..., alias="ledgerEntries")

from datetime import datetime, date
from pydantic import BaseModel, Field


class LedgerEntry(BaseModel):
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    id: str
    journal_entry: JournalEntry = Field(..., alias="journalEntry")
    ledger: Ledger
    ledger_version: int = Field(..., alias="ledgerVersion")
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    amount: Money
    ledger_balance: Money = Field(..., alias="ledgerBalance")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class Ledger(BaseModel):
    id: str
    account_type: LedgerAccountTypeEnum = Field(..., alias="accountType")
    balance: Money
    seller: Optional[Seller]
    type: LedgerTypeEnum
    version: int
    private_metadata: MetadataItem = Field(..., alias="privateMetadata")
    metadata: MetadataItem
    buyer: Optional[User]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class LedgerCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: LedgerCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class LedgerCountableEdge(BaseModel):
    node: Ledger
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SaleCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: SaleCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class SaleCountableEdge(BaseModel):
    node: Sale
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VoucherCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: VoucherCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class VoucherCountableEdge(BaseModel):
    node: Voucher
    cursor: str

from pydantic import BaseModel, Field


class DesignerDataType(BaseModel):
    tenant: Tenant
    id: str
    name: str
    json_content: Dict[str, Any] = Field(..., alias="jsonContent")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class ExportFile(BaseModel):
    id: str
    user: Optional[User]
    app: Optional[App]
    status: JobStatusEnum
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    message: Optional[str]
    url: Optional[str]
    events: List[ExportEvent]

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ExportEvent(BaseModel):
    id: str
    date: datetime
    type: ExportEventsEnum
    user: Optional[User]
    app: Optional[App]
    message: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ExportFileCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: ExportFileCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class ExportFileCountableEdge(BaseModel):
    node: ExportFile
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: CheckoutCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class CheckoutCountableEdge(BaseModel):
    node: Checkout
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutLineCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: CheckoutLineCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class CheckoutLineCountableEdge(BaseModel):
    node: CheckoutLine
    cursor: str

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomFieldTemplate(BaseModel):
    id: str
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    content_type: Optional[CustomFieldTemplateEnum] = Field(..., alias="contentType")
    custom_attributes: Attribute = Field(..., alias="customAttributes")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppInstallation(BaseModel):
    app_name: str = Field(..., alias="appName")
    manifest_url: str = Field(..., alias="manifestUrl")
    id: str
    status: JobStatusEnum
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    message: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: AppCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class AppCountableEdge(BaseModel):
    node: App
    cursor: str

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class AddressValidationData(BaseModel):
    country_code: Optional[str] = Field(..., alias="countryCode")
    country_name: Optional[str] = Field(..., alias="countryName")
    address_format: Optional[str] = Field(..., alias="addressFormat")
    address_latin_format: Optional[str] = Field(..., alias="addressLatinFormat")
    allowed_fields: List[str] = Field(..., alias="allowedFields")
    required_fields: List[str] = Field(..., alias="requiredFields")
    upper_fields: List[str] = Field(..., alias="upperFields")
    country_area_type: Optional[str] = Field(..., alias="countryAreaType")
    country_area_choices: List[ChoiceValue] = Field(..., alias="countryAreaChoices")
    city_type: Optional[str] = Field(..., alias="cityType")
    city_choices: List[ChoiceValue] = Field(..., alias="cityChoices")
    city_area_type: Optional[str] = Field(..., alias="cityAreaType")
    city_area_choices: List[ChoiceValue] = Field(..., alias="cityAreaChoices")
    postal_code_type: Optional[str] = Field(..., alias="postalCodeType")
    postal_code_matchers: List[str] = Field(..., alias="postalCodeMatchers")
    postal_code_examples: List[str] = Field(..., alias="postalCodeExamples")
    postal_code_prefix: Optional[str] = Field(..., alias="postalCodePrefix")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ChoiceValue(BaseModel):
    raw: Optional[str]
    verbose: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class GroupCountableConnection(BaseModel):
    page_info: PageInfo = Field(..., alias="pageInfo")
    edges: GroupCountableEdge
    total_count: Optional[int] = Field(..., alias="totalCount")

from pydantic import BaseModel, Field


class GroupCountableEdge(BaseModel):
    node: Group
    cursor: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class _Service(BaseModel):
    sdl: Optional[str]

from decimal import Decimal
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class Mutation(BaseModel):
    id: str
    input: PermissionGroupUpdateInput
    description: Optional[str]
    file: Upload
    related_object_id: str = Field(..., alias="relatedObjectId")
    document_id: str = Field(..., alias="documentId")
    ids: str
    target_ids: List[str] = Field(..., alias="targetIds")
    payout_id: str = Field(..., alias="payoutId")
    seller_id: Optional[str] = Field(..., alias="sellerId")
    gateway: str
    vendor_payout_id: str = Field(..., alias="vendorPayoutId")
    wishlist_id: Optional[str] = Field(..., alias="wishlistId")
    product_id: Optional[str] = Field(..., alias="productId")
    user_id: str = Field(..., alias="userId")
    variant_id: str = Field(..., alias="variantId")
    microsite_id: str = Field(..., alias="micrositeId")
    products: str
    moves: ReorderInput
    is_published: bool = Field(..., alias="isPublished")
    default_billing_address: Optional[AddressInput] = Field(..., alias="defaultBillingAddress")
    default_shipping_address: Optional[AddressInput] = Field(..., alias="defaultShippingAddress")
    seller: str
    user: str
    image: Upload
    banner: Upload
    address_id: str = Field(..., alias="addressId")
    type: AddressTypeEnum
    name: str
    shop_fetch_tax_rates: Optional[ShopFetchTaxRates] = Field(..., alias="shopFetchTaxRates")
    status: RefundStatusEnum
    line_items: RefundLineUpdateInput = Field(..., alias="lineItems")
    refund_id: Optional[str] = Field(..., alias="refundId")
    payments: RefundPaymentUpdateInput
    refund: str
    parent: Optional[str]
    collection_id: str = Field(..., alias="collectionId")
    variants: ProductVariantBulkCreateInput
    category: str
    is_available: bool = Field(..., alias="isAvailable")
    start_date: Optional[date] = Field(..., alias="startDate")
    images_ids: str = Field(..., alias="imagesIds")
    product_type_id: str = Field(..., alias="productTypeId")
    product: str
    stocks: StockInput
    warehouse_ids: List[str] = Field(..., alias="warehouseIds")
    image_id: str = Field(..., alias="imageId")
    transfer_image_ownership: Optional[bool] = Field(..., alias="transferImageOwnership")
    location_id: Optional[str] = Field(..., alias="locationId")
    amount: PositiveDecimal
    payment_id: Optional[str] = Field(..., alias="paymentId")
    payment_data: Optional[Dict[str, Any]] = Field(..., alias="paymentData")
    token: str
    currency: MarketplaceConfigurationCurrencyEnum
    order_id: str = Field(..., alias="orderId")
    nautical_order_id: str = Field(..., alias="nauticalOrderId")
    order: str
    voucher_code: Optional[str] = Field(..., alias="voucherCode")
    storefront_url: str = Field(..., alias="storefrontUrl")
    keys: str
    menu: str
    document_type: Optional[int] = Field(..., alias="documentType")
    number: Optional[str]
    refresh_url: str = Field(..., alias="refreshUrl")
    return_url: str = Field(..., alias="returnUrl")
    vendor_id: str = Field(..., alias="vendorId")
    vendor_type: Optional[str] = Field(..., alias="vendorType")
    plugin: str
    checkout_id: str = Field(..., alias="checkoutId")
    dashboard_embedding_token: Optional[DashboardEmbeddingToken] = Field(..., alias="dashboardEmbeddingToken")
    promo_code: str = Field(..., alias="promoCode")
    billing_address: AddressInput = Field(..., alias="billingAddress")
    microsite: Optional[str]
    po_number: str = Field(..., alias="poNumber")
    redirect_url: str = Field(..., alias="redirectUrl")
    user_override: Optional[str] = Field(..., alias="userOverride")
    volume_discount: Optional[float] = Field(..., alias="volumeDiscount")
    email: str
    note: str
    line_id: Optional[str] = Field(..., alias="lineId")
    lines: CheckoutLineInput
    shipping_address: AddressInput = Field(..., alias="shippingAddress")
    shipping_method_price_override_amount: Optional[PositiveDecimal] = Field(..., alias="shippingMethodPriceOverrideAmount")
    shipping_method_selection: str = Field(..., alias="shippingMethodSelection")
    seller_shipping_methods: List[SellerShippingMethodInput] = Field(..., alias="sellerShippingMethods")
    po_numbers: str = Field(..., alias="poNumbers")
    operations: AttributeAssignInput
    attribute_ids: str = Field(..., alias="attributeIds")
    template: CustomFieldTemplateEnum
    attribute_id: str = Field(..., alias="attributeId")
    custom: bool
    instance_id: str = Field(..., alias="instanceId")
    attribute: str
    values: str
    oauth_provider_source: OauthProviderSourceEnum = Field(..., alias="oauthProviderSource")
    oauth_provider_token: str = Field(..., alias="oauthProviderToken")
    password: str
    provider: Optional[SsoProviderType]
    access_code: str = Field(..., alias="accessCode")
    csrf_token: Optional[str] = Field(..., alias="csrfToken")
    refresh_token: Optional[str] = Field(..., alias="refreshToken")
    tokens_deactivate_all: Optional[DeactivateAllUserTokens] = Field(..., alias="tokensDeactivateAll")
    new_password: str = Field(..., alias="newPassword")
    old_password: str = Field(..., alias="oldPassword")
    new_email: str = Field(..., alias="newEmail")
    is_active: bool = Field(..., alias="isActive")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class EmailTemplateUpdate(BaseModel):
    email_template: Optional[EmailTemplate] = Field(..., alias="emailTemplate")
    notification_errors: NotificationError = Field(..., alias="notificationErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NotificationError(BaseModel):
    field: Optional[str]
    message: str
    code: NotificationErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TenantUpdate(BaseModel):
    tenant: Optional[Tenant]
    tenant_errors: TenantError = Field(..., alias="tenantErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TenantError(BaseModel):
    field: Optional[str]
    message: str
    code: TenantErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DocumentAdd(BaseModel):
    document: Optional[Document]
    instances: DocumentTargetInstance
    document_errors: DocumentError = Field(..., alias="documentErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DocumentError(BaseModel):
    field: Optional[str]
    message: str
    code: DocumentErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DocumentUpdate(BaseModel):
    document: Optional[Document]
    document_errors: DocumentError = Field(..., alias="documentErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DocumentAttach(BaseModel):
    document: Optional[Document]
    instances: DocumentTargetInstance
    document_errors: DocumentError = Field(..., alias="documentErrors")

from pydantic import BaseModel, Field


class DocumentRemove(BaseModel):
    instances: DocumentTargetInstance
    document_errors: DocumentError = Field(..., alias="documentErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class NauticalConfigurationUpdate(BaseModel):
    nautical_configuration_list: List[NauticalConfiguration] = Field(..., alias="nauticalConfigurationList")
    nautical_configuration_errors: NauticalConfigurationError = Field(..., alias="nauticalConfigurationErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalConfigurationError(BaseModel):
    field: Optional[str]
    message: str
    code: NauticalConfigurationErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MarketplaceConfigurationUpdate(BaseModel):
    marketplace_configuration: Optional[MarketplaceConfiguration] = Field(..., alias="marketplaceConfiguration")
    marketplace_configuration_errors: MarketplaceConfigurationError = Field(..., alias="marketplaceConfigurationErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MarketplaceConfigurationError(BaseModel):
    field: Optional[str]
    message: str
    code: MarketplaceConfigurationErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PayoutCreate(BaseModel):
    payout_errors: PayoutError = Field(..., alias="payoutErrors")
    payout: Optional[Payout]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PayoutError(BaseModel):
    field: Optional[str]
    message: str
    code: PayoutErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PayoutUpdate(BaseModel):
    payout: Optional[Payout]
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PayoutDelete(BaseModel):
    payout_errors: PayoutError = Field(..., alias="payoutErrors")
    payout: Optional[Payout]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PayoutStatusUpdate(BaseModel):
    payout: Optional[Payout]
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PayoutDatesUpdate(BaseModel):
    payout_errors: PayoutError = Field(..., alias="payoutErrors")
    payout: Optional[Payout]

from pydantic import BaseModel, Field


class PayoutBulkArchive(BaseModel):
    count: int
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VendorPayoutCreate(BaseModel):
    vendor_payout: Optional[VendorPayout] = Field(..., alias="vendorPayout")
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VendorPayoutStatusUpdate(BaseModel):
    vendor_payout: Optional[VendorPayout] = Field(..., alias="vendorPayout")
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field


class VendorPayoutsBulkInclude(BaseModel):
    count: int
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field


class VendorPayoutsBulkExclude(BaseModel):
    count: int
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field


class VendorPayoutsBulkProcess(BaseModel):
    count: int
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VendorPayoutNoteAdd(BaseModel):
    vendor_payout: Optional[VendorPayout] = Field(..., alias="vendorPayout")
    event: Optional[VendorPayoutEvent]
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VendorPayoutNoteUpdate(BaseModel):
    vendor_payout: Optional[VendorPayout] = Field(..., alias="vendorPayout")
    event: Optional[VendorPayoutEvent]
    payout_errors: PayoutError = Field(..., alias="payoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistCreate(BaseModel):
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")
    wishlist: Optional[Wishlist]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistError(BaseModel):
    field: Optional[str]
    message: str
    code: WishlistErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistCreateForBuyer(BaseModel):
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")
    wishlist: Optional[Wishlist]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistUpdate(BaseModel):
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")
    wishlist: Optional[Wishlist]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistDelete(BaseModel):
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")
    wishlist: Optional[Wishlist]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistSetDefault(BaseModel):
    wishlist: Optional[Wishlist]
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WishlistItemUpdate(BaseModel):
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")
    wishlist_item: Optional[WishlistItem] = Field(..., alias="wishlistItem")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class WishlistAddProduct(BaseModel):
    wishlist: List[WishlistItem]
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class WishlistRemoveProduct(BaseModel):
    wishlist: List[WishlistItem]
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class WishlistAddProductVariant(BaseModel):
    wishlist: List[WishlistItem]
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class WishlistRemoveProductVariant(BaseModel):
    wishlist: List[WishlistItem]
    wishlist_errors: WishlistError = Field(..., alias="wishlistErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MicrositeAddProducts(BaseModel):
    microsite: Optional[Microsite]
    microsite_errors: ProductError = Field(..., alias="micrositeErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class ProductError(BaseModel):
    field: Optional[str]
    message: str
    code: ProductErrorCode
    attributes: List[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MicrositeCreate(BaseModel):
    microsite_errors: ProductError = Field(..., alias="micrositeErrors")
    microsite: Optional[Microsite]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MicrositeDelete(BaseModel):
    microsite_errors: ProductError = Field(..., alias="micrositeErrors")
    microsite: Optional[Microsite]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MicrositeReorderProducts(BaseModel):
    microsite: Optional[Microsite]
    microsite_errors: ProductError = Field(..., alias="micrositeErrors")

from pydantic import BaseModel, Field


class MicrositeBulkDelete(BaseModel):
    count: int
    microsite_errors: ProductError = Field(..., alias="micrositeErrors")

from pydantic import BaseModel, Field


class MicrositeBulkPublish(BaseModel):
    count: int
    microsite_errors: ProductError = Field(..., alias="micrositeErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MicrositeRemoveProducts(BaseModel):
    microsite: Optional[Microsite]
    microsite_errors: ProductError = Field(..., alias="micrositeErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MicrositeUpdate(BaseModel):
    microsite_errors: ProductError = Field(..., alias="micrositeErrors")
    microsite: Optional[Microsite]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementCreate(BaseModel):
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")
    agreement: Optional[Agreement]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementError(BaseModel):
    field: Optional[str]
    message: str
    code: AgreementErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementDelete(BaseModel):
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")
    agreement: Optional[Agreement]

from pydantic import BaseModel, Field


class AgreementBulkDelete(BaseModel):
    count: int
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")

from pydantic import BaseModel, Field


class AgreementBulkPublish(BaseModel):
    count: int
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementUpdate(BaseModel):
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")
    agreement: Optional[Agreement]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementFeeCreate(BaseModel):
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")
    agreement_fees: Optional[AgreementFees] = Field(..., alias="agreementFees")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementFeeDelete(BaseModel):
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")
    agreement_fees: Optional[AgreementFees] = Field(..., alias="agreementFees")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementCommissionCreate(BaseModel):
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")
    agreement_commission: Optional[AgreementCommission] = Field(..., alias="agreementCommission")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AgreementCommissionDelete(BaseModel):
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")
    agreement_commission: Optional[AgreementCommission] = Field(..., alias="agreementCommission")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerAgreementAcknowledge(BaseModel):
    user: Optional[User]
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerAgreementDecline(BaseModel):
    user: Optional[User]
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerAgreementAssign(BaseModel):
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")
    seller_agreement: Optional[AgreementSellers] = Field(..., alias="sellerAgreement")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerAgreementDelete(BaseModel):
    agreement_errors: AgreementError = Field(..., alias="agreementErrors")
    agreement_sellers: Optional[AgreementSellers] = Field(..., alias="agreementSellers")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerWithOwnerCreate(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerError(BaseModel):
    field: Optional[str]
    message: str
    code: SellerErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerDataCreate(BaseModel):
    ok: Optional[bool]
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerUserMappingCreate(BaseModel):
    ok: Optional[bool]
    seller_user: Optional[SellerUserType] = Field(..., alias="sellerUser")
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerDataUpdate(BaseModel):
    ok: Optional[bool]
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerNoteCreate(BaseModel):
    ok: Optional[bool]
    note: Optional[str]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerLogoUpdate(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerLogoDelete(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerBannerUpdate(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerBannerDelete(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerAddressCreate(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")
    address: Optional[Address]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerAddressUpdate(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")
    address: Optional[Address]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerAddressDelete(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")
    address: Optional[Address]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerAddressSetDefault(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerOwnerDelete(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerShellCreate(BaseModel):
    ok: Optional[bool]
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerSettingsUpdate(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerOnboardingChecklistComplete(BaseModel):
    checklist: Optional[SellerOnboardingChecklist]
    checklist_errors: SellerOnboardingChecklistError = Field(..., alias="checklistErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerOnboardingChecklistError(BaseModel):
    field: Optional[str]
    message: str
    code: SellerOnboardingChecklistErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerApplicationUpdate(BaseModel):
    seller: Optional[Seller]
    seller_errors: SellerError = Field(..., alias="sellerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DesignerDataCreate(BaseModel):
    ok: Optional[bool]
    designerdata: Optional[DesignerDataType]
    designer_errors: MarketplaceConfigurationError = Field(..., alias="designerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DesignerDataUpdate(BaseModel):
    ok: Optional[bool]
    designerdata: Optional[DesignerDataType]
    designer_errors: MarketplaceConfigurationError = Field(..., alias="designerErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WebhookCreate(BaseModel):
    webhook_errors: WebhookError = Field(..., alias="webhookErrors")
    webhook: Optional[Webhook]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WebhookError(BaseModel):
    field: Optional[str]
    message: str
    code: WebhookErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WebhookDelete(BaseModel):
    webhook_errors: WebhookError = Field(..., alias="webhookErrors")
    webhook: Optional[Webhook]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WebhookUpdate(BaseModel):
    webhook_errors: WebhookError = Field(..., alias="webhookErrors")
    webhook: Optional[Webhook]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WarehouseCreate(BaseModel):
    warehouse_errors: WarehouseError = Field(..., alias="warehouseErrors")
    warehouse: Optional[Warehouse]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WarehouseError(BaseModel):
    field: Optional[str]
    message: str
    code: WarehouseErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WarehouseUpdate(BaseModel):
    warehouse_errors: WarehouseError = Field(..., alias="warehouseErrors")
    warehouse: Optional[Warehouse]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class WarehouseDelete(BaseModel):
    warehouse_errors: WarehouseError = Field(..., alias="warehouseErrors")
    warehouse: Optional[Warehouse]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentPageDataCreate(BaseModel):
    content_page_data: Optional[ContentPageData] = Field(..., alias="contentPageData")
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShopError(BaseModel):
    field: Optional[str]
    message: str
    code: ShopErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentPageDataUpdate(BaseModel):
    content_page_data: Optional[ContentPageData] = Field(..., alias="contentPageData")
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentCreate(BaseModel):
    content: Optional[Content]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentSave(BaseModel):
    content: Optional[Content]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentDiscard(BaseModel):
    content: Optional[Content]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentPublish(BaseModel):
    content: Optional[Content]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentDelete(BaseModel):
    shop_errors: ShopError = Field(..., alias="shopErrors")
    content: Optional[Content]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ContentDuplicate(BaseModel):
    content: Optional[Content]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MediaCreate(BaseModel):
    media: Optional[Media]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MediaUpdate(BaseModel):
    media: Optional[Media]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field


class MediaBulkDelete(BaseModel):
    count: int
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShopDomainUpdate(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShopSettingsUpdate(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShopFetchTaxRates(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShopAddressUpdate(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutThemeCreate(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutThemeUpdate(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomDomainCreate(BaseModel):
    domain: Optional[CustomDomain]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomDomainDelete(BaseModel):
    shop_errors: ShopError = Field(..., alias="shopErrors")
    domain: Optional[CustomDomain]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class StorefrontThemeCreate(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class StorefrontThemeUpdate(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerOnboardingSettingsCreate(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SellerOnboardingSettingsUpdate(BaseModel):
    shop: Optional[Shop]
    shop_errors: ShopError = Field(..., alias="shopErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShippingPriceCreate(BaseModel):
    shipping_zone: Optional[ShippingZone] = Field(..., alias="shippingZone")
    shipping_errors: ShippingError = Field(..., alias="shippingErrors")
    shipping_method: Optional[ShippingMethod] = Field(..., alias="shippingMethod")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class ShippingError(BaseModel):
    field: Optional[str]
    message: str
    code: ShippingErrorCode
    warehouses: List[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShippingPriceDelete(BaseModel):
    shipping_method: Optional[ShippingMethod] = Field(..., alias="shippingMethod")
    shipping_zone: Optional[ShippingZone] = Field(..., alias="shippingZone")
    shipping_errors: ShippingError = Field(..., alias="shippingErrors")

from pydantic import BaseModel, Field


class ShippingPriceBulkDelete(BaseModel):
    count: int
    shipping_errors: ShippingError = Field(..., alias="shippingErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShippingPriceUpdate(BaseModel):
    shipping_zone: Optional[ShippingZone] = Field(..., alias="shippingZone")
    shipping_errors: ShippingError = Field(..., alias="shippingErrors")
    shipping_method: Optional[ShippingMethod] = Field(..., alias="shippingMethod")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShippingZoneCreate(BaseModel):
    shipping_errors: ShippingError = Field(..., alias="shippingErrors")
    shipping_zone: Optional[ShippingZone] = Field(..., alias="shippingZone")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShippingZoneDelete(BaseModel):
    shipping_errors: ShippingError = Field(..., alias="shippingErrors")
    shipping_zone: Optional[ShippingZone] = Field(..., alias="shippingZone")

from pydantic import BaseModel, Field


class ShippingZoneBulkDelete(BaseModel):
    count: int
    shipping_errors: ShippingError = Field(..., alias="shippingErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ShippingZoneUpdate(BaseModel):
    shipping_errors: ShippingError = Field(..., alias="shippingErrors")
    shipping_zone: Optional[ShippingZone] = Field(..., alias="shippingZone")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundCreate(BaseModel):
    refund_errors: RefundError = Field(..., alias="refundErrors")
    refund: Optional[Refund]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundError(BaseModel):
    field: Optional[str]
    message: str
    code: RefundErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundUpdate(BaseModel):
    refund_errors: RefundError = Field(..., alias="refundErrors")
    refund: Optional[Refund]

from pydantic import BaseModel, Field


class RefundBulkDelete(BaseModel):
    count: int
    refund_errors: RefundError = Field(..., alias="refundErrors")

from pydantic import BaseModel, Field


class RefundsChangeStatus(BaseModel):
    count: int
    refund_errors: RefundError = Field(..., alias="refundErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundLinesAdd(BaseModel):
    refund: Optional[Refund]
    refund_errors: RefundError = Field(..., alias="refundErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundLinesUpdate(BaseModel):
    refund: Optional[Refund]
    refund_errors: RefundError = Field(..., alias="refundErrors")

from pydantic import BaseModel, Field


class RefundLineBulkDelete(BaseModel):
    count: int
    refund_errors: RefundError = Field(..., alias="refundErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundPaymentsAdd(BaseModel):
    refund: Optional[Refund]
    refund_errors: RefundError = Field(..., alias="refundErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefundPaymentsUpdate(BaseModel):
    refund: Optional[Refund]
    refund_errors: RefundError = Field(..., alias="refundErrors")

from pydantic import BaseModel, Field


class RefundPaymentsDelete(BaseModel):
    count: int
    refund_errors: RefundError = Field(..., alias="refundErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookCreate(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book: Optional[PriceBook] = Field(..., alias="priceBook")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookError(BaseModel):
    field: Optional[str]
    message: str
    code: PriceBookErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookUpdate(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book: Optional[PriceBook] = Field(..., alias="priceBook")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookDelete(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book: Optional[PriceBook] = Field(..., alias="priceBook")

from pydantic import BaseModel, Field


class PriceBookBulkDelete(BaseModel):
    count: int
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookVariantCreate(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book_variant: Optional[PriceBookVariant] = Field(..., alias="priceBookVariant")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookVariantUpdate(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book_variant: Optional[PriceBookVariant] = Field(..., alias="priceBookVariant")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookVariantDelete(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book_variant: Optional[PriceBookVariant] = Field(..., alias="priceBookVariant")

from pydantic import BaseModel, Field


class PriceBookVariantBulkDelete(BaseModel):
    count: int
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductCreate(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book_product: Optional[PriceBookProduct] = Field(..., alias="priceBookProduct")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductUpdate(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book_product: Optional[PriceBookProduct] = Field(..., alias="priceBookProduct")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductDelete(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book_product: Optional[PriceBookProduct] = Field(..., alias="priceBookProduct")

from pydantic import BaseModel, Field


class PriceBookProductBulkDelete(BaseModel):
    count: int
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductTypeCreate(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book_product_type: Optional[PriceBookProductType] = Field(..., alias="priceBookProductType")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductTypeUpdate(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book_product_type: Optional[PriceBookProductType] = Field(..., alias="priceBookProductType")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PriceBookProductTypeDelete(BaseModel):
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")
    price_book_product_type: Optional[PriceBookProductType] = Field(..., alias="priceBookProductType")

from pydantic import BaseModel, Field


class PriceBookProductTypeBulkDelete(BaseModel):
    count: int
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class UserAddToPriceBook(BaseModel):
    user: Optional[User]
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class UserRemoveFromPriceBook(BaseModel):
    user: Optional[User]
    price_book_errors: PriceBookError = Field(..., alias="priceBookErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CategoryCreate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    category: Optional[Category]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CategoryDelete(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    category: Optional[Category]

from pydantic import BaseModel, Field


class CategoryBulkDelete(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CategoryUpdate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    category: Optional[Category]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CollectionAddProducts(BaseModel):
    collection: Optional[Collection]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CollectionAddVariants(BaseModel):
    collection: Optional[Collection]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CollectionCreate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    collection: Optional[Collection]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CollectionDelete(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    collection: Optional[Collection]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CollectionReorderProducts(BaseModel):
    collection: Optional[Collection]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field


class CollectionBulkDelete(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field


class CollectionBulkPublish(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CollectionRemoveProducts(BaseModel):
    collection: Optional[Collection]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CollectionRemoveVariants(BaseModel):
    collection: Optional[Collection]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CollectionUpdate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    collection: Optional[Collection]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductCreate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    product: Optional[Product]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductDelete(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    product: Optional[Product]

from pydantic import BaseModel, Field


class ProductBulkDelete(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field


class ProductBulkPublish(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field


class ProductBulkCategoryUpdate(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductUpdate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    product: Optional[Product]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductSetAvailabilityForPurchase(BaseModel):
    product: Optional[Product]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductImageCreate(BaseModel):
    product: Optional[Product]
    image: Optional[ProductImage]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductReorderVariants(BaseModel):
    product: Optional[Product]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductImageDelete(BaseModel):
    product: Optional[Product]
    image: Optional[ProductImage]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field


class ProductImageBulkDelete(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class ProductImageReorder(BaseModel):
    product: Optional[Product]
    images: List[ProductImage]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductImageUpdate(BaseModel):
    product: Optional[Product]
    image: Optional[ProductImage]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductTypeCreate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    product_type: Optional[ProductType] = Field(..., alias="productType")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductTypeDelete(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    product_type: Optional[ProductType] = Field(..., alias="productType")

from pydantic import BaseModel, Field


class ProductTypeBulkDelete(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductTypeUpdate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    product_type: Optional[ProductType] = Field(..., alias="productType")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductTypeReorderAttributes(BaseModel):
    product_type: Optional[ProductType] = Field(..., alias="productType")
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DigitalContentCreate(BaseModel):
    variant: Optional[ProductVariant]
    content: Optional[DigitalContent]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DigitalContentDelete(BaseModel):
    variant: Optional[ProductVariant]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DigitalContentUpdate(BaseModel):
    variant: Optional[ProductVariant]
    content: Optional[DigitalContent]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DigitalContentUrlCreate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    digital_content_url: Optional[DigitalContentUrl] = Field(..., alias="digitalContentUrl")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantCreate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    product_variant: Optional[ProductVariant] = Field(..., alias="productVariant")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantDelete(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    product_variant: Optional[ProductVariant] = Field(..., alias="productVariant")

from pydantic import BaseModel, Field


class ProductVariantBulkCreate(BaseModel):
    count: int
    product_variants: ProductVariant = Field(..., alias="productVariants")
    bulk_product_errors: BulkProductError = Field(..., alias="bulkProductErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class BulkProductError(BaseModel):
    field: Optional[str]
    message: str
    code: ProductErrorCode
    attributes: List[str]
    index: Optional[int]
    warehouses: List[str]

from pydantic import BaseModel, Field


class ProductVariantBulkDelete(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantStocksCreate(BaseModel):
    product_variant: Optional[ProductVariant] = Field(..., alias="productVariant")
    bulk_stock_errors: BulkStockError = Field(..., alias="bulkStockErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class BulkStockError(BaseModel):
    field: Optional[str]
    message: str
    code: ProductErrorCode
    attributes: List[str]
    index: Optional[int]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantStocksDelete(BaseModel):
    product_variant: Optional[ProductVariant] = Field(..., alias="productVariant")
    stock_errors: StockError = Field(..., alias="stockErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class StockError(BaseModel):
    field: Optional[str]
    message: str
    code: StockErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantStocksUpdate(BaseModel):
    product_variant: Optional[ProductVariant] = Field(..., alias="productVariant")
    bulk_stock_errors: BulkStockError = Field(..., alias="bulkStockErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantUpdate(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    product_variant: Optional[ProductVariant] = Field(..., alias="productVariant")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantSetDefault(BaseModel):
    product: Optional[Product]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantImageAssign(BaseModel):
    product_variant: Optional[ProductVariant] = Field(..., alias="productVariant")
    image: Optional[ProductImage]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductVariantImageUnassign(BaseModel):
    product_variant: Optional[ProductVariant] = Field(..., alias="productVariant")
    image: Optional[ProductImage]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FeatureCreate(BaseModel):
    feature: Optional[Feature]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FeatureUpdate(BaseModel):
    feature: Optional[Feature]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FeatureDelete(BaseModel):
    product: Optional[Product]
    variant: Optional[ProductVariant]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductTypeFeatureCreate(BaseModel):
    product_type: Optional[ProductType] = Field(..., alias="productType")
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductTypeFeatureUpdate(BaseModel):
    product_type: Optional[ProductType] = Field(..., alias="productType")
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductTypeFeatureDelete(BaseModel):
    product_type: Optional[ProductType] = Field(..., alias="productType")
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductLocationCreate(BaseModel):
    product: Optional[Product]
    location: Optional[Location]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductLocationUpdate(BaseModel):
    product: Optional[Product]
    location: Optional[Location]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductLocationDelete(BaseModel):
    product: Optional[Product]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductSetLocationType(BaseModel):
    product: Optional[Product]
    location: Optional[Location]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PaymentCapture(BaseModel):
    payment: Optional[Payment]
    payment_errors: PaymentError = Field(..., alias="paymentErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PaymentError(BaseModel):
    field: Optional[str]
    message: str
    code: PaymentErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PaymentVoid(BaseModel):
    payment: Optional[Payment]
    payment_errors: PaymentError = Field(..., alias="paymentErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PageCreate(BaseModel):
    page_errors: PageError = Field(..., alias="pageErrors")
    page: Optional[Page]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PageError(BaseModel):
    field: Optional[str]
    message: str
    code: PageErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PageDelete(BaseModel):
    page_errors: PageError = Field(..., alias="pageErrors")
    page: Optional[Page]

from pydantic import BaseModel, Field


class PageBulkDelete(BaseModel):
    count: int
    page_errors: PageError = Field(..., alias="pageErrors")

from pydantic import BaseModel, Field


class PageBulkPublish(BaseModel):
    count: int
    page_errors: PageError = Field(..., alias="pageErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PageUpdate(BaseModel):
    page_errors: PageError = Field(..., alias="pageErrors")
    page: Optional[Page]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DraftOrderComplete(BaseModel):
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderError(BaseModel):
    field: Optional[str]
    message: str
    code: OrderErrorCode
    warehouse: Optional[str]
    order_line: Optional[str] = Field(..., alias="orderLine")
    variant: Optional[str]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class NauticalDraftOrderComplete(BaseModel):
    order: Optional[NauticalOrder]
    seller_orders: List[Order] = Field(..., alias="sellerOrders")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DraftOrderSetTransactionCurrency(BaseModel):
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalDraftOrderSetTransactionCurrency(BaseModel):
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DraftOrderCreate(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    order: Optional[Order]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalDraftOrderCreate(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalHistoricalOrderCreate(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DraftOrderDelete(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    order: Optional[Order]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalDraftOrderDelete(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")

from pydantic import BaseModel, Field


class DraftOrderBulkDelete(BaseModel):
    count: int
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field


class NauticalDraftOrderBulkDelete(BaseModel):
    count: int
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field


class DraftOrderLinesBulkDelete(BaseModel):
    count: int
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field


class NauticalDraftOrderLinesBulkDelete(BaseModel):
    count: int
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class DraftOrderLinesCreate(BaseModel):
    order: Optional[Order]
    order_lines: List[OrderLine] = Field(..., alias="orderLines")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class NauticalDraftOrderLinesCreate(BaseModel):
    order: Optional[NauticalOrder]
    order_lines: List[NauticalOrderLine] = Field(..., alias="orderLines")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DraftOrderLineDelete(BaseModel):
    order: Optional[Order]
    order_line: Optional[OrderLine] = Field(..., alias="orderLine")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalDraftOrderLineDelete(BaseModel):
    order: Optional[NauticalOrder]
    order_line: Optional[NauticalOrderLine] = Field(..., alias="orderLine")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DraftOrderLineUpdate(BaseModel):
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")
    order_line: Optional[OrderLine] = Field(..., alias="orderLine")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalDraftOrderLineUpdate(BaseModel):
    order: Optional[NauticalOrder]
    order_errors: OrderError = Field(..., alias="orderErrors")
    nautical_order_line: Optional[NauticalOrderLine] = Field(..., alias="nauticalOrderLine")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DraftOrderUpdate(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    order: Optional[Order]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalDraftOrderUpdate(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DraftOrderLinePriceOverride(BaseModel):
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")
    order_line: Optional[OrderLine] = Field(..., alias="orderLine")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalDraftOrderLinePriceOverride(BaseModel):
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    order_errors: OrderError = Field(..., alias="orderErrors")
    nautical_order_line: Optional[NauticalOrderLine] = Field(..., alias="nauticalOrderLine")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderAddNote(BaseModel):
    order: Optional[Order]
    event: Optional[OrderEvent]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderAddNote(BaseModel):
    order: Optional[NauticalOrder]
    event: Optional[NauticalOrderEvent]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderLineAddNote(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    order_line: Optional[OrderLine] = Field(..., alias="orderLine")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderLineAddNote(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    nautical_order_line: Optional[NauticalOrderLine] = Field(..., alias="nauticalOrderLine")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderReturnNotification(BaseModel):
    order: Optional[Order]
    event: Optional[OrderEvent]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderRefreshTaxes(BaseModel):
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderUpdateApplyVoucherCode(BaseModel):
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderUpdateDeleteDiscount(BaseModel):
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderReturnNotification(BaseModel):
    order: Optional[NauticalOrder]
    event: Optional[NauticalOrderEvent]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderReturnFromStorefrontNotification(BaseModel):
    order: Optional[NauticalOrder]
    event: Optional[NauticalOrderEvent]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class VendorOrderReturnFromStorefrontNotification(BaseModel):
    order: Optional[Order]
    event: List[OrderEvent]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderCancel(BaseModel):
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderCancel(BaseModel):
    order: Optional[NauticalOrder]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalQuoteOrderCancel(BaseModel):
    order: Optional[NauticalOrder]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderCapture(BaseModel):
    order: Optional[NauticalOrder]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class OrderFulfill(BaseModel):
    fulfillments: List[Fulfillment]
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class OrderDeclineFulfillment(BaseModel):
    fulfillments: List[Fulfillment]
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FulfillmentCancel(BaseModel):
    fulfillment: Optional[Fulfillment]
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FulfillmentReturn(BaseModel):
    fulfillment: Optional[Fulfillment]
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FulfillmentUpdateTracking(BaseModel):
    fulfillment: Optional[Fulfillment]
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FulfillmentReturnStatusBulkUpdate(BaseModel):
    fulfillment: Optional[Fulfillment]
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class FulfillmentBulkReturn(BaseModel):
    fulfillments: List[Fulfillment]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderMarkAsDelivered(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    order: Optional[Order]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderMarkAsPaid(BaseModel):
    order: Optional[NauticalOrder]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderUpdate(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    order: Optional[Order]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderUpdate(BaseModel):
    order_errors: OrderError = Field(..., alias="orderErrors")
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderPayoutStatusUpdate(BaseModel):
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderUpdateShipping(BaseModel):
    order: Optional[Order]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderUpdateShipping(BaseModel):
    order: Optional[NauticalOrder]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderUpdateMarketplaceShipping(BaseModel):
    order: Optional[NauticalOrder]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderVoid(BaseModel):
    order: Optional[NauticalOrder]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field


class OrderBulkCancel(BaseModel):
    count: int
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderLineBulkCancel(BaseModel):
    count: int
    order: Optional[NauticalOrder]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderPaymentCreate(BaseModel):
    order: Optional[NauticalOrder]
    payment: Optional[Payment]
    payment_errors: PaymentError = Field(..., alias="paymentErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalQuoteOrderSendToCustomer(BaseModel):
    order: Optional[NauticalOrder]
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderFeeCreate(BaseModel):
    order_fee: Optional[OrderFee] = Field(..., alias="orderFee")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderFeeDelete(BaseModel):
    order_fee: Optional[OrderFee] = Field(..., alias="orderFee")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class NauticalOrderLinesCsvUpload(BaseModel):
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    csv_file: Optional[ImportFile] = Field(..., alias="csvFile")
    successful_lines: Optional[int] = Field(..., alias="successfulLines")
    failed_lines: Optional[int] = Field(..., alias="failedLines")
    order_errors: OrderError = Field(..., alias="orderErrors")

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class ImportFile(BaseModel):
    id: str
    user: Optional[User]
    app: Optional[App]
    status: JobStatusEnum
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    message: Optional[str]
    url: Optional[str]
    events: List[ImportEvent]

from datetime import datetime, date
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ImportEvent(BaseModel):
    id: str
    date: datetime
    type: ImportEventsEnum
    user: Optional[User]
    app: Optional[App]
    message: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class OrderLinesCsvUpload(BaseModel):
    order: Optional[Order]
    csv_file: Optional[ImportFile] = Field(..., alias="csvFile")
    successful_lines: Optional[int] = Field(..., alias="successfulLines")
    failed_lines: Optional[int] = Field(..., alias="failedLines")
    order_errors: OrderError = Field(..., alias="orderErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MetadataDelete(BaseModel):
    metadata_errors: MetadataError = Field(..., alias="metadataErrors")
    item: Optional[ObjectWithMetadata]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MetadataError(BaseModel):
    field: Optional[str]
    message: str
    code: MetadataErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PrivateMetadataDelete(BaseModel):
    metadata_errors: MetadataError = Field(..., alias="metadataErrors")
    item: Optional[ObjectWithMetadata]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MetadataUpdate(BaseModel):
    metadata_errors: MetadataError = Field(..., alias="metadataErrors")
    item: Optional[ObjectWithMetadata]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PrivateMetadataUpdate(BaseModel):
    metadata_errors: MetadataError = Field(..., alias="metadataErrors")
    item: Optional[ObjectWithMetadata]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuCreate(BaseModel):
    menu_errors: MenuError = Field(..., alias="menuErrors")
    menu: Optional[Menu]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuError(BaseModel):
    field: Optional[str]
    message: str
    code: MenuErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuDelete(BaseModel):
    menu_errors: MenuError = Field(..., alias="menuErrors")
    menu: Optional[Menu]

from pydantic import BaseModel, Field


class MenuBulkDelete(BaseModel):
    count: int
    menu_errors: MenuError = Field(..., alias="menuErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuUpdate(BaseModel):
    menu_errors: MenuError = Field(..., alias="menuErrors")
    menu: Optional[Menu]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuItemCreate(BaseModel):
    menu_errors: MenuError = Field(..., alias="menuErrors")
    menu_item: Optional[MenuItem] = Field(..., alias="menuItem")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuItemDelete(BaseModel):
    menu_errors: MenuError = Field(..., alias="menuErrors")
    menu_item: Optional[MenuItem] = Field(..., alias="menuItem")

from pydantic import BaseModel, Field


class MenuItemBulkDelete(BaseModel):
    count: int
    menu_errors: MenuError = Field(..., alias="menuErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuItemUpdate(BaseModel):
    menu_errors: MenuError = Field(..., alias="menuErrors")
    menu_item: Optional[MenuItem] = Field(..., alias="menuItem")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class MenuItemMove(BaseModel):
    menu: Optional[Menu]
    menu_errors: MenuError = Field(..., alias="menuErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceRequest(BaseModel):
    order: Optional[Order]
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    refund: Optional[Refund]
    invoice_errors: InvoiceError = Field(..., alias="invoiceErrors")
    invoice: Optional[Invoice]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceError(BaseModel):
    field: Optional[str]
    message: str
    code: InvoiceErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceRequestDelete(BaseModel):
    invoice_errors: InvoiceError = Field(..., alias="invoiceErrors")
    invoice: Optional[Invoice]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceCreate(BaseModel):
    invoice_errors: InvoiceError = Field(..., alias="invoiceErrors")
    invoice: Optional[Invoice]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceDelete(BaseModel):
    invoice_errors: InvoiceError = Field(..., alias="invoiceErrors")
    invoice: Optional[Invoice]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceUpdate(BaseModel):
    invoice_errors: InvoiceError = Field(..., alias="invoiceErrors")
    invoice: Optional[Invoice]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceSendNotification(BaseModel):
    invoice_errors: InvoiceError = Field(..., alias="invoiceErrors")
    invoice: Optional[Invoice]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceRefresh(BaseModel):
    order: Optional[Order]
    nautical_order: Optional[NauticalOrder] = Field(..., alias="nauticalOrder")
    invoice_errors: InvoiceError = Field(..., alias="invoiceErrors")
    invoice: Optional[Invoice]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceFinalize(BaseModel):
    invoice_errors: InvoiceError = Field(..., alias="invoiceErrors")
    invoice: Optional[Invoice]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InvoiceCancel(BaseModel):
    invoice_errors: InvoiceError = Field(..., alias="invoiceErrors")
    invoice: Optional[Invoice]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PluginUpdate(BaseModel):
    plugin: Optional[Plugin]
    plugins_errors: PluginError = Field(..., alias="pluginsErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PluginError(BaseModel):
    field: Optional[str]
    message: str
    code: PluginErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CatalogImport(BaseModel):
    ok: Optional[bool]
    plugin: Optional[str]
    plugins_errors: PluginError = Field(..., alias="pluginsErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CatalogExport(BaseModel):
    ok: Optional[bool]
    plugin: Optional[str]
    plugins_errors: PluginError = Field(..., alias="pluginsErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomersExport(BaseModel):
    ok: Optional[bool]
    plugin: Optional[str]
    plugins_errors: PluginError = Field(..., alias="pluginsErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PluginFlowUpdate(BaseModel):
    flow: Optional[Flow]
    plugins_errors: PluginError = Field(..., alias="pluginsErrors")

from pydantic import BaseModel, Field


class PluginFlowDelete(BaseModel):
    plugins_errors: PluginError = Field(..., alias="pluginsErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VendorPayoutOnboardingLinkRequest(BaseModel):
    link: Optional[str]
    vendor: Optional[Vendor]
    plugins_errors: PluginError = Field(..., alias="pluginsErrors")

from pydantic import BaseModel, Field


class ExchangeRatesRefresh(BaseModel):
    plugins_errors: PluginError = Field(..., alias="pluginsErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutEventTriggered(BaseModel):
    checkout_event: Optional[CheckoutEvent] = Field(..., alias="checkoutEvent")
    plugins_errors: PluginError = Field(..., alias="pluginsErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class JournalEntryCorrect(BaseModel):
    financial_errors: FinancialError = Field(..., alias="financialErrors")
    journal_entry: Optional[JournalEntry] = Field(..., alias="journalEntry")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class FinancialError(BaseModel):
    field: Optional[str]
    message: str
    code: FinancialErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SaleCreate(BaseModel):
    discount_errors: DiscountError = Field(..., alias="discountErrors")
    sale: Optional[Sale]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DiscountError(BaseModel):
    field: Optional[str]
    message: str
    code: DiscountErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SaleDelete(BaseModel):
    discount_errors: DiscountError = Field(..., alias="discountErrors")
    sale: Optional[Sale]

from pydantic import BaseModel, Field


class SaleBulkDelete(BaseModel):
    count: int
    discount_errors: DiscountError = Field(..., alias="discountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SaleUpdate(BaseModel):
    discount_errors: DiscountError = Field(..., alias="discountErrors")
    sale: Optional[Sale]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SaleAddCatalogues(BaseModel):
    sale: Optional[Sale]
    discount_errors: DiscountError = Field(..., alias="discountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class SaleRemoveCatalogues(BaseModel):
    sale: Optional[Sale]
    discount_errors: DiscountError = Field(..., alias="discountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VoucherCreate(BaseModel):
    discount_errors: DiscountError = Field(..., alias="discountErrors")
    voucher: Optional[Voucher]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VoucherDelete(BaseModel):
    discount_errors: DiscountError = Field(..., alias="discountErrors")
    voucher: Optional[Voucher]

from pydantic import BaseModel, Field


class VoucherBulkDelete(BaseModel):
    count: int
    discount_errors: DiscountError = Field(..., alias="discountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VoucherUpdate(BaseModel):
    discount_errors: DiscountError = Field(..., alias="discountErrors")
    voucher: Optional[Voucher]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VoucherAddCatalogues(BaseModel):
    voucher: Optional[Voucher]
    discount_errors: DiscountError = Field(..., alias="discountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VoucherRemoveCatalogues(BaseModel):
    voucher: Optional[Voucher]
    discount_errors: DiscountError = Field(..., alias="discountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class DashboardEmbeddingToken(BaseModel):
    token: Optional[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductsExport(BaseModel):
    export_file: Optional[ExportFile] = Field(..., alias="exportFile")
    export_errors: ExportError = Field(..., alias="exportErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ExportError(BaseModel):
    field: Optional[str]
    message: str
    code: ExportErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ProductsImport(BaseModel):
    import_file: Optional[ImportFile] = Field(..., alias="importFile")
    import_errors: ImportError = Field(..., alias="importErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class ImportError(BaseModel):
    field: Optional[str]
    message: str
    code: ImportErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutAddPromoCode(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class CheckoutError(BaseModel):
    field: Optional[str]
    message: str
    code: CheckoutErrorCode
    variants: List[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutBillingAddressUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutComplete(BaseModel):
    order: Optional[NauticalOrder]
    confirmation_needed: bool = Field(..., alias="confirmationNeeded")
    confirmation_data: Optional[Dict[str, Any]] = Field(..., alias="confirmationData")
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutConvertToNauticalQuoteOrder(BaseModel):
    order: Optional[NauticalOrder]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutCreate(BaseModel):
    created: Optional[bool]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")
    checkout: Optional[Checkout]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutCustomerAttach(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutCustomerDetach(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutEmailUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutSetTransactionCurrency(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutNoteUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutLineDelete(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutLinesAdd(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutLinesUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutRemovePromoCode(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutPaymentCreate(BaseModel):
    checkout: Optional[Checkout]
    payment: Optional[Payment]
    payment_errors: PaymentError = Field(..., alias="paymentErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutShippingAddressUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutSellerShippingMethodsUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutMarketplaceShippingMethodUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutSellerShippingMethodsBulkUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutSellerShippingMethodsClear(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutDelete(BaseModel):
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")
    checkout: Optional[Checkout]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutAddPONumbers(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutRemovePONumbers(BaseModel):
    checkout: Optional[Checkout]
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CheckoutLineAddNote(BaseModel):
    checkout_errors: CheckoutError = Field(..., alias="checkoutErrors")
    checkout_line: Optional[CheckoutLine] = Field(..., alias="checkoutLine")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeCreate(BaseModel):
    attribute: Optional[Attribute]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeDelete(BaseModel):
    product_errors: ProductError = Field(..., alias="productErrors")
    attribute: Optional[Attribute]

from pydantic import BaseModel, Field


class AttributeBulkDelete(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeAssign(BaseModel):
    product_type: Optional[ProductType] = Field(..., alias="productType")
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeUnassign(BaseModel):
    product_type: Optional[ProductType] = Field(..., alias="productType")
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeUpdate(BaseModel):
    attribute: Optional[Attribute]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomAttributeAssign(BaseModel):
    custom_field_template: Optional[CustomFieldTemplate] = Field(..., alias="customFieldTemplate")
    attribute_errors: ProductError = Field(..., alias="attributeErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomAttributeUnassign(BaseModel):
    custom_field_template: Optional[CustomFieldTemplate] = Field(..., alias="customFieldTemplate")
    attribute_errors: ProductError = Field(..., alias="attributeErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class InstanceAttributeUnassign(BaseModel):
    instance: Optional[CustomFieldInstance]
    attribute_errors: AttributeError = Field(..., alias="attributeErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class AttributeError(BaseModel):
    field: Optional[str]
    message: str
    code: ProductErrorCode
    values: List[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeValueCreate(BaseModel):
    attribute: Optional[Attribute]
    product_errors: ProductError = Field(..., alias="productErrors")
    attribute_value: Optional[AttributeValue] = Field(..., alias="attributeValue")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeValueDelete(BaseModel):
    attribute: Optional[Attribute]
    product_errors: ProductError = Field(..., alias="productErrors")
    attribute_value: Optional[AttributeValue] = Field(..., alias="attributeValue")

from pydantic import BaseModel, Field


class AttributeValueBulkCreate(BaseModel):
    count: int
    attribute_values: AttributeValue = Field(..., alias="attributeValues")
    attribute_errors: AttributeError = Field(..., alias="attributeErrors")

from pydantic import BaseModel, Field


class AttributeValueBulkDelete(BaseModel):
    count: int
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeValueUpdate(BaseModel):
    attribute: Optional[Attribute]
    product_errors: ProductError = Field(..., alias="productErrors")
    attribute_value: Optional[AttributeValue] = Field(..., alias="attributeValue")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AttributeValuesReorder(BaseModel):
    attribute: Optional[Attribute]
    product_errors: ProductError = Field(..., alias="productErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppCreate(BaseModel):
    auth_token: Optional[str] = Field(..., alias="authToken")
    app_errors: AppError = Field(..., alias="appErrors")
    app: Optional[App]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class AppError(BaseModel):
    field: Optional[str]
    message: str
    code: AppErrorCode
    permissions: List[PermissionEnum]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppUpdate(BaseModel):
    app_errors: AppError = Field(..., alias="appErrors")
    app: Optional[App]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppDelete(BaseModel):
    app_errors: AppError = Field(..., alias="appErrors")
    app: Optional[App]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppTokenCreate(BaseModel):
    auth_token: Optional[str] = Field(..., alias="authToken")
    app_errors: AppError = Field(..., alias="appErrors")
    app_token: Optional[AppToken] = Field(..., alias="appToken")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppTokenDelete(BaseModel):
    app_errors: AppError = Field(..., alias="appErrors")
    app_token: Optional[AppToken] = Field(..., alias="appToken")

from pydantic import BaseModel, Field


class AppTokenVerify(BaseModel):
    valid: bool
    app_errors: AppError = Field(..., alias="appErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppInstall(BaseModel):
    app_errors: AppError = Field(..., alias="appErrors")
    app_installation: Optional[AppInstallation] = Field(..., alias="appInstallation")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppRetryInstall(BaseModel):
    app_errors: AppError = Field(..., alias="appErrors")
    app_installation: Optional[AppInstallation] = Field(..., alias="appInstallation")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppDeleteFailedInstallation(BaseModel):
    app_errors: AppError = Field(..., alias="appErrors")
    app_installation: Optional[AppInstallation] = Field(..., alias="appInstallation")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppFetchManifest(BaseModel):
    manifest: Optional[Manifest]
    app_errors: AppError = Field(..., alias="appErrors")

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class Manifest(BaseModel):
    identifier: str
    version: str
    name: str
    about: Optional[str]
    permissions: List[Permission]
    app_url: Optional[str] = Field(..., alias="appUrl")
    configuration_url: Optional[str] = Field(..., alias="configurationUrl")
    token_target_url: Optional[str] = Field(..., alias="tokenTargetUrl")
    data_privacy: Optional[str] = Field(..., alias="dataPrivacy")
    data_privacy_url: Optional[str] = Field(..., alias="dataPrivacyUrl")
    homepage_url: Optional[str] = Field(..., alias="homepageUrl")
    support_url: Optional[str] = Field(..., alias="supportUrl")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppActivate(BaseModel):
    app_errors: AppError = Field(..., alias="appErrors")
    app: Optional[App]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AppDeactivate(BaseModel):
    app_errors: AppError = Field(..., alias="appErrors")
    app: Optional[App]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CreateCustomerToken(BaseModel):
    nautical_token: Optional[str] = Field(..., alias="nauticalToken")
    refresh_token: Optional[str] = Field(..., alias="refreshToken")
    auth_errors: AuthError = Field(..., alias="authErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AuthError(BaseModel):
    field: Optional[str]
    message: str
    code: str

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CreateToken(BaseModel):
    token: Optional[str]
    refresh_token: Optional[str] = Field(..., alias="refreshToken")
    csrf_token: Optional[str] = Field(..., alias="csrfToken")
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AccountError(BaseModel):
    field: Optional[str]
    message: str
    code: AccountErrorCode

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AuthURLGenerate(BaseModel):
    auth_url: Optional[str] = Field(..., alias="authUrl")
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class TokenCreateSSO(BaseModel):
    token: Optional[str]
    refresh_token: Optional[str] = Field(..., alias="refreshToken")
    csrf_token: Optional[str] = Field(..., alias="csrfToken")
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class RefreshToken(BaseModel):
    token: Optional[str]
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class VerifyToken(BaseModel):
    user: Optional[User]
    is_valid: bool = Field(..., alias="isValid")
    payload: Optional[GenericScalar]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field


class DeactivateAllUserTokens(BaseModel):
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field


class PasswordRequestReset(BaseModel):
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AccountConfirm(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PasswordSet(BaseModel):
    token: Optional[str]
    refresh_token: Optional[str] = Field(..., alias="refreshToken")
    csrf_token: Optional[str] = Field(..., alias="csrfToken")
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PasswordChange(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class EmailChangeRequest(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class EmailChangeConfirm(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AccountAddressCreate(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")
    address: Optional[Address]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AccountAddressUpdate(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")
    address: Optional[Address]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AccountAddressDelete(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")
    address: Optional[Address]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AccountAddressSetDefault(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AccountRegister(BaseModel):
    requires_confirmation: Optional[bool] = Field(..., alias="requiresConfirmation")
    account_errors: AccountError = Field(..., alias="accountErrors")
    user: Optional[User]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AccountUpdate(BaseModel):
    account_errors: AccountError = Field(..., alias="accountErrors")
    user: Optional[User]

from pydantic import BaseModel, Field


class AccountRequestDeletion(BaseModel):
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AccountDelete(BaseModel):
    account_errors: AccountError = Field(..., alias="accountErrors")
    user: Optional[User]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AddressCreate(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")
    address: Optional[Address]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AddressUpdate(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")
    address: Optional[Address]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AddressDelete(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")
    address: Optional[Address]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class AddressSetDefault(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomerCreate(BaseModel):
    account_errors: AccountError = Field(..., alias="accountErrors")
    user: Optional[User]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomerUpdate(BaseModel):
    account_errors: AccountError = Field(..., alias="accountErrors")
    user: Optional[User]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class CustomerDelete(BaseModel):
    account_errors: AccountError = Field(..., alias="accountErrors")
    user: Optional[User]

from pydantic import BaseModel, Field


class CustomerBulkDelete(BaseModel):
    count: int
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class StaffCreate(BaseModel):
    staff_errors: StaffError = Field(..., alias="staffErrors")
    user: Optional[User]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class StaffError(BaseModel):
    field: Optional[str]
    message: str
    code: AccountErrorCode
    permissions: List[PermissionEnum]
    groups: List[str]
    users: List[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class StaffUpdate(BaseModel):
    staff_errors: StaffError = Field(..., alias="staffErrors")
    user: Optional[User]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class StaffDelete(BaseModel):
    staff_errors: StaffError = Field(..., alias="staffErrors")
    user: Optional[User]

from pydantic import BaseModel, Field


class StaffBulkDelete(BaseModel):
    count: int
    staff_errors: StaffError = Field(..., alias="staffErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class UserAvatarUpdate(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class UserAvatarDelete(BaseModel):
    user: Optional[User]
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field


class UserBulkSetActive(BaseModel):
    count: int
    account_errors: AccountError = Field(..., alias="accountErrors")

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PermissionGroupCreate(BaseModel):
    permission_group_errors: PermissionGroupError = Field(..., alias="permissionGroupErrors")
    group: Optional[Group]

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from typing import Optional, Dict, Any


class PermissionGroupError(BaseModel):
    field: Optional[str]
    message: str
    code: PermissionGroupErrorCode
    permissions: List[PermissionEnum]
    users: List[str]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PermissionGroupUpdate(BaseModel):
    permission_group_errors: PermissionGroupError = Field(..., alias="permissionGroupErrors")
    group: Optional[Group]

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PermissionGroupDelete(BaseModel):
    permission_group_errors: PermissionGroupError = Field(..., alias="permissionGroupErrors")
    group: Optional[Group]

