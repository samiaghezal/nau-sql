from datetime import datetime, date
from decimal import Decimal
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field



class RecipientTypeEnum(str):
    CUSTOMER = 'CUSTOMER'
    SELLER_PRIMARY_CONTACT = 'SELLER_PRIMARY_CONTACT'
    STAFF_MEMBER_MARKETPLACE = 'STAFF_MEMBER_MARKETPLACE'
    STAFF_MEMBER_SELLER = 'STAFF_MEMBER_SELLER'
    STAFF_MEMBER_MARKETPLACE_OR_SELLER = 'STAFF_MEMBER_MARKETPLACE_OR_SELLER'
    

class EventTypeEnum(str):
    ACCOUNT_CONFIRMATION = 'account_confirmation'
    ACCOUNT_PASSWORD_RESET = 'account_password_reset'
    ACCOUNT_CHANGE_EMAIL_REQUEST = 'account_change_email_request'
    ACCOUNT_CHANGE_EMAIL_CONFIRM = 'account_change_email_confirm'
    ACCOUNT_DELETE = 'account_delete'
    ACCOUNT_SET_CUSTOMER_PASSWORD = 'account_set_customer_password'
    INVOICE_READY = 'invoice_ready'
    ORDER_CONFIRMATION = 'order_confirmation'
    ORDER_FULFILLMENT_CONFIRMATION = 'order_fulfillment_confirmation'
    ORDER_FULFILLMENT_DENIED = 'order_fulfillment_denied'
    ORDER_FULFILLMENT_UPDATE = 'order_fulfillment_update'
    ORDER_CANCELED = 'order_canceled'
    PARTIAL_ORDER_CANCEL = 'partial_order_cancel'
    ORDER_REFUND_CONFIRMATION = 'order_refund_confirmation'
    PENDING_QUOTE = 'pending_quote'
    ACCOUNT_SET_STAFF_PASSWORD = 'account_set_staff_password'
    CSV_EXPORT_PRODUCTS_SUCCESS = 'csv_export_products_success'
    CSV_EXPORT_FAILED = 'csv_export_failed'
    STAFF_ORDER_CONFIRMATION = 'staff_order_confirmation'
    ACCOUNT_STAFF_RESET_PASSWORD = 'account_staff_reset_password'
    VENDOR_PAYOUT_CONFIRMATION = 'vendor_payout_confirmation'
    PENDING_SELLER = 'pending_seller'
    UPDATED_STATUS = 'updated_status'
    SELLER_STATUS_PENDING = 'seller_status_pending'
    SELLER_STATUS_APPROVED = 'seller_status_approved'
    SELLER_STATUS_DECLINED = 'seller_status_declined'
    SELLER_STATUS_PAUSED = 'seller_status_paused'
    SELLER_AGREEMENT_ACCEPTED = 'seller_agreement_accepted'
    SELLER_AGREEMENT_NOT_ACCEPTED = 'seller_agreement_not_accepted'
    IMPORT_CATALOG_FAILED = 'import_catalog_failed'
    IMPORT_CATALOG_SUCCESS = 'import_catalog_success'
    ACCOUNT_ACTIVATE_REQUEST = 'account_activate_request'
    ACCOUNT_ACTIVATED = 'account_activated'
    ACCOUNT_DEACTIVATED = 'account_deactivated'
    PENDING_ORDER = 'pending_order'
    PENDING_CUSTOMER = 'pending_customer'
    QUOTE_REQUESTED = 'quote_requested'
    

class OrderDirection(str):
    SPECIFIES_AN_ASCENDING_SORT_ORDER. = 'Specifies an ascending sort order.'
    ASC = 'ASC'
    SPECIFIES_A_DESCENDING_SORT_ORDER. = 'Specifies a descending sort order.'
    DESC = 'DESC'
    

class EmailTemplateSortField(str):
    SORT_EMAIL_TEMPLATE_BY_TITLE = 'Sort email template by title.'
    TITLE = 'TITLE'
    SORT_EMAIL_TEMPLATE_BY_SUBJECT = 'Sort email template by subject.'
    SUBJECT = 'SUBJECT'
    SORT_EMAIL_TEMPLATE_BY_RECIPIENT_TYPE = 'Sort email template by recipient type.'
    RECIPIENT_TYPE = 'RECIPIENT_TYPE'

class UserExternalPayoutSource(str):
    NAUTICAL_PAYMENTS_STRIPE_PATH = 'nautical.payments.stripe'
    NAUTICAL_PAYMENTS_STRIPE = 'NAUTICAL_PAYMENTS_STRIPE'
    NAUTICAL_PAYMENTS_PAYPAL_PATH = 'nautical.payments.paypal'
    NAUTICAL_PAYMENTS_PAYPAL = 'NAUTICAL_PAYMENTS_PAYPAL'
    NAUTICAL_PAYMENTS_TROLLEY_PATH = 'nautical.payments.trolley'
    NAUTICAL_PAYMENTS_TROLLEY = 'NAUTICAL_PAYMENTS_TROLLEY'

class WeightUnitsEnum(str):
    KG = 'KG'
    LB = 'LB'
    OZ = 'OZ'
    G = 'G'
    

class ShippingMethodTypeEnum(str):
    PRICE_BASED_SHIPPING = 'Price based shipping'
    PRICE = 'PRICE'
    WEIGHT_BASED_SHIPPING = 'Weight based shipping'
    WEIGHT = 'WEIGHT'
    

class ProductVariantStatus(str):
    DRAFT = 'Draft'
    DRAFT = 'DRAFT'
    ACTIVE = 'Active'
    ACTIVE = 'ACTIVE'
    

class ProductVariantSubStatus(str):
    IN_REVIEW = 'In review'
    IN_REVIEW = 'IN_REVIEW'
    DECLINED = 'Declined'
    DECLINED = 'DECLINED'
    APPROVED = 'Approved'
    APPROVED = 'APPROVED'
    

class SellerStatus(str):
    APPLYING = 'Applying'
    APPLYING = 'APPLYING'
    PENDING = 'Pending'
    PENDING = 'PENDING'
    APPROVED = 'Approved'
    APPROVED = 'APPROVED'
    DECLINED = 'Declined'
    DECLINED = 'DECLINED'
    PAUSED = 'Paused'
    PAUSED = 'PAUSED'
    SUSPENDED = 'Suspended'
    SUSPENDED = 'SUSPENDED'
    BANNED = 'Banned'
    BANNED = 'BANNED'
    DEACTIVATED = 'Deactivated'
    DEACTIVATED = 'DEACTIVATED'
    

class SellerExternalPayoutSource(str):
    NAUTICAL_PAYMENTS_STRIPE_DISPLAY = 'nautical.payments.stripe'
    NAUTICAL_PAYMENTS_STRIPE = 'NAUTICAL_PAYMENTS_STRIPE'
    NAUTICAL_PAYMENTS_PAYPAL_DISPLAY = 'nautical.payments.paypal'
    NAUTICAL_PAYMENTS_PAYPAL = 'NAUTICAL_PAYMENTS_PAYPAL'
    NAUTICAL_PAYMENTS_TROLLEY_DISPLAY = 'nautical.payments.trolley'
    NAUTICAL_PAYMENTS_TROLLEY = 'NAUTICAL_PAYMENTS_TROLLEY'
    

class SellerEventsEnum(str):
    THE_SELLER_WAS_CREATED = 'The seller was created'
    SELLER_CREATED = 'SELLER_CREATED'
    SELLER_STATUS_WAS_UPDATED = 'Seller status was updated'
    SELLER_STATUS_CHANGED = 'SELLER_STATUS_CHANGED'
    THE_SELLER_WAS_DELETED = 'The seller was deleted'
    SELLER_DELETED = 'SELLER_DELETED'
    A_NOTE_WAS_ADDED_TO_THE_SELLER = 'A note was added to the seller'
    SELLER_NOTE_ADDED = 'SELLER_NOTE_ADDED'
    

class SellerChecklistCompletionTriggersEnum(str):
    PAYOUT_ACCOUNT_CREATED = 'Payout Account Created'
    PAYOUT_ACCOUNT_CREATED = 'PAYOUT_ACCOUNT_CREATED'
    FIRST_WAREHOUSE_CREATED = 'First Warehouse Created'
    FIRST_WAREHOUSE_CREATED = 'FIRST_WAREHOUSE_CREATED'
    FIRST_PRODUCT_CREATED = 'First Product Created'
    FIRST_PRODUCT_CREATED = 'FIRST_PRODUCT_CREATED'
    FIRST_SHIPPING_ZONE_CREATED = 'First Shipping Zone Created'
    FIRST_SHIPPING_ZONE_CREATED = 'FIRST_SHIPPING_ZONE_CREATED'
    PAGE_SETUP_IN_STORE = 'Page Setup in Store'
    PAGE_SETUP_IN_STORE = 'PAGE_SETUP_IN_STORE'
    INVITE_STAFF = 'Invite Staff'
    INVITE_STAFF = 'INVITE_STAFF'
    

class SellerApplicationCheckpoint(str):
    WELCOME = 'Welcome'
    WELCOME = 'WELCOME'
    USER_INFO = 'User Info'
    USER_INFO = 'USER_INFO'
    BUSINESS_INFO = 'Business Info'
    BUSINESS_INFO = 'BUSINESS_INFO'
    BUSINESS_STATEMENTS = 'Business Statements'
    BUSINESS_STATEMENTS = 'BUSINESS_STATEMENTS'
    BUSINESS_STRUCTURE = 'Business Structure'
    BUSINESS_STRUCTURE = 'BUSINESS_STRUCTURE'
    TIN = 'Tin'
    TIN = 'TIN'
    ADDRESS = 'Address'
    ADDRESS = 'ADDRESS'
    BUSINESS_SELL = 'Business Sell'
    BUSINESS_SELL = 'BUSINESS_SELL'
    COMPLETE = 'Complete'
    COMPLETE = 'COMPLETE'
    

class PayoutStatus(str):
    DRAFT = 'Draft'
    DRAFT = 'DRAFT'
    PAID = 'Paid'
    PAID = 'PAID'
    ARCHIVED = 'Archived'
    ARCHIVED = 'ARCHIVED'
    LOCKED = 'Locked'
    LOCKED = 'LOCKED'
    ERROR = 'Error'
    ERROR = 'ERROR'
    

class VendorPayoutStatus(str):
    PAID = 'Paid'
    PAID = 'PAID'
    UNPAID = 'Unpaid'
    UNPAID = 'UNPAID'
    ERROR = 'Error'
    ERROR = 'ERROR'
    

class VendorPayoutEventsEnum(str):
    THE_VENDOR_PAYOUT_WAS_CREATED. = 'The vendor payout was created.'
    VENDOR_PAYOUT_CREATED = 'VENDOR_PAYOUT_CREATED'
    THE_VENDOR_PAYOUT_WAS_UPDATED. = 'The vendor payout was updated.'
    VENDOR_PAYOUT_UPDATED = 'VENDOR_PAYOUT_UPDATED'
    VENDOR_PAYOUT_STATUS_WAS_UPDATED. = 'Vendor payout status was updated.'
    VENDOR_PAYOUT_STATUS_UPDATED = 'VENDOR_PAYOUT_STATUS_UPDATED'
    A_NOTE_WAS_ADDED_TO_THE_VENDOR_PAYOUT = 'A note was added to the vendor payout'
    NOTE_ADDED = 'NOTE_ADDED'
    THE_VENDOR_PAYOUT_EMAIL_WAS_SENT. = 'The vendor payout email was sent.'
    VENDOR_PAYOUT_EMAIL_SENT = 'VENDOR_PAYOUT_EMAIL_SENT'
    

class OrderOrderSource(str):
    CHECKOUT = 'checkout'
    CHECKOUT = 'CHECKOUT'
    DRAFT = 'draft'
    DRAFT = 'DRAFT'
    QUOTE = 'quote'
    QUOTE = 'QUOTE'
    MANUAL = 'manual'
    MANUAL = 'MANUAL'
    EXTERNAL = 'external'
    EXTERNAL = 'EXTERNAL'
    

class OrderStatus(str):
    DRAFT = 'DRAFT'
    QUOTE = 'QUOTE'
    UNFULFILLED = 'UNFULFILLED'
    PARTIALLY_FULFILLED = 'PARTIALLY_FULFILLED'
    FULFILLED = 'FULFILLED'
    DELIVERED = 'DELIVERED'
    CANCELED = 'CANCELED'
    RETURN_REQUESTED = 'RETURN_REQUESTED'
    RETURN_AUTHORIZED = 'RETURN_AUTHORIZED'
    RETURN_DECLINED = 'RETURN_DECLINED'
    RETURN_CANCELLED = 'RETURN_CANCELLED'
    RETURN_COMPLETE = 'RETURN_COMPLETE'
    

class OrderSubStatus(str):
    IN_REVIEW = 'In Review'
    IN_REVIEW = 'IN_REVIEW'
    QUOTE_REQUESTED = 'Quote Requested'
    QUOTE_REQUESTED = 'QUOTE_REQUESTED'
    AWAITING_PAYMENT = 'Awaiting Payment'
    AWAITING_PAYMENT = 'AWAITING_PAYMENT'
    COMPLETE = 'Complete'
    COMPLETE = 'COMPLETE'
    

class VoucherTypeEnum(str):
    SHIPPING = 'SHIPPING'
    ENTIRE_ORDER = 'ENTIRE_ORDER'
    SPECIFIC_PRODUCT = 'SPECIFIC_PRODUCT'
    

class DiscountValueTypeEnum(str):
    FIXED = 'FIXED'
    PERCENTAGE = 'PERCENTAGE'
    

class AttributeFilterConnector(str):
    AND = 'AND'
    OR = 'OR'
    

class StockAvailability(str):
    IN_STOCK = 'IN_STOCK'
    OUT_OF_STOCK = 'OUT_OF_STOCK'
    

class ProductSubStatusEnum(str):
    IN_REVIEW = 'In review'
    IN_REVIEW = 'IN_REVIEW'
    DECLINED = 'Declined'
    DECLINED = 'DECLINED'
    APPROVED = 'Approved'
    APPROVED = 'APPROVED'
    

class FeatureFilterConnector(str):
    AND = 'AND'
    OR = 'OR'
    

class FeatureFilterOperationCondition(str):
    AND = 'AND'
    OR = 'OR'
    

class LocationTypeEnum(str):
    PRIMARY = 'Primary'
    PRIMARY = 'PRIMARY'
    ORIGIN = 'Origin'
    ORIGIN = 'ORIGIN'
    DESTINATION = 'Destination'
    DESTINATION = 'DESTINATION'
    

class DistanceUnit(str):
    KM = 'KM'
    MI = 'MI'
    

class ProductSearchFieldEnum(str):
    NAME = 'NAME'
    BRAND = 'BRAND'
    MANUFACTURER = 'MANUFACTURER'
    MPN = 'MPN'
    MODEL = 'MODEL'
    SELLER_NAME = 'SELLER_NAME'
    CATEGORY_NAME = 'CATEGORY_NAME'
    NSN = 'NSN'
    SKU = 'SKU'
    VARIANT_NAME = 'VARIANT_NAME'
    PRODUCT_ATTRIBUTE_NAME = 'PRODUCT_ATTRIBUTE_NAME'
    PRODUCT_ATTRIBUTE_VALUE_NAME = 'PRODUCT_ATTRIBUTE_VALUE_NAME'
    PRODUCT_ATTRIBUTE_VALUE_VALUE = 'PRODUCT_ATTRIBUTE_VALUE_VALUE'
    VARIANT_ATTRIBUTE_NAME = 'VARIANT_ATTRIBUTE_NAME'
    VARIANT_ATTRIBUTE_VALUE_NAME = 'VARIANT_ATTRIBUTE_VALUE_NAME'
    VARIANT_ATTRIBUTE_VALUE_VALUE = 'VARIANT_ATTRIBUTE_VALUE_VALUE'
    DESCRIPTION = 'DESCRIPTION'
    

class ProductOrderField(str):
    SORT_PRODUCTS_BY_NAME. = 'Sort products by name.'
    NAME = 'NAME'
    SORT_PRODUCTS_BY_SKU. = 'Sort products by sku.'
    SKU = 'SKU'
    SORT_PRODUCTS_BY_PRICE = 'Sort products by price.'
    PRICE = 'PRICE'
    SORT_PRODUCTS_BY_A_MINIMAL_PRICE_OF_A_PRODUCT_S_VARIANT = "Sort products by a minimal price of a product's variant."
    MINIMAL_PRICE = 'MINIMAL_PRICE'
    SORT_PRODUCTS_BY_UPDATE_DATE = 'Sort products by update date.'
    DATE = 'DATE'
    SORT_PRODUCTS_BY_CREATE_DATE. = 'Sort products by create date.'
    CREATED = 'CREATED'
    SORT_PRODUCTS_BY_TYPE. = 'Sort products by type.'
    TYPE = 'TYPE'
    SORT_PRODUCTS_BY_PUBLICATION_STATUS. = 'Sort products by publication status.'
    PUBLISHED = 'PUBLISHED'
    SORT_PRODUCTS_BY_PUBLICATION_DATE. = 'Sort products by publication date.'
    PUBLICATION_DATE = 'PUBLICATION_DATE'
    SORT_PRODUCTS_BY_SELLER. = 'Sort products by seller.'
    SELLER = 'SELLER'
    SORT_PRODUCTS_BY_CATEGORY. = 'Sort products by category.'
    CATEGORY = 'CATEGORY'
    SORT_PRODUCTS_BY_SUB_STATUS. = 'Sort products by sub status.'
    SUB_STATUS = 'SUB_STATUS'
    SORT_PRODUCTS_BY_SORT_PRIORITY_WEIGHT. = 'Sort products by sort priority weight.'
    SORT_PRIORITY_WEIGHT = 'SORT_PRIORITY_WEIGHT'
    SORT_PRODUCTS_BY_BRAND. = 'Sort products by brand.'
    BRAND = 'BRAND'
    SORT_PRODUCTS_BY_MANUFACTURER. = 'Sort products by manufacturer.'
    MANUFACTURER = 'MANUFACTURER'
    SORT_PRODUCTS_BY_EXTERNAL_ID. = 'Sort products by external id.'
    EXTERNAL_ID = 'EXTERNAL_ID'
    SORT_PRODUCTS_BY_EXTERNAL_SOURCE. = 'Sort products by external source.'
    EXTERNAL_SOURCE = 'EXTERNAL_SOURCE'
    

class FeatureTypeEnum(str):
    DROPDOWN = 'Dropdown'
    DROPDOWN = 'DROPDOWN'
    MULTI_SELECT = 'Multi Select'
    MULTISELECT = 'MULTISELECT'
    TEXT = 'Text'
    TEXT = 'TEXT'
    

class PermissionEnum(str):
    MANAGE_USERS = 'MANAGE_USERS'
    MANAGE_STAFF = 'MANAGE_STAFF'
    MANAGE_PERMISSIONS = 'MANAGE_PERMISSIONS'
    MANAGE_APPS = 'MANAGE_APPS'
    MANAGE_DISCOUNTS = 'MANAGE_DISCOUNTS'
    MANAGE_DOCUMENTS = 'MANAGE_DOCUMENTS'
    MANAGE_EMAILS = 'MANAGE_EMAILS'
    MANAGE_PLUGINS = 'MANAGE_PLUGINS'
    MANAGE_PRICEBOOKS = 'MANAGE_PRICEBOOKS'
    MANAGE_STOREFRONTS = 'MANAGE_STOREFRONTS'
    MANAGE_MENUS = 'MANAGE_MENUS'
    MANAGE_ORDERS = 'MANAGE_ORDERS'
    MANAGE_DRAFT_AND_QUOTE_ORDERS = 'MANAGE_DRAFT_AND_QUOTE_ORDERS'
    MANAGE_FULFILLMENTS = 'MANAGE_FULFILLMENTS'
    MANAGE_PAGES = 'MANAGE_PAGES'
    MANAGE_PRODUCTS = 'MANAGE_PRODUCTS'
    MANAGE_INVENTORY = 'MANAGE_INVENTORY'
    MANAGE_PRODUCT_TYPES_AND_ATTRIBUTES = 'MANAGE_PRODUCT_TYPES_AND_ATTRIBUTES'
    MANAGE_SHIPPING = 'MANAGE_SHIPPING'
    MANAGE_SETTINGS = 'MANAGE_SETTINGS'
    MANAGE_TRANSLATIONS = 'MANAGE_TRANSLATIONS'
    MANAGE_CHECKOUTS = 'MANAGE_CHECKOUTS'
    MANAGE_AGREEMENTS = 'MANAGE_AGREEMENTS'
    MANAGE_MARKETPLACE = 'MANAGE_MARKETPLACE'
    MANAGE_MARKETPLACE_CONFIGURATION = 'MANAGE_MARKETPLACE_CONFIGURATION'
    MANAGE_MICROSITES = 'MANAGE_MICROSITES'
    MANAGE_PAYOUTS = 'MANAGE_PAYOUTS'
    MANAGE_PAYMENTS = 'MANAGE_PAYMENTS'
    MANAGE_REFUNDS = 'MANAGE_REFUNDS'
    MANAGE_COLLECTIONS = 'MANAGE_COLLECTIONS'
    

class AppTypeEnum(str):
    LOCAL = 'local'
    LOCAL = 'LOCAL'
    THIRDPARTY = 'thirdparty'
    THIRDPARTY = 'THIRDPARTY'
    

class WebhookEventTypeEnum(str):
    ANY_EVENTS = 'ANY_EVENTS'
    AGREEMENT_CREATED = 'AGREEMENT_CREATED'
    AGREEMENT_DELETED = 'AGREEMENT_DELETED'
    AGREEMENT_UPDATED = 'AGREEMENT_UPDATED'
    CATEGORY_CREATED = 'CATEGORY_CREATED'
    CATEGORY_DELETED = 'CATEGORY_DELETED'
    CATEGORY_UPDATED = 'CATEGORY_UPDATED'
    CHECKOUT_CREATED = 'CHECKOUT_CREATED'
    CHECKOUT_UPDATED = 'CHECKOUT_UPDATED'
    COLLECTION_CREATED = 'COLLECTION_CREATED'
    COLLECTION_DELETED = 'COLLECTION_DELETED'
    COLLECTION_UPDATED = 'COLLECTION_UPDATED'
    CUSTOMER_CREATED = 'CUSTOMER_CREATED'
    CUSTOMER_UPDATED = 'CUSTOMER_UPDATED'
    CUSTOMER_DELETED = 'CUSTOMER_DELETED'
    FULFILLMENT_CREATED = 'FULFILLMENT_CREATED'
    INVOICE_DELETED = 'INVOICE_DELETED'
    INVOICE_REQUESTED = 'INVOICE_REQUESTED'
    INVOICE_SENT = 'INVOICE_SENT'
    MICROSITE_CREATED = 'MICROSITE_CREATED'
    MICROSITE_UPDATED = 'MICROSITE_UPDATED'
    NAUTICAL_ORDER_CANCELLED = 'NAUTICAL_ORDER_CANCELLED'
    NAUTICAL_ORDER_CREATED = 'NAUTICAL_ORDER_CREATED'
    NAUTICAL_ORDER_FULFILLED = 'NAUTICAL_ORDER_FULFILLED'
    NAUTICAL_ORDER_FULLY_PAID = 'NAUTICAL_ORDER_FULLY_PAID'
    NAUTICAL_ORDER_UPDATED = 'NAUTICAL_ORDER_UPDATED'
    ORDER_CANCELLED = 'ORDER_CANCELLED'
    ORDER_CREATED = 'ORDER_CREATED'
    ORDER_FULFILLED = 'ORDER_FULFILLED'
    ORDER_FULLY_PAID = 'ORDER_FULLY_PAID'
    ORDER_UPDATED = 'ORDER_UPDATED'
    PAYMENT_CREATED = 'PAYMENT_CREATED'
    PAYMENT_UPDATED = 'PAYMENT_UPDATED'
    PAYOUT_CREATED = 'PAYOUT_CREATED'
    PAYOUT_UPDATED = 'PAYOUT_UPDATED'
    PAYOUT_DELETED = 'PAYOUT_DELETED'
    PRICE_BOOK_CREATED = 'PRICE_BOOK_CREATED'
    PRICE_BOOK_UPDATED = 'PRICE_BOOK_UPDATED'
    PRODUCT_CREATED = 'PRODUCT_CREATED'
    PRODUCT_DELETED = 'PRODUCT_DELETED'
    PRODUCT_UPDATED = 'PRODUCT_UPDATED'
    REFUND_CREATED = 'REFUND_CREATED'
    REFUND_DELETED = 'REFUND_DELETED'
    REFUND_UPDATED = 'REFUND_UPDATED'
    SELLER_CREATED = 'SELLER_CREATED'
    SELLER_UPDATED = 'SELLER_UPDATED'
    SELLER_AGREEMENT_ACKNOWLEDGED = 'SELLER_AGREEMENT_ACKNOWLEDGED'
    SELLER_AGREEMENT_DECLINED = 'SELLER_AGREEMENT_DECLINED'
    VARIANT_CREATED = 'VARIANT_CREATED'
    VARIANT_DELETED = 'VARIANT_DELETED'
    VARIANT_UPDATED = 'VARIANT_UPDATED'
    STOCK_CREATED = 'STOCK_CREATED'
    STOCK_DELETED = 'STOCK_DELETED'
    STOCK_UPDATED = 'STOCK_UPDATED'
    STOCK_ALLOCATED = 'STOCK_ALLOCATED'
    STOCK_DEALLOCATED = 'STOCK_DEALLOCATED'
    VENDOR_PAYOUT_CREATED = 'VENDOR_PAYOUT_CREATED'
    VENDOR_PAYOUT_UPDATED = 'VENDOR_PAYOUT_UPDATED'
    WAREHOUSE_CREATED = 'WAREHOUSE_CREATED'
    WAREHOUSE_DELETED = 'WAREHOUSE_DELETED'
    WAREHOUSE_UPDATED = 'WAREHOUSE_UPDATED'
    

class AttributeInputTypeEnum(str):
    DROPDOWN = 'Dropdown'
    DROPDOWN = 'DROPDOWN'
    MULTI_SELECT = 'Multi Select'
    MULTISELECT = 'MULTISELECT'
    DATE = 'Date'
    DATE = 'DATE'
    DATE_TIME = 'Date Time'
    DATE_TIME = 'DATE_TIME'
    RICH_TEXT = 'Rich Text'
    RICH_TEXT = 'RICH_TEXT'
    PLAIN_TEXT = 'Plain Text'
    PLAIN_TEXT = 'PLAIN_TEXT'
    REFERENCE = 'Reference'
    REFERENCE = 'REFERENCE'
    MONEY = 'Money'
    MONEY = 'MONEY'
    BOOLEAN = 'Boolean'
    BOOLEAN = 'BOOLEAN'
    NUMERIC = 'Numeric'
    NUMERIC = 'NUMERIC'
    FILE = 'File'
    FILE = 'FILE'
    SWATCH = 'Swatch'
    SWATCH = 'SWATCH'
    

class AttributeValueType(str):
    COLOR = 'COLOR'
    GRADIENT = 'GRADIENT'
    URL = 'URL'
    STRING = 'STRING'
    

class ProductVariantSubStatusEnum(str):
    IN_REVIEW = 'In review'
    IN_REVIEW = 'IN_REVIEW'
    DECLINED = 'Declined'
    DECLINED = 'DECLINED'
    APPROVED = 'Approved'
    APPROVED = 'APPROVED'
    

class ProductVariantSearchFieldEnum(str):
    PRIMARY_KEY = 'PRIMARY_KEY'
    NAME = 'NAME'
    PRODUCT_NAME = 'PRODUCT_NAME'
    CATEGORY_NAME = 'CATEGORY_NAME'
    SKU = 'SKU'
    NSN = 'NSN'
    VARIANT_ATTRIBUTE_NAME = 'VARIANT_ATTRIBUTE_NAME'
    VARIANT_ATTRIBUTE_VALUE_NAME = 'VARIANT_ATTRIBUTE_VALUE_NAME'
    VARIANT_ATTRIBUTE_VALUE_VALUE = 'VARIANT_ATTRIBUTE_VALUE_VALUE'
    DESCRIPTION = 'DESCRIPTION'
    

class VariantSortField(str):
    NAME_DESC = 'Sort variants by name.'
    NAME = 'NAME'
    SKU_DESC = 'Sort variants by sku.'
    SKU = 'SKU'
    PRICE_DESC = 'Sort variants by price.'
    PRICE = 'PRICE'
    CREATED_DESC = 'Sort variants by create date.'
    CREATED = 'CREATED'
    UPDATED_DESC = 'Sort variants by update date.'
    UPDATED = 'UPDATED'
    TYPE_DESC = 'Sort variants by type.'
    TYPE = 'TYPE'
    SELLER_DESC = 'Sort variants by seller.'
    SELLER = 'SELLER'
    SUB_STATUS_DESC = 'Sort variants by sub status.'
    SUB_STATUS = 'SUB_STATUS'
    VARIANT_ID_DESC = 'Sort variants by variant id.'
    VARIANT_ID = 'VARIANT_ID'
    CATEGORY_DESC = 'Sort variants by category.'
    CATEGORY = 'CATEGORY'
    BRAND_DESC = 'Sort variants by brand.'
    BRAND = 'BRAND'
    MANUFACTURER_DESC = 'Sort variants by manufacturer.'
    MANUFACTURER = 'MANUFACTURER'
    EXTERNAL_ID_DESC = 'Sort variants by external id.'
    EXTERNAL_ID = 'EXTERNAL_ID'
    EXTERNAL_SOURCE_DESC = 'Sort variants by external source.'
    EXTERNAL_SOURCE = 'EXTERNAL_SOURCE'

class CollectionTypeEnum(str):
    PRODUCT = 'Product'
    PRODUCT = 'PRODUCT'
    VARIANT = 'Variant'
    VARIANT = 'VARIANT'
    

class SaleTypeEnum(str):
    SHIPPING = 'SHIPPING'
    SPECIFIC_PRODUCT = 'SPECIFIC_PRODUCT'
    

class NauticalOrderOrderSource(str):
    CHECKOUT = 'checkout'
    CHECKOUT = 'CHECKOUT'
    DRAFT = 'draft'
    DRAFT = 'DRAFT'
    QUOTE = 'quote'
    QUOTE = 'QUOTE'
    MANUAL = 'manual'
    MANUAL = 'MANUAL'
    EXTERNAL = 'external'
    EXTERNAL = 'EXTERNAL'
    

class NauticalOrderStatus(str):
    DRAFT = 'DRAFT'
    QUOTE = 'QUOTE'
    UNFULFILLED = 'UNFULFILLED'
    PARTIALLY_FULFILLED = 'PARTIALLY_FULFILLED'
    FULFILLED = 'FULFILLED'
    DELIVERED = 'DELIVERED'
    CANCELED = 'CANCELED'
    RETURN_REQUESTED = 'RETURN_REQUESTED'
    RETURN_AUTHORIZED = 'RETURN_AUTHORIZED'
    RETURN_DECLINED = 'RETURN_DECLINED'
    RETURN_CANCELLED = 'RETURN_CANCELLED'
    RETURN_COMPLETE = 'RETURN_COMPLETE'
    

class NauticalOrderSubStatus(str):
    IN_REVIEW = 'In Review'
    IN_REVIEW = 'IN_REVIEW'
    QUOTE_REQUESTED = 'Quote Requested'
    QUOTE_REQUESTED = 'QUOTE_REQUESTED'
    AWAITING_PAYMENT = 'Awaiting Payment'
    AWAITING_PAYMENT = 'AWAITING_PAYMENT'
    COMPLETE = 'Complete'
    COMPLETE = 'COMPLETE'
    

class OrderSubStatusEnum(str):
    IN_REVIEW = 'In Review'
    IN_REVIEW = 'IN_REVIEW'
    QUOTE_REQUESTED = 'Quote Requested'
    QUOTE_REQUESTED = 'QUOTE_REQUESTED'
    AWAITING_PAYMENT = 'Awaiting Payment'
    AWAITING_PAYMENT = 'AWAITING_PAYMENT'
    COMPLETE = 'Complete'
    COMPLETE = 'COMPLETE'
    

class PriceBookVariantValueType(str):
    OVERRIDE = 'Override'
    OVERRIDE = 'OVERRIDE'
    ADJUST_PERCENTAGE = 'Adjust Percentage'
    ADJUST_PERCENTAGE = 'ADJUST_PERCENTAGE'
    ADJUST_FIXED = 'Adjust Fixed'
    ADJUST_FIXED = 'ADJUST_FIXED'
    

class PriceBookProductValueType(str):
    ADJUST_PERCENTAGE = 'adjust_percentage'
    ADJUST_PERCENTAGE = 'ADJUST_PERCENTAGE'
    ADJUST_FIXED = 'adjust_fixed'
    ADJUST_FIXED = 'ADJUST_FIXED'
    

class PriceBookProductTypeValueType(str):
    ADJUST_PERCENTAGE = 'adjust_percentage'
    ADJUST_PERCENTAGE = 'ADJUST_PERCENTAGE'
    ADJUST_FIXED = 'adjust_fixed'
    ADJUST_FIXED = 'ADJUST_FIXED'
    

class OrderAction(str):
    REPRESENTS_THE_CAPTURE_ACTION. = 'Represents the capture action.'
    CAPTURE = 'CAPTURE'
    REPRESENTS_A_MARK-AS-PAID_ACTION. = 'Represents a mark-as-paid action.'
    MARK_AS_PAID = 'MARK_AS_PAID'
    REPRESENTS_A_REFUND_ACTION. = 'Represents a refund action.'
    REFUND = 'REFUND'
    REPRESENTS_A_VOID_ACTION. = 'Represents a void action.'
    VOID = 'VOID'
    

class JobStatusEnum(str):
    PENDING = 'Pending'
    PENDING = 'PENDING'
    PROCESSING = 'Processing'
    PROCESSING = 'PROCESSING'
    SUCCESS = 'Success'
    SUCCESS = 'SUCCESS'
    FAILED = 'Failed'
    FAILED = 'FAILED'
    DELETED = 'Deleted'
    DELETED = 'DELETED'
    

class PaymentChargeStatusEnum(str):
    NOT_CHARGED = 'NOT_CHARGED'
    PENDING = 'PENDING'
    PARTIALLY_CHARGED = 'PARTIALLY_CHARGED'
    FULLY_CHARGED = 'FULLY_CHARGED'
    PARTIALLY_REFUNDED = 'PARTIALLY_REFUNDED'
    FULLY_REFUNDED = 'FULLY_REFUNDED'
    REFUSED = 'REFUSED'
    CANCELLED = 'CANCELLED'
    VOIDED = 'VOIDED'
    

class TransactionKind(str):
    AUTHORIZATION = 'Authorization'
    AUTH = 'AUTH'
    CAPTURE = 'Capture'
    CAPTURE = 'CAPTURE'
    CAPTURE_FAILED = 'Capture failed'
    CAPTURE_FAILED = 'CAPTURE_FAILED'
    ACTION_TO_CONFIRM = 'Action to confirm'
    ACTION_TO_CONFIRM = 'ACTION_TO_CONFIRM'
    VOID = 'Void'
    VOID = 'VOID'
    PENDING = 'Pending'
    PENDING = 'PENDING'
    REFUND = 'Refund'
    REFUND = 'REFUND'
    REFUND_IN_PROGRESS = 'Refund in progress'
    REFUND_ONGOING = 'REFUND_ONGOING'
    REFUND_FAILED = 'Refund failed'
    REFUND_FAILED = 'REFUND_FAILED'
    REFUND_REVERSED = 'Refund reversed'
    REFUND_REVERSED = 'REFUND_REVERSED'
    CONFIRM = 'Confirm'
    CONFIRM = 'CONFIRM'
    CANCEL = 'Cancel'
    CANCEL = 'CANCEL'
    CREATED = 'Created'
    CREATED = 'CREATED'
    

class OrderEventsEnum(str):
    ORDER_WAS_CONFIRMED = 'Order was confirmed'
    CONFIRMED = 'CONFIRMED'
    THE_DRAFT_ORDER_WAS_CREATED = 'The draft order was created'
    DRAFT_CREATED = 'DRAFT_CREATED'
    THE_QUOTE_ORDER_WAS_CREATED = 'The quote order was created'
    QUOTE_CREATED = 'QUOTE_CREATED'
    THE_DRAFT_ORDER_WAS_UPDATED = 'The draft order was updated'
    DRAFT_UPDATED = 'DRAFT_UPDATED'
    THE_QUOTE_ORDER_WAS_UPDATED = 'The quote order was updated'
    QUOTE_UPDATED = 'QUOTE_UPDATED'
    SOME_PRODUCTS_WERE_ADDED_TO_THE_ORDER = 'Some products were added to the order'
    ADDED_PRODUCTS = 'ADDED_PRODUCTS'
    SOME_PRODUCTS_WERE_REMOVED_FROM_THE_ORDER = 'Some products were removed from the order'
    REMOVED_PRODUCTS = 'REMOVED_PRODUCTS'
    SOME_PRODUCTS_WERE_ADDED_TO_THE_DRAFT_ORDER = 'Some products were added to the draft order'
    DRAFT_ADDED_PRODUCTS = 'DRAFT_ADDED_PRODUCTS'
    SOME_PRODUCTS_WERE_REMOVED_FROM_THE_DRAFT_ORDER = 'Some products were removed from the draft order'
    DRAFT_REMOVED_PRODUCTS = 'DRAFT_REMOVED_PRODUCTS'
    SOME_PRODUCTS_WERE_ADDED_TO_THE_QUOTE_ORDER = 'Some products were added to the quote order'
    QUOTE_ADDED_PRODUCTS = 'QUOTE_ADDED_PRODUCTS'
    SOME_PRODUCTS_WERE_REMOVED_FROM_THE_QUOTE_ORDER = 'Some products were removed from the quote order'
    QUOTE_REMOVED_PRODUCTS = 'QUOTE_REMOVED_PRODUCTS'
    THE_ORDER_WAS_PLACED = 'The order was placed'
    PLACED = 'PLACED'
    THE_DRAFT_ORDER_WAS_PLACED = 'The draft order was placed'
    PLACED_FROM_DRAFT = 'PLACED_FROM_DRAFT'
    THE_QUOTE_ORDER_WAS_PLACED = 'The quote order was placed'
    PLACED_FROM_QUOTE = 'PLACED_FROM_QUOTE'
    THE_DRAFT_ORDER_WAS_PLACED_WITH_OVERSOLD_ITEMS = 'The draft order was placed with oversold items'
    OVERSOLD_ITEMS = 'OVERSOLD_ITEMS'
    THE_ORDER_WAS_CANCELED = 'The order was canceled'
    CANCELED = 'CANCELED'
    THE_ORDER_WAS_MANUALLY_MARKED_AS_FULLY_PAID = 'The order was manually marked as fully paid'
    ORDER_MARKED_AS_PAID = 'ORDER_MARKED_AS_PAID'
    THE_ORDER_WAS_MANUALLY_MARKED_AS_DELIVERED = 'The order was manually marked as delivered'
    ORDER_MARKED_AS_DELIVERED = 'ORDER_MARKED_AS_DELIVERED'
    THE_ORDER_WAS_FULLY_PAID = 'The order was fully paid'
    ORDER_FULLY_PAID = 'ORDER_FULLY_PAID'
    THE_ADDRESS_FROM_THE_PLACED_ORDER_WAS_UPDATED = 'The address from the placed order was updated'
    UPDATED_ADDRESS = 'UPDATED_ADDRESS'
    THE_EMAIL_WAS_SENT = 'The email was sent'
    EMAIL_SENT = 'EMAIL_SENT'
    THE_ORDER_PAYOUT_STATUS_WAS_MANUALLY_CHANGED = 'The order payout status was manually changed'
    PAYOUT_STATUS_MANUALLY_CHANGED = 'PAYOUT_STATUS_MANUALLY_CHANGED'
    THE_PAYMENT_WAS_AUTHORIZED = 'The payment was authorized'
    PAYMENT_AUTHORIZED = 'PAYMENT_AUTHORIZED'
    THE_PAYMENT_WAS_CAPTURED = 'The payment was captured'
    PAYMENT_CAPTURED = 'PAYMENT_CAPTURED'
    THE_PAYMENT_WAS_REFUNDED = 'The payment was refunded'
    PAYMENT_REFUNDED = 'PAYMENT_REFUNDED'
    THE_PAYMENT_WAS_VOIDED = 'The payment was voided'
    PAYMENT_VOIDED = 'PAYMENT_VOIDED'
    THE_PAYMENT_WAS_FAILED = 'The payment was failed'
    PAYMENT_FAILED = 'PAYMENT_FAILED'
    NOTIFICATION_FROM_EXTERNAL_SERVICE = 'Notification from external service'
    EXTERNAL_SERVICE_NOTIFICATION = 'EXTERNAL_SERVICE_NOTIFICATION'
    AN_INVOICE_WAS_REQUESTED = 'An invoice was requested'
    INVOICE_REQUESTED = 'INVOICE_REQUESTED'
    AN_INVOICE_WAS_GENERATED = 'An invoice was generated'
    INVOICE_GENERATED = 'INVOICE_GENERATED'
    AN_INVOICE_WAS_UPDATED = 'An invoice was updated'
    INVOICE_UPDATED = 'INVOICE_UPDATED'
    AN_INVOICE_WAS_SENT = 'An invoice was sent'
    INVOICE_SENT = 'INVOICE_SENT'
    A_FULFILLMENT_WAS_CANCELED = 'A fulfillment was canceled'
    FULFILLMENT_CANCELED = 'FULFILLMENT_CANCELED'
    THE_ITEMS_OF_THE_FULFILLMENT_WERE_RESTOCKED = 'The items of the fulfillment were restocked'
    FULFILLMENT_RESTOCKED_ITEMS = 'FULFILLMENT_RESTOCKED_ITEMS'
    SOME_ITEMS_WERE_FULFILLED = 'Some items were fulfilled'
    FULFILLMENT_FULFILLED_ITEMS = 'FULFILLMENT_FULFILLED_ITEMS'
    SOME_ITEMS_HAD_FULFILLMENT_DECLINED = 'Some items had fulfillment declined'
    FULFILLMENT_DECLINED_ITEMS = 'FULFILLMENT_DECLINED_ITEMS'
    THE_FULFILLMENT_TRACKING_CODE_WAS_UPDATED = 'The fulfillment tracking code was updated'
    TRACKING_CODE_UPDATED = 'TRACKING_CODE_UPDATED'
    TRACKING_UPDATED = 'TRACKING_UPDATED'
    A_NOTE_WAS_ADDED_TO_THE_ORDER = 'A note was added to the order'
    NOTE_ADDED = 'NOTE_ADDED'
    A_LINE_UNIT_PRICE_WAS_OVERRIDDEN = 'A line unit price was overridden'
    LINE_PRICE_OVERRIDDEN = 'LINE_PRICE_OVERRIDDEN'
    AN_UNKNOWN_ORDER_EVENT_CONTAINING_A_MESSAGE = 'An unknown order event containing a message'
    OTHER = 'OTHER'
    A_REFUND_RECEIPT_WAS_GENERATED = 'A refund receipt was generated'
    REFUND_RECEIPT_GENERATED = 'REFUND_RECEIPT_GENERATED'
    A_RETURN_WAS_REQUESTED_FOR_THE_ORDER = 'A return was requested for the order'
    RETURN_REQUESTED = 'RETURN_REQUESTED'
    A_RETURN_REQUEST_WAS_AUTHORIZED_FOR_THE_ORDER = 'A return request was authorized for the order'
    RETURN_AUTHORIZED = 'RETURN_AUTHORIZED'
    A_RETURN_REQUEST_WAS_DECLINED_FOR_THE_ORDER = 'A return request was declined for the order'
    RETURN_DECLINED = 'RETURN_DECLINED'
    A_RETURN_REQUEST_WAS_RECEIVED_FOR_THE_ORDER = 'A return request was received for the order'
    RETURN_RECEIVED = 'RETURN_RECEIVED'
    A_RETURN_REQUEST_WAS_CANCELLED_FOR_THE_ORDER = 'A return request was cancelled for the order'
    RETURN_CANCELLED = 'RETURN_CANCELLED'
    A_RETURN_HAS_BEEN_COMPLETED_FOR_THE_ORDER = 'A return has been completed for the order'
    RETURN_COMPLETE = 'RETURN_COMPLETE'
    

class OrderEventsEmailsEnum(str):
    THE_ORDER_CONFIRMED_EMAIL_WAS_SENT = 'The order confirmed email was sent'
    CONFIRMED = 'CONFIRMED'
    THE_PAYMENT_CONFIRMATION_EMAIL_WAS_SENT = 'The payment confirmation email was sent'
    PAYMENT_CONFIRMATION = 'PAYMENT_CONFIRMATION'
    THE_SHIPPING_CONFIRMATION_EMAIL_WAS_SENT = 'The shipping confirmation email was sent'
    SHIPPING_CONFIRMATION = 'SHIPPING_CONFIRMATION'
    THE_FULFILLMENT_TRACKING_CODE_EMAIL_WAS_SENT = 'The fulfillment tracking code email was sent'
    TRACKING_UPDATED = 'TRACKING_UPDATED'
    THE_ORDER_PLACEMENT_CONFIRMATION_EMAIL_WAS_SENT = 'The order placement confirmation email was sent'
    ORDER_CONFIRMATION = 'ORDER_CONFIRMATION'
    THE_ORDER_CANCEL_CONFIRMATION_EMAIL_WAS_SENT = 'The order cancel confirmation email was sent'
    ORDER_CANCEL = 'ORDER_CANCEL'
    THE_ORDER_REFUND_CONFIRMATION_EMAIL_WAS_SENT = 'The order refund confirmation email was sent'
    ORDER_REFUND = 'ORDER_REFUND'
    THE_FULFILLMENT_CONFIRMATION_EMAIL_WAS_SENT = 'The fulfillment confirmation email was sent'
    FULFILLMENT_CONFIRMATION = 'FULFILLMENT_CONFIRMATION'
    FULFILLMENT_DENIED = 'fulfillment_denied'
    FULFILLMENT_DENIED = 'FULFILLMENT_DENIED'
    THE_EMAIL_CONTAINING_THE_DIGITAL_LINKS_WAS_SENT = 'The email containing the digital links was sent'
    DIGITAL_LINKS = 'DIGITAL_LINKS'
    THE_PARTIAL_ORDER_CANCEL_CONFIRMATION_EMAIL_WAS_SENT = 'The partial order cancel confirmation email was sent'
    PARTIAL_ORDER_CANCEL = 'PARTIAL_ORDER_CANCEL'
    THE_MARKETPLACE_OPERATOR_ORDER_NOTIFICATION_EMAIL_WAS_SENT = 'The marketplace operator order notification email was sent'
    MPO_ORDER_NOTIFICATION = 'MPO_ORDER_NOTIFICATION'
    THE_QUOTE_EMAIL_WAS_SENT = 'The quote email was sent'
    QUOTE_SENT = 'QUOTE_SENT'
    THE_QUOTE_REQUEST_EMAIL_WAS_SENT_TO_THE_MARKETPLACE_OPERATOR = 'The quote request email was sent to the marketplace operator'
    QUOTE_REQUESTED = 'QUOTE_REQUESTED'
    

class RefundChargeToEnum(str):
    MARKETPLACE = 'Marketplace'
    MARKETPLACE = 'MARKETPLACE'
    SELLER = 'Seller'
    SELLER = 'SELLER'
    

class RefundLineScopeEnum(str):
    BUYER_ORDER = 'Buyer Order'
    BUYERORDER = 'BUYERORDER'
    ORDER_LINE = 'Order Line'
    ORDERLINE = 'ORDERLINE'
    SELLER_ORDER = 'Seller Order'
    SELLERORDER = 'SELLERORDER'
    

class RefundLineTypeEnum(str):
    ENTIRE_SCOPE = 'ENTIRE_SCOPE'
    FIXED_AMOUNT = 'FIXED_AMOUNT'
    PARTIAL_QUANTITY = 'PARTIAL_QUANTITY'
    PERCENTAGE = 'PERCENTAGE'
    SHIPPING = 'SHIPPING'
    TAX = 'TAX'
    

class RefundPaymentTypeEnum(str):
    TRANSACTION = 'Transaction'
    TRANSACTION = 'TRANSACTION'
    VOUCHER = 'Voucher'
    VOUCHER = 'VOUCHER'
    

class RefundStatusEnum(str):
    REQUESTED = 'Requested'
    REQUESTED = 'REQUESTED'
    CANCELED = 'Canceled'
    CANCELED = 'CANCELED'
    DECLINED = 'Declined'
    DECLINED = 'DECLINED'
    APPROVED = 'Approved'
    APPROVED = 'APPROVED'
    PROCESSING = 'Processing'
    PROCESSING = 'PROCESSING'
    FAILED = 'Failed'
    FAILED = 'FAILED'
    PAID = 'Paid'
    PAID = 'PAID'
    LOCKED = 'Locked'
    LOCKED = 'LOCKED'
    SETTLED = 'Settled'
    SETTLED = 'SETTLED'
    

class RefundTypeEnum(str):
    MANUAL_REFUND = 'Manual Refund'
    MANUALREFUND = 'MANUALREFUND'
    ORDER_LINE_REFUND = 'Order Line Refund'
    ORDERLINEREFUND = 'ORDERLINEREFUND'
    

class FulfillmentStatus(str):
    FULFILLED = 'Fulfilled'
    FULFILLED = 'FULFILLED'
    CANCELED = 'Canceled'
    CANCELED = 'CANCELED'
    RETURNED = 'Returned'
    RETURNED = 'RETURNED'
    DECLINED = 'Declined'
    DECLINED = 'DECLINED'
    RETURN_REQUESTED = 'Return requested'
    RETURN_REQUESTED = 'RETURN_REQUESTED'
    RETURN_AUTHORIZED = 'Return authorized'
    RETURN_AUTHORIZED = 'RETURN_AUTHORIZED'
    RETURN_DECLINED = 'Return declined'
    RETURN_DECLINED = 'RETURN_DECLINED'
    RETURN_RECEIVED = 'Return received'
    RETURN_RECEIVED = 'RETURN_RECEIVED'
    RETURN_COMPLETE = 'Return complete'
    RETURN_COMPLETE = 'RETURN_COMPLETE'
    RETURN_CANCELLED = 'Return cancelled'
    RETURN_CANCELLED = 'RETURN_CANCELLED'
    

class SourceFeeEnum(str):
    AGREEMENT_FEES = 'Agreement Fees'
    AGREEMENT_FEES = 'AGREEMENT_FEES'
    MANUAL_ORDER_FEE = 'Manual Order Fee'
    MANUAL_ORDER_FEE = 'MANUAL_ORDER_FEE'
    

class OrderPayoutStatusEnum(str):
    NOT_READY = 'Not ready'
    NOT_READY = 'NOT_READY'
    NOT_PAID = 'Not paid'
    NOT_PAID = 'NOT_PAID'
    READY_FOR_PAYOUT = 'Ready for payout'
    READY_FOR_PAYOUT = 'READY_FOR_PAYOUT'
    PENDING_FINAL_PAYOUT = 'Pending final payout'
    PENDING_FINAL_PAYOUT = 'PENDING_FINAL_PAYOUT'
    @DEPRECATED(REASON:_"THIS_WILL_BE_REMOVED_ON_FEBRUARY_26,_2025") = '@deprecated(reason: "This will be removed on February 26, 2025")'
    PAID_OUT = 'Paid out'
    PAID_OUT = 'PAID_OUT'
    PARTIALLY_PAID_OUT = 'Partially paid out'
    PARTIALLY_PAID_OUT = 'PARTIALLY_PAID_OUT'
    ERROR = 'Error'
    ERROR = 'ERROR'
    

class PayoutStatusEnum(str):
    DRAFT = 'Draft'
    DRAFT = 'DRAFT'
    PAID = 'Paid'
    PAID = 'PAID'
    ARCHIVED = 'Archived'
    ARCHIVED = 'ARCHIVED'
    LOCKED = 'Locked'
    LOCKED = 'LOCKED'
    ERROR = 'Error'
    ERROR = 'ERROR'
    

class CommissionTypeEnum(str):
    GROSS_PRICE_COMMISSION = 'Gross Price Commission'
    MARKETPLACE = 'MARKETPLACE'
    MARKUP_COMMISSION = 'Markup Commission'
    WHOLESALE = 'WHOLESALE'
    ABSOLUTE_PRICE_COMMISSION = 'Absolute Price Commission'
    DROPSHIPPING = 'DROPSHIPPING'
    

class MarkupCommissionTypeEnum(str):
    PERCENTAGE = 'Percentage'
    PERCENTAGE = 'PERCENTAGE'
    

class FeeType(str):
    PERCENTAGE = 'PERCENTAGE'
    FIXED = 'FIXED'
    

class FeeScope(str):
    LINE = 'LINE'
    TOTAL = 'TOTAL'
    

class ProductStatus(str):
    DRAFT = 'Draft'
    DRAFT = 'DRAFT'
    ACTIVE = 'Active'
    ACTIVE = 'ACTIVE'
    

class ProductSubStatus(str):
    IN_REVIEW = 'In review'
    IN_REVIEW = 'IN_REVIEW'
    DECLINED = 'Declined'
    DECLINED = 'DECLINED'
    APPROVED = 'Approved'
    APPROVED = 'APPROVED'
    

class LocationKindEnum(str):
    BUSINESS = 'Business'
    BUSINESS = 'BUSINESS'
    RESIDENTIAL = 'Residential'
    RESIDENTIAL = 'RESIDENTIAL'
    AUCTION = 'Auction'
    AUCTION = 'AUCTION'
    

class ProductAction(str):
    REPRESENTS_A_PRODUCT_THAT_WAS_DECLINED_MASTER_PRODUCT_STATUS. = 'Represents a product that was declined master product status.'
    DECLINED = 'DECLINED'
    REPRESENTS_A_PRODUCT_THAT_WAS_APPROVED_FOR_MASTER_PRODUCT_STATUS. = 'Represents a product that was approved for master product status.'
    APPROVED = 'APPROVED'
    

class DistanceUnitsEnum(str):
    INCH = 'Inch'
    INCH = 'INCH'
    FOOT = 'Foot'
    FT = 'FT'
    YARD = 'Yard'
    YD = 'YD'
    MILE = 'Mile'
    ML = 'ML'
    MILLIMETER = 'Millimeter'
    MM = 'MM'
    CENTIMETER = 'Centimeter'
    CM = 'CM'
    METER = 'Meter'
    M = 'M'
    KILOMETER = 'Kilometer'
    KM = 'KM'
    

class CountryCode(str):
    AF = 'AF'
    AX = 'AX'
    AL = 'AL'
    DZ = 'DZ'
    AS = 'AS'
    AD = 'AD'
    AO = 'AO'
    AI = 'AI'
    AQ = 'AQ'
    AG = 'AG'
    AR = 'AR'
    AM = 'AM'
    AW = 'AW'
    AU = 'AU'
    AT = 'AT'
    AZ = 'AZ'
    BS = 'BS'
    BH = 'BH'
    BD = 'BD'
    BB = 'BB'
    BY = 'BY'
    BE = 'BE'
    BZ = 'BZ'
    BJ = 'BJ'
    BM = 'BM'
    BT = 'BT'
    BO = 'BO'
    BQ = 'BQ'
    BA = 'BA'
    BW = 'BW'
    BV = 'BV'
    BR = 'BR'
    IO = 'IO'
    BN = 'BN'
    BG = 'BG'
    BF = 'BF'
    BI = 'BI'
    CV = 'CV'
    KH = 'KH'
    CM = 'CM'
    CA = 'CA'
    KY = 'KY'
    CF = 'CF'
    TD = 'TD'
    CL = 'CL'
    CN = 'CN'
    CX = 'CX'
    CC = 'CC'
    CO = 'CO'
    KM = 'KM'
    CG = 'CG'
    CD = 'CD'
    CK = 'CK'
    CR = 'CR'
    CI = 'CI'
    HR = 'HR'
    CU = 'CU'
    CW = 'CW'
    CY = 'CY'
    CZ = 'CZ'
    DK = 'DK'
    DJ = 'DJ'
    DM = 'DM'
    DO = 'DO'
    EC = 'EC'
    EG = 'EG'
    SV = 'SV'
    GQ = 'GQ'
    ER = 'ER'
    EE = 'EE'
    SZ = 'SZ'
    ET = 'ET'
    FK = 'FK'
    FO = 'FO'
    FJ = 'FJ'
    FI = 'FI'
    FR = 'FR'
    GF = 'GF'
    PF = 'PF'
    TF = 'TF'
    GA = 'GA'
    GM = 'GM'
    GE = 'GE'
    DE = 'DE'
    GH = 'GH'
    GI = 'GI'
    GR = 'GR'
    GL = 'GL'
    GD = 'GD'
    GP = 'GP'
    GU = 'GU'
    GT = 'GT'
    GG = 'GG'
    GN = 'GN'
    GW = 'GW'
    GY = 'GY'
    HT = 'HT'
    HM = 'HM'
    VA = 'VA'
    HN = 'HN'
    HK = 'HK'
    HU = 'HU'
    IS = 'IS'
    IN = 'IN'
    ID = 'ID'
    IR = 'IR'
    IQ = 'IQ'
    IE = 'IE'
    IM = 'IM'
    IL = 'IL'
    IT = 'IT'
    JM = 'JM'
    JP = 'JP'
    JE = 'JE'
    JO = 'JO'
    KZ = 'KZ'
    KE = 'KE'
    KI = 'KI'
    KW = 'KW'
    KG = 'KG'
    LA = 'LA'
    LV = 'LV'
    LB = 'LB'
    LS = 'LS'
    LR = 'LR'
    LY = 'LY'
    LI = 'LI'
    LT = 'LT'
    LU = 'LU'
    MO = 'MO'
    MG = 'MG'
    MW = 'MW'
    MY = 'MY'
    MV = 'MV'
    ML = 'ML'
    MT = 'MT'
    MH = 'MH'
    MQ = 'MQ'
    MR = 'MR'
    MU = 'MU'
    YT = 'YT'
    MX = 'MX'
    FM = 'FM'
    MD = 'MD'
    MC = 'MC'
    MN = 'MN'
    ME = 'ME'
    MS = 'MS'
    MA = 'MA'
    MZ = 'MZ'
    MM = 'MM'
    NA = 'NA'
    NR = 'NR'
    NP = 'NP'
    NL = 'NL'
    NC = 'NC'
    NZ = 'NZ'
    NI = 'NI'
    NE = 'NE'
    NG = 'NG'
    NU = 'NU'
    NF = 'NF'
    KP = 'KP'
    MK = 'MK'
    MP = 'MP'
    NO = 'NO'
    OM = 'OM'
    PK = 'PK'
    PW = 'PW'
    PS = 'PS'
    PA = 'PA'
    PG = 'PG'
    PY = 'PY'
    PE = 'PE'
    PH = 'PH'
    PN = 'PN'
    PL = 'PL'
    PT = 'PT'
    PR = 'PR'
    QA = 'QA'
    RE = 'RE'
    RO = 'RO'
    RU = 'RU'
    RW = 'RW'
    BL = 'BL'
    SH = 'SH'
    KN = 'KN'
    LC = 'LC'
    MF = 'MF'
    PM = 'PM'
    VC = 'VC'
    WS = 'WS'
    SM = 'SM'
    ST = 'ST'
    SA = 'SA'
    SN = 'SN'
    RS = 'RS'
    SC = 'SC'
    SL = 'SL'
    SG = 'SG'
    SX = 'SX'
    SK = 'SK'
    SI = 'SI'
    SB = 'SB'
    SO = 'SO'
    ZA = 'ZA'
    GS = 'GS'
    KR = 'KR'
    SS = 'SS'
    ES = 'ES'
    LK = 'LK'
    SD = 'SD'
    SR = 'SR'
    SJ = 'SJ'
    SE = 'SE'
    CH = 'CH'
    SY = 'SY'
    TW = 'TW'
    TJ = 'TJ'
    TZ = 'TZ'
    TH = 'TH'
    TL = 'TL'
    TG = 'TG'
    TK = 'TK'
    TO = 'TO'
    TT = 'TT'
    TN = 'TN'
    TR = 'TR'
    TM = 'TM'
    TC = 'TC'
    TV = 'TV'
    UG = 'UG'
    UA = 'UA'
    AE = 'AE'
    GB = 'GB'
    UM = 'UM'
    US = 'US'
    UY = 'UY'
    UZ = 'UZ'
    VU = 'VU'
    VE = 'VE'
    VN = 'VN'
    VG = 'VG'
    VI = 'VI'
    WF = 'WF'
    EH = 'EH'
    YE = 'YE'
    ZM = 'ZM'
    ZW = 'ZW'
    

class StockEventType(str):
    STOCK_WAS_CREATED = 'Stock was created'
    STOCK_CREATED = 'STOCK_CREATED'
    STOCK_WAS_UPDATED = 'Stock was updated'
    STOCK_UPDATED = 'STOCK_UPDATED'
    STOCK_WAS_DELETED = 'Stock was deleted'
    STOCK_DELETED = 'STOCK_DELETED'
    STOCK_WAS_ALLOCATED = 'Stock was allocated'
    STOCK_ALLOCATED = 'STOCK_ALLOCATED'
    STOCK_WAS_DEALLOCATED = 'Stock was deallocated'
    STOCK_DEALLOCATED = 'STOCK_DEALLOCATED'
    

class OrderStatusFilter(str):
    READY_TO_FULFILL = 'READY_TO_FULFILL'
    READY_TO_CAPTURE = 'READY_TO_CAPTURE'
    UNFULFILLED = 'UNFULFILLED'
    PARTIALLY_FULFILLED = 'PARTIALLY_FULFILLED'
    FULFILLED = 'FULFILLED'
    DELIVERED = 'DELIVERED'
    CANCELED = 'CANCELED'
    

class OrderSourceFilter(str):
    CHECKOUT = 'CHECKOUT'
    DRAFT = 'DRAFT'
    QUOTE = 'QUOTE'
    MANUAL = 'MANUAL'
    EXTERNAL = 'EXTERNAL'
    

class OfferOrderSubStatusFilter(str):
    OFFER_APPROVED = 'OFFER_APPROVED'
    OFFER_CANCELLED = 'OFFER_CANCELLED'
    OFFER_CREATED = 'OFFER_CREATED'
    OFFER_EXPIRED = 'OFFER_EXPIRED'
    OFFER_NEGOTIATING = 'OFFER_NEGOTIATING'
    OFFER_REJECTED = 'OFFER_REJECTED'
    

class OrderSortField(str):
    SORT_ORDERS_BY_NUMBER. = 'Sort orders by number.'
    NUMBER = 'NUMBER'
    SORT_ORDERS_BY_CREATION_DATE. = 'Sort orders by creation date.'
    CREATION_DATE = 'CREATION_DATE'
    SORT_ORDERS_BY_UPDATE_DATE. = 'Sort orders by update date.'
    UPDATE_DATE = 'UPDATE_DATE'
    SORT_ORDERS_BY_CUSTOMER. = 'Sort orders by customer.'
    CUSTOMER = 'CUSTOMER'
    SORT_ORDERS_BY_PAYMENT. = 'Sort orders by payment.'
    PAYMENT = 'PAYMENT'
    SORT_ORDERS_BY_PAYMENT_DATE. = 'Sort orders by payment date.'
    PAYMENT_DATE = 'PAYMENT_DATE'
    SORT_ORDERS_BY_FULFILLMENT_STATUS. = 'Sort orders by fulfillment status.'
    FULFILLMENT_STATUS = 'FULFILLMENT_STATUS'
    SORT_ORDERS_BY_TOTAL. = 'Sort orders by total.'
    TOTAL = 'TOTAL'
    SORT_ORDERS_BY_PO_NUMBERS. = 'Sort orders by po numbers.'
    PO_NUMBERS = 'PO_NUMBERS'
    SORT_ORDERS_BY_EXTERNAL_ID. = 'Sort orders by external id.'
    EXTERNAL_ID = 'EXTERNAL_ID'
    SORT_ORDERS_BY_EXTERNAL_SOURCE. = 'Sort orders by external source.'
    EXTERNAL_SOURCE = 'EXTERNAL_SOURCE'
    

class CustomerEventsEnum(str):
    THE_ACCOUNT_WAS_CREATED = 'The account was created'
    ACCOUNT_CREATED = 'ACCOUNT_CREATED'
    PASSWORD_RESET_LINK_WAS_SENT_TO_THE_CUSTOMER = 'Password reset link was sent to the customer'
    PASSWORD_RESET_LINK_SENT = 'PASSWORD_RESET_LINK_SENT'
    THE_ACCOUNT_PASSWORD_WAS_RESET = 'The account password was reset'
    PASSWORD_RESET = 'PASSWORD_RESET'
    THE_USER_REQUESTED_TO_CHANGE_THE_ACCOUNT_EMAIL_ADDRESS = 'The user requested to change the account email address'
    EMAIL_CHANGED_REQUEST = 'EMAIL_CHANGED_REQUEST'
    THE_ACCOUNT_PASSWORD_WAS_CHANGED = 'The account password was changed'
    PASSWORD_CHANGED = 'PASSWORD_CHANGED'
    THE_ACCOUNT_EMAIL_ADDRESS_WAS_CHANGED = 'The account email address was changed'
    EMAIL_CHANGED = 'EMAIL_CHANGED'
    AN_ORDER_WAS_PLACED = 'An order was placed'
    PLACED_ORDER = 'PLACED_ORDER'
    A_NOTE_WAS_ADDED = 'A note was added'
    NOTE_ADDED_TO_ORDER = 'NOTE_ADDED_TO_ORDER'
    A_DIGITAL_GOOD_WAS_DOWNLOADED = 'A digital good was downloaded'
    DIGITAL_LINK_DOWNLOADED = 'DIGITAL_LINK_DOWNLOADED'
    A_CUSTOMER_WAS_DELETED = 'A customer was deleted'
    CUSTOMER_DELETED = 'CUSTOMER_DELETED'
    A_CUSTOMER_NAME_WAS_EDITED = 'A customer name was edited'
    NAME_ASSIGNED = 'NAME_ASSIGNED'
    A_CUSTOMER_EMAIL_ADDRESS_WAS_EDITED = 'A customer email address was edited'
    EMAIL_ASSIGNED = 'EMAIL_ASSIGNED'
    A_NOTE_WAS_ADDED_TO_THE_CUSTOMER = 'A note was added to the customer'
    NOTE_ADDED = 'NOTE_ADDED'
    

class WishlistItemSortField(str):
    SORT_WISHLIST_ITEMS_BY_CREATED_AT. = 'Sort wishlist items by created at.'
    CREATED_AT = 'CREATED_AT'
    

class WebhookSampleEventTypeEnum(str):
    AGREEMENT_CREATED = 'AGREEMENT_CREATED'
    AGREEMENT_DELETED = 'AGREEMENT_DELETED'
    AGREEMENT_UPDATED = 'AGREEMENT_UPDATED'
    CATEGORY_CREATED = 'CATEGORY_CREATED'
    CATEGORY_DELETED = 'CATEGORY_DELETED'
    CATEGORY_UPDATED = 'CATEGORY_UPDATED'
    CHECKOUT_CREATED = 'CHECKOUT_CREATED'
    CHECKOUT_UPDATED = 'CHECKOUT_UPDATED'
    COLLECTION_CREATED = 'COLLECTION_CREATED'
    COLLECTION_DELETED = 'COLLECTION_DELETED'
    COLLECTION_UPDATED = 'COLLECTION_UPDATED'
    CUSTOMER_CREATED = 'CUSTOMER_CREATED'
    CUSTOMER_UPDATED = 'CUSTOMER_UPDATED'
    CUSTOMER_DELETED = 'CUSTOMER_DELETED'
    FULFILLMENT_CREATED = 'FULFILLMENT_CREATED'
    INVOICE_DELETED = 'INVOICE_DELETED'
    INVOICE_REQUESTED = 'INVOICE_REQUESTED'
    INVOICE_SENT = 'INVOICE_SENT'
    MICROSITE_CREATED = 'MICROSITE_CREATED'
    MICROSITE_UPDATED = 'MICROSITE_UPDATED'
    NAUTICAL_ORDER_CANCELLED = 'NAUTICAL_ORDER_CANCELLED'
    NAUTICAL_ORDER_CREATED = 'NAUTICAL_ORDER_CREATED'
    NAUTICAL_ORDER_FULFILLED = 'NAUTICAL_ORDER_FULFILLED'
    NAUTICAL_ORDER_FULLY_PAID = 'NAUTICAL_ORDER_FULLY_PAID'
    NAUTICAL_ORDER_UPDATED = 'NAUTICAL_ORDER_UPDATED'
    ORDER_CANCELLED = 'ORDER_CANCELLED'
    ORDER_CREATED = 'ORDER_CREATED'
    ORDER_FULFILLED = 'ORDER_FULFILLED'
    ORDER_FULLY_PAID = 'ORDER_FULLY_PAID'
    ORDER_UPDATED = 'ORDER_UPDATED'
    PAYMENT_CREATED = 'PAYMENT_CREATED'
    PAYMENT_UPDATED = 'PAYMENT_UPDATED'
    PAYOUT_CREATED = 'PAYOUT_CREATED'
    PAYOUT_UPDATED = 'PAYOUT_UPDATED'
    PAYOUT_DELETED = 'PAYOUT_DELETED'
    PRICE_BOOK_CREATED = 'PRICE_BOOK_CREATED'
    PRICE_BOOK_UPDATED = 'PRICE_BOOK_UPDATED'
    PRODUCT_CREATED = 'PRODUCT_CREATED'
    PRODUCT_DELETED = 'PRODUCT_DELETED'
    PRODUCT_UPDATED = 'PRODUCT_UPDATED'
    REFUND_CREATED = 'REFUND_CREATED'
    REFUND_DELETED = 'REFUND_DELETED'
    REFUND_UPDATED = 'REFUND_UPDATED'
    SELLER_CREATED = 'SELLER_CREATED'
    SELLER_UPDATED = 'SELLER_UPDATED'
    SELLER_AGREEMENT_ACKNOWLEDGED = 'SELLER_AGREEMENT_ACKNOWLEDGED'
    SELLER_AGREEMENT_DECLINED = 'SELLER_AGREEMENT_DECLINED'
    VARIANT_CREATED = 'VARIANT_CREATED'
    VARIANT_DELETED = 'VARIANT_DELETED'
    VARIANT_UPDATED = 'VARIANT_UPDATED'
    STOCK_CREATED = 'STOCK_CREATED'
    STOCK_DELETED = 'STOCK_DELETED'
    STOCK_UPDATED = 'STOCK_UPDATED'
    STOCK_ALLOCATED = 'STOCK_ALLOCATED'
    STOCK_DEALLOCATED = 'STOCK_DEALLOCATED'
    VENDOR_PAYOUT_CREATED = 'VENDOR_PAYOUT_CREATED'
    VENDOR_PAYOUT_UPDATED = 'VENDOR_PAYOUT_UPDATED'
    WAREHOUSE_CREATED = 'WAREHOUSE_CREATED'
    WAREHOUSE_DELETED = 'WAREHOUSE_DELETED'
    WAREHOUSE_UPDATED = 'WAREHOUSE_UPDATED'
    

class WebhookDirectionEnum(str):
    WEBHOOK_HAS_BEEN_RECEIVED = 'Webhook has been received'
    RECEIVED = 'RECEIVED'
    WEBHOOK_HAS_BEEN_SENT = 'Webhook has been sent'
    EMITTED = 'EMITTED'
    

class GenericWebhookTransactionType(str):
    A_PAYLOAD_FOR_ORDER_CREATE_WAS_RECEIVED = 'A payload for order create was received'
    ORDER_CREATE = 'ORDER_CREATE'
    A_PAYLOAD_FOR_ORDER_UPDATE_WAS_RECEIVED = 'A payload for order update was received'
    ORDER_UPDATE = 'ORDER_UPDATE'
    A_PAYLOAD_FOR_ORDER_CANCEL_WAS_RECEIVED = 'A payload for order cancel was received'
    ORDER_CANCEL = 'ORDER_CANCEL'
    A_PAYLOAD_FOR_PRODUCT_CREATE_WAS_RECEIVED. = 'A payload for product create was received.'
    PRODUCT_CREATE = 'PRODUCT_CREATE'
    A_PAYLOAD_FOR_PRODUCT_UPDATE_WAS_RECEIVED. = 'A payload for product update was received.'
    PRODUCT_UPDATE = 'PRODUCT_UPDATE'
    A_PAYLOAD_FOR_PRODUCT_DELETE_WAS_RECEIVED. = 'A payload for product delete was received.'
    PRODUCT_DELETE = 'PRODUCT_DELETE'
    A_PAYLOAD_FOR_PRODUCT_INVENTORY_TRACKING_UPDATE_WAS_RECEIVED. = 'A payload for product inventory tracking update was received.'
    INVENTORY_TRACKING_UPDATE = 'INVENTORY_TRACKING_UPDATE'
    A_PAYLOAD_FOR_STOCK_CREATE_WAS_RECEIVED. = 'A payload for stock create was received.'
    STOCK_CREATE = 'STOCK_CREATE'
    A_PAYLOAD_FOR_STOCK_UPDATE_WAS_RECEIVED. = 'A payload for stock update was received.'
    STOCK_UPDATE = 'STOCK_UPDATE'
    A_PAYLOAD_FOR_STOCK_DELETE_WAS_RECEIVED. = 'A payload for stock delete was received.'
    STOCK_DELETE = 'STOCK_DELETE'
    A_PAYLOAD_FOR_WAREHOUSE_CREATE_WAS_RECEIVED. = 'A payload for warehouse create was received.'
    WAREHOUSE_CREATE = 'WAREHOUSE_CREATE'
    A_PAYLOAD_FOR_WAREHOUSE_UPDATE_WAS_RECEIVED. = 'A payload for warehouse update was received.'
    WAREHOUSE_UPDATE = 'WAREHOUSE_UPDATE'
    A_PAYLOAD_FOR_WAREHOUSE_DELETE_WAS_RECEIVED. = 'A payload for warehouse delete was received.'
    WAREHOUSE_DELETE = 'WAREHOUSE_DELETE'
    A_PAYLOAD_FOR_FULFILLMENT_CREATE_WAS_RECEIVED. = 'A payload for fulfillment create was received.'
    FULFILLMENT_CREATE = 'FULFILLMENT_CREATE'
    A_PAYLOAD_FOR_FULFILLMENT_UPDATE_WAS_RECEIVED. = 'A payload for fulfillment update was received.'
    FULFILLMENT_UPDATE = 'FULFILLMENT_UPDATE'
    A_PAYLOD_FOR_CUSTOMER_CREATE_WAS_RECEIVED = 'A paylod for customer create was received'
    CUSTOMER_CREATE = 'CUSTOMER_CREATE'
    A_PAYLOAD_FOR_SELLER_CREATE_WAS_RECEIVED = 'A payload for seller create was received'
    SELLER_CREATE = 'SELLER_CREATE'
    A_PAYLOAD_FOR_VEHICLES_WAS_RECEIVED = 'A payload for vehicles was received'
    VEHICLE_PAYLOAD = 'VEHICLE_PAYLOAD'
    A_PAYLOAD_FOR_ITEM_SHIPMENT_THAT_WAS_RECEIVED = 'A payload for item shipment that was received'
    ITEM_SHIP_NOTIFY = 'ITEM_SHIP_NOTIFY'
    

class WebhookJobStatus(str):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'
    PENDING = 'PENDING'
    DELETED = 'DELETED'
    

class WebhookJobSource(str):
    DEFAULT = 'DEFAULT'
    SHOPIFY = 'SHOPIFY'
    

class WebhookJobType(str):
    ORDER_CREATE = 'ORDER_CREATE'
    ORDER_UPDATE = 'ORDER_UPDATE'
    

class WebhookJobSortField(str):
    SORT_WEBHOOK_JOBS_BY_SOURCE. = 'Sort webhook jobs by source.'
    SOURCE = 'SOURCE'
    SORT_WEBHOOK_JOBS_BY_TYPE. = 'Sort webhook jobs by type.'
    TYPE = 'TYPE'
    SORT_WEBHOOK_JOBS_BY_STATUS. = 'Sort webhook jobs by status.'
    STATUS = 'STATUS'
    SORT_WEBHOOK_JOBS_BY_CREATED_AT. = 'Sort webhook jobs by created at.'
    CREATED_AT = 'CREATED_AT'
    

class WarehouseSortField(str):
    SORT_WAREHOUSES_BY_NAME. = 'Sort warehouses by name.'
    NAME = 'NAME'
    SORT_WAREHOUSES_BY_EXTERNAL_ID. = 'Sort warehouses by external id.'
    EXTERNAL_ID = 'EXTERNAL_ID'
    SORT_WAREHOUSES_BY_EXTERNAL_SOURCE. = 'Sort warehouses by external source.'
    EXTERNAL_SOURCE = 'EXTERNAL_SOURCE'
    

class ContentSortField(str):
    SLUG = 'SLUG'
    CREATED_AT = 'CREATED_AT'
    UPDATED_AT = 'UPDATED_AT'
    LOCKED_BY = 'LOCKED_BY'
    LOCK_EXPIRY = 'LOCK_EXPIRY'
    IS_PUBLISHED = 'IS_PUBLISHED'
    

class MediaSortField(str):
    TITLE = 'TITLE'
    CREATED_AT = 'CREATED_AT'
    

class LanguageCodeEnum(str):
    AR = 'AR'
    AZ = 'AZ'
    BG = 'BG'
    BN = 'BN'
    CA = 'CA'
    CS = 'CS'
    DA = 'DA'
    DE = 'DE'
    EL = 'EL'
    EN = 'EN'
    ES = 'ES'
    ES_CO = 'ES_CO'
    ET = 'ET'
    FA = 'FA'
    FI = 'FI'
    FR = 'FR'
    HI = 'HI'
    HU = 'HU'
    HY = 'HY'
    ID = 'ID'
    IS = 'IS'
    IT = 'IT'
    JA = 'JA'
    KA = 'KA'
    KM = 'KM'
    KO = 'KO'
    LT = 'LT'
    MN = 'MN'
    MY = 'MY'
    NB = 'NB'
    NL = 'NL'
    PL = 'PL'
    PT = 'PT'
    PT_BR = 'PT_BR'
    RO = 'RO'
    RU = 'RU'
    SK = 'SK'
    SL = 'SL'
    SQ = 'SQ'
    SR = 'SR'
    SV = 'SV'
    SW = 'SW'
    TA = 'TA'
    TH = 'TH'
    TR = 'TR'
    UK = 'UK'
    VI = 'VI'
    ZH_HANS = 'ZH_HANS'
    ZH_HANT = 'ZH_HANT'
    

class PluginConfigurationCategory(str):
    AUTH = 'Auth'
    AUTH = 'AUTH'
    FULFILLMENT = 'Fulfillment'
    FULFILLMENT = 'FULFILLMENT'
    ECOMMERCE = 'Ecommerce'
    ECOMMERCE = 'ECOMMERCE'
    DATA_CONNECTIVITY = 'Data Connectivity'
    DATA_CONNECTIVITY = 'DATA_CONNECTIVITY'
    ORDER_EXTENSIONS = 'Order Extensions'
    ORDER_EXTENSIONS = 'ORDER_EXTENSIONS'
    UTILITY = 'Utility'
    UTILITY = 'UTILITY'
    TAXES = 'Taxes'
    TAXES = 'TAXES'
    MARKETING = 'Marketing'
    MARKETING = 'MARKETING'
    LOCATIONS = 'Locations'
    LOCATIONS = 'LOCATIONS'
    PAYMENTS = 'Payments'
    PAYMENTS = 'PAYMENTS'
    

class ConfigurationTypeFieldEnum(str):
    STRING = 'STRING'
    MULTILINE = 'MULTILINE'
    BOOLEAN = 'BOOLEAN'
    SECRET = 'SECRET'
    SECRET_MULTILINE = 'SECRET_MULTILINE'
    PASSWORD = 'PASSWORD'
    SINGLE_SELECT = 'SINGLE_SELECT'
    OUTPUT = 'OUTPUT'
    

class DomainStatusEnum(str):
    UNVERIFIED = 'UNVERIFIED'
    DNS_VERIFIED = 'DNS_VERIFIED'
    PROVISIONING = 'PROVISIONING'
    PROVISIONED = 'PROVISIONED'
    ERROR = 'ERROR'
    QUEUED_FOR_DELETION = 'QUEUED_FOR_DELETION'
    DELETING = 'DELETING'
    DELETED = 'DELETED'
    

class SellerStatusFilter(str):
    APPLYING = 'APPLYING'
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    DECLINED = 'DECLINED'
    SUSPENDED = 'SUSPENDED'
    BANNED = 'BANNED'
    DEACTIVATED = 'DEACTIVATED'
    PAUSED = 'PAUSED'
    

class SellerSortField(str):
    SORT_SELLERS_BY_COMPANY_NAME. = 'Sort sellers by company name.'
    COMPANY_NAME = 'COMPANY_NAME'
    SORT_SELLERS_BY_OWNER. = 'Sort sellers by owner.'
    OWNER = 'OWNER'
    SORT_SELLERS_BY_STATUS. = 'Sort sellers by status.'
    STATUS = 'STATUS'
    SORT_SELLERS_BY_CREATED. = 'Sort sellers by created.'
    CREATED = 'CREATED'
    

class ReportingPeriod(str):
    TODAY = 'TODAY'
    THIS_MONTH = 'THIS_MONTH'
    

class RefundSortField(str):
    SORT_REFUND_BY_NAME. = 'Sort refund by name.'
    NAME = 'NAME'
    SORT_REFUND_BY_CREATED. = 'Sort refund by created.'
    CREATED = 'CREATED'
    SORT_REFUND_BY_UPDATED. = 'Sort refund by updated.'
    UPDATED = 'UPDATED'
    SORT_REFUND_BY_STATUS. = 'Sort refund by status.'
    STATUS = 'STATUS'
    SORT_REFUND_BY_BUYER. = 'Sort refund by buyer.'
    BUYER = 'BUYER'
    SORT_REFUND_BY_EXTERNAL_ID. = 'Sort refund by external id.'
    EXTERNAL_ID = 'EXTERNAL_ID'
    SORT_REFUND_BY_TOKEN. = 'Sort refund by token.'
    TOKEN = 'TOKEN'
    

class CategorySortField(str):
    SORT_CATEGORIES_BY_NAME. = 'Sort categories by name.'
    NAME = 'NAME'
    SORT_CATEGORIES_BY_PRODUCT_COUNT. = 'Sort categories by product count.'
    PRODUCT_COUNT = 'PRODUCT_COUNT'
    SORT_CATEGORIES_BY_SUBCATEGORY_COUNT. = 'Sort categories by subcategory count.'
    SUBCATEGORY_COUNT = 'SUBCATEGORY_COUNT'
    SORT_CATEGORIES_BY_EXTERNAL_ID. = 'Sort categories by external id.'
    EXTERNAL_ID = 'EXTERNAL_ID'
    SORT_CATEGORIES_BY_EXTERNAL_SOURCE. = 'Sort categories by external source.'
    EXTERNAL_SOURCE = 'EXTERNAL_SOURCE'
    

class CollectionPublished(str):
    PUBLISHED = 'PUBLISHED'
    HIDDEN = 'HIDDEN'
    

class CollectionVisible(str):
    VISIBLE = 'VISIBLE'
    HIDDEN = 'HIDDEN'
    

class CollectionSortField(str):
    SORT_COLLECTIONS_BY_NAME. = 'Sort collections by name.'
    NAME = 'NAME'
    SORT_COLLECTIONS_BY_AVAILABILITY. = 'Sort collections by availability.'
    AVAILABILITY = 'AVAILABILITY'
    SORT_COLLECTIONS_BY_PRODUCT_COUNT. = 'Sort collections by product count.'
    PRODUCT_COUNT = 'PRODUCT_COUNT'
    SORT_COLLECTIONS_BY_PUBLICATION_DATE. = 'Sort collections by publication date.'
    PUBLICATION_DATE = 'PUBLICATION_DATE'
    

class ProductTypeEnum(str):
    DIGITAL = 'DIGITAL'
    SHIPPABLE = 'SHIPPABLE'
    

class ProductTypeConfigurable(str):
    CONFIGURABLE = 'CONFIGURABLE'
    SIMPLE = 'SIMPLE'
    

class ProductTypeSortField(str):
    SORT_PRODUCTS_BY_NAME. = 'Sort products by name.'
    NAME = 'NAME'
    SORT_PRODUCTS_BY_TYPE. = 'Sort products by type.'
    DIGITAL = 'DIGITAL'
    SORT_PRODUCTS_BY_SHIPPING. = 'Sort products by shipping.'
    SHIPPING_REQUIRED = 'SHIPPING_REQUIRED'
    SORT_PRODUCTS_BY_EXTERNAL_ID. = 'Sort products by external id.'
    EXTERNAL_ID = 'EXTERNAL_ID'
    SORT_PRODUCTS_BY_EXTERNAL_SOURCE. = 'Sort products by external source.'
    EXTERNAL_SOURCE = 'EXTERNAL_SOURCE'
    

class PriceBookSortField(str):
    SORT_PRICEBOOK_BY_NAME. = 'Sort pricebook by name.'
    NAME = 'NAME'
    

class PriceBookVariantSortField(str):
    SORT_PRICEBOOK_VARIANT_HISTORY_BY_NUMBER. = 'Sort pricebook variant history by number.'
    NUMBER = 'NUMBER'
    SORT_PRICEBOOK_VARIANT_HISTORY_BY_TYPE. = 'Sort pricebook variant history by type.'
    TYPE = 'TYPE'
    SORT_PRICEBOOK_VARIANT_HISTORY_BY_PRICE. = 'Sort pricebook variant history by price.'
    PRICE = 'PRICE'
    SORT_PRICEBOOK_VARIANT_HISTORY_BY_PERCENTAGE. = 'Sort pricebook variant history by percentage.'
    PERCENTAGE = 'PERCENTAGE'
    

class PriceBookProductSortField(str):
    SORT_PRICEBOOK_PRODUCT_HISTORY_BY_NUMBER. = 'Sort pricebook product history by number.'
    NUMBER = 'NUMBER'
    SORT_PRICEBOOK_PRODUCT_HISTORY_BY_TYPE. = 'Sort pricebook product history by type.'
    TYPE = 'TYPE'
    SORT_PRICEBOOK_PRODUCT_HISTORY_BY_PRICE. = 'Sort pricebook product history by price.'
    PRICE = 'PRICE'
    SORT_PRICEBOOK_PRODUCT_HISTORY_BY_PERCENTAGE. = 'Sort pricebook product history by percentage.'
    PERCENTAGE = 'PERCENTAGE'
    

class PriceBookProductTypeSortField(str):
    SORT_PRICEBOOK_PRODUCT_TYPE_HISTORY_BY_NUMBER. = 'Sort pricebook product type history by number.'
    NUMBER = 'NUMBER'
    SORT_PRICEBOOK_PRODUCT_TYPE_HISTORY_BY_TYPE. = 'Sort pricebook product type history by type.'
    TYPE = 'TYPE'
    SORT_PRICEBOOK_PRODUCT_TYPE_HISTORY_BY_PRICE. = 'Sort pricebook product type history by price.'
    PRICE = 'PRICE'
    SORT_PRICEBOOK_PRODUCT_TYPE_HISTORY_BY_PERCENTAGE. = 'Sort pricebook product type history by percentage.'
    PERCENTAGE = 'PERCENTAGE'
    

class PriceBookVariantHistoryValueType(str):
    OVERRIDE = 'Override'
    OVERRIDE = 'OVERRIDE'
    ADJUST_PERCENTAGE = 'Adjust Percentage'
    ADJUST_PERCENTAGE = 'ADJUST_PERCENTAGE'
    ADJUST_FIXED = 'Adjust Fixed'
    ADJUST_FIXED = 'ADJUST_FIXED'
    

class PriceBookVariantHistorySortField(str):
    SORT_PRICEBOOK_VARIANT_HISTORY_BY_NUMBER. = 'Sort pricebook variant history by number.'
    NUMBER = 'NUMBER'
    SORT_PRICEBOOK_VARIANT_HISTORY_BY_TYPE. = 'Sort pricebook variant history by type.'
    TYPE = 'TYPE'
    SORT_PRICEBOOK_VARIANT_HISTORY_BY_PRICE. = 'Sort pricebook variant history by price.'
    PRICE = 'PRICE'
    SORT_PRICEBOOK_VARIANT_HISTORY_BY_PERCENTAGE. = 'Sort pricebook variant history by percentage.'
    PERCENTAGE = 'PERCENTAGE'
    SORT_PRICEBOOK_VARIANT_HISTORY_BY_CREATION_DATE. = 'Sort pricebook variant history by creation date.'
    CREATION_DATE = 'CREATION_DATE'
    

class PriceBookProductHistoryValueType(str):
    ADJUST_PERCENTAGE = 'adjust_percentage'
    ADJUST_PERCENTAGE = 'ADJUST_PERCENTAGE'
    ADJUST_FIXED = 'adjust_fixed'
    ADJUST_FIXED = 'ADJUST_FIXED'
    

class PriceBookProductHistorySortField(str):
    SORT_PRICEBOOK_PRODUCT_HISTORY_BY_NUMBER. = 'Sort pricebook product history by number.'
    NUMBER = 'NUMBER'
    SORT_PRICEBOOK_PRODUCT_HISTORY_BY_TYPE. = 'Sort pricebook product history by type.'
    TYPE = 'TYPE'
    SORT_PRICEBOOK_PRODUCT_HISTORY_BY_PRICE. = 'Sort pricebook product history by price.'
    PRICE = 'PRICE'
    SORT_PRICEBOOK_PRODUCT_HISTORY_BY_PERCENTAGE. = 'Sort pricebook product history by percentage.'
    PERCENTAGE = 'PERCENTAGE'
    SORT_PRICEBOOK_PRODUCT_HISTORY_BY_CREATION_DATE. = 'Sort pricebook product history by creation date.'
    CREATION_DATE = 'CREATION_DATE'
    

class PriceBookProductTypeHistoryValueType(str):
    ADJUST_PERCENTAGE = 'adjust_percentage'
    ADJUST_PERCENTAGE = 'ADJUST_PERCENTAGE'
    ADJUST_FIXED = 'adjust_fixed'
    ADJUST_FIXED = 'ADJUST_FIXED'
    

class PriceBookProductTypeHistorySortField(str):
    SORT_PRICEBOOK_PRODUCT_TYPE_HISTORY_BY_NUMBER. = 'Sort pricebook product type history by number.'
    NUMBER = 'NUMBER'
    SORT_PRICEBOOK_PRODUCT_TYPE_HISTORY_BY_TYPE. = 'Sort pricebook product type history by type.'
    TYPE = 'TYPE'
    SORT_PRICEBOOK_PRODUCT_TYPE_HISTORY_BY_PRICE. = 'Sort pricebook product type history by price.'
    PRICE = 'PRICE'
    SORT_PRICEBOOK_PRODUCT_TYPE_HISTORY_BY_PERCENTAGE. = 'Sort pricebook product type history by percentage.'
    PERCENTAGE = 'PERCENTAGE'
    SORT_PRICEBOOK_PRODUCT_TYPE_HISTORY_BY_CREATION_DATE. = 'Sort pricebook product type history by creation date.'
    CREATION_DATE = 'CREATION_DATE'
    

class UserSortField(str):
    SORT_USERS_BY_FIRST_NAME. = 'Sort users by first name.'
    FIRST_NAME = 'FIRST_NAME'
    SORT_USERS_BY_LAST_NAME. = 'Sort users by last name.'
    LAST_NAME = 'LAST_NAME'
    SORT_USERS_BY_EMAIL. = 'Sort users by email.'
    EMAIL = 'EMAIL'
    SORT_USERS_BY_ORDER_COUNT. = 'Sort users by order count.'
    ORDER_COUNT = 'ORDER_COUNT'
    SORT_USERS_BY_VENDOR. = 'Sort users by vendor.'
    VENDOR = 'VENDOR'
    SORT_USERS_BY_COMPANY_NAME. = 'Sort users by company name.'
    COMPANY_NAME = 'COMPANY_NAME'
    SORT_USERS_BY_IS_ACTIVE. = 'Sort users by is active.'
    IS_ACTIVE = 'IS_ACTIVE'
    SORT_USERS_BY_EXTERNAL_ID. = 'Sort users by external id.'
    EXTERNAL_ID = 'EXTERNAL_ID'
    SORT_USERS_BY_EXTERNAL_SOURCE. = 'Sort users by external source.'
    EXTERNAL_SOURCE = 'EXTERNAL_SOURCE'
    

class PluginSortField(str):
    NAME = 'NAME'
    IS_ACTIVE = 'IS_ACTIVE'
    

class CatalogImportProcessStatus(str):
    PENDING = 'Pending'
    PENDING = 'PENDING'
    PROCESSING = 'Processing'
    PROCESSING = 'PROCESSING'
    SUCCESS = 'Success'
    SUCCESS = 'SUCCESS'
    FAILED = 'Failed'
    FAILED = 'FAILED'
    DELETED = 'Deleted'
    DELETED = 'DELETED'
    

class CatalogImportProcessLogRecordOperation(str):
    ATTRIBUTE_CREATED = 'Attribute Created'
    ATTRIBUTE_CREATED = 'ATTRIBUTE_CREATED'
    ATTRIBUTE_UPDATED = 'Attribute Updated'
    ATTRIBUTE_UPDATED = 'ATTRIBUTE_UPDATED'
    CATEGORY_CREATED = 'Category Created'
    CATEGORY_CREATED = 'CATEGORY_CREATED'
    CATEGORY_UPDATED = 'Category Updated'
    CATEGORY_UPDATED = 'CATEGORY_UPDATED'
    PRODUCT_CREATED = 'Product Created'
    PRODUCT_CREATED = 'PRODUCT_CREATED'
    PRODUCT_UPDATED = 'Product Updated'
    PRODUCT_UPDATED = 'PRODUCT_UPDATED'
    PRODUCT_UPDATED_OR_CREATED = 'Product Updated or Created'
    PRODUCT_UPDATED_OR_CREATED = 'PRODUCT_UPDATED_OR_CREATED'
    PRODUCT_ARCHIVED = 'Product Archived'
    PRODUCT_ARCHIVED = 'PRODUCT_ARCHIVED'
    PRODUCT_TYPE_CREATED = 'Product Type Created'
    PRODUCT_TYPE_CREATED = 'PRODUCT_TYPE_CREATED'
    PRODUCT_TYPE_UPDATED = 'Product Type Updated'
    PRODUCT_TYPE_UPDATED = 'PRODUCT_TYPE_UPDATED'
    WAREHOUSE_CREATED = 'Warehouse Created'
    WAREHOUSE_CREATED = 'WAREHOUSE_CREATED'
    WAREHOUSE_UPDATED = 'Warehouse Updated'
    WAREHOUSE_UPDATED = 'WAREHOUSE_UPDATED'
    

class CatalogImportOperation(str):
    ATTRIBUTE_CREATED = 'ATTRIBUTE_CREATED'
    ATTRIBUTE_UPDATED = 'ATTRIBUTE_UPDATED'
    CATEGORY_CREATED = 'CATEGORY_CREATED'
    CATEGORY_UPDATED = 'CATEGORY_UPDATED'
    PRODUCT_CREATED = 'PRODUCT_CREATED'
    PRODUCT_UPDATED = 'PRODUCT_UPDATED'
    PRODUCT_UPDATED_OR_CREATED = 'PRODUCT_UPDATED_OR_CREATED'
    PRODUCT_ARCHIVED = 'PRODUCT_ARCHIVED'
    PRODUCT_TYPE_CREATED = 'PRODUCT_TYPE_CREATED'
    PRODUCT_TYPE_UPDATED = 'PRODUCT_TYPE_UPDATED'
    WAREHOUSE_CREATED = 'WAREHOUSE_CREATED'
    WAREHOUSE_UPDATED = 'WAREHOUSE_UPDATED'
    

class CatalogImportProcessLogRecordSortField(str):
    SORT_USERS_BY_CREATED_AT. = 'Sort users by created at.'
    CREATED_AT = 'CREATED_AT'
    

class CatalogImportProcessSortField(str):
    SORT_USERS_BY_CREATED_AT. = 'Sort users by created at.'
    CREATED_AT = 'CREATED_AT'
    SORT_USERS_BY_FINISHED_AT. = 'Sort users by finished at.'
    FINISHED_AT = 'FINISHED_AT'
    

class FlowProcess(str):
    CUSTOMER_CREATION = 'customer_creation'
    CUSTOMER_CREATION = 'CUSTOMER_CREATION'
    SELLER_CREATION = 'seller_creation'
    SELLER_CREATION = 'SELLER_CREATION'
    

class CheckoutEventType(str):
    CHECKOUT_STARTED = 'Checkout started'
    CHECKOUT_STARTED = 'CHECKOUT_STARTED'
    SHIPPING_INFORMATION_ENTERED = 'Shipping information entered'
    SHIPPING_INFORMATION_ENTERED = 'SHIPPING_INFORMATION_ENTERED'
    PAYMENT_INFORMATION_ENTERED = 'Payment information entered'
    PAYMENT_INFORMATION_ENTERED = 'PAYMENT_INFORMATION_ENTERED'
    PURCHASE = 'Purchase'
    PURCHASE = 'PURCHASE'
    

class CheckoutEventSortField(str):
    SORT_CHECKOUT_EVENTS_BY_CREATED_AT. = 'Sort checkout events by created at.'
    CREATED_AT = 'CREATED_AT'
    SORT_CHECKOUT_EVENTS_BY_TYPE. = 'Sort checkout events by type.'
    TYPE = 'TYPE'
    

class PayoutStatusFilter(str):
    PAID = 'paid'
    DRAFT = 'draft'
    ARCHIVED = 'archived'
    LOCKED = 'locked'
    

class PayoutSortField(str):
    SORT_PAYOUTS_BY_REPORT. = 'Sort payouts by report.'
    REPORT = 'REPORT'
    SORT_PAYOUTS_BY_END_DATE. = 'Sort payouts by end date.'
    END_DATE = 'END_DATE'
    SORT_PAYOUTS_BY_CREATED. = 'Sort payouts by created.'
    CREATED = 'CREATED'
    SORT_PAYOUTS_BY_STATUS. = 'Sort payouts by status.'
    STATUS = 'STATUS'
    

class PageSortField(str):
    SORT_PAGES_BY_TITLE. = 'Sort pages by title.'
    TITLE = 'TITLE'
    SORT_PAGES_BY_SLUG. = 'Sort pages by slug.'
    SLUG = 'SLUG'
    SORT_PAGES_BY_VISIBILITY. = 'Sort pages by visibility.'
    VISIBILITY = 'VISIBILITY'
    SORT_PAGES_BY_CREATION_DATE. = 'Sort pages by creation date.'
    CREATION_DATE = 'CREATION_DATE'
    SORT_PAGES_BY_PUBLICATION_DATE. = 'Sort pages by publication date.'
    PUBLICATION_DATE = 'PUBLICATION_DATE'
    

class QuoteOrderSubStatusFilter(str):
    IN_REVIEW = 'IN_REVIEW'
    QUOTE_REQUESTED = 'QUOTE_REQUESTED'
    AWAITING_PAYMENT = 'AWAITING_PAYMENT'
    

class FulfillmentStatusFilter(str):
    FULFILLED = 'FULFILLED'
    CANCELED = 'CANCELED'
    RETURNED = 'RETURNED'
    DECLINED = 'DECLINED'
    RETURN_REQUESTED = 'RETURN_REQUESTED'
    RETURN_AUTHORIZED = 'RETURN_AUTHORIZED'
    RETURN_DECLINED = 'RETURN_DECLINED'
    RETURN_RECEIVED = 'RETURN_RECEIVED'
    RETURN_COMPLETE = 'RETURN_COMPLETE'
    RETURN_CANCELLED = 'RETURN_CANCELLED'
    

class ReturnFulfillmentSortField(str):
    SORT_RETURN_FULFILLMENTS_BY_NUMBER. = 'Sort return fulfillments by number.'
    NUMBER = 'NUMBER'
    SORT_RETURN_FULFILLMENTS_BY_TRACKING_NUMBER. = 'Sort return fulfillments by tracking number.'
    TRACKING_NUMBER = 'TRACKING_NUMBER'
    SORT_RETURN_FULFILLMENTS_BY_CREATION_DATE. = 'Sort return fulfillments by creation date.'
    CREATION_DATE = 'CREATION_DATE'
    SORT_RETURN_FULFILLMENTS_BY_CUSTOMER. = 'Sort return fulfillments by customer.'
    CUSTOMER = 'CUSTOMER'
    SORT_RETURN_FULFILLMENTS_BY_ITEMS. = 'Sort return fulfillments by items.'
    ITEMS = 'ITEMS'
    SORT_RETURN_FULFILLMENTS_BY_PRICE. = 'Sort return fulfillments by price.'
    PRICE = 'PRICE'
    SORT_RETURN_FULFILLMENTS_BY_RETURN_STATUS. = 'Sort return fulfillments by return status.'
    RETURN_STATUS = 'RETURN_STATUS'
    

class MicrositePublished(str):
    PUBLISHED = 'PUBLISHED'
    HIDDEN = 'HIDDEN'
    

class MicrositeSortField(str):
    SORT_MICROSITES_BY_NAME. = 'Sort microsites by name.'
    NAME = 'NAME'
    SORT_MICROSITES_BY_AVAILABILITY. = 'Sort microsites by availability.'
    AVAILABILITY = 'AVAILABILITY'
    SORT_MICROSITES_BY_PRODUCT_COUNT. = 'Sort microsites by product count.'
    PRODUCT_COUNT = 'PRODUCT_COUNT'
    SORT_MICROSITES_BY_PUBLICATION_DATE. = 'Sort microsites by publication date.'
    PUBLICATION_DATE = 'PUBLICATION_DATE'
    

class MenuSortField(str):
    SORT_MENUS_BY_NAME. = 'Sort menus by name.'
    NAME = 'NAME'
    SORT_MENUS_BY_ITEMS_COUNT. = 'Sort menus by items count.'
    ITEMS_COUNT = 'ITEMS_COUNT'
    

class MenuItemsSortField(str):
    SORT_MENU_ITEMS_BY_NAME. = 'Sort menu items by name.'
    NAME = 'NAME'
    

class MarketplaceConfigurationPayoutAutomationStrategyEnum(str):
    COMPLETELY_MANUALLY_CONTROLLED_PAYOUT_STATUS = 'Completely Manually controlled Payout Status'
    MANUAL = 'MANUAL'
    READY_FOR_PAYOUT_WHEN_STATUS_IS_PAID_AND_FULFILLED = 'Ready for payout when status is paid and fulfilled'
    AUTOMATED_BY_FULFILLMENT = 'AUTOMATED_BY_FULFILLMENT'
    

class MarketplaceConfigurationCurrencyEnum(str):
    UNITED_ARAB_EMIRATES_DIRHAM = 'United Arab Emirates Dirham'
    AED = 'AED'
    AFGHAN_AFGHANI = 'Afghan Afghani'
    AFN = 'AFN'
    ALBANIAN_LEK = 'Albanian Lek'
    ALL = 'ALL'
    ARMENIAN_DRAM = 'Armenian Dram'
    AMD = 'AMD'
    NETHERLANDS_ANTILLEAN_GUILDER = 'Netherlands Antillean Guilder'
    ANG = 'ANG'
    ANGOLAN_KWANZA = 'Angolan Kwanza'
    AOA = 'AOA'
    ARGENTINE_PESO = 'Argentine Peso'
    ARS = 'ARS'
    AUSTRALIAN_DOLLAR = 'Australian Dollar'
    AUD = 'AUD'
    ARUBAN_FLORIN = 'Aruban Florin'
    AWG = 'AWG'
    AZERBAIJANI_MANAT = 'Azerbaijani Manat'
    AZN = 'AZN'
    BOSNIA-HERZEGOVINA_CONVERTIBLE_MARK = 'Bosnia-Herzegovina Convertible Mark'
    BAM = 'BAM'
    BARBADIAN_DOLLAR = 'Barbadian Dollar'
    BBD = 'BBD'
    BANGLADESHI_TAKA = 'Bangladeshi Taka'
    BDT = 'BDT'
    BULGARIAN_LEV = 'Bulgarian Lev'
    BGN = 'BGN'
    BAHRAINI_DINAR = 'Bahraini Dinar'
    BHD = 'BHD'
    BURUNDIAN_FRANC = 'Burundian Franc'
    BIF = 'BIF'
    BERMUDAN_DOLLAR = 'Bermudan Dollar'
    BMD = 'BMD'
    BRUNEI_DOLLAR = 'Brunei Dollar'
    BND = 'BND'
    BOLIVIAN_BOLIVIANO = 'Bolivian Boliviano'
    BOB = 'BOB'
    BRAZILIAN_REAL = 'Brazilian Real'
    BRL = 'BRL'
    BAHAMIAN_DOLLAR = 'Bahamian Dollar'
    BSD = 'BSD'
    BITCOIN = 'Bitcoin'
    BTC = 'BTC'
    BHUTANESE_NGULTRUM = 'Bhutanese Ngultrum'
    BTN = 'BTN'
    BOTSWANAN_PULA = 'Botswanan Pula'
    BWP = 'BWP'
    BELARUSIAN_RUBLE = 'Belarusian Ruble'
    BYN = 'BYN'
    BELARUSIAN_RUBLE_(PRE-2016) = 'Belarusian Ruble (pre-2016)'
    BYR = 'BYR'
    BELIZE_DOLLAR = 'Belize Dollar'
    BZD = 'BZD'
    CANADIAN_DOLLAR = 'Canadian Dollar'
    CAD = 'CAD'
    CONGOLESE_FRANC = 'Congolese Franc'
    CDF = 'CDF'
    SWISS_FRANC = 'Swiss Franc'
    CHF = 'CHF'
    CHILEAN_UNIT_OF_ACCOUNT_(UF) = 'Chilean Unit of Account (UF)'
    CLF = 'CLF'
    CHILEAN_PESO = 'Chilean Peso'
    CLP = 'CLP'
    CHINESE_YUAN_(OFFSHORE) = 'Chinese Yuan (Offshore)'
    CNH = 'CNH'
    CHINESE_YUAN = 'Chinese Yuan'
    CNY = 'CNY'
    COLOMBIAN_PESO = 'Colombian Peso'
    COP = 'COP'
    COSTA_RICAN_COLÓN = 'Costa Rican Colón'
    CRC = 'CRC'
    CUBAN_CONVERTIBLE_PESO = 'Cuban Convertible Peso'
    CUC = 'CUC'
    CUBAN_PESO = 'Cuban Peso'
    CUP = 'CUP'
    CAPE_VERDEAN_ESCUDO = 'Cape Verdean Escudo'
    CVE = 'CVE'
    CZECH_REPUBLIC_KORUNA = 'Czech Republic Koruna'
    CZK = 'CZK'
    DJIBOUTIAN_FRANC = 'Djiboutian Franc'
    DJF = 'DJF'
    DANISH_KRONE = 'Danish Krone'
    DKK = 'DKK'
    DOMINICAN_PESO = 'Dominican Peso'
    DOP = 'DOP'
    ALGERIAN_DINAR = 'Algerian Dinar'
    DZD = 'DZD'
    ESTONIAN_KROON = 'Estonian Kroon'
    EEK = 'EEK'
    EGYPTIAN_POUND = 'Egyptian Pound'
    EGP = 'EGP'
    ERITREAN_NAKFA = 'Eritrean Nakfa'
    ERN = 'ERN'
    ETHIOPIAN_BIRR = 'Ethiopian Birr'
    ETB = 'ETB'
    EURO = 'Euro'
    EUR = 'EUR'
    FIJIAN_DOLLAR = 'Fijian Dollar'
    FJD = 'FJD'
    FALKLAND_ISLANDS_POUND = 'Falkland Islands Pound'
    FKP = 'FKP'
    BRITISH_POUND_STERLING = 'British Pound Sterling'
    GBP = 'GBP'
    GEORGIAN_LARI = 'Georgian Lari'
    GEL = 'GEL'
    GUERNSEY_POUND = 'Guernsey Pound'
    GGP = 'GGP'
    GHANAIAN_CEDI = 'Ghanaian Cedi'
    GHS = 'GHS'
    GIBRALTAR_POUND = 'Gibraltar Pound'
    GIP = 'GIP'
    GAMBIAN_DALASI = 'Gambian Dalasi'
    GMD = 'GMD'
    GUINEAN_FRANC = 'Guinean Franc'
    GNF = 'GNF'
    GUATEMALAN_QUETZAL = 'Guatemalan Quetzal'
    GTQ = 'GTQ'
    GUYANAESE_DOLLAR = 'Guyanaese Dollar'
    GYD = 'GYD'
    HONG_KONG_DOLLAR = 'Hong Kong Dollar'
    HKD = 'HKD'
    HONDURAN_LEMPIRA = 'Honduran Lempira'
    HNL = 'HNL'
    CROATIAN_KUNA = 'Croatian Kuna'
    HRK = 'HRK'
    HAITIAN_GOURDE = 'Haitian Gourde'
    HTG = 'HTG'
    HUNGARIAN_FORINT = 'Hungarian Forint'
    HUF = 'HUF'
    INDONESIAN_RUPIAH = 'Indonesian Rupiah'
    IDR = 'IDR'
    ISRAELI_NEW_SHEQEL = 'Israeli New Sheqel'
    ILS = 'ILS'
    MANX_POUND = 'Manx pound'
    IMP = 'IMP'
    INDIAN_RUPEE = 'Indian Rupee'
    INR = 'INR'
    IRAQI_DINAR = 'Iraqi Dinar'
    IQD = 'IQD'
    IRANIAN_RIAL = 'Iranian Rial'
    IRR = 'IRR'
    ICELANDIC_KRÓNA = 'Icelandic Króna'
    ISK = 'ISK'
    JERSEY_POUND = 'Jersey Pound'
    JEP = 'JEP'
    JAMAICAN_DOLLAR = 'Jamaican Dollar'
    JMD = 'JMD'
    JORDANIAN_DINAR = 'Jordanian Dinar'
    JOD = 'JOD'
    JAPANESE_YEN = 'Japanese Yen'
    JPY = 'JPY'
    KENYAN_SHILLING = 'Kenyan Shilling'
    KES = 'KES'
    KYRGYSTANI_SOM = 'Kyrgystani Som'
    KGS = 'KGS'
    CAMBODIAN_RIEL = 'Cambodian Riel'
    KHR = 'KHR'
    COMORIAN_FRANC = 'Comorian Franc'
    KMF = 'KMF'
    NORTH_KOREAN_WON = 'North Korean Won'
    KPW = 'KPW'
    SOUTH_KOREAN_WON = 'South Korean Won'
    KRW = 'KRW'
    KUWAITI_DINAR = 'Kuwaiti Dinar'
    KWD = 'KWD'
    CAYMAN_ISLANDS_DOLLAR = 'Cayman Islands Dollar'
    KYD = 'KYD'
    KAZAKHSTANI_TENGE = 'Kazakhstani Tenge'
    KZT = 'KZT'
    LAOTIAN_KIP = 'Laotian Kip'
    LAK = 'LAK'
    LEBANESE_POUND = 'Lebanese Pound'
    LBP = 'LBP'
    SRI_LANKAN_RUPEE = 'Sri Lankan Rupee'
    LKR = 'LKR'
    LIBERIAN_DOLLAR = 'Liberian Dollar'
    LRD = 'LRD'
    LESOTHO_LOTI = 'Lesotho Loti'
    LSL = 'LSL'
    LIBYAN_DINAR = 'Libyan Dinar'
    LYD = 'LYD'
    MOROCCAN_DIRHAM = 'Moroccan Dirham'
    MAD = 'MAD'
    MOLDOVAN_LEU = 'Moldovan Leu'
    MDL = 'MDL'
    MALAGASY_ARIARY = 'Malagasy Ariary'
    MGA = 'MGA'
    MACEDONIAN_DENAR = 'Macedonian Denar'
    MKD = 'MKD'
    MYANMA_KYAT = 'Myanma Kyat'
    MMK = 'MMK'
    MONGOLIAN_TUGRIK = 'Mongolian Tugrik'
    MNT = 'MNT'
    MACANESE_PATACA = 'Macanese Pataca'
    MOP = 'MOP'
    MAURITANIAN_OUGUIYA_(PRE-2018) = 'Mauritanian Ouguiya (pre-2018)'
    MRO = 'MRO'
    MAURITANIAN_OUGUIYA = 'Mauritanian Ouguiya'
    MRU = 'MRU'
    MALTESE_LIRA = 'Maltese Lira'
    MTL = 'MTL'
    MAURITIAN_RUPEE = 'Mauritian Rupee'
    MUR = 'MUR'
    MALDIVIAN_RUFIYAA = 'Maldivian Rufiyaa'
    MVR = 'MVR'
    MALAWIAN_KWACHA = 'Malawian Kwacha'
    MWK = 'MWK'
    MEXICAN_PESO = 'Mexican Peso'
    MXN = 'MXN'
    MALAYSIAN_RINGGIT = 'Malaysian Ringgit'
    MYR = 'MYR'
    MOZAMBICAN_METICAL = 'Mozambican Metical'
    MZN = 'MZN'
    NAMIBIAN_DOLLAR = 'Namibian Dollar'
    NAD = 'NAD'
    NIGERIAN_NAIRA = 'Nigerian Naira'
    NGN = 'NGN'
    NICARAGUAN_CÓRDOBA = 'Nicaraguan Córdoba'
    NIO = 'NIO'
    NORWEGIAN_KRONE = 'Norwegian Krone'
    NOK = 'NOK'
    NEPALESE_RUPEE = 'Nepalese Rupee'
    NPR = 'NPR'
    NEW_ZEALAND_DOLLAR = 'New Zealand Dollar'
    NZD = 'NZD'
    OMANI_RIAL = 'Omani Rial'
    OMR = 'OMR'
    PANAMANIAN_BALBOA = 'Panamanian Balboa'
    PAB = 'PAB'
    PERUVIAN_NUEVO_SOL = 'Peruvian Nuevo Sol'
    PEN = 'PEN'
    PAPUA_NEW_GUINEAN_KINA = 'Papua New Guinean Kina'
    PGK = 'PGK'
    PHILIPPINE_PESO = 'Philippine Peso'
    PHP = 'PHP'
    PAKISTANI_RUPEE = 'Pakistani Rupee'
    PKR = 'PKR'
    POLISH_ZLOTY = 'Polish Zloty'
    PLN = 'PLN'
    PARAGUAYAN_GUARANI = 'Paraguayan Guarani'
    PYG = 'PYG'
    QATARI_RIAL = 'Qatari Rial'
    QAR = 'QAR'
    ROMANIAN_LEU = 'Romanian Leu'
    RON = 'RON'
    SERBIAN_DINAR = 'Serbian Dinar'
    RSD = 'RSD'
    RUSSIAN_RUBLE = 'Russian Ruble'
    RUB = 'RUB'
    RWANDAN_FRANC = 'Rwandan Franc'
    RWF = 'RWF'
    SAUDI_RIYAL = 'Saudi Riyal'
    SAR = 'SAR'
    SOLOMON_ISLANDS_DOLLAR = 'Solomon Islands Dollar'
    SBD = 'SBD'
    SEYCHELLOIS_RUPEE = 'Seychellois Rupee'
    SCR = 'SCR'
    SUDANESE_POUND = 'Sudanese Pound'
    SDG = 'SDG'
    SWEDISH_KRONA = 'Swedish Krona'
    SEK = 'SEK'
    SINGAPORE_DOLLAR = 'Singapore Dollar'
    SGD = 'SGD'
    SAINT_HELENA_POUND = 'Saint Helena Pound'
    SHP = 'SHP'
    SIERRA_LEONEAN_LEONE = 'Sierra Leonean Leone'
    SLL = 'SLL'
    SOMALI_SHILLING = 'Somali Shilling'
    SOS = 'SOS'
    SURINAMESE_DOLLAR = 'Surinamese Dollar'
    SRD = 'SRD'
    SOUTH_SUDANESE_POUND = 'South Sudanese Pound'
    SSP = 'SSP'
    SÃO_TOMÉ_AND_PRÍNCIPE_DOBRA_(PRE-2018) = 'São Tomé and Príncipe Dobra (pre-2018)'
    STD = 'STD'
    SÃO_TOMÉ_AND_PRÍNCIPE_DOBRA = 'São Tomé and Príncipe Dobra'
    STN = 'STN'
    SALVADORAN_COLÓN = 'Salvadoran Colón'
    SVC = 'SVC'
    SYRIAN_POUND = 'Syrian Pound'
    SYP = 'SYP'
    SWAZI_LILANGENI = 'Swazi Lilangeni'
    SZL = 'SZL'
    THAI_BAHT = 'Thai Baht'
    THB = 'THB'
    TAJIKISTANI_SOMONI = 'Tajikistani Somoni'
    TJS = 'TJS'
    TURKMENISTANI_MANAT = 'Turkmenistani Manat'
    TMT = 'TMT'
    TUNISIAN_DINAR = 'Tunisian Dinar'
    TND = 'TND'
    TONGAN_PAʻANGA = 'Tongan Paʻanga'
    TOP = 'TOP'
    TURKISH_LIRA = 'Turkish Lira'
    TRY = 'TRY'
    TRINIDAD_AND_TOBAGO_DOLLAR = 'Trinidad and Tobago Dollar'
    TTD = 'TTD'
    NEW_TAIWAN_DOLLAR = 'New Taiwan Dollar'
    TWD = 'TWD'
    TANZANIAN_SHILLING = 'Tanzanian Shilling'
    TZS = 'TZS'
    UKRAINIAN_HRYVNIA = 'Ukrainian Hryvnia'
    UAH = 'UAH'
    UGANDAN_SHILLING = 'Ugandan Shilling'
    UGX = 'UGX'
    UNITED_STATES_DOLLAR = 'United States Dollar'
    USD = 'USD'
    URUGUAYAN_PESO = 'Uruguayan Peso'
    UYU = 'UYU'
    UZBEKISTAN_SOM = 'Uzbekistan Som'
    UZS = 'UZS'
    VENEZUELAN_BOLÍVAR_FUERTE = 'Venezuelan Bolívar Fuerte'
    VEF = 'VEF'
    VIETNAMESE_DONG = 'Vietnamese Dong'
    VND = 'VND'
    VANUATU_VATU = 'Vanuatu Vatu'
    VUV = 'VUV'
    SAMOAN_TALA = 'Samoan Tala'
    WST = 'WST'
    CFA_FRANC_BEAC = 'CFA Franc BEAC'
    XAF = 'XAF'
    SILVER_(TROY_OUNCE) = 'Silver (troy ounce)'
    XAG = 'XAG'
    GOLD_(TROY_OUNCE) = 'Gold (troy ounce)'
    XAU = 'XAU'
    EAST_CARIBBEAN_DOLLAR = 'East Caribbean Dollar'
    XCD = 'XCD'
    SPECIAL_DRAWING_RIGHTS = 'Special Drawing Rights'
    XDR = 'XDR'
    CFA_FRANC_BCEAO = 'CFA Franc BCEAO'
    XOF = 'XOF'
    PALLADIUM_OUNCE = 'Palladium Ounce'
    XPD = 'XPD'
    CFP_FRANC = 'CFP Franc'
    XPF = 'XPF'
    PLATINUM_OUNCE = 'Platinum Ounce'
    XPT = 'XPT'
    YEMENI_RIAL = 'Yemeni Rial'
    YER = 'YER'
    SOUTH_AFRICAN_RAND = 'South African Rand'
    ZAR = 'ZAR'
    ZAMBIAN_KWACHA_(PRE-2013) = 'Zambian Kwacha (pre-2013)'
    ZMK = 'ZMK'
    ZAMBIAN_KWACHA = 'Zambian Kwacha'
    ZMW = 'ZMW'
    

class VariantUniquenessEnum(str):
    DISABLE_ANY_UNIQUENESS_CHECK_FOR_VARIANT_ATTRIBUTE_SETS = 'Disable any uniqueness check for variant attribute sets'
    DISABLED_UNIQUE_CHECKING = 'DISABLED_UNIQUE_CHECKING'
    CHECK_FOR_DUPLICATED_VARIANT_ATTRIBUTE_SETS_WITHIN_A_SELLER,_DUPLICATED_VARIANTS_MAY_STILL_EXIST_GLOBALLY_(PRE-PRODUCT) = 'Check for duplicated variant attribute sets within a seller, duplicated variants may still exist globally (pre-product)'
    UNIQUE_PER_SELLER = 'UNIQUE_PER_SELLER'
    CHECK_FOR_DUPLICATED_VARIANT_ATTRIBUTE_SETS_GLOBALLY_(PER-PRODUCT),_DUPLICATED_VARIANTS_MAY_NOT_EXIST_IN_THE_SYSTEM = 'Check for duplicated variant attribute sets globally (per-product), duplicated variants may not exist in the system'
    UNIQUE_PER_MARKETPLACE = 'UNIQUE_PER_MARKETPLACE'
    

class RevenueAccrualStrategyEnum(str):
    ACCRUE_REVENUE_TO_THE_MARKETPLACE_AND_SELLERS_WHEN_ORDERS_ARE_FULFILLED. = 'Accrue revenue to the marketplace and sellers when orders are fulfilled.'
    FULFILLMENT = 'FULFILLMENT'
    ACCRUE_ALL_REVENUE_TO_THE_MARKETPLACE_AND_SELLERS_WHEN_ORDERS_ARE_PLACED. = 'Accrue all revenue to the marketplace and sellers when orders are placed.'
    ORDER_PLACEMENT = 'ORDER_PLACEMENT'
    

class AvailableShippingStrategyEnum(str):
    AVAILABLE_SHIPPING_METHODS_PER_SELLER_ARE_CALCULATED_USING_ONLY_THE_LINE_TOTALS_FOR_THE_SELLER. = 'Available shipping methods per seller are calculated using only the line totals for the seller.'
    SELLER_LINES = 'SELLER_LINES'
    AVAILABLE_SHIPPING_METHODS_PER_SELLER_ARE_CALCULATED_USING_EVERY_LINE_TOTAL,_NOT_JUST_THE_SELLERS'_LINES. = 'Available shipping methods per seller are calculated using every line total, not just the sellers' lines.'
    MARKETPLACE_LINES = 'MARKETPLACE_LINES'
    

class MarketplaceConfigurationAttributeTemplateStrategy(str):
    ASSIGNED_ATTRIBUTES_MAY_ONLY_COME_FROM_TEMPLATES_(PRODUCTTYPE_FOR_PIM-SPECIFIC_ATTRIBUTE_USAGE_OR_CUSTOMFIELDTEMPLATE_FOR_CUSTOM_FIELD_ATTRIBUTE_USAGE),_NO_NON-TEMPLATED_ATTRIBUTE_ASSIGNMENT_IS_ALLOWED = 'Assigned attributes may only come from templates (ProductType for PIM-specific attribute usage or CustomFieldTemplate for custom field attribute usage), no non-templated attribute assignment is allowed'
    STRICT = 'STRICT'
    ASSIGNED_ATTRIBUTES_MAY_COME_FROM_BOTH_ATTRIBUTE_TEMPLATES_AND_NON-TEMPLATED_ATTRIBUTE_ASSIGNMENTS = 'Assigned attributes may come from BOTH attribute templates and non-templated attribute assignments'
    FLEXIBLE = 'FLEXIBLE'
    

class FulfillmentModelEnum(str):
    FULFILLED_BY_MARKETPLACE = 'Fulfilled by marketplace'
    FULFILLED_BY_MARKETPLACE = 'FULFILLED_BY_MARKETPLACE'
    FULFILLED_BY_SELLER = 'Fulfilled by seller'
    FULFILLED_BY_SELLER = 'FULFILLED_BY_SELLER'
    HYBRID = 'Hybrid'
    HYBRID = 'HYBRID'
    

class EmailEventMessageType(str):
    ACCOUNT_CONFIRMATION = 'Account Confirmation'
    ACCOUNT_CONFIRMATION = 'ACCOUNT_CONFIRMATION'
    ACCOUNT_PASSWORD_RESET = 'Account Password Reset'
    ACCOUNT_PASSWORD_RESET = 'ACCOUNT_PASSWORD_RESET'
    ACCOUNT_CHANGE_EMAIL_REQUEST = 'Account Change Email Request'
    ACCOUNT_CHANGE_EMAIL_REQUEST = 'ACCOUNT_CHANGE_EMAIL_REQUEST'
    ACCOUNT_CHANGE_EMAIL_CONFIRM = 'Account Change Email Confirm'
    ACCOUNT_CHANGE_EMAIL_CONFIRM = 'ACCOUNT_CHANGE_EMAIL_CONFIRM'
    ACCOUNT_DELETE = 'Account Delete'
    ACCOUNT_DELETE = 'ACCOUNT_DELETE'
    ACCOUNT_SET_CUSTOMER_PASSWORD = 'Account Set Customer Password'
    ACCOUNT_SET_CUSTOMER_PASSWORD = 'ACCOUNT_SET_CUSTOMER_PASSWORD'
    INVOICE_READY = 'Invoice Ready'
    INVOICE_READY = 'INVOICE_READY'
    ORDER_CONFIRMATION = 'Order Confirmation'
    ORDER_CONFIRMATION = 'ORDER_CONFIRMATION'
    ORDER_FULFILLMENT_CONFIRMATION = 'Order Fulfillment Confirmation'
    ORDER_FULFILLMENT_CONFIRMATION = 'ORDER_FULFILLMENT_CONFIRMATION'
    ORDER_FULFILLMENT_DENIED = 'Order Fulfillment Denied'
    ORDER_FULFILLMENT_DENIED = 'ORDER_FULFILLMENT_DENIED'
    ORDER_FULFILLMENT_UPDATE = 'Order Fulfillment Update'
    ORDER_FULFILLMENT_UPDATE = 'ORDER_FULFILLMENT_UPDATE'
    ORDER_CANCELED = 'Order Canceled'
    ORDER_CANCELED = 'ORDER_CANCELED'
    PARTIAL_ORDER_CANCEL = 'Partial Order Cancel'
    PARTIAL_ORDER_CANCEL = 'PARTIAL_ORDER_CANCEL'
    ORDER_REFUND_CONFIRMATION = 'Order Refund Confirmation'
    ORDER_REFUND_CONFIRMATION = 'ORDER_REFUND_CONFIRMATION'
    PENDING_QUOTE = 'Pending Quote'
    PENDING_QUOTE = 'PENDING_QUOTE'
    ACCOUNT_SET_STAFF_PASSWORD = 'Account Set Staff Password'
    ACCOUNT_SET_STAFF_PASSWORD = 'ACCOUNT_SET_STAFF_PASSWORD'
    CSV_EXPORT_PRODUCTS_SUCCESS = 'Csv Export Products Success'
    CSV_EXPORT_PRODUCTS_SUCCESS = 'CSV_EXPORT_PRODUCTS_SUCCESS'
    CSV_EXPORT_FAILED = 'Csv Export Failed'
    CSV_EXPORT_FAILED = 'CSV_EXPORT_FAILED'
    STAFF_ORDER_CONFIRMATION = 'Staff Order Confirmation'
    STAFF_ORDER_CONFIRMATION = 'STAFF_ORDER_CONFIRMATION'
    ACCOUNT_STAFF_RESET_PASSWORD = 'Account Staff Reset Password'
    ACCOUNT_STAFF_RESET_PASSWORD = 'ACCOUNT_STAFF_RESET_PASSWORD'
    VENDOR_PAYOUT_CONFIRMATION = 'Vendor Payout Confirmation'
    VENDOR_PAYOUT_CONFIRMATION = 'VENDOR_PAYOUT_CONFIRMATION'
    PENDING_SELLER = 'Pending Seller'
    PENDING_SELLER = 'PENDING_SELLER'
    UPDATED_STATUS = 'Updated Status'
    UPDATED_STATUS = 'UPDATED_STATUS'
    SELLER_STATUS_PENDING = 'Seller Status Pending'
    SELLER_STATUS_PENDING = 'SELLER_STATUS_PENDING'
    SELLER_STATUS_APPROVED = 'Seller Status Approved'
    SELLER_STATUS_APPROVED = 'SELLER_STATUS_APPROVED'
    SELLER_STATUS_DECLINED = 'Seller Status Declined'
    SELLER_STATUS_DECLINED = 'SELLER_STATUS_DECLINED'
    SELLER_STATUS_PAUSED = 'Seller Status Paused'
    SELLER_STATUS_PAUSED = 'SELLER_STATUS_PAUSED'
    SELLER_AGREEMENT_ACCEPTED = 'Seller Agreement Accepted'
    SELLER_AGREEMENT_ACCEPTED = 'SELLER_AGREEMENT_ACCEPTED'
    SELLER_AGREEMENT_NOT_ACCEPTED = 'Seller Agreement Not Accepted'
    SELLER_AGREEMENT_NOT_ACCEPTED = 'SELLER_AGREEMENT_NOT_ACCEPTED'
    IMPORT_CATALOG_FAILED = 'Import Catalog Failed'
    IMPORT_CATALOG_FAILED = 'IMPORT_CATALOG_FAILED'
    IMPORT_CATALOG_SUCCESS = 'Import Catalog Success'
    IMPORT_CATALOG_SUCCESS = 'IMPORT_CATALOG_SUCCESS'
    ACCOUNT_ACTIVATE_REQUEST = 'Account Activate Request'
    ACCOUNT_ACTIVATE_REQUEST = 'ACCOUNT_ACTIVATE_REQUEST'
    ACCOUNT_ACTIVATED = 'Account Activated'
    ACCOUNT_ACTIVATED = 'ACCOUNT_ACTIVATED'
    ACCOUNT_DEACTIVATED = 'Account Deactivated'
    ACCOUNT_DEACTIVATED = 'ACCOUNT_DEACTIVATED'
    PENDING_ORDER = 'Pending Order'
    PENDING_ORDER = 'PENDING_ORDER'
    PENDING_CUSTOMER = 'Pending Customer'
    PENDING_CUSTOMER = 'PENDING_CUSTOMER'
    QUOTE_REQUESTED = 'Quote Requested'
    QUOTE_REQUESTED = 'QUOTE_REQUESTED'
    

class NotifyEventTypeEnum(str):
    ACCOUNT_CONFIRMATION = 'Account Confirmation'
    ACCOUNT_CONFIRMATION = 'ACCOUNT_CONFIRMATION'
    ACCOUNT_PASSWORD_RESET = 'Account Password Reset'
    ACCOUNT_PASSWORD_RESET = 'ACCOUNT_PASSWORD_RESET'
    ACCOUNT_CHANGE_EMAIL_REQUEST = 'Account Change Email Request'
    ACCOUNT_CHANGE_EMAIL_REQUEST = 'ACCOUNT_CHANGE_EMAIL_REQUEST'
    ACCOUNT_CHANGE_EMAIL_CONFIRM = 'Account Change Email Confirm'
    ACCOUNT_CHANGE_EMAIL_CONFIRM = 'ACCOUNT_CHANGE_EMAIL_CONFIRM'
    ACCOUNT_DELETE = 'Account Delete'
    ACCOUNT_DELETE = 'ACCOUNT_DELETE'
    ACCOUNT_SET_CUSTOMER_PASSWORD = 'Account Set Customer Password'
    ACCOUNT_SET_CUSTOMER_PASSWORD = 'ACCOUNT_SET_CUSTOMER_PASSWORD'
    INVOICE_READY = 'Invoice Ready'
    INVOICE_READY = 'INVOICE_READY'
    ORDER_CONFIRMATION = 'Order Confirmation'
    ORDER_CONFIRMATION = 'ORDER_CONFIRMATION'
    ORDER_FULFILLMENT_CONFIRMATION = 'Order Fulfillment Confirmation'
    ORDER_FULFILLMENT_CONFIRMATION = 'ORDER_FULFILLMENT_CONFIRMATION'
    ORDER_FULFILLMENT_DENIED = 'Order Fulfillment Denied'
    ORDER_FULFILLMENT_DENIED = 'ORDER_FULFILLMENT_DENIED'
    ORDER_FULFILLMENT_UPDATE = 'Order Fulfillment Update'
    ORDER_FULFILLMENT_UPDATE = 'ORDER_FULFILLMENT_UPDATE'
    ORDER_CANCELED = 'Order Canceled'
    ORDER_CANCELED = 'ORDER_CANCELED'
    PARTIAL_ORDER_CANCEL = 'Partial Order Cancel'
    PARTIAL_ORDER_CANCEL = 'PARTIAL_ORDER_CANCEL'
    ORDER_REFUND_CONFIRMATION = 'Order Refund Confirmation'
    ORDER_REFUND_CONFIRMATION = 'ORDER_REFUND_CONFIRMATION'
    PENDING_QUOTE = 'Pending Quote'
    PENDING_QUOTE = 'PENDING_QUOTE'
    ACCOUNT_SET_STAFF_PASSWORD = 'Account Set Staff Password'
    ACCOUNT_SET_STAFF_PASSWORD = 'ACCOUNT_SET_STAFF_PASSWORD'
    CSV_EXPORT_PRODUCTS_SUCCESS = 'Csv Export Products Success'
    CSV_EXPORT_PRODUCTS_SUCCESS = 'CSV_EXPORT_PRODUCTS_SUCCESS'
    CSV_EXPORT_FAILED = 'Csv Export Failed'
    CSV_EXPORT_FAILED = 'CSV_EXPORT_FAILED'
    STAFF_ORDER_CONFIRMATION = 'Staff Order Confirmation'
    STAFF_ORDER_CONFIRMATION = 'STAFF_ORDER_CONFIRMATION'
    ACCOUNT_STAFF_RESET_PASSWORD = 'Account Staff Reset Password'
    ACCOUNT_STAFF_RESET_PASSWORD = 'ACCOUNT_STAFF_RESET_PASSWORD'
    VENDOR_PAYOUT_CONFIRMATION = 'Vendor Payout Confirmation'
    VENDOR_PAYOUT_CONFIRMATION = 'VENDOR_PAYOUT_CONFIRMATION'
    PENDING_SELLER = 'Pending Seller'
    PENDING_SELLER = 'PENDING_SELLER'
    UPDATED_STATUS = 'Updated Status'
    UPDATED_STATUS = 'UPDATED_STATUS'
    SELLER_STATUS_PENDING = 'Seller Status Pending'
    SELLER_STATUS_PENDING = 'SELLER_STATUS_PENDING'
    SELLER_STATUS_APPROVED = 'Seller Status Approved'
    SELLER_STATUS_APPROVED = 'SELLER_STATUS_APPROVED'
    SELLER_STATUS_DECLINED = 'Seller Status Declined'
    SELLER_STATUS_DECLINED = 'SELLER_STATUS_DECLINED'
    SELLER_STATUS_PAUSED = 'Seller Status Paused'
    SELLER_STATUS_PAUSED = 'SELLER_STATUS_PAUSED'
    SELLER_AGREEMENT_ACCEPTED = 'Seller Agreement Accepted'
    SELLER_AGREEMENT_ACCEPTED = 'SELLER_AGREEMENT_ACCEPTED'
    SELLER_AGREEMENT_NOT_ACCEPTED = 'Seller Agreement Not Accepted'
    SELLER_AGREEMENT_NOT_ACCEPTED = 'SELLER_AGREEMENT_NOT_ACCEPTED'
    IMPORT_CATALOG_FAILED = 'Import Catalog Failed'
    IMPORT_CATALOG_FAILED = 'IMPORT_CATALOG_FAILED'
    IMPORT_CATALOG_SUCCESS = 'Import Catalog Success'
    IMPORT_CATALOG_SUCCESS = 'IMPORT_CATALOG_SUCCESS'
    ACCOUNT_ACTIVATE_REQUEST = 'Account Activate Request'
    ACCOUNT_ACTIVATE_REQUEST = 'ACCOUNT_ACTIVATE_REQUEST'
    ACCOUNT_ACTIVATED = 'Account Activated'
    ACCOUNT_ACTIVATED = 'ACCOUNT_ACTIVATED'
    ACCOUNT_DEACTIVATED = 'Account Deactivated'
    ACCOUNT_DEACTIVATED = 'ACCOUNT_DEACTIVATED'
    PENDING_ORDER = 'Pending Order'
    PENDING_ORDER = 'PENDING_ORDER'
    PENDING_CUSTOMER = 'Pending Customer'
    PENDING_CUSTOMER = 'PENDING_CUSTOMER'
    QUOTE_REQUESTED = 'Quote Requested'
    QUOTE_REQUESTED = 'QUOTE_REQUESTED'
    

class EmailEventSortField(str):
    SORT_RETURN_EMAIL_LOGS_BY_DATE. = 'Sort return email_logs by date.'
    DATE = 'DATE'
    

class InsightDimensionEnum(str):
    DAY = 'DAY'
    WEEK = 'WEEK'
    MONTH = 'MONTH'
    QUARTER = 'QUARTER'
    YEAR = 'YEAR'
    

class PerformancePerspective(str):
    TOP = 'TOP'
    WORST = 'WORST'
    

class JournalEntryTypeEnum(str):
    ADJUSTMENT = 'ADJUSTMENT'
    COMMISSION = 'COMMISSION'
    DISCOUNT = 'DISCOUNT'
    FEES = 'FEES'
    ORDER_ACCRUED = 'ORDER_ACCRUED'
    ORDER_CANCELLED = 'ORDER_CANCELLED'
    ORDER_DECLINE_FULFILLMENT = 'ORDER_DECLINE_FULFILLMENT'
    ORDER_PLACED = 'ORDER_PLACED'
    PAYMENT_CAPTURED = 'PAYMENT_CAPTURED'
    PAYOUT = 'PAYOUT'
    PAYOUT_ADJUSTMENT = 'PAYOUT_ADJUSTMENT'
    REFUND_COMMISSION = 'REFUND_COMMISSION'
    REFUND_ORDER = 'REFUND_ORDER'
    SHIPPING_ACCRUED = 'SHIPPING_ACCRUED'
    

class LedgerAccountTypeEnum(str):
    ASSET = 'ASSET'
    CONTRA_ASSET = 'CONTRA_ASSET'
    CONTRA_LIABILITY = 'CONTRA_LIABILITY'
    CONTRA_REVENUE = 'CONTRA_REVENUE'
    EXPENSE = 'EXPENSE'
    LIABILITY = 'LIABILITY'
    REVENUE = 'REVENUE'
    

class LedgerTypeEnum(str):
    CUSTOMER_RECEIVABLE = 'CUSTOMER_RECEIVABLE'
    DEFERRED_DISCOUNTS = 'DEFERRED_DISCOUNTS'
    DEFERRED_SALES_REVENUE = 'DEFERRED_SALES_REVENUE'
    DEFERRED_SHIPPING_REVENUE = 'DEFERRED_SHIPPING_REVENUE'
    FOREIGN_EXCHANGE = 'FOREIGN_EXCHANGE'
    FUNDS_PAYMENTS = 'FUNDS_PAYMENTS'
    GUEST_CUSTOMER_RECEIVABLE = 'GUEST_CUSTOMER_RECEIVABLE'
    MARKETPLACE_COMMISSION = 'MARKETPLACE_COMMISSION'
    MARKETPLACE_DISCOUNTS = 'MARKETPLACE_DISCOUNTS'
    MARKETPLACE_FEES = 'MARKETPLACE_FEES'
    REFUNDS = 'REFUNDS'
    SALES_TAX = 'SALES_TAX'
    SELLER_DISCOUNTS = 'SELLER_DISCOUNTS'
    SELLER_PAYABLE = 'SELLER_PAYABLE'
    SELLER_PAYOUT_DISBURSEMENT = 'SELLER_PAYOUT_DISBURSEMENT'
    

class JournalEntrySortField(str):
    SORT_JOURNAL_ENTRIES_BY_DATE. = 'Sort journal entries by date.'
    DATE = 'DATE'
    SORT_JOURNAL_ENTRIES_BY_TYPE. = 'Sort journal entries by type.'
    TYPE = 'TYPE'
    

class LedgerSortField(str):
    SORT_LEDGERS_BY_BALANCE. = 'Sort ledgers by balance.'
    BALANCE = 'BALANCE'
    SORT_LEDGERS_BY_TYPE. = 'Sort ledgers by type.'
    TYPE = 'TYPE'
    

class DiscountStatusEnum(str):
    ACTIVE = 'ACTIVE'
    EXPIRED = 'EXPIRED'
    SCHEDULED = 'SCHEDULED'
    

class SaleSortField(str):
    SORT_SALES_BY_NAME. = 'Sort sales by name.'
    NAME = 'NAME'
    SORT_SALES_BY_START_DATE. = 'Sort sales by start date.'
    START_DATE = 'START_DATE'
    SORT_SALES_BY_END_DATE. = 'Sort sales by end date.'
    END_DATE = 'END_DATE'
    SORT_SALES_BY_VALUE. = 'Sort sales by value.'
    VALUE = 'VALUE'
    SORT_SALES_BY_TYPE. = 'Sort sales by type.'
    TYPE = 'TYPE'
    

class VoucherDiscountType(str):
    FIXED = 'FIXED'
    PERCENTAGE = 'PERCENTAGE'
    SHIPPING = 'SHIPPING'
    

class VoucherSortField(str):
    SORT_VOUCHERS_BY_CODE. = 'Sort vouchers by code.'
    CODE = 'CODE'
    SORT_VOUCHERS_BY_START_DATE. = 'Sort vouchers by start date.'
    START_DATE = 'START_DATE'
    SORT_VOUCHERS_BY_END_DATE. = 'Sort vouchers by end date.'
    END_DATE = 'END_DATE'
    SORT_VOUCHERS_BY_VALUE. = 'Sort vouchers by value.'
    VALUE = 'VALUE'
    SORT_VOUCHERS_BY_TYPE. = 'Sort vouchers by type.'
    TYPE = 'TYPE'
    SORT_VOUCHERS_BY_USAGE_LIMIT. = 'Sort vouchers by usage limit.'
    USAGE_LIMIT = 'USAGE_LIMIT'
    SORT_VOUCHERS_BY_MINIMUM_SPENT_AMOUNT. = 'Sort vouchers by minimum spent amount.'
    MINIMUM_SPENT_AMOUNT = 'MINIMUM_SPENT_AMOUNT'
    

class ExportEventsEnum(str):
    DATA_EXPORT_WAS_STARTED. = 'Data export was started.'
    EXPORT_PENDING = 'EXPORT_PENDING'
    DATA_EXPORT_WAS_COMPLETED_SUCCESSFULLY. = 'Data export was completed successfully.'
    EXPORT_SUCCESS = 'EXPORT_SUCCESS'
    DATA_EXPORT_FAILED. = 'Data export failed.'
    EXPORT_FAILED = 'EXPORT_FAILED'
    EXPORT_FILE_WAS_DELETED. = 'Export file was deleted.'
    EXPORT_DELETED = 'EXPORT_DELETED'
    EMAIL_WITH_LINK_TO_DOWNLOAD_FILE_WAS_SENT_TO_THE_CUSTOMER. = 'Email with link to download file was sent to the customer.'
    EXPORTED_FILE_SENT = 'EXPORTED_FILE_SENT'
    EMAIL_WITH_INFO_THAT_EXPORT_FAILED_WAS_SENT_TO_THE_CUSTOMER. = 'Email with info that export failed was sent to the customer.'
    EXPORT_FAILED_INFO_SENT = 'EXPORT_FAILED_INFO_SENT'
    

class ExportFileSortField(str):
    SORT_EXPORT_FILE_BY_STATUS. = 'Sort export file by status.'
    STATUS = 'STATUS'
    SORT_EXPORT_FILE_BY_CREATED_AT. = 'Sort export file by created at.'
    CREATED_AT = 'CREATED_AT'
    SORT_EXPORT_FILE_BY_UPDATED_AT. = 'Sort export file by updated at.'
    UPDATED_AT = 'UPDATED_AT'
    

class AttributeSortField(str):
    SORT_ATTRIBUTES_BY_NAME = 'Sort attributes by name'
    NAME = 'NAME'
    SORT_ATTRIBUTES_BY_SLUG = 'Sort attributes by slug'
    SLUG = 'SLUG'
    SORT_ATTRIBUTES_BY_EXTERNAL_ID = 'Sort attributes by external ID'
    EXTERNAL_ID = 'EXTERNAL_ID'
    SORT_ATTRIBUTES_BY_EXTERNAL_SOURCE = 'Sort attributes by external source'
    EXTERNAL_SOURCE = 'EXTERNAL_SOURCE'
    SORT_ATTRIBUTES_BY_THE_VALUE_REQUIRED_FLAG = 'Sort attributes by the value required flag'
    VALUE_REQUIRED = 'VALUE_REQUIRED'
    SORT_ATTRIBUTES_BY_THE_VARIANT_ONLY_FLAG = 'Sort attributes by the variant only flag'
    IS_VARIANT_ONLY = 'IS_VARIANT_ONLY'
    SORT_ATTRIBUTES_BY_VISIBILITY_IN_THE_STOREFRONT = 'Sort attributes by visibility in the storefront'
    VISIBLE_IN_STOREFRONT = 'VISIBLE_IN_STOREFRONT'
    SORT_ATTRIBUTES_BY_THE_FILTERABLE_IN_STOREFRONT_FLAG = 'Sort attributes by the filterable in storefront flag'
    FILTERABLE_IN_STOREFRONT = 'FILTERABLE_IN_STOREFRONT'
    SORT_ATTRIBUTES_BY_THE_FILTERABLE_IN_DASHBOARD_FLAG = 'Sort attributes by the filterable in dashboard flag'
    FILTERABLE_IN_DASHBOARD = 'FILTERABLE_IN_DASHBOARD'
    SORT_ATTRIBUTES_BY_THEIR_POSITION_IN_STOREFRONT = 'Sort attributes by their position in storefront'
    STOREFRONT_SEARCH_POSITION = 'STOREFRONT_SEARCH_POSITION'
    SORT_ATTRIBUTES_BASED_ON_WHETHER_THEY_CAN_BE_DISPLAYED_OR_NOT_IN_A_PRODUCT_GRID. = 'Sort attributes based on whether they can be displayed or not in a product grid.'
    AVAILABLE_IN_GRID = 'AVAILABLE_IN_GRID'
    

class CustomFieldTemplateEnum(str):
    USER = 'USER'
    PRODUCT = 'PRODUCT'
    VARIANT = 'VARIANT'
    CATEGORY = 'CATEGORY'
    COLLECTION = 'COLLECTION'
    FULFILLMENT = 'FULFILLMENT'
    

class AppSortField(str):
    SORT_APPS_BY_NAME. = 'Sort apps by name.'
    NAME = 'NAME'
    SORT_APPS_BY_CREATION_DATE. = 'Sort apps by creation date.'
    CREATION_DATE = 'CREATION_DATE'
    

class AgreementSortField(str):
    SORT_AGREEMENTS_BY_TITLE. = 'Sort agreements by title.'
    TITLE = 'TITLE'
    SORT_AGREEMENTS_BY_SLUG. = 'Sort agreements by slug.'
    SLUG = 'SLUG'
    SORT_AGREEMENTS_BY_VISIBILITY. = 'Sort agreements by visibility.'
    VISIBILITY = 'VISIBILITY'
    SORT_AGREEMENTS_BY_CREATION_DATE. = 'Sort agreements by creation date.'
    CREATION_DATE = 'CREATION_DATE'
    SORT_AGREEMENTS_BY_PUBLICATION_DATE. = 'Sort agreements by publication date.'
    PUBLICATION_DATE = 'PUBLICATION_DATE'
    

class PermissionGroupSortField(str):
    SORT_PERMISSION_GROUP_ACCOUNTS_BY_NAME. = 'Sort permission group accounts by name.'
    NAME = 'NAME'
    

class StaffMemberStatus(str):
    ACTIVE = 'ACTIVE'
    DEACTIVATED = 'DEACTIVATED'
    

class NotificationErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    INVALID = 'INVALID'
    

class TenantErrorCode(str):
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    NOT_ALLOWED = 'NOT_ALLOWED'
    

class DocumentErrorCode(str):
    REQUIRED = 'REQUIRED'
    NOT_READY = 'NOT_READY'
    URL_NOT_SET = 'URL_NOT_SET'
    EMAIL_NOT_SET = 'EMAIL_NOT_SET'
    NUMBER_NOT_SET = 'NUMBER_NOT_SET'
    INVALID_STATUS = 'INVALID_STATUS'
    NOT_FOUND = 'NOT_FOUND'
    INVALID = 'INVALID'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    UNSUPPORTED_FILE_TYPE = 'UNSUPPORTED_FILE_TYPE'
    FILE_TOO_LARGE = 'FILE_TOO_LARGE'
    

class NauticalConfigurationErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    

class MarketplaceConfigurationErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    

class AttributeTemplateStrategyEnum(str):
    ASSIGNED_ATTRIBUTES_MAY_ONLY_COME_FROM_TEMPLATES_(PRODUCTTYPE_FOR_PIM-SPECIFIC_ATTRIBUTE_USAGE_OR_CUSTOMFIELDTEMPLATE_FOR_CUSTOM_FIELD_ATTRIBUTE_USAGE),_NO_NON-TEMPLATED_ATTRIBUTE_ASSIGNMENT_IS_ALLOWED = 'Assigned attributes may only come from templates (ProductType for PIM-specific attribute usage or CustomFieldTemplate for custom field attribute usage), no non-templated attribute assignment is allowed'
    STRICT = 'STRICT'
    ASSIGNED_ATTRIBUTES_MAY_COME_FROM_BOTH_ATTRIBUTE_TEMPLATES_AND_NON-TEMPLATED_ATTRIBUTE_ASSIGNMENTS = 'Assigned attributes may come from BOTH attribute templates and non-templated attribute assignments'
    FLEXIBLE = 'FLEXIBLE'
    

class PayoutErrorCode(str):
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    NOT_FOUND_VALID_ORDERS = 'NOT_FOUND_VALID_ORDERS'
    

class WishlistErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    FORBIDDEN = 'FORBIDDEN'
    

class ProductErrorCode(str):
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    ATTRIBUTE_ALREADY_ASSIGNED = 'ATTRIBUTE_ALREADY_ASSIGNED'
    ATTRIBUTE_CANNOT_BE_ASSIGNED = 'ATTRIBUTE_CANNOT_BE_ASSIGNED'
    ATTRIBUTE_VARIANTS_DISABLED = 'ATTRIBUTE_VARIANTS_DISABLED'
    DUPLICATED_INPUT_ITEM = 'DUPLICATED_INPUT_ITEM'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    INVALID_PHONE = 'INVALID_PHONE'
    NOT_PRODUCTS_IMAGE = 'NOT_PRODUCTS_IMAGE'
    NOT_PRODUCTS_VARIANT = 'NOT_PRODUCTS_VARIANT'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    VARIANT_NO_DIGITAL_CONTENT = 'VARIANT_NO_DIGITAL_CONTENT'
    VARIANT_IN_ACTIVE_ORDER = 'VARIANT_IN_ACTIVE_ORDER'
    CATEGORY_CANNOT_BE_ASSIGNED = 'CATEGORY_CANNOT_BE_ASSIGNED'
    CATEGORY_CANNOT_BE_DELETED = 'CATEGORY_CANNOT_BE_DELETED'
    COLLECTION_CANNOT_BE_CHANGED = 'COLLECTION_CANNOT_BE_CHANGED'
    COLLECTION_ALLOWED_FOR_PRODUCTS_ONLY = 'COLLECTION_ALLOWED_FOR_PRODUCTS_ONLY'
    COLLECTION_ALLOWED_FOR_VARIANTS_ONLY = 'COLLECTION_ALLOWED_FOR_VARIANTS_ONLY'
    INVENTORY_FIELD_CANNOT_BE_EDITED = 'INVENTORY_FIELD_CANNOT_BE_EDITED'
    

class AgreementErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    EXISTING_VENDOR_AGREEMENTS = 'EXISTING_VENDOR_AGREEMENTS'
    INPUT_INVALID = 'INPUT_INVALID'
    

class AgreementGranularCommissionType(str):
    CATEGORY = 'CATEGORY'
    

class SellerErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    INVALID_PHONE = 'INVALID_PHONE'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    JWT_SIGNATURE_EXPIRED = 'JWT_SIGNATURE_EXPIRED'
    JWT_INVALID_TOKEN = 'JWT_INVALID_TOKEN'
    JWT_DECODE_ERROR = 'JWT_DECODE_ERROR'
    JWT_MISSING_TOKEN = 'JWT_MISSING_TOKEN'
    JWT_INVALID_CSRF_TOKEN = 'JWT_INVALID_CSRF_TOKEN'
    

class SellerStatusEnum(str):
    APPLYING = 'Applying'
    APPLYING = 'APPLYING'
    PENDING = 'Pending'
    PENDING = 'PENDING'
    APPROVED = 'Approved'
    APPROVED = 'APPROVED'
    DECLINED = 'Declined'
    DECLINED = 'DECLINED'
    PAUSED = 'Paused'
    PAUSED = 'PAUSED'
    SUSPENDED = 'Suspended'
    SUSPENDED = 'SUSPENDED'
    BANNED = 'Banned'
    BANNED = 'BANNED'
    DEACTIVATED = 'Deactivated'
    DEACTIVATED = 'DEACTIVATED'
    

class AddressTypeEnum(str):
    BILLING = 'Billing'
    BILLING = 'BILLING'
    SHIPPING = 'Shipping'
    SHIPPING = 'SHIPPING'
    

class SellerOnboardingChecklistErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    

class WebhookErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    

class WarehouseErrorCode(str):
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    DUPLICATED_INPUT_ITEM = 'DUPLICATED_INPUT_ITEM'
    

class ShopErrorCode(str):
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    CANNOT_FETCH_TAX_RATES = 'CANNOT_FETCH_TAX_RATES'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    NOT_ALLOWED = 'NOT_ALLOWED'
    STALE_DATA = 'STALE_DATA'
    

class ShippingErrorCode(str):
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    MAX_LESS_THAN_MIN = 'MAX_LESS_THAN_MIN'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    DUPLICATED_INPUT_ITEM = 'DUPLICATED_INPUT_ITEM'
    

class RefundErrorCode(str):
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    NOT_ALLOWED = 'NOT_ALLOWED'
    INVALID_STATUS = 'INVALID_STATUS'
    INVALID_QUANTITY = 'INVALID_QUANTITY'
    DUPLICATED_INPUT_ITEM = 'DUPLICATED_INPUT_ITEM'
    INVALID_CHARGED_TO = 'INVALID_CHARGED_TO'
    

class PriceBookErrorCode(str):
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    NOT_ALLOWED = 'NOT_ALLOWED'
    

class PriceBookValueTypeEnum(str):
    OVERRIDE = 'Override'
    OVERRIDE = 'OVERRIDE'
    ADJUST_PERCENTAGE = 'Adjust Percentage'
    ADJUST_PERCENTAGE = 'ADJUST_PERCENTAGE'
    ADJUST_FIXED = 'Adjust Fixed'
    ADJUST_FIXED = 'ADJUST_FIXED'
    

class AttributeTypeEnum(str):
    PRODUCT = 'PRODUCT'
    VARIANT = 'VARIANT'
    CUSTOM = 'CUSTOM'
    

class StockErrorCode(str):
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    

class PaymentErrorCode(str):
    BILLING_ADDRESS_NOT_SET = 'BILLING_ADDRESS_NOT_SET'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    PARTIAL_PAYMENT_NOT_ALLOWED = 'PARTIAL_PAYMENT_NOT_ALLOWED'
    SHIPPING_ADDRESS_NOT_SET = 'SHIPPING_ADDRESS_NOT_SET'
    INVALID_SHIPPING_METHOD = 'INVALID_SHIPPING_METHOD'
    SHIPPING_METHOD_NOT_SET = 'SHIPPING_METHOD_NOT_SET'
    PAYMENT_ERROR = 'PAYMENT_ERROR'
    NOT_SUPPORTED_GATEWAY = 'NOT_SUPPORTED_GATEWAY'
    INSUFFICIENT_STOCK = 'INSUFFICIENT_STOCK'
    

class PageErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    

class OrderErrorCode(str):
    ATTRIBUTE_CANNOT_BE_ASSIGNED = 'ATTRIBUTE_CANNOT_BE_ASSIGNED'
    BILLING_ADDRESS_NOT_SET = 'BILLING_ADDRESS_NOT_SET'
    CANNOT_ADD_FEE = 'CANNOT_ADD_FEE'
    CANNOT_CANCEL_FULFILLMENT = 'CANNOT_CANCEL_FULFILLMENT'
    CANNOT_RETURN_FULFILLMENT = 'CANNOT_RETURN_FULFILLMENT'
    CANNOT_UPDATE_FULFILLMENT = 'CANNOT_UPDATE_FULFILLMENT'
    CANNOT_DECLINE_FULFILLMENT = 'CANNOT_DECLINE_FULFILLMENT'
    CANNOT_CANCEL_ORDER = 'CANNOT_CANCEL_ORDER'
    CANNOT_FULFILL_ORDER = 'CANNOT_FULFILL_ORDER'
    CANNOT_DELETE = 'CANNOT_DELETE'
    CANNOT_REFUND = 'CANNOT_REFUND'
    CAPTURE_INACTIVE_PAYMENT = 'CAPTURE_INACTIVE_PAYMENT'
    NOT_EDITABLE = 'NOT_EDITABLE'
    FULFILL_ORDER_LINE = 'FULFILL_ORDER_LINE'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    INVALID_PHONE = 'INVALID_PHONE'
    PRODUCT_NOT_PUBLISHED = 'PRODUCT_NOT_PUBLISHED'
    PRODUCT_UNAVAILABLE_FOR_PURCHASE = 'PRODUCT_UNAVAILABLE_FOR_PURCHASE'
    NOT_FOUND = 'NOT_FOUND'
    ORDER_NO_SHIPPING_ADDRESS = 'ORDER_NO_SHIPPING_ADDRESS'
    PAYMENT_ERROR = 'PAYMENT_ERROR'
    PAYMENT_MISSING = 'PAYMENT_MISSING'
    PERMISSION_DENIED = 'PERMISSION_DENIED'
    PAYOUT_STATUS_CHANGE_NOT_ALLOWED = 'PAYOUT_STATUS_CHANGE_NOT_ALLOWED'
    QUOTE_PAYMENT_ERROR = 'QUOTE_PAYMENT_ERROR'
    REQUIRED = 'REQUIRED'
    SHIPPING_METHOD_NOT_APPLICABLE = 'SHIPPING_METHOD_NOT_APPLICABLE'
    SHIPPING_METHOD_REQUIRED = 'SHIPPING_METHOD_REQUIRED'
    TAX_ERROR = 'TAX_ERROR'
    UNIQUE = 'UNIQUE'
    VOID_INACTIVE_PAYMENT = 'VOID_INACTIVE_PAYMENT'
    ZERO_QUANTITY = 'ZERO_QUANTITY'
    INSUFFICIENT_STOCK = 'INSUFFICIENT_STOCK'
    DUPLICATED_INPUT_ITEM = 'DUPLICATED_INPUT_ITEM'
    PRICE_OVERRIDE_NOT_ALLOWED = 'PRICE_OVERRIDE_NOT_ALLOWED'
    VOUCHER_NOT_APPLICABLE = 'VOUCHER_NOT_APPLICABLE'
    

class DraftOrderInitialStatus(str):
    DRAFT = 'DRAFT'
    QUOTE = 'QUOTE'
    

class ImportEventsEnum(str):
    DATA_IMPORT_WAS_STARTED. = 'Data import was started.'
    IMPORT_PENDING = 'IMPORT_PENDING'
    DATA_IMPORT_WAS_COMPLETED_SUCCESSFULLY. = 'Data import was completed successfully.'
    IMPORT_SUCCESS = 'IMPORT_SUCCESS'
    IMPORT_FAILED = 'Import Failed'
    IMPORT_FAILED = 'IMPORT_FAILED'
    DATA_IMPORT_FAILED. = 'Data import failed.'
    IMPORT_DELETED = 'IMPORT_DELETED'
    IMPORT_FILE_WAS_DELETED. = 'Import file was deleted.'
    IMPORTED_FILE_SENT = 'IMPORTED_FILE_SENT'
    

class MetadataErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    

class MenuErrorCode(str):
    CANNOT_ASSIGN_NODE = 'CANNOT_ASSIGN_NODE'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    INVALID_MENU_ITEM = 'INVALID_MENU_ITEM'
    NO_MENU_ITEM_PROVIDED = 'NO_MENU_ITEM_PROVIDED'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    TOO_MANY_MENU_ITEMS = 'TOO_MANY_MENU_ITEMS'
    UNIQUE = 'UNIQUE'
    

class InvoiceErrorCode(str):
    REQUIRED = 'REQUIRED'
    NOT_READY = 'NOT_READY'
    URL_NOT_SET = 'URL_NOT_SET'
    EMAIL_NOT_SET = 'EMAIL_NOT_SET'
    NUMBER_NOT_SET = 'NUMBER_NOT_SET'
    NOT_FOUND = 'NOT_FOUND'
    INVALID_STATUS = 'INVALID_STATUS'
    NOT_ALLOWED = 'NOT_ALLOWED'
    

class PluginErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    PLUGIN_MISCONFIGURED = 'PLUGIN_MISCONFIGURED'
    NOT_FOUND = 'NOT_FOUND'
    NOT_ACTIVE = 'NOT_ACTIVE'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    NOT_ALLOWED = 'NOT_ALLOWED'
    

class FinancialErrorCode(str):
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    

class DiscountErrorCode(str):
    ALREADY_EXISTS = 'ALREADY_EXISTS'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    

class ExportErrorCode(str):
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    

class ExportScope(str):
    EXPORT_ALL_PRODUCTS. = 'Export all products.'
    ALL = 'ALL'
    EXPORT_PRODUCTS_WITH_GIVEN_IDS. = 'Export products with given ids.'
    IDS = 'IDS'
    EXPORT_THE_FILTERED_PRODUCTS. = 'Export the filtered products.'
    FILTER = 'FILTER'
    

class ProductFieldEnum(str):
    NAME = 'NAME'
    DESCRIPTION = 'DESCRIPTION'
    PRODUCT_TYPE = 'PRODUCT_TYPE'
    CATEGORY = 'CATEGORY'
    VISIBLE = 'VISIBLE'
    AVAILABLE_FOR_PURCHASE = 'AVAILABLE_FOR_PURCHASE'
    SEARCHABLE = 'SEARCHABLE'
    PRODUCT_WEIGHT = 'PRODUCT_WEIGHT'
    COLLECTIONS = 'COLLECTIONS'
    CHARGE_TAXES = 'CHARGE_TAXES'
    PRODUCT_IMAGES = 'PRODUCT_IMAGES'
    VARIANT_SKU = 'VARIANT_SKU'
    VARIANT_PRICE = 'VARIANT_PRICE'
    COST_PRICE = 'COST_PRICE'
    VARIANT_WEIGHT = 'VARIANT_WEIGHT'
    VARIANT_IMAGES = 'VARIANT_IMAGES'
    

class FileTypesEnum(str):
    PLAIN_CSV_FILE. = 'Plain CSV file.'
    CSV = 'CSV'
    EXCEL_XLSX_FILE. = 'Excel XLSX file.'
    XLSX = 'XLSX'
    

class ImportErrorCode(str):
    INVALID = 'INVALID'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    

class CheckoutErrorCode(str):
    BILLING_ADDRESS_NOT_SET = 'BILLING_ADDRESS_NOT_SET'
    CHECKOUT_NOT_FULLY_PAID = 'CHECKOUT_NOT_FULLY_PAID'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    PRODUCT_NOT_PUBLISHED = 'PRODUCT_NOT_PUBLISHED'
    PRODUCT_UNAVAILABLE_FOR_PURCHASE = 'PRODUCT_UNAVAILABLE_FOR_PURCHASE'
    INSUFFICIENT_STOCK = 'INSUFFICIENT_STOCK'
    INVALID = 'INVALID'
    INVALID_PHONE = 'INVALID_PHONE'
    INVALID_SHIPPING_METHOD = 'INVALID_SHIPPING_METHOD'
    LOGIN_REQUIRED_FOR_CHECKOUT = 'LOGIN_REQUIRED_FOR_CHECKOUT'
    NOT_FOUND = 'NOT_FOUND'
    PAYMENT_ERROR = 'PAYMENT_ERROR'
    QUANTITY_GREATER_THAN_LIMIT = 'QUANTITY_GREATER_THAN_LIMIT'
    ORDER_PRICE_LESS_THAN_LIMIT = 'ORDER_PRICE_LESS_THAN_LIMIT'
    REQUIRED = 'REQUIRED'
    SHIPPING_ADDRESS_NOT_SET = 'SHIPPING_ADDRESS_NOT_SET'
    SHIPPING_METHOD_NOT_APPLICABLE = 'SHIPPING_METHOD_NOT_APPLICABLE'
    SHIPPING_METHOD_NOT_SET = 'SHIPPING_METHOD_NOT_SET'
    SHIPPING_NOT_REQUIRED = 'SHIPPING_NOT_REQUIRED'
    TAX_ERROR = 'TAX_ERROR'
    UNIQUE = 'UNIQUE'
    VOUCHER_NOT_APPLICABLE = 'VOUCHER_NOT_APPLICABLE'
    ZERO_QUANTITY = 'ZERO_QUANTITY'
    PRICE_OVERRIDE_NOT_ALLOWED = 'PRICE_OVERRIDE_NOT_ALLOWED'
    DOES_NOT_EXIST = 'DOES_NOT_EXIST'
    

class AppErrorCode(str):
    FORBIDDEN = 'FORBIDDEN'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    INVALID_STATUS = 'INVALID_STATUS'
    INVALID_PERMISSION = 'INVALID_PERMISSION'
    INVALID_URL_FORMAT = 'INVALID_URL_FORMAT'
    INVALID_MANIFEST_FORMAT = 'INVALID_MANIFEST_FORMAT'
    MANIFEST_URL_CANT_CONNECT = 'MANIFEST_URL_CANT_CONNECT'
    NOT_FOUND = 'NOT_FOUND'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    OUT_OF_SCOPE_APP = 'OUT_OF_SCOPE_APP'
    OUT_OF_SCOPE_PERMISSION = 'OUT_OF_SCOPE_PERMISSION'
    

class OauthProviderSourceEnum(str):
    FIREBASE = 'FIREBASE'
    WORKOS = 'WORKOS'
    

class AccountErrorCode(str):
    ACTIVATE_OWN_ACCOUNT = 'ACTIVATE_OWN_ACCOUNT'
    ACTIVATE_SUPERUSER_ACCOUNT = 'ACTIVATE_SUPERUSER_ACCOUNT'
    ACCOUNT_NOT_ACTIVE = 'ACCOUNT_NOT_ACTIVE'
    ATTRIBUTE_CANNOT_BE_ASSIGNED = 'ATTRIBUTE_CANNOT_BE_ASSIGNED'
    DUPLICATED_INPUT_ITEM = 'DUPLICATED_INPUT_ITEM'
    DEACTIVATE_OWN_ACCOUNT = 'DEACTIVATE_OWN_ACCOUNT'
    DEACTIVATE_SUPERUSER_ACCOUNT = 'DEACTIVATE_SUPERUSER_ACCOUNT'
    DELETE_NON_STAFF_USER = 'DELETE_NON_STAFF_USER'
    DELETE_OWN_ACCOUNT = 'DELETE_OWN_ACCOUNT'
    DELETE_STAFF_ACCOUNT = 'DELETE_STAFF_ACCOUNT'
    DELETE_SUPERUSER_ACCOUNT = 'DELETE_SUPERUSER_ACCOUNT'
    GRAPHQL_ERROR = 'GRAPHQL_ERROR'
    INVALID = 'INVALID'
    INVALID_PHONE = 'INVALID_PHONE'
    INVALID_PASSWORD = 'INVALID_PASSWORD'
    LEFT_NOT_MANAGEABLE_PERMISSION = 'LEFT_NOT_MANAGEABLE_PERMISSION'
    MUST_CHOOSE_PERMISSION_GROUP = 'MUST_CHOOSE_PERMISSION_GROUP'
    INVALID_CREDENTIALS = 'INVALID_CREDENTIALS'
    NO_SELLER = 'NO_SELLER'
    NOT_FOUND = 'NOT_FOUND'
    OUT_OF_SCOPE_SERVICE_ACCOUNT = 'OUT_OF_SCOPE_SERVICE_ACCOUNT'
    OUT_OF_SCOPE_USER = 'OUT_OF_SCOPE_USER'
    OUT_OF_SCOPE_GROUP = 'OUT_OF_SCOPE_GROUP'
    OUT_OF_SCOPE_PERMISSION = 'OUT_OF_SCOPE_PERMISSION'
    PASSWORD_ENTIRELY_NUMERIC = 'PASSWORD_ENTIRELY_NUMERIC'
    PASSWORD_IDENTICAL = 'PASSWORD_IDENTICAL'
    PASSWORD_TOO_COMMON = 'PASSWORD_TOO_COMMON'
    PASSWORD_TOO_SHORT = 'PASSWORD_TOO_SHORT'
    PASSWORD_TOO_SIMILAR = 'PASSWORD_TOO_SIMILAR'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    JWT_SIGNATURE_EXPIRED = 'JWT_SIGNATURE_EXPIRED'
    JWT_INVALID_TOKEN = 'JWT_INVALID_TOKEN'
    JWT_DECODE_ERROR = 'JWT_DECODE_ERROR'
    JWT_MISSING_TOKEN = 'JWT_MISSING_TOKEN'
    JWT_INVALID_CSRF_TOKEN = 'JWT_INVALID_CSRF_TOKEN'
    

class SsoProviderType(str):
    GITHUBOAUTH = 'GitHubOAuth'
    GOOGLEOAUTH = 'GoogleOAuth'
    MICROSOFTOAUTH = 'MicrosoftOAuth'
    

class PermissionGroupErrorCode(str):
    ASSIGN_NON_STAFF_MEMBER = 'ASSIGN_NON_STAFF_MEMBER'
    DUPLICATED_INPUT_ITEM = 'DUPLICATED_INPUT_ITEM'
    CANNOT_REMOVE_FROM_LAST_GROUP = 'CANNOT_REMOVE_FROM_LAST_GROUP'
    LEFT_NOT_MANAGEABLE_PERMISSION = 'LEFT_NOT_MANAGEABLE_PERMISSION'
    OUT_OF_SCOPE_PERMISSION = 'OUT_OF_SCOPE_PERMISSION'
    OUT_OF_SCOPE_USER = 'OUT_OF_SCOPE_USER'
    REQUIRED = 'REQUIRED'
    UNIQUE = 'UNIQUE'
    

class PageInfo(BaseModel):
    hasNextPage: bool
    hasPreviousPage: bool
    startCursor: Optional[str]
    endCursor: Optional[str]

class Query(BaseModel):
    id: str
    content: str
    filter: Optional[StaffUserInput]
    sortBy: Optional[UserSortingInput]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    wishlistName: str
    webhookEvents: List[Optional[WebhookEvent]]
    eventType: WebhookSampleEventTypeEnum
    identifier: Optional[str]
    slug: Optional[str]
    shop: Shop
    analyticsId: Optional[str]
    customStorefrontDomain: Optional[CustomDomain]
    number: Optional[str]
    taxId: Optional[str]
    email: str
    seller: Optional[str]
    query: Optional[str]
    period: Optional[ReportingPeriod]
    allCategories: Optional[List[Optional[Category]]]
    level: Optional[int]
    microsite: Optional[str]
    nsn: Optional[str]
    priceBookId: str
    variantId: Optional[str]
    productId: Optional[str]
    productTypeId: str
    source: str
    availableImportSources: Optional[List[Optional[Plugin]]]
    taxExemptCodes: Optional[List[Optional[TaxExemptCode]]]
    page: Optional[int]
    search: Optional[str]
    gateway: str
    paymentInformation: StripeClientPaymentData
    getPayoutGateways: Optional[List[Optional[PaymentGateway]]]
    endDate: date
    payoutId: Optional[str]
    vendorType: Optional[str]
    vendorId: Optional[str]
    token: Optional[NauticalUUID]
    isMarketplace: bool
    startDate: date
    configurationName: str
    nauticalConfigurationList: Optional[List[Optional[NauticalConfiguration]]]
    name: Optional[str]
    marketplaceConfiguration: MarketplaceConfiguration
    currencies: List[Optional[NauticalCurrency]]
    countries: List[Optional[CountryDisplay]]
    searchData: str
    locationData: Optional[str]
    perspective: PerformancePerspective
    dimension: Optional[str]
    designerdatalist: List[Optional[DesignerDataType]]
    integrationEmbeddingToken: Optional[str]
    taxTypes: List[Optional[TaxType]]
    customFieldTemplates: List[Optional[CustomFieldTemplate]]
    contentType: Optional[CustomFieldTemplateEnum]
    appsInstallations: List[Optional[AppInstallation]]
    countryCode: CountryCode
    countryArea: Optional[str]
    city: Optional[str]
    cityArea: Optional[str]
    me: Optional[User]
    _service: _Service

class EmailTemplate(BaseModel):
    id: str
    title: str
    subject: str
    senderEmailAddress: Optional[str]
    content: Optional[str]
    defaultContent: Optional[str]
    renderedContent: Optional[str]
    description: Optional[str]
    isCustom: bool
    isActive: bool
    isEditable: bool
    createdAt: datetime
    updatedAt: datetime
    recipientType: RecipientTypeEnum
    eventType: EventTypeEnum

class EmailTemplatePreview(BaseModel):
    id: Optional[str]
    renderedContent: Optional[str]

class EmailTemplateCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[EmailTemplateCountableEdge]]
    totalCount: Optional[int]

class EmailTemplateCountableEdge(BaseModel):
    node: EmailTemplate
    cursor: str

class WishlistItemCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[WishlistItemCountableEdge]]
    totalCount: Optional[int]

class WishlistItemCountableEdge(BaseModel):
    node: WishlistItem
    cursor: str

class WishlistItem(BaseModel):
    id: str
    wishlist: Wishlist
    product: Optional[Product]
    variant: Optional[ProductVariant]
    note: Optional[str]
    expiryDate: Optional[datetime]
    quantity: int
    requestedPrice: Optional[Money]

class Wishlist(BaseModel):
    id: str
    createdAt: datetime
    name: str
    isDefault: bool
    user: Optional[User]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

class User(BaseModel):
    id: str
    lastLogin: Optional[datetime]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    externalId: Optional[str]
    externalSource: Optional[str]
    externalPayoutAccountId: Optional[str]
    externalPayoutSource: Optional[UserExternalPayoutSource]
    externalPayoutOnboardingUrl: Optional[str]
    companyName: str
    email: str
    firstName: str
    lastName: str
    isStaff: bool
    isActive: bool
    note: Optional[str]
    dateJoined: datetime
    lastStatusChangedAt: Optional[datetime]
    defaultShippingAddress: Optional[Address]
    defaultBillingAddress: Optional[Address]
    personalPhone: Optional[str]
    taxExemptCode: Optional[str]
    vatIdentificationNumber: Optional[str]
    addresses: List[Optional[Address]]
    checkout: Optional[Checkout]
    filter: Optional[CustomerNauticalOrderFilterInput]
    sortBy: Optional[OrderSortingInput]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    numOrders: Optional[int]
    userPermissions: List[Optional[UserPermission]]
    permissionGroups: List[Optional[Group]]
    editableGroups: List[Optional[Group]]
    size: Optional[int]
    events: List[Optional[CustomerEvent]]
    storedPaymentSources: List[Optional[PaymentSource]]
    seller: Optional[Seller]
    isAssignable: Optional[bool]
    documents: List[Optional[Document]]
    priceBook: Optional[PriceBook]
    dashboardEmbeddingToken: Optional[str]
    customFields: List[Optional[SelectedAttribute]]

class MetadataItem(BaseModel):
    key: str
    value: str

class Address(BaseModel):
    id: str
    firstName: str
    lastName: str
    companyName: str
    streetAddress1: str
    streetAddress2: str
    city: str
    cityArea: str
    postalCode: str
    country: CountryDisplay
    countryArea: str
    phone: Optional[str]
    isDefaultShippingAddress: Optional[bool]
    isDefaultBillingAddress: Optional[bool]

class CountryDisplay(BaseModel):
    code: str
    country: str
    requiredFields: Optional[List[Optional[str]]]
    allowedCountryAreas: Optional[List[Optional[str]]]
    detailedAllowedCountryAreas: List[Optional[CountryArea]]

class CountryArea(BaseModel):
    code: str
    name: str

class Checkout(BaseModel):
    created: datetime
    lastChange: datetime
    user: Optional[User]
    quantity: int
    billingAddress: Optional[Address]
    shippingAddress: Optional[Address]
    note: str
    currency: str
    discount: Optional[Money]
    discountName: Optional[str]
    translatedDiscountName: Optional[str]
    voucherCode: Optional[str]
    poNumbers: Optional[List[Optional[str]]]
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    availableMarketplaceShippingMethods: List[Optional[ShippingMethod]]
    availableShippingMethodsBySeller: List[Optional[MultiSellerShippingMethod]]
    applicableVolumeDiscounts: Optional[Money]
    applicableVolumeDiscountsBySeller: List[Optional[SellerVolumeDiscount]]
    availablePaymentGateways: List[Optional[PaymentGateway]]
    email: str
    isShippingRequired: bool
    lines: List[Optional[CheckoutLine]]
    shippingPrice: TaxedMoney
    subtotalPrice: TaxedMoney
    token: NauticalUUID
    totalPrice: TaxedMoney
    discountType: Optional[VoucherTypeEnum]
    shippingMethods: List[Optional[CheckoutSellerShipping]]
    shippingSaleDiscount: Money
    marketplaceShippingMethod: Optional[ShippingMethod]
    marketplaceShippingPrice: TaxedMoney

class Money(BaseModel):
    currency: str
    baseAmount: int

class ShippingMethod(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    name: str
    price: Optional[Money]
    minimumOrderPrice: Optional[Money]
    maximumOrderPrice: Optional[Money]
    minimumOrderWeight: Optional[Weight]
    maximumOrderWeight: Optional[Weight]
    type: Optional[ShippingMethodTypeEnum]
    requiresSecondaryAddress: Optional[bool]

class Weight(BaseModel):
    unit: WeightUnitsEnum
    value: float

class MultiSellerShippingMethod(BaseModel):
    seller: Optional[int]
    sellerId: str
    sellerName: str
    value: List[Optional[ShippingMethod]]

class SellerVolumeDiscount(BaseModel):
    seller: Optional[int]
    volumeDiscount: Optional[Money]

class PaymentGateway(BaseModel):
    name: str
    id: str
    config: List[Optional[GatewayConfigLine]]
    currencies: List[Optional[str]]

class GatewayConfigLine(BaseModel):
    field: str
    value: Optional[str]

class CheckoutLine(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    isLinePriceOverridden: bool
    unitPriceOverriddenNote: Optional[str]
    note: Optional[str]
    variant: ProductVariant
    quantity: int
    sale: Optional[Sale]
    totalPrice: TaxedMoney
    requiresShipping: Optional[bool]
    seller: Optional[SellerType]
    discountedUnitPrice: TaxedMoney
    originalUnitPrice: TaxedMoney

class ProductVariant(BaseModel):
    id: str
    createdAt: datetime
    updatedAt: datetime
    description: str
    descriptionHtml: str
    externalId: Optional[str]
    externalSource: Optional[str]
    seoTitle: Optional[str]
    seoDescription: Optional[str]
    sku: Optional[str]
    name: str
    nauticalStockNumber: str
    status: ProductVariantStatus
    subStatus: ProductVariantSubStatus
    currency: Optional[str]
    product: Product
    trackInventory: bool
    weight: Optional[Weight]
    seller: Optional[Seller]
    publishedAt: Optional[datetime]
    isPublished: bool
    overrideCurrency: bool
    requiresQuote: bool
    allowBackorders: Optional[bool]
    isPriceOverrideAllowed: bool
    isShippingRequired: bool
    isDigital: bool
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    price: Optional[Money]
    pricing: Optional[VariantPricingInfo]
    isVisible: bool
    size: Optional[VariantSize]
    attributes: List[Optional[SelectedAttribute]]
    customFields: List[Optional[SelectedAttribute]]
    costPrice: Optional[Money]
    margin: Optional[int]
    quantityOrdered: Optional[int]
    features: Optional[List[Optional[VariantFeature]]]
    images: Optional[List[Optional[ProductImage]]]
    availableImages: Optional[List[Optional[ProductImage]]]
    digitalContent: Optional[DigitalContent]
    countryCode: Optional[CountryCode]
    netRevenue: Optional[float]
    grossRevenue: Optional[float]
    sortOrderInCollection: Optional[int]
    documents: Optional[List[Optional[Document]]]
    stockEvents: Optional[List[Optional[StockEvent]]]
    sales: List[Optional[Sale]]
    vouchers: List[Optional[Voucher]]

class Product(BaseModel):
    id: Optional[str]
    publicationDate: Optional[date]
    description: str
    descriptionHtml: str
    externalId: Optional[str]
    externalSource: Optional[str]
    seller: Optional[Seller]
    mpn: Optional[str]
    brand: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    seoTitle: Optional[str]
    seoDescription: Optional[str]
    productType: Optional[ProductType]
    name: str
    slug: str
    category: Optional[Category]
    currency: str
    updatedAt: Optional[datetime]
    createdAt: datetime
    chargeTaxes: bool
    weight: Optional[Weight]
    availableForPurchase: Optional[date]
    visibleInListings: bool
    defaultVariant: Optional[ProductVariant]
    overridePrice: bool
    overrideCurrency: bool
    status: ProductStatus
    subStatus: ProductSubStatus
    isPriceOverrideAllowed: bool
    isShippingRequired: bool
    isDigital: bool
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    size: Optional[int]
    pricing: Optional[ProductPricingInfo]
    isAvailable: Optional[bool]
    minimalVariantPrice: Optional[Money]
    taxType: Optional[TaxType]
    attributes: List[Optional[SelectedAttribute]]
    customFields: List[Optional[SelectedAttribute]]
    purchaseCost: Optional[MoneyRange]
    margin: Optional[Margin]
    variants: Optional[List[Optional[ProductVariant]]]
    images: Optional[List[Optional[ProductImage]]]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    collections: Optional[List[Optional[Collection]]]
    isAvailableForPurchase: Optional[bool]
    sortOrder: Optional[int]
    isPublished: bool
    features: Optional[List[Optional[ProductFeature]]]
    locations: Optional[List[Optional[Location]]]
    originLocation: Optional[Location]
    destinationLocation: Optional[Location]
    primaryLocation: Optional[Location]
    warehousesStats: Optional[List[Optional[WarehouseStats]]]
    actions: Optional[List[Optional[ProductAction]]]
    documents: List[Optional[Document]]
    sales: List[Optional[Sale]]
    vouchers: List[Optional[Voucher]]
    sortPriorityWeight: Optional[Decimal]
    productStatusLogs: Optional[List[Optional[ProductStatusLog]]]

class Seller(BaseModel):
    id: str
    companyName: str
    slug: str
    size: Optional[int]
    status: SellerStatus
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    externalPayoutAccountId: Optional[str]
    externalPayoutSource: Optional[SellerExternalPayoutSource]
    externalPayoutOnboardingUrl: Optional[str]
    isMarketplaceSeller: bool
    identification: Optional[List[Optional[str]]]
    addresses: Optional[List[Optional[Address]]]
    defaultShippingAddress: Optional[Address]
    defaultBillingAddress: Optional[Address]
    owner: Optional[User]
    defaultCurrency: str
    fulfilledByMarketplace: bool
    checklists: Optional[List[Optional[SellerOnboardingChecklist]]]
    application: Optional[SellerApplication]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    agreement: Optional[Agreement]
    agreementAcknowledged: Optional[datetime]
    canUseInStorefront: Optional[bool]
    microsite: Optional[Microsite]
    pk: Optional[int]
    externalPayoutStatus: Optional[bool]
    externalPayoutSchedule: Optional[str]
    agreementDecisionReason: Optional[str]
    storeDescription: Optional[str]
    documents: Optional[List[Optional[Document]]]
    approvedDate: Optional[datetime]
    firstProductCreatedDate: Optional[datetime]
    firstOrderPlacedDate: Optional[datetime]
    created: datetime
    updated: datetime
    accountSetupTasksAreDone: Optional[bool]

class Image(BaseModel):
    url: str
    alt: Optional[str]

class ProductCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[ProductCountableEdge]]
    totalCount: Optional[int]

class ProductCountableEdge(BaseModel):
    node: Product
    cursor: str

class ProductVariantCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[ProductVariantCountableEdge]]
    totalCount: Optional[int]

class ProductVariantCountableEdge(BaseModel):
    node: ProductVariant
    cursor: str

class SellerUserTypeCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[SellerUserTypeCountableEdge]]
    totalCount: Optional[int]

class SellerUserTypeCountableEdge(BaseModel):
    node: SellerUserType
    cursor: str

class SellerUserType(BaseModel):
    id: str
    tenant: Tenant
    seller: Seller
    user: User
    isDefault: bool

class Tenant(BaseModel):
    id: str
    name: str
    isActive: bool

class SellerEventTypeCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[SellerEventTypeCountableEdge]]
    totalCount: Optional[int]

class SellerEventTypeCountableEdge(BaseModel):
    node: SellerEventType
    cursor: str

class SellerEventType(BaseModel):
    id: str
    date: Optional[datetime]
    type: Optional[SellerEventsEnum]
    user: Optional[User]
    parameters: Optional[str]
    status: Optional[str]
    message: Optional[str]
    seller: Optional[Seller]

class SellerOnboardingChecklist(BaseModel):
    id: str
    createdAt: datetime
    updatedAt: datetime
    tenant: Tenant
    seller: Seller
    position: int
    title: str
    description: str
    completeOn: Optional[SellerChecklistCompletionTriggersEnum]
    completedAt: Optional[datetime]

class SellerApplication(BaseModel):
    createdAt: datetime
    updatedAt: datetime
    checkpoint: SellerApplicationCheckpoint
    formData: str
    seller: Seller
    submittedAt: Optional[datetime]
    id: str

class VendorPayoutCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[VendorPayoutCountableEdge]]
    totalCount: Optional[int]

class VendorPayoutCountableEdge(BaseModel):
    node: VendorPayout
    cursor: str

class VendorPayout(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
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
    volumeDiscounts: Decimal
    commission: Decimal
    feeAmount: Decimal
    fees: Money
    payoutAmount: Decimal
    payable: Money
    included: bool
    status: VendorPayoutStatus
    statusMessage: Optional[str]
    adjustmentAmount: Decimal
    adjustment: Money
    refundAmount: Decimal
    refund: Money
    ledgerVersion: int
    eventTypes: Optional[List[Optional[VendorPayoutEventsEnum]]]
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    commissionMoney: Money
    discountsMoney: Money
    netSales: Money
    shippingMoney: Money
    subtotal: Money
    total: Money

class Payout(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    tenant: Tenant
    created: str
    updated: datetime
    startDate: Optional[date]
    endDate: str
    status: PayoutStatus
    name: Optional[str]
    currency: str
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    vendors: int
    netSales: Money
    discounts: Money
    shipping: Money
    commission: Money
    fees: Money
    refunds: Money
    adjustments: Money
    payout: Money

class VendorPayoutEvent(BaseModel):
    id: str
    parameters: str
    date: datetime
    createdAt: datetime
    updatedAt: datetime
    type: VendorPayoutEventsEnum
    user: Optional[User]
    message: Optional[str]

class OrderCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[OrderCountableEdge]]
    totalCount: Optional[int]

class OrderCountableEdge(BaseModel):
    node: Order
    cursor: str

class Order(BaseModel):
    id: str
    externalId: Optional[str]
    externalSource: Optional[str]
    orderSource: OrderOrderSource
    seller: Optional[Seller]
    created: datetime
    updated: Optional[datetime]
    status: OrderStatus
    subStatus: Optional[OrderSubStatus]
    user: Optional[User]
    languageCode: str
    trackingClientId: str
    billingAddress: Optional[Address]
    shippingAddress: Optional[Address]
    vatCode: str
    euInvoiceMessaging: Optional[str]
    vatIdentificationNumber: Optional[str]
    mpVatIdentificationNumber: Optional[str]
    currency: str
    shippingMethod: Optional[ShippingMethod]
    shippingMethodName: Optional[str]
    shippingPrice: Optional[TaxedMoney]
    isShippingPriceOverridden: bool
    token: str
    voucher: Optional[Voucher]
    discount: Optional[Money]
    discountName: Optional[str]
    translatedDiscountName: Optional[str]
    displayGrossPrices: bool
    customerNote: str
    weight: Optional[Weight]
    importedAt: Optional[datetime]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    fulfillments: List[Optional[Fulfillment]]
    fees: Optional[List[Optional[OrderFee]]]
    lines: List[Optional[OrderLine]]
    allowedSubStatuses: Optional[List[Optional[OrderSubStatusEnum]]]
    availableShippingMethods: Optional[List[Optional[ShippingMethod]]]
    invoices: Optional[List[Optional[Invoice]]]
    number: Optional[str]
    marketplaceOrderNumber: Optional[str]
    isPaid: Optional[bool]
    paymentStatus: PaymentChargeStatusEnum
    paymentStatusDisplay: str
    total: Optional[TaxedMoney]
    originalTotal: Optional[TaxedMoney]
    subtotal: Optional[TaxedMoney]
    statusDisplay: Optional[str]
    canFinalize: bool
    events: Optional[List[Optional[OrderEvent]]]
    userEmail: Optional[str]
    isShippingRequired: bool
    payoutStatus: Optional[PayoutStatusEnum]
    availablePayoutBalance: Optional[Money]
    sellerCommission: Optional[Money]
    volumeDiscount: Optional[TaxedMoney]
    validationStatus: Optional[List[Optional[ValidationStatus]]]
    isOnlySellerOnNauticalOrder: Optional[bool]
    marketplaceOrder: Optional[NauticalOrder]
    vendorPayout: Optional[VendorPayout]
    vendorPayouts: Optional[List[Optional[VendorPayout]]]

class TaxedMoney(BaseModel):
    currency: str
    gross: Money
    net: Money
    tax: Money

class Voucher(BaseModel):
    id: str
    type: VoucherTypeEnum
    name: Optional[str]
    code: str
    usageLimit: Optional[int]
    used: int
    startDate: datetime
    endDate: Optional[datetime]
    applyOncePerOrder: bool
    applyOncePerCustomer: bool
    discountValueType: DiscountValueTypeEnum
    discountValue: Decimal
    currency: str
    minSpent: Optional[Money]
    minCheckoutItemsQuantity: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    countries: List[Optional[CountryDisplay]]

class CategoryCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[CategoryCountableEdge]]
    totalCount: Optional[int]

class CategoryCountableEdge(BaseModel):
    node: Category
    cursor: str

class Category(BaseModel):
    id: str
    description: str
    descriptionHtml: str
    externalId: Optional[str]
    externalSource: Optional[str]
    seoTitle: Optional[str]
    seoDescription: Optional[str]
    name: str
    slug: str
    parent: Optional[Category]
    allowProductAssignment: bool
    level: int
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    filter: Optional[ProductFilterInput]
    sortBy: Optional[ProductOrder]
    size: Optional[int]
    trailingBreadcrumbs: Optional[List[Optional[Category]]]
    customFields: List[Optional[SelectedAttribute]]

class SelectedAttribute(BaseModel):
    attribute: Attribute
    values: List[Optional[AttributeValue]]
    templated: Optional[bool]

class Attribute(BaseModel):
    id: str
    externalId: Optional[str]
    externalSource: Optional[str]
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    inputType: AttributeInputTypeEnum
    name: str
    slug: str
    allProductTypes: List[Optional[ProductType]]
    values: List[Optional[AttributeValue]]
    valueRequired: bool
    visibleInStorefront: bool
    filterableInStorefront: bool
    filterableInDashboard: bool
    availableInGrid: bool
    storefrontSearchPosition: int
    createdBy: Optional[Seller]

class ProductTypeCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[ProductTypeCountableEdge]]
    totalCount: Optional[int]

class ProductTypeCountableEdge(BaseModel):
    node: ProductType
    cursor: str

class ProductType(BaseModel):
    id: str
    externalId: Optional[str]
    externalSource: Optional[str]
    name: str
    slug: str
    isShippingRequired: bool
    isDigital: bool
    weight: Optional[Weight]
    isPriceOverrideAllowed: bool
    createdBy: Optional[Seller]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    taxType: Optional[TaxType]
    variantAttributes: List[Optional[Attribute]]
    hasVariants: Optional[bool]
    productAttributes: List[Optional[Attribute]]
    filter: Optional[AttributeFilterInput]
    productFeatures: List[Optional[ProductTypeProductFeature]]
    variantFeatures: List[Optional[ProductTypeVariantFeature]]
    model: Optional[str]

class TaxType(BaseModel):
    description: Optional[str]
    taxCode: Optional[str]

class AttributeCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[AttributeCountableEdge]]
    totalCount: Optional[int]

class AttributeCountableEdge(BaseModel):
    node: Attribute
    cursor: str

class ProductTypeProductFeature(BaseModel):
    id: str
    sortOrder: Optional[int]
    tenant: Tenant
    featureType: FeatureTypeEnum
    name: str
    description: str
    options: Optional[List[Optional[str]]]
    productType: ProductType
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

class ProductFeatureCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[ProductFeatureCountableEdge]]
    totalCount: Optional[int]

class ProductFeatureCountableEdge(BaseModel):
    node: ProductFeature
    cursor: str

class ProductFeature(BaseModel):
    id: str
    sortOrder: Optional[int]
    deletedAt: Optional[datetime]
    deletedByUser: Optional[User]
    deletedByApp: Optional[App]
    deletionBatchUuid: Optional[UUID]
    tenant: Tenant
    featureType: FeatureTypeEnum
    name: str
    description: str
    options: Optional[List[Optional[str]]]
    product: Product
    productTypeFeature: Optional[ProductTypeProductFeature]

class App(BaseModel):
    id: str
    name: Optional[str]
    created: Optional[datetime]
    isActive: Optional[bool]
    permissions: Optional[List[Optional[Permission]]]
    user: Optional[User]
    tokens: Optional[List[Optional[AppToken]]]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    type: Optional[AppTypeEnum]
    webhooks: Optional[List[Optional[Webhook]]]
    aboutApp: Optional[str]
    dataPrivacy: Optional[str]
    dataPrivacyUrl: Optional[str]
    homepageUrl: Optional[str]
    supportUrl: Optional[str]
    configurationUrl: Optional[str]
    appUrl: Optional[str]
    version: Optional[str]
    accessToken: Optional[str]

class Permission(BaseModel):
    code: PermissionEnum
    name: str

class AppToken(BaseModel):
    name: str
    authToken: str
    id: str

class Webhook(BaseModel):
    name: str
    targetUrl: str
    isActive: bool
    secretKey: Optional[str]
    connectionString: Optional[str]
    queueName: Optional[str]
    id: str
    events: List[Optional[WebhookEvent]]
    app: App

class WebhookEvent(BaseModel):
    eventType: WebhookEventTypeEnum
    name: str

class ProductTypeVariantFeature(BaseModel):
    id: str
    sortOrder: Optional[int]
    tenant: Tenant
    featureType: FeatureTypeEnum
    name: str
    description: str
    options: Optional[List[Optional[str]]]
    productType: ProductType
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

class VariantFeatureCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[VariantFeatureCountableEdge]]
    totalCount: Optional[int]

class VariantFeatureCountableEdge(BaseModel):
    node: VariantFeature
    cursor: str

class VariantFeature(BaseModel):
    id: str
    sortOrder: Optional[int]
    tenant: Tenant
    featureType: FeatureTypeEnum
    name: str
    description: str
    options: Optional[List[Optional[str]]]
    variant: ProductVariant
    productTypeFeature: Optional[ProductTypeVariantFeature]

class AttributeValue(BaseModel):
    id: str
    sortOrder: Optional[int]
    tenant: Tenant
    name: str
    value: str
    slug: str
    attribute: Attribute
    dateTime: Optional[datetime]
    plainText: str
    richText: str
    currency: str
    amount: Decimal
    money: Optional[Money]
    reference: str
    boolean: bool
    file: Optional[File]
    fileUrl: Optional[str]
    date: Optional[date]
    type: Optional[AttributeValueType]
    inputType: AttributeInputTypeEnum

class File(BaseModel):
    url: str

class CollectionCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[CollectionCountableEdge]]
    totalCount: Optional[int]

class CollectionCountableEdge(BaseModel):
    node: Collection
    cursor: str

class Collection(BaseModel):
    id: str
    publicationDate: Optional[date]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    description: str
    descriptionHtml: str
    seoTitle: Optional[str]
    seoDescription: Optional[str]
    isVisible: bool
    name: str
    slug: str
    filter: Optional[ProductVariantFilterInput]
    sortBy: Optional[VariantSortingInput]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    size: Optional[int]
    isPublished: bool
    type: Optional[CollectionTypeEnum]
    customFields: List[Optional[SelectedAttribute]]
    sales: List[Optional[Sale]]
    vouchers: List[Optional[Voucher]]
    onSale: Optional[bool]

class Sale(BaseModel):
    id: str
    name: str
    type: DiscountValueTypeEnum
    value: Decimal
    startDate: datetime
    endDate: Optional[datetime]
    currency: str
    minSpent: Optional[Money]
    minCheckoutItemsQuantity: int
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    saleType: SaleTypeEnum

class Fulfillment(BaseModel):
    id: str
    fulfillmentOrder: int
    relatedTo: Optional[Fulfillment]
    order: Order
    nauticalOrder: Optional[NauticalOrder]
    status: FulfillmentStatus
    trackingCompany: Optional[str]
    trackingNumber: Optional[str]
    trackingUrl: Optional[str]
    shippingLabelUrl: Optional[str]
    created: datetime
    updated: datetime
    user: Optional[User]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    lines: Optional[List[Optional[FulfillmentLine]]]
    seller: Optional[Seller]
    statusDisplay: Optional[str]
    warehouse: Optional[Warehouse]
    totalLinesQuantity: Optional[int]
    totalLinesMoney: Money
    customFields: List[Optional[SelectedAttribute]]

class NauticalOrder(BaseModel):
    id: str
    externalId: Optional[str]
    externalSource: Optional[str]
    orderSource: NauticalOrderOrderSource
    created: datetime
    updated: Optional[datetime]
    status: NauticalOrderStatus
    subStatus: Optional[NauticalOrderSubStatus]
    user: Optional[User]
    languageCode: str
    trackingClientId: str
    billingAddress: Optional[Address]
    shippingAddress: Optional[Address]
    currency: str
    isMarketplaceShippingPriceOverridden: bool
    shippingPrice: Optional[TaxedMoney]
    euInvoiceMessaging: Optional[str]
    vatIdentificationNumber: Optional[str]
    mpVatIdentificationNumber: Optional[str]
    token: str
    voucher: Optional[Voucher]
    shippingDiscount: Optional[Money]
    discount: Optional[Money]
    discountName: Optional[str]
    translatedDiscountName: Optional[str]
    displayGrossPrices: bool
    customerNote: str
    weight: Optional[Weight]
    importedAt: Optional[datetime]
    poNumbers: Optional[List[Optional[str]]]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    availableMarketplaceShippingMethods: Optional[List[Optional[ShippingMethod]]]
    sellerFulfillments: List[Optional[Fulfillment]]
    allowedSubStatuses: Optional[List[Optional[OrderSubStatusEnum]]]
    sellerUnfulfilled: List[Optional[OrderLine]]
    lines: List[Optional[NauticalOrderLine]]
    actions: List[Optional[OrderAction]]
    availableShippingMethodsBySeller: Optional[List[Optional[MultiSellerShippingMethod]]]
    invoices: Optional[List[Optional[Invoice]]]
    number: Optional[str]
    isPaid: Optional[bool]
    paymentStatus: PaymentChargeStatusEnum
    paymentStatusDisplay: str
    payments: Optional[List[Optional[Payment]]]
    total: Optional[TaxedMoney]
    subtotal: Optional[TaxedMoney]
    statusDisplay: Optional[str]
    canFinalize: bool
    validationStatus: Optional[List[Optional[ValidationStatus]]]
    totalAuthorized: Optional[Money]
    totalCaptured: Optional[Money]
    totalRefunded: Optional[Money]
    events: Optional[List[Optional[NauticalOrderEvent]]]
    positive: Optional[bool]
    userEmail: Optional[str]
    isShippingRequired: bool
    volumeDiscount: Optional[TaxedMoney]
    shippingMethodName: str
    subOrders: Optional[List[Optional[Order]]]
    refunds: Optional[List[Optional[Refund]]]
    marketplaceShippingPrice: TaxedMoney
    marketplaceShippingMethod: Optional[ShippingMethod]
    marketplaceShippingMethodName: Optional[str]

class OrderLine(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    isLinePriceOverridden: bool
    unitPriceOverriddenNote: Optional[str]
    note: Optional[str]
    productName: str
    variantName: str
    productSku: Optional[str]
    isShippingRequired: bool
    quantityFulfilled: int
    quantityDeclined: int
    digitalContentUrl: Optional[DigitalContentUrl]
    order: Order
    nauticalOrderLine: NauticalOrderLine
    size: Optional[int]
    unitPrice: Optional[TaxedMoney]
    totalPrice: Optional[TaxedMoney]
    variant: Optional[ProductVariant]
    translatedProductName: str
    translatedVariantName: str
    allocations: Optional[List[Optional[Allocation]]]
    priceBook: Optional[PriceBook]
    quantityOrdered: int
    unfulfilledQuantityRefunded: int
    fulfilledQuantityRefunded: int

class DigitalContentUrl(BaseModel):
    content: DigitalContent
    created: datetime
    downloadNum: int
    id: str
    url: Optional[str]
    token: NauticalUUID

class DigitalContent(BaseModel):
    useDefaultSettings: bool
    automaticFulfillment: bool
    productVariant: ProductVariant
    contentFile: Optional[str]
    maxDownloads: Optional[int]
    urlValidDays: Optional[int]
    urls: Optional[List[Optional[DigitalContentUrl]]]
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]

class NauticalOrderLine(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    isLinePriceOverridden: bool
    unitPriceOverriddenNote: Optional[str]
    note: Optional[str]
    productName: str
    variantName: str
    productSku: Optional[str]
    isShippingRequired: bool
    digitalContentUrl: Optional[DigitalContentUrl]
    size: Optional[int]
    unitPrice: Optional[TaxedMoney]
    totalPrice: Optional[TaxedMoney]
    variant: Optional[ProductVariant]
    translatedProductName: str
    translatedVariantName: str
    priceBook: Optional[PriceBook]
    sellerOrderline: Optional[OrderLine]
    quantityOrdered: int
    sale: Optional[Sale]
    saleDiscount: Optional[Money]
    voucherDiscount: Optional[Money]
    originalUnitPrice: Optional[TaxedMoney]
    discountedUnitPrice: Optional[TaxedMoney]

class PriceBook(BaseModel):
    description: str
    descriptionHtml: str
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    name: str
    deleted: bool
    priceBookVariants: Optional[List[Optional[PriceBookVariant]]]
    priceBookProducts: Optional[List[Optional[PriceBookProduct]]]
    priceBookProductTypes: Optional[List[Optional[PriceBookProductType]]]
    numberOfProducts: int
    numberOfProductTypes: int
    numberOfVariants: int

class PriceBookVariant(BaseModel):
    id: str
    priceBook: PriceBook
    variant: ProductVariant
    valueType: PriceBookVariantValueType
    currency: str
    price: Money
    percentage: float

class PriceBookProduct(BaseModel):
    id: str
    priceBook: PriceBook
    product: Product
    valueType: PriceBookProductValueType
    currency: str
    price: Money
    percentage: float

class PriceBookProductType(BaseModel):
    id: str
    priceBook: PriceBook
    productType: ProductType
    valueType: PriceBookProductTypeValueType
    currency: str
    price: Money
    percentage: float

class Allocation(BaseModel):
    id: str
    quantity: int
    warehouse: Warehouse

class Warehouse(BaseModel):
    externalId: Optional[str]
    externalSource: Optional[str]
    id: str
    name: str
    slug: str
    companyName: str
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    address: Address
    email: str
    seller: Seller
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]

class ShippingZoneCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[ShippingZoneCountableEdge]]
    totalCount: Optional[int]

class ShippingZoneCountableEdge(BaseModel):
    node: ShippingZone
    cursor: str

class ShippingZone(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    name: str
    seller: Seller
    warehouses: List[Optional[Warehouse]]
    priceRange: MoneyRange
    countries: List[Optional[CountryDisplay]]
    shippingMethods: List[Optional[ShippingMethod]]
    countryAreas: List[Optional[ShippingZoneCountryArea]]

class MoneyRange(BaseModel):
    start: Optional[Money]
    stop: Optional[Money]

class ShippingZoneCountryArea(BaseModel):
    id: str
    country: CountryDisplay
    countryArea: CountryArea

class Invoice(BaseModel):
    id: str
    metadata: List[Optional[MetadataItem]]
    status: JobStatusEnum
    number: str
    externalUrl: Optional[str]
    isValid: bool
    isEditable: bool
    privateMetadata: List[Optional[MetadataItem]]
    createdAt: datetime
    updatedAt: datetime
    message: Optional[str]
    url: Optional[str]

class Payment(BaseModel):
    id: str
    gateway: str
    isActive: bool
    created: datetime
    modified: datetime
    token: str
    checkout: Optional[Checkout]
    nauticalOrder: Optional[NauticalOrder]
    paymentMethodType: str
    paymentMethodToken: Optional[str]
    customerIpAddress: Optional[str]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    chargeStatus: PaymentChargeStatusEnum
    actions: List[Optional[OrderAction]]
    total: Optional[Money]
    capturedAmount: Optional[Money]
    transactions: Optional[List[Optional[Transaction]]]
    availableCaptureAmount: Optional[Money]
    availableRefundAmount: Optional[Money]
    creditCard: Optional[CreditCard]

class Transaction(BaseModel):
    id: str
    created: datetime
    payment: Payment
    token: str
    kind: TransactionKind
    isSuccess: bool
    error: Optional[str]
    amount: Optional[Money]

class CreditCard(BaseModel):
    brand: str
    firstDigits: Optional[str]
    lastDigits: str
    expMonth: Optional[int]
    expYear: Optional[int]

class ValidationStatus(BaseModel):
    message: Optional[str]
    code: Optional[str]
    variant: Optional[str]

class NauticalOrderEvent(BaseModel):
    id: str
    date: datetime
    type: OrderEventsEnum
    user: Optional[User]
    message: Optional[str]
    email: Optional[str]
    emailType: Optional[OrderEventsEmailsEnum]
    amount: Optional[float]
    paymentId: Optional[str]
    paymentGateway: Optional[str]
    quantity: Optional[int]
    composedId: Optional[str]
    orderNumber: Optional[str]
    invoiceNumber: Optional[str]
    oversoldItems: Optional[List[Optional[str]]]
    lines: Optional[List[Optional[NauticalOrderEventOrderLineObject]]]
    warehouse: Optional[Warehouse]

class NauticalOrderEventOrderLineObject(BaseModel):
    quantity: Optional[int]
    orderLine: Optional[NauticalOrderLine]
    itemName: Optional[str]

class Refund(BaseModel):
    createdAt: datetime
    updatedAt: datetime
    description: str
    descriptionHtml: str
    id: str
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    buyer: Optional[User]
    externalId: Optional[str]
    name: str
    order: NauticalOrder
    status: RefundStatusEnum
    token: str
    refundType: RefundTypeEnum

class RefundLineCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[RefundLineCountableEdge]]
    totalCount: Optional[int]

class RefundLineCountableEdge(BaseModel):
    node: RefundLine
    cursor: str

class RefundLine(BaseModel):
    createdAt: datetime
    updatedAt: datetime
    id: str
    chargedTo: RefundChargeToEnum
    currency: str
    lineScope: RefundLineScopeEnum
    lineType: RefundLineTypeEnum
    percentage: float
    quantityFulfilled: int
    quantityUnfulfilled: int
    refund: Refund
    refundScope: RefundScope
    total: TaxedMoney

class RefundPaymentCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[RefundPaymentCountableEdge]]
    totalCount: Optional[int]

class RefundPaymentCountableEdge(BaseModel):
    node: RefundPayment
    cursor: str

class RefundPayment(BaseModel):
    createdAt: datetime
    updatedAt: datetime
    id: str
    paymentType: RefundPaymentTypeEnum
    refund: Refund
    refundMethod: RefundMethod

class FulfillmentLine(BaseModel):
    id: str
    quantity: int
    orderLine: Optional[OrderLine]
    returnReason: Optional[str]

class OrderFee(BaseModel):
    id: str
    tenant: Tenant
    order: Optional[Order]
    currency: NauticalCurrency
    transactionAmount: Decimal
    transactionCurrency: NauticalCurrency
    transactionFee: Optional[Money]
    domiciledAmount: Decimal
    domiciledFee: Optional[Money]
    source: Optional[SourceFeeEnum]
    name: str
    notes: str
    data: str

class NauticalCurrency(BaseModel):
    code: str

class OrderEvent(BaseModel):
    id: str
    date: datetime
    type: Optional[OrderEventsEnum]
    user: Optional[User]
    message: Optional[str]
    email: Optional[str]
    emailType: Optional[OrderEventsEmailsEnum]
    amount: Optional[float]
    paymentId: Optional[str]
    paymentGateway: Optional[str]
    quantity: Optional[int]
    composedId: Optional[str]
    orderNumber: Optional[str]
    invoiceNumber: Optional[str]
    oversoldItems: Optional[List[Optional[str]]]
    lines: Optional[List[Optional[OrderEventOrderLineObject]]]
    fulfilledItems: Optional[List[Optional[FulfillmentLine]]]
    warehouse: Optional[Warehouse]

class OrderEventOrderLineObject(BaseModel):
    quantity: Optional[int]
    orderLine: Optional[OrderLine]
    itemName: Optional[str]

class OrderPayoutSummary(BaseModel):
    commissions: Money
    discounts: Money
    fees: Money
    refunds: Money
    refundsCommission: Money
    sales: Money
    shipping: Money
    total: Money
    vendorPayout: VendorPayout

class AgreementSellersCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[AgreementSellersCountableEdge]]
    totalCount: Optional[int]

class AgreementSellersCountableEdge(BaseModel):
    node: AgreementSellers
    cursor: str

class AgreementSellers(BaseModel):
    id: str
    tenant: Tenant
    seller: Seller
    acknowledgedOn: Optional[datetime]
    plan: Optional[Agreement]
    effectiveAt: datetime
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]

class Agreement(BaseModel):
    id: str
    publicationDate: Optional[date]
    isPublished: bool
    createdAt: datetime
    updatedAt: datetime
    content: str
    contentHtml: str
    tenant: Tenant
    seoTitle: Optional[str]
    seoDescription: Optional[str]
    slug: str
    title: str
    commissionType: CommissionTypeEnum
    defaultCommission: Decimal
    markupCommissionType: MarkupCommissionTypeEnum
    markupCommissionValue: Optional[Decimal]
    isActive: Optional[bool]
    granularCommissions: List[Optional[AgreementCommission]]
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    fees: List[Optional[AgreementFees]]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]

class AgreementCommission(BaseModel):
    id: str
    tenant: Tenant
    commission: Decimal
    agreement: Agreement
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    instance: Optional[Category]

class AgreementFees(BaseModel):
    id: str
    tenant: Tenant
    agreement: Agreement
    feeType: FeeType
    feeScope: FeeScope
    feeValue: Decimal
    feeName: str

class WarehouseCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[WarehouseCountableEdge]]
    totalCount: Optional[int]

class WarehouseCountableEdge(BaseModel):
    node: Warehouse
    cursor: str

class Microsite(BaseModel):
    id: str
    publicationDate: Optional[date]
    description: str
    descriptionHtml: str
    seoTitle: Optional[str]
    seoDescription: Optional[str]
    name: str
    slug: str
    footerText: Optional[str]
    seller: Optional[Seller]
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    filter: Optional[ProductFilterInput]
    sortBy: Optional[ProductOrder]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]
    size: Optional[int]
    isPublished: bool

class Document(BaseModel):
    id: str
    createdAt: datetime
    updatedAt: datetime
    tenant: Tenant
    file: str
    name: str
    description: str
    fileExtension: str
    fileContentType: Optional[str]
    fileSize: Optional[FileSize]
    url: Optional[str]

class FileSize(BaseModel):
    bytes: Optional[int]
    kilobytes: Optional[Decimal]
    megabytes: Optional[Decimal]

class ProductPricingInfo(BaseModel):
    onSale: bool
    discount: TaxedMoney
    discountLocalCurrency: TaxedMoney
    priceRange: TaxedMoneyRange
    priceRangeUndiscounted: TaxedMoneyRange
    priceRangeLocalCurrency: TaxedMoneyRange
    priceRangeUndiscountedLocalCurrency: TaxedMoneyRange

class TaxedMoneyRange(BaseModel):
    start: Optional[TaxedMoney]
    stop: Optional[TaxedMoney]

class Margin(BaseModel):
    start: Optional[int]
    stop: Optional[int]

class ProductImage(BaseModel):
    id: str
    sortOrder: Optional[int]
    externalId: Optional[str]
    externalSource: Optional[str]
    alt: str
    size: Optional[int]

class ProductImageCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[ProductImageCountableEdge]]
    totalCount: Optional[int]

class ProductImageCountableEdge(BaseModel):
    node: ProductImage
    cursor: str

class Location(BaseModel):
    id: str
    lon: Optional[float]
    lat: Optional[float]
    locationType: Optional[LocationTypeEnum]
    locationKind: Optional[LocationKindEnum]
    companyName: str
    streetAddress1: str
    streetAddress2: str
    city: str
    cityArea: str
    postalCode: str
    country: CountryDisplay
    countryArea: str
    phone: Optional[str]

class WarehouseStats(BaseModel):
    warehouseId: str
    quantity: int
    quantityAllocated: int
    quantityAvailable: int

class ProductStatusLog(BaseModel):
    user: Optional[User]
    subStatus: Optional[ProductSubStatusEnum]
    subStatusReason: Optional[str]
    createdAt: Optional[datetime]
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]

class VariantPricingInfo(BaseModel):
    onSale: bool
    discount: TaxedMoney
    discountLocalCurrency: TaxedMoney
    price: TaxedMoney
    priceUndiscounted: TaxedMoney
    priceLocalCurrency: TaxedMoney
    priceUndiscountedLocalCurrency: TaxedMoney

class VariantSize(BaseModel):
    length: Optional[Decimal]
    width: Optional[Decimal]
    height: Optional[Decimal]
    sizeUnits: Optional[DistanceUnitsEnum]

class Stock(BaseModel):
    warehouse: Warehouse
    productVariant: ProductVariant
    quantity: int
    outOfStockThreshold: Optional[int]
    quantityAllocated: int
    id: str
    quantityAvailable: int

class StockEvent(BaseModel):
    id: str
    date: datetime
    type: StockEventType
    stock: Optional[Stock]
    parameters: str
    user: Optional[User]

class SellerType(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    pk: Optional[int]
    companyName: Optional[str]
    owner: Optional[UserType]

class UserType(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    defaultShippingAddress: Optional[AddressType]

class AddressType(BaseModel):
    id: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    firstName: Optional[str]
    lastName: Optional[str]
    streetAddress1: Optional[str]
    streetAddress2: Optional[str]
    city: Optional[str]
    postalCode: Optional[str]
    country: Optional[str]
    countryArea: Optional[str]
    phone: Optional[str]

class CheckoutSellerShipping(BaseModel):
    tenant: Tenant
    id: str
    seller: Seller
    shippingMethod: ShippingMethod
    isPriceOverridden: bool
    priceOverrideAmount: Decimal

class NauticalOrderCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[NauticalOrderCountableEdge]]
    totalCount: Optional[int]

class NauticalOrderCountableEdge(BaseModel):
    node: NauticalOrder
    cursor: str

class UserPermission(BaseModel):
    code: PermissionEnum
    name: str
    userId: Optional[str]

class Group(BaseModel):
    id: str
    name: str
    permissions: List[Optional[Permission]]
    users: List[Optional[User]]
    userCanManage: bool

class CustomerEvent(BaseModel):
    id: str
    date: Optional[datetime]
    type: Optional[CustomerEventsEnum]
    user: Optional[User]
    message: Optional[str]
    count: Optional[int]
    order: Optional[Order]
    orderLine: Optional[OrderLine]
    nauticalOrder: Optional[NauticalOrder]

class PaymentSource(BaseModel):
    id: str
    gateway: str
    creditCardInfo: Optional[CreditCard]

class WishlistCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[WishlistCountableEdge]]
    totalCount: Optional[int]

class WishlistCountableEdge(BaseModel):
    node: Wishlist
    cursor: str

class WebhookEventLogCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[WebhookEventLogCountableEdge]]
    totalCount: Optional[int]

class WebhookEventLogCountableEdge(BaseModel):
    node: WebhookEventLog
    cursor: str

class WebhookEventLog(BaseModel):
    id: str
    tenant: Tenant
    date: datetime
    targetUrl: Optional[str]
    eventType: str
    webhookId: Optional[str]
    transactionId: Optional[str]
    appId: Optional[str]
    pluginId: Optional[str]
    payload: str
    error: Optional[str]
    direction: Optional[WebhookDirectionEnum]

class WebhookJobCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[WebhookJobCountableEdge]]
    totalCount: Optional[int]

class WebhookJobCountableEdge(BaseModel):
    node: WebhookJob
    cursor: str

class WebhookJob(BaseModel):
    id: str
    status: JobStatusEnum
    message: Optional[str]
    createdAt: datetime
    updatedAt: datetime
    tenant: Tenant
    body: Optional[str]
    requestMeta: Optional[str]
    source: Optional[str]
    type: Optional[GenericWebhookTransactionType]
    vendorEntityLink: Optional[str]
    marketplaceEntityLink: Optional[str]
    seller: Optional[Seller]

class StockCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[StockCountableEdge]]
    totalCount: Optional[int]

class StockCountableEdge(BaseModel):
    node: Stock
    cursor: str

class Content(BaseModel):
    publicationDate: Optional[date]
    isPublished: bool
    createdAt: datetime
    updatedAt: datetime
    id: str
    slug: str
    isPage: bool
    lockedBy: Optional[User]
    lockExpiry: Optional[datetime]
    data: str
    draftData: str
    revision: int
    hasActiveDraft: Optional[bool]
    contentPageData: Optional[ContentPageData]

class ContentPageData(BaseModel):
    seoTitle: Optional[str]
    seoDescription: Optional[str]
    id: str

class ContentCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[ContentCountableEdge]]
    totalCount: Optional[int]

class ContentCountableEdge(BaseModel):
    node: Content
    cursor: str

class Media(BaseModel):
    tenant: Tenant
    id: str
    title: str
    createdAt: str
    image: Optional[Image]
    alt: str

class MediaCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[MediaCountableEdge]]
    totalCount: Optional[int]

class MediaCountableEdge(BaseModel):
    node: Media
    cursor: str

class TenantCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[TenantCountableEdge]]
    totalCount: Optional[int]

class TenantCountableEdge(BaseModel):
    node: Tenant
    cursor: str

class Shop(BaseModel):
    currency: Optional[str]
    geolocalization: Optional[Geolocalization]
    languageCode: Optional[LanguageCodeEnum]
    supportedCurrencies: List[Optional[NauticalCurrency]]
    defaultCountry: Optional[CountryDisplay]
    defaultMailSenderName: Optional[str]
    defaultMailSenderAddress: Optional[str]
    defaultMailSupportAddress: Optional[str]
    description: Optional[str]
    domain: Domain
    apiUrl: Optional[str]
    dashboardUrl: Optional[str]
    enableQuoteOrders: Optional[bool]
    enableOfferOrders: Optional[bool]
    name: str
    permissions: List[Optional[Permission]]
    phonePrefixes: List[Optional[str]]
    includeTaxesInPrices: bool
    chargeTaxesOnShipping: bool
    trackInventoryByDefault: Optional[bool]
    defaultWeightUnit: Optional[WeightUnitsEnum]
    automaticFulfillmentDigitalProducts: Optional[bool]
    defaultDigitalMaxDownloads: Optional[int]
    defaultDigitalUrlValidDays: Optional[int]
    companyAddress: Optional[Address]
    customerSetPasswordUrl: Optional[str]
    loginForCheckout: Optional[bool]
    loginForPrice: Optional[bool]
    activePlugins: List[Optional[Plugin]]
    crispWebsiteId: Optional[str]
    geolocationEnabled: Optional[bool]
    requireProductApproval: Optional[bool]
    timezone: str
    checkoutTheme: Optional[CheckoutTheme]
    storefrontTheme: Optional[StorefrontTheme]
    sellerOnboardingSettings: Optional[SellerOnboardingSettings]

class Geolocalization(BaseModel):
    country: Optional[CountryDisplay]

class Domain(BaseModel):
    host: str
    url: str

class Plugin(BaseModel):
    id: str
    privateMetadata: str
    metadata: str
    company: Optional[str]
    category: Optional[PluginConfigurationCategory]
    descriptionShort: str
    logoUrl: Optional[str]
    created: datetime
    externalUrl: Optional[str]
    supportUrl: Optional[str]
    allowSellers: Optional[bool]
    allowManyActivePluginsInCategory: bool
    tenant: Tenant
    identifier: str
    name: str
    description: str
    active: bool
    configuration: Optional[List[Optional[ConfigurationItem]]]
    defaultConfiguration: Optional[List[Optional[ConfigurationItem]]]
    supportSellerConfiguration: Optional[bool]
    version: str

class ConfigurationItem(BaseModel):
    name: str
    value: Optional[str]
    type: Optional[ConfigurationTypeFieldEnum]
    helpText: Optional[str]
    label: Optional[str]
    options: Optional[List[Optional[str]]]

class CheckoutTheme(BaseModel):
    id: str
    confirmationUrl: str

class StorefrontTheme(BaseModel):
    id: str
    primaryColor: Optional[str]
    backgroundColor: Optional[str]
    logo: Optional[Image]
    faviconImage: Optional[Image]
    faviconUrl: Optional[str]
    font: Optional[Font]
    fontColor: Optional[str]

class Font(BaseModel):
    id: str
    name: Optional[str]
    slug: Optional[str]

class SellerOnboardingSettings(BaseModel):
    id: str
    isAcceptingNewSellers: Optional[bool]
    summary: Optional[str]
    welcomeMessage: Optional[str]
    fulfillmentModel: Optional[str]
    requiredDocuments: Optional[str]
    notAcceptingSellersMessage: Optional[str]
    isProductImportAllowed: Optional[bool]

class CustomDomain(BaseModel):
    id: str
    domain: str
    status: DomainStatusEnum
    errorDetails: str
    sslCertName: str

class PublicSeller(BaseModel):
    id: str
    companyName: str
    slug: str
    size: Optional[int]
    status: SellerStatus
    storeDescription: str
    offset: Optional[int]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

class SellerCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[SellerCountableEdge]]
    totalCount: Optional[int]

class SellerCountableEdge(BaseModel):
    node: Seller
    cursor: str

class UserCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[UserCountableEdge]]
    totalCount: Optional[int]

class UserCountableEdge(BaseModel):
    node: User
    cursor: str

class AgreementCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[AgreementCountableEdge]]
    totalCount: Optional[int]

class AgreementCountableEdge(BaseModel):
    node: Agreement
    cursor: str

class SellerCards(BaseModel):
    newSellers: Optional[int]
    sellerOrders: Optional[int]
    sellerCommissions: Optional[Money]

class SellerDetailCards(BaseModel):
    sellerOrders: Optional[int]
    sellerCommissions: Optional[Money]
    sellerSales: Optional[TaxedMoney]

class RefundCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[RefundCountableEdge]]
    totalCount: Optional[int]

class RefundCountableEdge(BaseModel):
    node: Refund
    cursor: str

class DigitalContentCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[DigitalContentCountableEdge]]
    totalCount: Optional[int]

class DigitalContentCountableEdge(BaseModel):
    node: DigitalContent
    cursor: str

class PriceBookCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PriceBookCountableEdge]]
    totalCount: Optional[int]

class PriceBookCountableEdge(BaseModel):
    node: PriceBook
    cursor: str

class PriceBookVariantCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PriceBookVariantCountableEdge]]
    totalCount: Optional[int]

class PriceBookVariantCountableEdge(BaseModel):
    node: PriceBookVariant
    cursor: str

class PriceBookProductCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PriceBookProductCountableEdge]]
    totalCount: Optional[int]

class PriceBookProductCountableEdge(BaseModel):
    node: PriceBookProduct
    cursor: str

class PriceBookProductTypeCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PriceBookProductTypeCountableEdge]]
    totalCount: Optional[int]

class PriceBookProductTypeCountableEdge(BaseModel):
    node: PriceBookProductType
    cursor: str

class PriceBookVariantHistoryCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PriceBookVariantHistoryCountableEdge]]
    totalCount: Optional[int]

class PriceBookVariantHistoryCountableEdge(BaseModel):
    node: PriceBookVariantHistory
    cursor: str

class PriceBookVariantHistory(BaseModel):
    id: str
    priceBook: Optional[PriceBook]
    variantId: int
    valueType: PriceBookVariantHistoryValueType
    currency: str
    createdAt: date
    price: Money
    percentage: float
    deleted: bool

class PriceBookProductHistoryCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PriceBookProductHistoryCountableEdge]]
    totalCount: Optional[int]

class PriceBookProductHistoryCountableEdge(BaseModel):
    node: PriceBookProductHistory
    cursor: str

class PriceBookProductHistory(BaseModel):
    id: str
    priceBook: Optional[PriceBook]
    productId: int
    valueType: PriceBookProductHistoryValueType
    currency: str
    createdAt: date
    price: Money
    percentage: float
    deleted: bool

class PriceBookProductTypeHistoryCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PriceBookProductTypeHistoryCountableEdge]]
    totalCount: Optional[int]

class PriceBookProductTypeHistoryCountableEdge(BaseModel):
    node: PriceBookProductTypeHistory
    cursor: str

class PriceBookProductTypeHistory(BaseModel):
    id: str
    priceBook: Optional[PriceBook]
    productTypeId: int
    valueType: PriceBookProductTypeHistoryValueType
    currency: str
    createdAt: date
    price: Money
    percentage: float
    deleted: bool

class PluginCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PluginCountableEdge]]
    totalCount: Optional[int]

class PluginCountableEdge(BaseModel):
    node: Plugin
    cursor: str

class TaxCertificate(BaseModel):
    id: Optional[int]
    companyId: Optional[str]
    signedDate: Optional[str]
    expirationDate: Optional[str]
    filename: Optional[str]
    documentExists: Optional[bool]
    downloadUrl: Optional[str]
    valid: Optional[bool]
    verified: Optional[bool]
    exemptPercentage: Optional[str]
    isSingleCertificate: Optional[bool]
    exemptionNumber: Optional[str]
    exemptionReasonName: Optional[str]
    exemptionReasonId: Optional[int]
    status: Optional[str]
    createdDate: Optional[str]
    modifiedDate: Optional[str]
    taxNumberType: Optional[str]
    businessNumberType: Optional[str]
    exposureZoneName: Optional[str]

class CatalogImportProcess(BaseModel):
    status: CatalogImportProcessStatus
    message: Optional[str]
    createdAt: datetime
    updatedAt: datetime
    taskId: Optional[str]
    externalSource: str
    finishedAt: Optional[datetime]
    createdBy: Optional[User]
    seller: Optional[Seller]
    internalNotes: Optional[str]
    id: str
    filter: Optional[CatalogImportProcessLogRecordFilterInput]
    sortBy: Optional[CatalogImportProcessLogRecordSortInput]
    before: Optional[str]
    after: Optional[str]
    first: Optional[int]
    last: Optional[int]

class CatalogImportProcessLogRecordCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[CatalogImportProcessLogRecordCountableEdge]]
    totalCount: Optional[int]

class CatalogImportProcessLogRecordCountableEdge(BaseModel):
    node: CatalogImportProcessLogRecord
    cursor: str

class CatalogImportProcessLogRecord(BaseModel):
    id: str
    createdAt: datetime
    taskId: Optional[str]
    objectId: Optional[str]
    operation: CatalogImportProcessLogRecordOperation
    relatedObjectName: Optional[str]

class CatalogImportProcessCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[CatalogImportProcessCountableEdge]]
    totalCount: Optional[int]

class CatalogImportProcessCountableEdge(BaseModel):
    node: CatalogImportProcess
    cursor: str

class TaxExemptCode(BaseModel):
    code: str
    name: str
    description: str
    validCountries: Optional[List[Optional[str]]]

class TypeformForms(BaseModel):
    totalItems: Optional[int]
    pageCount: Optional[int]
    items: Optional[List[Optional[TypeformFormsItem]]]

class TypeformFormsItem(BaseModel):
    Links: Optional[TypeformFormsItemLink]
    id: Optional[str]
    lastUpdatedAt: Optional[str]
    self: Optional[TypeformFormsItemSelf]
    theme: Optional[TypeformFormsItemSelf]
    title: Optional[str]

class TypeformFormsItemLink(BaseModel):
    display: Optional[str]

class TypeformFormsItemSelf(BaseModel):
    href: Optional[str]

class TypeformForm(BaseModel):
    id: Optional[str]
    title: Optional[str]
    language: Optional[str]
    fields: Optional[List[Optional[TypeformFormFields]]]
    hidden: Optional[List[Optional[str]]]

class TypeformFormFields(BaseModel):
    attachment: Optional[TypeformFormAttachment]
    fieldType: Optional[str]
    id: Optional[str]
    layout: Optional[TypeformFormLayout]
    name: Optional[str]
    options: Optional[List[Optional[TypeformFormOption]]]
    ref: Optional[str]
    required: Optional[bool]
    title: Optional[str]
    properties: Optional[TypeformFormProperties]
    type: Optional[str]

class TypeformFormAttachment(BaseModel):
    type: Optional[str]
    href: Optional[str]
    properties: Optional[TypeformFormProperties]

class TypeformFormProperties(BaseModel):
    description: Optional[str]
    fields: Optional[List[Optional[TypeformGroupProperties]]]

class TypeformGroupProperties(BaseModel):
    id: Optional[str]
    title: Optional[str]
    ref: Optional[str]
    type: Optional[str]

class TypeformFormLayout(BaseModel):
    type: Optional[str]
    placement: Optional[str]
    attachment: Optional[TypeformFormAttachment]

class TypeformFormOption(BaseModel):
    label: Optional[str]

class Flow(BaseModel):
    id: str
    tenant: Tenant
    identifier: str
    seller: Optional[Seller]
    process: FlowProcess
    mapping: str
    formId: str

class AvalaraRequestLogCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[AvalaraRequestLogCountableEdge]]
    totalCount: Optional[int]

class AvalaraRequestLogCountableEdge(BaseModel):
    node: AvalaraRequestLog
    cursor: str

class AvalaraRequestLog(BaseModel):
    createdAt: datetime
    requestUrl: Optional[str]
    requestData: str
    responseData: str
    error: Optional[str]
    id: str

class CheckoutEventCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[CheckoutEventCountableEdge]]
    totalCount: Optional[int]

class CheckoutEventCountableEdge(BaseModel):
    node: CheckoutEvent
    cursor: str

class CheckoutEvent(BaseModel):
    tenant: Tenant
    id: str
    createdAt: datetime
    type: CheckoutEventType
    checkoutId: str

class PayoutCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PayoutCountableEdge]]
    totalCount: Optional[int]

class PayoutCountableEdge(BaseModel):
    node: Payout
    cursor: str

class VendorPayoutReport(BaseModel):
    included: Optional[VendorPayoutReportSubset]
    excluded: Optional[VendorPayoutReportSubset]

class VendorPayoutReportSubset(BaseModel):
    category: Optional[str]
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: Optional[OrderVendorSummaryType]
    report: Optional[List[Optional[OrderVendorReportType]]]
    title: Optional[str]

class ColumnObjectType(BaseModel):
    display: str
    fieldType: str
    name: str
    order: int

class FilterObjectType(BaseModel):
    display: str
    fieldType: str
    name: str
    placeholder: str
    required: bool
    value: Optional[str]

class OrderVendorSummaryType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    vendors: Optional[int]
    adjustments: Optional[Decimal]
    penalties: Optional[Decimal]
    refunds: Optional[Decimal]
    fees: Optional[Decimal]

class OrderVendorReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    vendorId: Optional[int]
    vendor: Optional[Vendor]
    vendorPayout: Optional[VendorPayout]
    adjustments: Optional[Decimal]
    penalties: Optional[Decimal]
    refunds: Optional[Decimal]
    fees: Optional[Decimal]

class SingleVendorPayoutReport(BaseModel):
    payouts: Optional[List[Optional[SingleVendorReportType]]]
    summary: Optional[SingleVendorSummaryType]

class SingleVendorReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[Decimal]
    adjustments: Optional[Decimal]
    penalties: Optional[Decimal]
    refunds: Optional[Decimal]
    fees: Optional[Decimal]
    startDate: Optional[str]
    endDate: Optional[str]
    payoutEndDate: Optional[str]
    status: Optional[str]
    vendorPayout: Optional[VendorPayout]

class SingleVendorSummaryType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    adjustments: Optional[Decimal]
    penalties: Optional[Decimal]
    refunds: Optional[Decimal]
    fees: Optional[Decimal]

class PaymentCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PaymentCountableEdge]]
    totalCount: Optional[int]

class PaymentCountableEdge(BaseModel):
    node: Payment
    cursor: str

class Page(BaseModel):
    id: str
    publicationDate: Optional[date]
    createdAt: datetime
    updatedAt: datetime
    content: str
    contentHtml: str
    seoTitle: Optional[str]
    seoDescription: Optional[str]
    slug: str
    title: str
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    isPublished: bool

class PageCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[PageCountableEdge]]
    totalCount: Optional[int]

class PageCountableEdge(BaseModel):
    node: Page
    cursor: str

class OrderEventCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[OrderEventCountableEdge]]
    totalCount: Optional[int]

class OrderEventCountableEdge(BaseModel):
    node: OrderEvent
    cursor: str

class NauticalOrderEventCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[NauticalOrderEventCountableEdge]]
    totalCount: Optional[int]

class NauticalOrderEventCountableEdge(BaseModel):
    node: NauticalOrderEvent
    cursor: str

class FulfillmentCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[FulfillmentCountableEdge]]
    totalCount: Optional[int]

class FulfillmentCountableEdge(BaseModel):
    node: Fulfillment
    cursor: str

class OptimizedHome(BaseModel):
    sales: Optional[TaxedMoney]
    orders: Optional[int]
    toFulfill: Optional[int]
    toCapture: Optional[int]
    outOfStock: Optional[int]
    topProducts: List[Optional[ProductVariant]]
    sellerActivities: List[Optional[OrderEvent]]
    marketplaceActivities: List[Optional[NauticalOrderEvent]]

class NauticalConfiguration(BaseModel):
    configurationName: Optional[str]
    configurationValue: Optional[bool]
    configurationValueDatetime: Optional[datetime]
    configurationValueString: Optional[str]

class MicrositeCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[MicrositeCountableEdge]]
    totalCount: Optional[int]

class MicrositeCountableEdge(BaseModel):
    node: Microsite
    cursor: str

class Menu(BaseModel):
    id: str
    name: str
    slug: str
    items: List[Optional[MenuItem]]

class MenuItem(BaseModel):
    id: str
    menu: Menu
    name: str
    parent: Optional[MenuItem]
    category: Optional[Category]
    collection: Optional[Collection]
    page: Optional[Page]
    level: int
    children: List[Optional[MenuItem]]
    url: Optional[str]

class MenuCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[MenuCountableEdge]]
    totalCount: Optional[int]

class MenuCountableEdge(BaseModel):
    node: Menu
    cursor: str

class MenuItemCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[MenuItemCountableEdge]]
    totalCount: Optional[int]

class MenuItemCountableEdge(BaseModel):
    node: MenuItem
    cursor: str

class MarketplaceConfiguration(BaseModel):
    tenant: Tenant
    id: UUID
    marketplaceName: str
    requireProductApproval: bool
    requireProductTypes: bool
    payoutAutomationStrategy: Optional[MarketplaceConfigurationPayoutAutomationStrategyEnum]
    domiciledCurrency: MarketplaceConfigurationCurrencyEnum
    supportedCurrencies: List[Optional[str]]
    defaultCountry: str
    supportedCountries: List[Optional[str]]
    sellerCanSendQuote: bool
    variantUniqueness: Optional[VariantUniquenessEnum]
    defaultSellerChecklists: List[Optional[DefaultSellerChecklist]]
    enableStockAllocationForQuotes: bool
    enableStockAllocationForOffers: Optional[bool]
    enableStockAllocationForDrafts: bool
    validateStockOnOrderPaymentCreation: bool
    timezone: str
    enableBackorders: bool
    revenueAccrualStrategy: Optional[RevenueAccrualStrategyEnum]
    availableShippingStrategy: Optional[AvailableShippingStrategyEnum]
    attributeTemplateStrategy: MarketplaceConfigurationAttributeTemplateStrategy
    fulfillmentModel: FulfillmentModelEnum
    defaultWeightUnit: Optional[WeightUnitsEnum]
    automaticFulfillmentDigitalProducts: bool
    defaultDigitalMaxDownloads: Optional[int]
    defaultDigitalUrlValidDays: Optional[int]
    trackInventoryByDefault: bool
    description: str
    name: str
    companyAddress: Optional[Address]
    defaultMailSenderName: Optional[str]
    defaultMailSenderAddress: Optional[str]
    defaultMailSupportAddress: Optional[str]
    customerSetPasswordUrl: Optional[str]
    includeTaxesInPrices: bool
    chargeTaxesOnShipping: bool

class DefaultSellerChecklist(BaseModel):
    title: str
    description: str
    completeOn: Optional[SellerChecklistCompletionTriggersEnum]
    isEnabled: bool

class EmailEventCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[EmailEventCountableEdge]]
    totalCount: Optional[int]

class EmailEventCountableEdge(BaseModel):
    node: EmailEvent
    cursor: str

class EmailEvent(BaseModel):
    id: str
    tenant: Tenant
    date: datetime
    fromEmail: str
    toEmails: Optional[List[Optional[str]]]
    bccEmails: Optional[List[Optional[str]]]
    ccEmails: Optional[List[Optional[str]]]
    messageType: EmailEventMessageType
    emailPluginId: str
    template: Optional[str]
    payload: str
    error: Optional[str]

class LocationSuggestion(BaseModel):
    label: str
    address: Optional[Address]

class Coordinates(BaseModel):
    label: Optional[str]
    latitude: Optional[Decimal]
    longitude: Optional[Decimal]

class InReportOrderCustomerSummaryType(BaseModel):
    category: str
    title: str
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: OrderSellerSummaryType
    report: Optional[List[Optional[OrderCustomerReportType]]]

class OrderSellerSummaryType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    sellers: Optional[float]

class OrderCustomerReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    userId: Optional[int]
    user: Optional[User]

class InReportOrderSellerSummaryType(BaseModel):
    category: str
    title: str
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: OrderSellerSummaryType
    report: Optional[List[Optional[OrderSellerReportType]]]

class OrderSellerReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    sellerId: Optional[int]
    seller: Optional[Seller]

class InReportOrderMarketplaceSummaryType(BaseModel):
    category: str
    title: str
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: OrderSellerSummaryType
    report: Optional[List[Optional[OrderMarketplaceReportType]]]

class OrderMarketplaceReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    dimension: Optional[date]

class InReportMarketplacePayoutsSummaryType(BaseModel):
    category: str
    title: str
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: OrderSellerSummaryType
    report: Optional[List[Optional[OrderSellerReportType]]]

class InReportMarketplaceTaxSummaryType(BaseModel):
    category: str
    title: str
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: AbstractOrderSellerReportType
    report: Optional[List[Optional[MarketplaceTaxReportType]]]

class AbstractOrderSellerReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]

class MarketplaceTaxReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    dimension: Optional[date]

class InReportMarketplaceTaxesByCountryType(BaseModel):
    category: str
    title: str
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: AbstractOrderSellerReportType
    report: Optional[List[Optional[MarketplaceTaxReportByLocaleType]]]

class MarketplaceTaxReportByLocaleType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    billingAddress_Country: Optional[str]
    billingAddress_CountryArea: Optional[str]
    countryArea: Optional[str]
    country: Optional[str]
    countryName: Optional[str]
    countryAreaName: Optional[str]
    countryState: Optional[CountryState]

class CountryState(BaseModel):
    area: Optional[str]
    areaName: Optional[str]
    country: Optional[str]
    countryName: Optional[str]

class InReportTopPerformingProductsType(BaseModel):
    category: str
    title: str
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: AbstractProductVariantType
    report: Optional[List[Optional[ProductVariantReportType]]]

class AbstractProductVariantType(BaseModel):
    totals: Optional[int]
    grossRevenue: Optional[float]
    quantityOrdered: Optional[int]
    avgPriceGrossAmount: Optional[float]
    maxPriceGrossAmount: Optional[float]
    minPriceGrossAmount: Optional[float]
    revenue: Optional[float]
    avgPrice: Optional[float]
    maxPrice: Optional[float]
    minPrice: Optional[float]

class ProductVariantReportType(BaseModel):
    totals: Optional[int]
    grossRevenue: Optional[float]
    quantityOrdered: Optional[int]
    avgPriceGrossAmount: Optional[float]
    maxPriceGrossAmount: Optional[float]
    minPriceGrossAmount: Optional[float]
    revenue: Optional[float]
    avgPrice: Optional[float]
    maxPrice: Optional[float]
    minPrice: Optional[float]
    productId: int
    product: Product
    name: str
    id: str

class InReportTopPerformingCategoriesType(BaseModel):
    category: str
    title: str
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: AbstractProductVariantType
    report: Optional[List[Optional[ProductCategoryReportType]]]

class ProductCategoryReportType(BaseModel):
    totals: Optional[int]
    grossRevenue: Optional[float]
    quantityOrdered: Optional[int]
    avgPriceGrossAmount: Optional[float]
    maxPriceGrossAmount: Optional[float]
    minPriceGrossAmount: Optional[float]
    revenue: Optional[float]
    avgPrice: Optional[float]
    maxPrice: Optional[float]
    minPrice: Optional[float]
    product_CategoryId: Optional[int]
    category: Optional[Category]

class InReportMarketplacePaymentsSummaryType(BaseModel):
    category: str
    title: str
    columns: Optional[List[Optional[ColumnObjectType]]]
    filters: Optional[List[Optional[FilterObjectType]]]
    summary: AbstractPaymentsType
    report: Optional[List[Optional[PaymentsDayReportType]]]

class AbstractPaymentsType(BaseModel):
    payments: Optional[int]
    totalAuthorized: Optional[float]
    captured: Optional[float]
    average: Optional[float]

class PaymentsDayReportType(BaseModel):
    payments: Optional[int]
    totalAuthorized: Optional[float]
    captured: Optional[float]
    average: Optional[float]
    dimension: Optional[date]
    chargeStatus: Optional[str]

class DashboardOrdersSummaryType(BaseModel):
    filters: Optional[List[Optional[FilterObjectType]]]
    current: Optional[AbstractOrderSellerReportType]
    previous: Optional[AbstractOrderSellerReportType]
    deltas: Optional[OrderSummaryDeltaDataType]
    ordersToFulfill: Optional[int]
    paymentsToProcess: Optional[int]
    returnsToProcess: Optional[int]
    pendingReviews: Optional[int]
    pendingPayouts: Optional[int]

class OrderSummaryDeltaDataType(BaseModel):
    percent: Optional[AbstractPercentReportType]
    values: Optional[AbstractOrderSellerReportType]

class AbstractPercentReportType(BaseModel):
    gross: Optional[float]
    orders: Optional[float]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[float]

class DashboardTopSellerPerformanceType(BaseModel):
    filters: Optional[List[Optional[FilterObjectType]]]
    current: Optional[List[Optional[DashboardSellerOrderPerformanceType]]]
    previous: Optional[List[Optional[DashboardSellerOrderPerformanceType]]]

class DashboardSellerOrderPerformanceType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    sellerId: Optional[int]
    seller: Optional[Seller]

class DashboardGraphType(BaseModel):
    filters: Optional[List[Optional[FilterObjectType]]]
    graph: Optional[List[Optional[GraphDataType]]]

class GraphDataType(BaseModel):
    gross: Optional[float]
    orders: Optional[int]
    net: Optional[float]
    shipping: Optional[float]
    average: Optional[float]
    taxes: Optional[float]
    discounts: Optional[float]
    volumeDiscounts: Optional[float]
    revenue: Optional[float]
    totals: Optional[int]
    commission: Optional[float]
    payout: Optional[float]
    dimension: Optional[datetime]

class FontCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[FontCountableEdge]]
    totalCount: Optional[int]

class FontCountableEdge(BaseModel):
    node: Font
    cursor: str

class JournalEntryCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[JournalEntryCountableEdge]]
    totalCount: Optional[int]

class JournalEntryCountableEdge(BaseModel):
    node: JournalEntry
    cursor: str

class JournalEntry(BaseModel):
    createdAt: datetime
    updatedAt: datetime
    id: str
    description: str
    fulfillmentLine: Optional[FulfillmentLine]
    nauticalOrder: Optional[NauticalOrder]
    order: Optional[Order]
    orderLine: Optional[OrderLine]
    payment: Optional[Payment]
    refund: Optional[Refund]
    refundLine: Optional[RefundLine]
    vendorPayout: Optional[VendorPayout]
    type: JournalEntryTypeEnum
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    ledgerEntries: List[Optional[LedgerEntry]]

class LedgerEntry(BaseModel):
    createdAt: datetime
    updatedAt: datetime
    id: str
    journalEntry: JournalEntry
    ledger: Ledger
    ledgerVersion: int
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    amount: Money
    ledgerBalance: Money

class Ledger(BaseModel):
    id: str
    accountType: LedgerAccountTypeEnum
    balance: Money
    seller: Optional[Seller]
    type: LedgerTypeEnum
    version: int
    privateMetadata: List[Optional[MetadataItem]]
    metadata: List[Optional[MetadataItem]]
    buyer: Optional[User]

class LedgerCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[LedgerCountableEdge]]
    totalCount: Optional[int]

class LedgerCountableEdge(BaseModel):
    node: Ledger
    cursor: str

class SaleCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[SaleCountableEdge]]
    totalCount: Optional[int]

class SaleCountableEdge(BaseModel):
    node: Sale
    cursor: str

class VoucherCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[VoucherCountableEdge]]
    totalCount: Optional[int]

class VoucherCountableEdge(BaseModel):
    node: Voucher
    cursor: str

class DesignerDataType(BaseModel):
    tenant: Tenant
    id: str
    name: str
    jsonContent: str

class ExportFile(BaseModel):
    id: str
    user: Optional[User]
    app: Optional[App]
    status: JobStatusEnum
    createdAt: datetime
    updatedAt: datetime
    message: Optional[str]
    url: Optional[str]
    events: Optional[List[Optional[ExportEvent]]]

class ExportEvent(BaseModel):
    id: str
    date: datetime
    type: ExportEventsEnum
    user: Optional[User]
    app: Optional[App]
    message: str

class ExportFileCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[ExportFileCountableEdge]]
    totalCount: Optional[int]

class ExportFileCountableEdge(BaseModel):
    node: ExportFile
    cursor: str

class CheckoutCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[CheckoutCountableEdge]]
    totalCount: Optional[int]

class CheckoutCountableEdge(BaseModel):
    node: Checkout
    cursor: str

class CheckoutLineCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[CheckoutLineCountableEdge]]
    totalCount: Optional[int]

class CheckoutLineCountableEdge(BaseModel):
    node: CheckoutLine
    cursor: str

class CustomFieldTemplate(BaseModel):
    id: str
    createdAt: datetime
    updatedAt: datetime
    contentType: Optional[CustomFieldTemplateEnum]
    customAttributes: List[Optional[Attribute]]

class AppInstallation(BaseModel):
    appName: str
    manifestUrl: str
    id: str
    status: JobStatusEnum
    createdAt: datetime
    updatedAt: datetime
    message: Optional[str]

class AppCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[AppCountableEdge]]
    totalCount: Optional[int]

class AppCountableEdge(BaseModel):
    node: App
    cursor: str

class AddressValidationData(BaseModel):
    countryCode: Optional[str]
    countryName: Optional[str]
    addressFormat: Optional[str]
    addressLatinFormat: Optional[str]
    allowedFields: Optional[List[Optional[str]]]
    requiredFields: Optional[List[Optional[str]]]
    upperFields: Optional[List[Optional[str]]]
    countryAreaType: Optional[str]
    countryAreaChoices: Optional[List[Optional[ChoiceValue]]]
    cityType: Optional[str]
    cityChoices: Optional[List[Optional[ChoiceValue]]]
    cityAreaType: Optional[str]
    cityAreaChoices: Optional[List[Optional[ChoiceValue]]]
    postalCodeType: Optional[str]
    postalCodeMatchers: Optional[List[Optional[str]]]
    postalCodeExamples: Optional[List[Optional[str]]]
    postalCodePrefix: Optional[str]

class ChoiceValue(BaseModel):
    raw: Optional[str]
    verbose: Optional[str]

class GroupCountableConnection(BaseModel):
    pageInfo: PageInfo
    edges: List[Optional[GroupCountableEdge]]
    totalCount: Optional[int]

class GroupCountableEdge(BaseModel):
    node: Group
    cursor: str

class _Service(BaseModel):
    sdl: Optional[str]

class Mutation(BaseModel):
    id: str
    input: PermissionGroupUpdateInput
    description: Optional[str]
    file: Upload
    relatedObjectId: str
    documentId: str
    ids: List[Optional[str]]
    targetIds: Optional[List[Optional[str]]]
    payoutId: str
    sellerId: Optional[str]
    gateway: str
    vendorPayoutId: str
    wishlistId: Optional[str]
    productId: Optional[str]
    userId: str
    variantId: str
    micrositeId: str
    products: List[Optional[str]]
    moves: List[Optional[ReorderInput]]
    isPublished: bool
    defaultBillingAddress: Optional[AddressInput]
    defaultShippingAddress: Optional[AddressInput]
    seller: str
    user: str
    image: Upload
    banner: Upload
    addressId: str
    type: AddressTypeEnum
    name: str
    shopFetchTaxRates: Optional[ShopFetchTaxRates]
    status: RefundStatusEnum
    lineItems: List[Optional[RefundLineUpdateInput]]
    refundId: Optional[str]
    payments: List[Optional[RefundPaymentUpdateInput]]
    refund: str
    parent: Optional[str]
    collectionId: str
    variants: List[Optional[ProductVariantBulkCreateInput]]
    category: str
    isAvailable: bool
    startDate: Optional[date]
    imagesIds: List[Optional[str]]
    productTypeId: str
    product: str
    stocks: List[Optional[StockInput]]
    warehouseIds: Optional[List[Optional[str]]]
    imageId: str
    transferImageOwnership: Optional[bool]
    locationId: Optional[str]
    amount: PositiveDecimal
    paymentId: Optional[str]
    paymentData: Optional[str]
    token: str
    currency: MarketplaceConfigurationCurrencyEnum
    orderId: str
    nauticalOrderId: str
    order: str
    voucherCode: Optional[str]
    storefrontUrl: str
    keys: List[Optional[str]]
    menu: str
    documentType: Optional[int]
    number: Optional[str]
    refreshUrl: str
    returnUrl: str
    vendorId: str
    vendorType: Optional[str]
    plugin: str
    checkoutId: str
    dashboardEmbeddingToken: Optional[DashboardEmbeddingToken]
    promoCode: str
    billingAddress: AddressInput
    microsite: Optional[str]
    poNumber: str
    redirectUrl: str
    userOverride: Optional[str]
    volumeDiscount: Optional[float]
    email: str
    note: str
    lineId: Optional[str]
    lines: List[Optional[CheckoutLineInput]]
    shippingAddress: AddressInput
    shippingMethodPriceOverrideAmount: Optional[PositiveDecimal]
    shippingMethodSelection: str
    sellerShippingMethods: Optional[List[Optional[SellerShippingMethodInput]]]
    poNumbers: List[Optional[str]]
    operations: List[Optional[AttributeAssignInput]]
    attributeIds: List[Optional[str]]
    template: CustomFieldTemplateEnum
    attributeId: str
    custom: bool
    instanceId: str
    attribute: str
    values: List[Optional[str]]
    oauthProviderSource: OauthProviderSourceEnum
    oauthProviderToken: str
    password: str
    provider: Optional[SsoProviderType]
    accessCode: str
    csrfToken: Optional[str]
    refreshToken: Optional[str]
    tokensDeactivateAll: Optional[DeactivateAllUserTokens]
    newPassword: str
    oldPassword: str
    newEmail: str
    isActive: bool

class EmailTemplateUpdate(BaseModel):
    emailTemplate: Optional[EmailTemplate]
    notificationErrors: List[Optional[NotificationError]]

class NotificationError(BaseModel):
    field: Optional[str]
    message: str
    code: NotificationErrorCode

class TenantUpdate(BaseModel):
    tenant: Optional[Tenant]
    tenantErrors: List[Optional[TenantError]]

class TenantError(BaseModel):
    field: Optional[str]
    message: str
    code: TenantErrorCode

class DocumentAdd(BaseModel):
    document: Optional[Document]
    instances: List[Optional[DocumentTargetInstance]]
    documentErrors: List[Optional[DocumentError]]

class DocumentError(BaseModel):
    field: Optional[str]
    message: str
    code: DocumentErrorCode

class DocumentUpdate(BaseModel):
    document: Optional[Document]
    documentErrors: List[Optional[DocumentError]]

class DocumentAttach(BaseModel):
    document: Optional[Document]
    instances: List[Optional[DocumentTargetInstance]]
    documentErrors: List[Optional[DocumentError]]

class DocumentRemove(BaseModel):
    instances: List[Optional[DocumentTargetInstance]]
    documentErrors: List[Optional[DocumentError]]

class NauticalConfigurationUpdate(BaseModel):
    nauticalConfigurationList: Optional[List[Optional[NauticalConfiguration]]]
    nauticalConfigurationErrors: List[Optional[NauticalConfigurationError]]

class NauticalConfigurationError(BaseModel):
    field: Optional[str]
    message: str
    code: NauticalConfigurationErrorCode

class MarketplaceConfigurationUpdate(BaseModel):
    marketplaceConfiguration: Optional[MarketplaceConfiguration]
    marketplaceConfigurationErrors: List[Optional[MarketplaceConfigurationError]]

class MarketplaceConfigurationError(BaseModel):
    field: Optional[str]
    message: str
    code: MarketplaceConfigurationErrorCode

class PayoutCreate(BaseModel):
    payoutErrors: List[Optional[PayoutError]]
    payout: Optional[Payout]

class PayoutError(BaseModel):
    field: Optional[str]
    message: str
    code: PayoutErrorCode

class PayoutUpdate(BaseModel):
    payout: Optional[Payout]
    payoutErrors: List[Optional[PayoutError]]

class PayoutDelete(BaseModel):
    payoutErrors: List[Optional[PayoutError]]
    payout: Optional[Payout]

class PayoutStatusUpdate(BaseModel):
    payout: Optional[Payout]
    payoutErrors: List[Optional[PayoutError]]

class PayoutDatesUpdate(BaseModel):
    payoutErrors: List[Optional[PayoutError]]
    payout: Optional[Payout]

class PayoutBulkArchive(BaseModel):
    count: int
    payoutErrors: List[Optional[PayoutError]]

class VendorPayoutCreate(BaseModel):
    vendorPayout: Optional[VendorPayout]
    payoutErrors: List[Optional[PayoutError]]

class VendorPayoutStatusUpdate(BaseModel):
    vendorPayout: Optional[VendorPayout]
    payoutErrors: List[Optional[PayoutError]]

class VendorPayoutsBulkInclude(BaseModel):
    count: int
    payoutErrors: List[Optional[PayoutError]]

class VendorPayoutsBulkExclude(BaseModel):
    count: int
    payoutErrors: List[Optional[PayoutError]]

class VendorPayoutsBulkProcess(BaseModel):
    count: int
    payoutErrors: List[Optional[PayoutError]]

class VendorPayoutNoteAdd(BaseModel):
    vendorPayout: Optional[VendorPayout]
    event: Optional[VendorPayoutEvent]
    payoutErrors: List[Optional[PayoutError]]

class VendorPayoutNoteUpdate(BaseModel):
    vendorPayout: Optional[VendorPayout]
    event: Optional[VendorPayoutEvent]
    payoutErrors: List[Optional[PayoutError]]

class WishlistCreate(BaseModel):
    wishlistErrors: List[Optional[WishlistError]]
    wishlist: Optional[Wishlist]

class WishlistError(BaseModel):
    field: Optional[str]
    message: str
    code: WishlistErrorCode

class WishlistCreateForBuyer(BaseModel):
    wishlistErrors: List[Optional[WishlistError]]
    wishlist: Optional[Wishlist]

class WishlistUpdate(BaseModel):
    wishlistErrors: List[Optional[WishlistError]]
    wishlist: Optional[Wishlist]

class WishlistDelete(BaseModel):
    wishlistErrors: List[Optional[WishlistError]]
    wishlist: Optional[Wishlist]

class WishlistSetDefault(BaseModel):
    wishlist: Optional[Wishlist]
    wishlistErrors: List[Optional[WishlistError]]

class WishlistItemUpdate(BaseModel):
    wishlistErrors: List[Optional[WishlistError]]
    wishlistItem: Optional[WishlistItem]

class WishlistAddProduct(BaseModel):
    wishlist: Optional[List[Optional[WishlistItem]]]
    wishlistErrors: List[Optional[WishlistError]]

class WishlistRemoveProduct(BaseModel):
    wishlist: Optional[List[Optional[WishlistItem]]]
    wishlistErrors: List[Optional[WishlistError]]

class WishlistAddProductVariant(BaseModel):
    wishlist: Optional[List[Optional[WishlistItem]]]
    wishlistErrors: List[Optional[WishlistError]]

class WishlistRemoveProductVariant(BaseModel):
    wishlist: Optional[List[Optional[WishlistItem]]]
    wishlistErrors: List[Optional[WishlistError]]

class MicrositeAddProducts(BaseModel):
    microsite: Optional[Microsite]
    micrositeErrors: List[Optional[ProductError]]

class ProductError(BaseModel):
    field: Optional[str]
    message: str
    code: ProductErrorCode
    attributes: Optional[List[Optional[str]]]

class MicrositeCreate(BaseModel):
    micrositeErrors: List[Optional[ProductError]]
    microsite: Optional[Microsite]

class MicrositeDelete(BaseModel):
    micrositeErrors: List[Optional[ProductError]]
    microsite: Optional[Microsite]

class MicrositeReorderProducts(BaseModel):
    microsite: Optional[Microsite]
    micrositeErrors: List[Optional[ProductError]]

class MicrositeBulkDelete(BaseModel):
    count: int
    micrositeErrors: List[Optional[ProductError]]

class MicrositeBulkPublish(BaseModel):
    count: int
    micrositeErrors: List[Optional[ProductError]]

class MicrositeRemoveProducts(BaseModel):
    microsite: Optional[Microsite]
    micrositeErrors: List[Optional[ProductError]]

class MicrositeUpdate(BaseModel):
    micrositeErrors: List[Optional[ProductError]]
    microsite: Optional[Microsite]

class AgreementCreate(BaseModel):
    agreementErrors: List[Optional[AgreementError]]
    agreement: Optional[Agreement]

class AgreementError(BaseModel):
    field: Optional[str]
    message: str
    code: AgreementErrorCode

class AgreementDelete(BaseModel):
    agreementErrors: List[Optional[AgreementError]]
    agreement: Optional[Agreement]

class AgreementBulkDelete(BaseModel):
    count: int
    agreementErrors: List[Optional[AgreementError]]

class AgreementBulkPublish(BaseModel):
    count: int
    agreementErrors: List[Optional[AgreementError]]

class AgreementUpdate(BaseModel):
    agreementErrors: List[Optional[AgreementError]]
    agreement: Optional[Agreement]

class AgreementFeeCreate(BaseModel):
    agreementErrors: List[Optional[AgreementError]]
    agreementFees: Optional[AgreementFees]

class AgreementFeeDelete(BaseModel):
    agreementErrors: List[Optional[AgreementError]]
    agreementFees: Optional[AgreementFees]

class AgreementCommissionCreate(BaseModel):
    agreementErrors: List[Optional[AgreementError]]
    agreementCommission: Optional[AgreementCommission]

class AgreementCommissionDelete(BaseModel):
    agreementErrors: List[Optional[AgreementError]]
    agreementCommission: Optional[AgreementCommission]

class SellerAgreementAcknowledge(BaseModel):
    user: Optional[User]
    agreementErrors: List[Optional[AgreementError]]

class SellerAgreementDecline(BaseModel):
    user: Optional[User]
    agreementErrors: List[Optional[AgreementError]]

class SellerAgreementAssign(BaseModel):
    agreementErrors: List[Optional[AgreementError]]
    sellerAgreement: Optional[AgreementSellers]

class SellerAgreementDelete(BaseModel):
    agreementErrors: List[Optional[AgreementError]]
    agreementSellers: Optional[AgreementSellers]

class SellerWithOwnerCreate(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerError(BaseModel):
    field: Optional[str]
    message: str
    code: SellerErrorCode

class SellerDataCreate(BaseModel):
    ok: Optional[bool]
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerUserMappingCreate(BaseModel):
    ok: Optional[bool]
    sellerUser: Optional[SellerUserType]
    sellerErrors: List[Optional[SellerError]]

class SellerDataUpdate(BaseModel):
    ok: Optional[bool]
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerNoteCreate(BaseModel):
    ok: Optional[bool]
    note: Optional[str]
    sellerErrors: List[Optional[SellerError]]

class SellerLogoUpdate(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerLogoDelete(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerBannerUpdate(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerBannerDelete(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerAddressCreate(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]
    address: Optional[Address]

class SellerAddressUpdate(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]
    address: Optional[Address]

class SellerAddressDelete(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]
    address: Optional[Address]

class SellerAddressSetDefault(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerOwnerDelete(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerShellCreate(BaseModel):
    ok: Optional[bool]
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerSettingsUpdate(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class SellerOnboardingChecklistComplete(BaseModel):
    checklist: Optional[SellerOnboardingChecklist]
    checklistErrors: List[Optional[SellerOnboardingChecklistError]]

class SellerOnboardingChecklistError(BaseModel):
    field: Optional[str]
    message: str
    code: SellerOnboardingChecklistErrorCode

class SellerApplicationUpdate(BaseModel):
    seller: Optional[Seller]
    sellerErrors: List[Optional[SellerError]]

class DesignerDataCreate(BaseModel):
    ok: Optional[bool]
    designerdata: Optional[DesignerDataType]
    designerErrors: List[Optional[MarketplaceConfigurationError]]

class DesignerDataUpdate(BaseModel):
    ok: Optional[bool]
    designerdata: Optional[DesignerDataType]
    designerErrors: List[Optional[MarketplaceConfigurationError]]

class WebhookCreate(BaseModel):
    webhookErrors: List[Optional[WebhookError]]
    webhook: Optional[Webhook]

class WebhookError(BaseModel):
    field: Optional[str]
    message: str
    code: WebhookErrorCode

class WebhookDelete(BaseModel):
    webhookErrors: List[Optional[WebhookError]]
    webhook: Optional[Webhook]

class WebhookUpdate(BaseModel):
    webhookErrors: List[Optional[WebhookError]]
    webhook: Optional[Webhook]

class WarehouseCreate(BaseModel):
    warehouseErrors: List[Optional[WarehouseError]]
    warehouse: Optional[Warehouse]

class WarehouseError(BaseModel):
    field: Optional[str]
    message: str
    code: WarehouseErrorCode

class WarehouseUpdate(BaseModel):
    warehouseErrors: List[Optional[WarehouseError]]
    warehouse: Optional[Warehouse]

class WarehouseDelete(BaseModel):
    warehouseErrors: List[Optional[WarehouseError]]
    warehouse: Optional[Warehouse]

class ContentPageDataCreate(BaseModel):
    contentPageData: Optional[ContentPageData]
    shopErrors: List[Optional[ShopError]]

class ShopError(BaseModel):
    field: Optional[str]
    message: str
    code: ShopErrorCode

class ContentPageDataUpdate(BaseModel):
    contentPageData: Optional[ContentPageData]
    shopErrors: List[Optional[ShopError]]

class ContentCreate(BaseModel):
    content: Optional[Content]
    shopErrors: List[Optional[ShopError]]

class ContentSave(BaseModel):
    content: Optional[Content]
    shopErrors: List[Optional[ShopError]]

class ContentDiscard(BaseModel):
    content: Optional[Content]
    shopErrors: List[Optional[ShopError]]

class ContentPublish(BaseModel):
    content: Optional[Content]
    shopErrors: List[Optional[ShopError]]

class ContentDelete(BaseModel):
    shopErrors: List[Optional[ShopError]]
    content: Optional[Content]

class ContentDuplicate(BaseModel):
    content: Optional[Content]
    shopErrors: List[Optional[ShopError]]

class MediaCreate(BaseModel):
    media: Optional[Media]
    shopErrors: List[Optional[ShopError]]

class MediaUpdate(BaseModel):
    media: Optional[Media]
    shopErrors: List[Optional[ShopError]]

class MediaBulkDelete(BaseModel):
    count: int
    shopErrors: List[Optional[ShopError]]

class ShopDomainUpdate(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class ShopSettingsUpdate(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class ShopFetchTaxRates(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class ShopAddressUpdate(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class CheckoutThemeCreate(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class CheckoutThemeUpdate(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class CustomDomainCreate(BaseModel):
    domain: Optional[CustomDomain]
    shopErrors: List[Optional[ShopError]]

class CustomDomainDelete(BaseModel):
    shopErrors: List[Optional[ShopError]]
    domain: Optional[CustomDomain]

class StorefrontThemeCreate(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class StorefrontThemeUpdate(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class SellerOnboardingSettingsCreate(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class SellerOnboardingSettingsUpdate(BaseModel):
    shop: Optional[Shop]
    shopErrors: List[Optional[ShopError]]

class ShippingPriceCreate(BaseModel):
    shippingZone: Optional[ShippingZone]
    shippingErrors: List[Optional[ShippingError]]
    shippingMethod: Optional[ShippingMethod]

class ShippingError(BaseModel):
    field: Optional[str]
    message: str
    code: ShippingErrorCode
    warehouses: Optional[List[Optional[str]]]

class ShippingPriceDelete(BaseModel):
    shippingMethod: Optional[ShippingMethod]
    shippingZone: Optional[ShippingZone]
    shippingErrors: List[Optional[ShippingError]]

class ShippingPriceBulkDelete(BaseModel):
    count: int
    shippingErrors: List[Optional[ShippingError]]

class ShippingPriceUpdate(BaseModel):
    shippingZone: Optional[ShippingZone]
    shippingErrors: List[Optional[ShippingError]]
    shippingMethod: Optional[ShippingMethod]

class ShippingZoneCreate(BaseModel):
    shippingErrors: List[Optional[ShippingError]]
    shippingZone: Optional[ShippingZone]

class ShippingZoneDelete(BaseModel):
    shippingErrors: List[Optional[ShippingError]]
    shippingZone: Optional[ShippingZone]

class ShippingZoneBulkDelete(BaseModel):
    count: int
    shippingErrors: List[Optional[ShippingError]]

class ShippingZoneUpdate(BaseModel):
    shippingErrors: List[Optional[ShippingError]]
    shippingZone: Optional[ShippingZone]

class RefundCreate(BaseModel):
    refundErrors: List[Optional[RefundError]]
    refund: Optional[Refund]

class RefundError(BaseModel):
    field: Optional[str]
    message: str
    code: RefundErrorCode

class RefundUpdate(BaseModel):
    refundErrors: List[Optional[RefundError]]
    refund: Optional[Refund]

class RefundBulkDelete(BaseModel):
    count: int
    refundErrors: List[Optional[RefundError]]

class RefundsChangeStatus(BaseModel):
    count: int
    refundErrors: List[Optional[RefundError]]

class RefundLinesAdd(BaseModel):
    refund: Optional[Refund]
    refundErrors: List[Optional[RefundError]]

class RefundLinesUpdate(BaseModel):
    refund: Optional[Refund]
    refundErrors: List[Optional[RefundError]]

class RefundLineBulkDelete(BaseModel):
    count: int
    refundErrors: List[Optional[RefundError]]

class RefundPaymentsAdd(BaseModel):
    refund: Optional[Refund]
    refundErrors: List[Optional[RefundError]]

class RefundPaymentsUpdate(BaseModel):
    refund: Optional[Refund]
    refundErrors: List[Optional[RefundError]]

class RefundPaymentsDelete(BaseModel):
    count: int
    refundErrors: List[Optional[RefundError]]

class PriceBookCreate(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBook: Optional[PriceBook]

class PriceBookError(BaseModel):
    field: Optional[str]
    message: str
    code: PriceBookErrorCode

class PriceBookUpdate(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBook: Optional[PriceBook]

class PriceBookDelete(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBook: Optional[PriceBook]

class PriceBookBulkDelete(BaseModel):
    count: int
    priceBookErrors: List[Optional[PriceBookError]]

class PriceBookVariantCreate(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBookVariant: Optional[PriceBookVariant]

class PriceBookVariantUpdate(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBookVariant: Optional[PriceBookVariant]

class PriceBookVariantDelete(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBookVariant: Optional[PriceBookVariant]

class PriceBookVariantBulkDelete(BaseModel):
    count: int
    priceBookErrors: List[Optional[PriceBookError]]

class PriceBookProductCreate(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBookProduct: Optional[PriceBookProduct]

class PriceBookProductUpdate(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBookProduct: Optional[PriceBookProduct]

class PriceBookProductDelete(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBookProduct: Optional[PriceBookProduct]

class PriceBookProductBulkDelete(BaseModel):
    count: int
    priceBookErrors: List[Optional[PriceBookError]]

class PriceBookProductTypeCreate(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBookProductType: Optional[PriceBookProductType]

class PriceBookProductTypeUpdate(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBookProductType: Optional[PriceBookProductType]

class PriceBookProductTypeDelete(BaseModel):
    priceBookErrors: List[Optional[PriceBookError]]
    priceBookProductType: Optional[PriceBookProductType]

class PriceBookProductTypeBulkDelete(BaseModel):
    count: int
    priceBookErrors: List[Optional[PriceBookError]]

class UserAddToPriceBook(BaseModel):
    user: Optional[User]
    priceBookErrors: List[Optional[PriceBookError]]

class UserRemoveFromPriceBook(BaseModel):
    user: Optional[User]
    priceBookErrors: List[Optional[PriceBookError]]

class CategoryCreate(BaseModel):
    productErrors: List[Optional[ProductError]]
    category: Optional[Category]

class CategoryDelete(BaseModel):
    productErrors: List[Optional[ProductError]]
    category: Optional[Category]

class CategoryBulkDelete(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class CategoryUpdate(BaseModel):
    productErrors: List[Optional[ProductError]]
    category: Optional[Category]

class CollectionAddProducts(BaseModel):
    collection: Optional[Collection]
    productErrors: List[Optional[ProductError]]

class CollectionAddVariants(BaseModel):
    collection: Optional[Collection]
    productErrors: List[Optional[ProductError]]

class CollectionCreate(BaseModel):
    productErrors: List[Optional[ProductError]]
    collection: Optional[Collection]

class CollectionDelete(BaseModel):
    productErrors: List[Optional[ProductError]]
    collection: Optional[Collection]

class CollectionReorderProducts(BaseModel):
    collection: Optional[Collection]
    productErrors: List[Optional[ProductError]]

class CollectionBulkDelete(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class CollectionBulkPublish(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class CollectionRemoveProducts(BaseModel):
    collection: Optional[Collection]
    productErrors: List[Optional[ProductError]]

class CollectionRemoveVariants(BaseModel):
    collection: Optional[Collection]
    productErrors: List[Optional[ProductError]]

class CollectionUpdate(BaseModel):
    productErrors: List[Optional[ProductError]]
    collection: Optional[Collection]

class ProductCreate(BaseModel):
    productErrors: List[Optional[ProductError]]
    product: Optional[Product]

class ProductDelete(BaseModel):
    productErrors: List[Optional[ProductError]]
    product: Optional[Product]

class ProductBulkDelete(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class ProductBulkPublish(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class ProductBulkCategoryUpdate(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class ProductUpdate(BaseModel):
    productErrors: List[Optional[ProductError]]
    product: Optional[Product]

class ProductSetAvailabilityForPurchase(BaseModel):
    product: Optional[Product]
    productErrors: List[Optional[ProductError]]

class ProductImageCreate(BaseModel):
    product: Optional[Product]
    image: Optional[ProductImage]
    productErrors: List[Optional[ProductError]]

class ProductReorderVariants(BaseModel):
    product: Optional[Product]
    productErrors: List[Optional[ProductError]]

class ProductImageDelete(BaseModel):
    product: Optional[Product]
    image: Optional[ProductImage]
    productErrors: List[Optional[ProductError]]

class ProductImageBulkDelete(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class ProductImageReorder(BaseModel):
    product: Optional[Product]
    images: Optional[List[Optional[ProductImage]]]
    productErrors: List[Optional[ProductError]]

class ProductImageUpdate(BaseModel):
    product: Optional[Product]
    image: Optional[ProductImage]
    productErrors: List[Optional[ProductError]]

class ProductTypeCreate(BaseModel):
    productErrors: List[Optional[ProductError]]
    productType: Optional[ProductType]

class ProductTypeDelete(BaseModel):
    productErrors: List[Optional[ProductError]]
    productType: Optional[ProductType]

class ProductTypeBulkDelete(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class ProductTypeUpdate(BaseModel):
    productErrors: List[Optional[ProductError]]
    productType: Optional[ProductType]

class ProductTypeReorderAttributes(BaseModel):
    productType: Optional[ProductType]
    productErrors: List[Optional[ProductError]]

class DigitalContentCreate(BaseModel):
    variant: Optional[ProductVariant]
    content: Optional[DigitalContent]
    productErrors: List[Optional[ProductError]]

class DigitalContentDelete(BaseModel):
    variant: Optional[ProductVariant]
    productErrors: List[Optional[ProductError]]

class DigitalContentUpdate(BaseModel):
    variant: Optional[ProductVariant]
    content: Optional[DigitalContent]
    productErrors: List[Optional[ProductError]]

class DigitalContentUrlCreate(BaseModel):
    productErrors: List[Optional[ProductError]]
    digitalContentUrl: Optional[DigitalContentUrl]

class ProductVariantCreate(BaseModel):
    productErrors: List[Optional[ProductError]]
    productVariant: Optional[ProductVariant]

class ProductVariantDelete(BaseModel):
    productErrors: List[Optional[ProductError]]
    productVariant: Optional[ProductVariant]

class ProductVariantBulkCreate(BaseModel):
    count: int
    productVariants: List[Optional[ProductVariant]]
    bulkProductErrors: List[Optional[BulkProductError]]

class BulkProductError(BaseModel):
    field: Optional[str]
    message: str
    code: ProductErrorCode
    attributes: Optional[List[Optional[str]]]
    index: Optional[int]
    warehouses: Optional[List[Optional[str]]]

class ProductVariantBulkDelete(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class ProductVariantStocksCreate(BaseModel):
    productVariant: Optional[ProductVariant]
    bulkStockErrors: List[Optional[BulkStockError]]

class BulkStockError(BaseModel):
    field: Optional[str]
    message: str
    code: ProductErrorCode
    attributes: Optional[List[Optional[str]]]
    index: Optional[int]

class ProductVariantStocksDelete(BaseModel):
    productVariant: Optional[ProductVariant]
    stockErrors: List[Optional[StockError]]

class StockError(BaseModel):
    field: Optional[str]
    message: str
    code: StockErrorCode

class ProductVariantStocksUpdate(BaseModel):
    productVariant: Optional[ProductVariant]
    bulkStockErrors: List[Optional[BulkStockError]]

class ProductVariantUpdate(BaseModel):
    productErrors: List[Optional[ProductError]]
    productVariant: Optional[ProductVariant]

class ProductVariantSetDefault(BaseModel):
    product: Optional[Product]
    productErrors: List[Optional[ProductError]]

class ProductVariantImageAssign(BaseModel):
    productVariant: Optional[ProductVariant]
    image: Optional[ProductImage]
    productErrors: List[Optional[ProductError]]

class ProductVariantImageUnassign(BaseModel):
    productVariant: Optional[ProductVariant]
    image: Optional[ProductImage]
    productErrors: List[Optional[ProductError]]

class FeatureCreate(BaseModel):
    feature: Optional[Feature]
    productErrors: List[Optional[ProductError]]

class FeatureUpdate(BaseModel):
    feature: Optional[Feature]
    productErrors: List[Optional[ProductError]]

class FeatureDelete(BaseModel):
    product: Optional[Product]
    variant: Optional[ProductVariant]
    productErrors: List[Optional[ProductError]]

class ProductTypeFeatureCreate(BaseModel):
    productType: Optional[ProductType]
    productErrors: List[Optional[ProductError]]

class ProductTypeFeatureUpdate(BaseModel):
    productType: Optional[ProductType]
    productErrors: List[Optional[ProductError]]

class ProductTypeFeatureDelete(BaseModel):
    productType: Optional[ProductType]
    productErrors: List[Optional[ProductError]]

class ProductLocationCreate(BaseModel):
    product: Optional[Product]
    location: Optional[Location]
    productErrors: List[Optional[ProductError]]

class ProductLocationUpdate(BaseModel):
    product: Optional[Product]
    location: Optional[Location]
    productErrors: List[Optional[ProductError]]

class ProductLocationDelete(BaseModel):
    product: Optional[Product]
    productErrors: List[Optional[ProductError]]

class ProductSetLocationType(BaseModel):
    product: Optional[Product]
    location: Optional[Location]
    productErrors: List[Optional[ProductError]]

class PaymentCapture(BaseModel):
    payment: Optional[Payment]
    paymentErrors: List[Optional[PaymentError]]

class PaymentError(BaseModel):
    field: Optional[str]
    message: str
    code: PaymentErrorCode

class PaymentVoid(BaseModel):
    payment: Optional[Payment]
    paymentErrors: List[Optional[PaymentError]]

class PageCreate(BaseModel):
    pageErrors: List[Optional[PageError]]
    page: Optional[Page]

class PageError(BaseModel):
    field: Optional[str]
    message: str
    code: PageErrorCode

class PageDelete(BaseModel):
    pageErrors: List[Optional[PageError]]
    page: Optional[Page]

class PageBulkDelete(BaseModel):
    count: int
    pageErrors: List[Optional[PageError]]

class PageBulkPublish(BaseModel):
    count: int
    pageErrors: List[Optional[PageError]]

class PageUpdate(BaseModel):
    pageErrors: List[Optional[PageError]]
    page: Optional[Page]

class DraftOrderComplete(BaseModel):
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class OrderError(BaseModel):
    field: Optional[str]
    message: str
    code: OrderErrorCode
    warehouse: Optional[str]
    orderLine: Optional[str]
    variant: Optional[str]

class NauticalDraftOrderComplete(BaseModel):
    order: Optional[NauticalOrder]
    sellerOrders: Optional[List[Optional[Order]]]
    orderErrors: List[Optional[OrderError]]

class DraftOrderSetTransactionCurrency(BaseModel):
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class NauticalDraftOrderSetTransactionCurrency(BaseModel):
    nauticalOrder: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class DraftOrderCreate(BaseModel):
    orderErrors: List[Optional[OrderError]]
    order: Optional[Order]

class NauticalDraftOrderCreate(BaseModel):
    orderErrors: List[Optional[OrderError]]
    nauticalOrder: Optional[NauticalOrder]

class NauticalHistoricalOrderCreate(BaseModel):
    orderErrors: List[Optional[OrderError]]
    nauticalOrder: Optional[NauticalOrder]

class DraftOrderDelete(BaseModel):
    orderErrors: List[Optional[OrderError]]
    order: Optional[Order]

class NauticalDraftOrderDelete(BaseModel):
    orderErrors: List[Optional[OrderError]]
    nauticalOrder: Optional[NauticalOrder]

class DraftOrderBulkDelete(BaseModel):
    count: int
    orderErrors: List[Optional[OrderError]]

class NauticalDraftOrderBulkDelete(BaseModel):
    count: int
    orderErrors: List[Optional[OrderError]]

class DraftOrderLinesBulkDelete(BaseModel):
    count: int
    orderErrors: List[Optional[OrderError]]

class NauticalDraftOrderLinesBulkDelete(BaseModel):
    count: int
    orderErrors: List[Optional[OrderError]]

class DraftOrderLinesCreate(BaseModel):
    order: Optional[Order]
    orderLines: Optional[List[Optional[OrderLine]]]
    orderErrors: List[Optional[OrderError]]

class NauticalDraftOrderLinesCreate(BaseModel):
    order: Optional[NauticalOrder]
    orderLines: Optional[List[Optional[NauticalOrderLine]]]
    orderErrors: List[Optional[OrderError]]

class DraftOrderLineDelete(BaseModel):
    order: Optional[Order]
    orderLine: Optional[OrderLine]
    orderErrors: List[Optional[OrderError]]

class NauticalDraftOrderLineDelete(BaseModel):
    order: Optional[NauticalOrder]
    orderLine: Optional[NauticalOrderLine]
    orderErrors: List[Optional[OrderError]]

class DraftOrderLineUpdate(BaseModel):
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]
    orderLine: Optional[OrderLine]

class NauticalDraftOrderLineUpdate(BaseModel):
    order: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]
    nauticalOrderLine: Optional[NauticalOrderLine]

class DraftOrderUpdate(BaseModel):
    orderErrors: List[Optional[OrderError]]
    order: Optional[Order]

class NauticalDraftOrderUpdate(BaseModel):
    orderErrors: List[Optional[OrderError]]
    nauticalOrder: Optional[NauticalOrder]

class DraftOrderLinePriceOverride(BaseModel):
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]
    orderLine: Optional[OrderLine]

class NauticalDraftOrderLinePriceOverride(BaseModel):
    nauticalOrder: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]
    nauticalOrderLine: Optional[NauticalOrderLine]

class OrderAddNote(BaseModel):
    order: Optional[Order]
    event: Optional[OrderEvent]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderAddNote(BaseModel):
    order: Optional[NauticalOrder]
    event: Optional[NauticalOrderEvent]
    orderErrors: List[Optional[OrderError]]

class OrderLineAddNote(BaseModel):
    orderErrors: List[Optional[OrderError]]
    orderLine: Optional[OrderLine]

class NauticalOrderLineAddNote(BaseModel):
    orderErrors: List[Optional[OrderError]]
    nauticalOrderLine: Optional[NauticalOrderLine]

class OrderReturnNotification(BaseModel):
    order: Optional[Order]
    event: Optional[OrderEvent]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderRefreshTaxes(BaseModel):
    nauticalOrder: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderUpdateApplyVoucherCode(BaseModel):
    nauticalOrder: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderUpdateDeleteDiscount(BaseModel):
    nauticalOrder: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderReturnNotification(BaseModel):
    order: Optional[NauticalOrder]
    event: Optional[NauticalOrderEvent]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderReturnFromStorefrontNotification(BaseModel):
    order: Optional[NauticalOrder]
    event: Optional[NauticalOrderEvent]
    orderErrors: List[Optional[OrderError]]

class VendorOrderReturnFromStorefrontNotification(BaseModel):
    order: Optional[Order]
    event: Optional[List[Optional[OrderEvent]]]
    orderErrors: List[Optional[OrderError]]

class OrderCancel(BaseModel):
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderCancel(BaseModel):
    order: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class NauticalQuoteOrderCancel(BaseModel):
    order: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderCapture(BaseModel):
    order: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class OrderFulfill(BaseModel):
    fulfillments: Optional[List[Optional[Fulfillment]]]
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class OrderDeclineFulfillment(BaseModel):
    fulfillments: Optional[List[Optional[Fulfillment]]]
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class FulfillmentCancel(BaseModel):
    fulfillment: Optional[Fulfillment]
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class FulfillmentReturn(BaseModel):
    fulfillment: Optional[Fulfillment]
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class FulfillmentUpdateTracking(BaseModel):
    fulfillment: Optional[Fulfillment]
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class FulfillmentReturnStatusBulkUpdate(BaseModel):
    fulfillment: Optional[Fulfillment]
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class FulfillmentBulkReturn(BaseModel):
    fulfillments: Optional[List[Optional[Fulfillment]]]
    orderErrors: List[Optional[OrderError]]

class OrderMarkAsDelivered(BaseModel):
    orderErrors: List[Optional[OrderError]]
    order: Optional[Order]

class NauticalOrderMarkAsPaid(BaseModel):
    order: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class OrderUpdate(BaseModel):
    orderErrors: List[Optional[OrderError]]
    order: Optional[Order]

class NauticalOrderUpdate(BaseModel):
    orderErrors: List[Optional[OrderError]]
    nauticalOrder: Optional[NauticalOrder]

class OrderPayoutStatusUpdate(BaseModel):
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class OrderUpdateShipping(BaseModel):
    order: Optional[Order]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderUpdateShipping(BaseModel):
    order: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderUpdateMarketplaceShipping(BaseModel):
    order: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderVoid(BaseModel):
    order: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class OrderBulkCancel(BaseModel):
    count: int
    orderErrors: List[Optional[OrderError]]

class NauticalOrderLineBulkCancel(BaseModel):
    count: int
    order: Optional[NauticalOrder]

class NauticalOrderPaymentCreate(BaseModel):
    order: Optional[NauticalOrder]
    payment: Optional[Payment]
    paymentErrors: List[Optional[PaymentError]]

class NauticalQuoteOrderSendToCustomer(BaseModel):
    order: Optional[NauticalOrder]
    orderErrors: List[Optional[OrderError]]

class OrderFeeCreate(BaseModel):
    orderFee: Optional[OrderFee]
    orderErrors: List[Optional[OrderError]]

class OrderFeeDelete(BaseModel):
    orderFee: Optional[OrderFee]
    orderErrors: List[Optional[OrderError]]

class NauticalOrderLinesCsvUpload(BaseModel):
    nauticalOrder: Optional[NauticalOrder]
    csvFile: Optional[ImportFile]
    successfulLines: Optional[int]
    failedLines: Optional[int]
    orderErrors: List[Optional[OrderError]]

class ImportFile(BaseModel):
    id: str
    user: Optional[User]
    app: Optional[App]
    status: JobStatusEnum
    createdAt: datetime
    updatedAt: datetime
    message: Optional[str]
    url: Optional[str]
    events: Optional[List[Optional[ImportEvent]]]

class ImportEvent(BaseModel):
    id: str
    date: datetime
    type: ImportEventsEnum
    user: Optional[User]
    app: Optional[App]
    message: str

class OrderLinesCsvUpload(BaseModel):
    order: Optional[Order]
    csvFile: Optional[ImportFile]
    successfulLines: Optional[int]
    failedLines: Optional[int]
    orderErrors: List[Optional[OrderError]]

class MetadataDelete(BaseModel):
    metadataErrors: List[Optional[MetadataError]]
    item: Optional[ObjectWithMetadata]

class MetadataError(BaseModel):
    field: Optional[str]
    message: str
    code: MetadataErrorCode

class PrivateMetadataDelete(BaseModel):
    metadataErrors: List[Optional[MetadataError]]
    item: Optional[ObjectWithMetadata]

class MetadataUpdate(BaseModel):
    metadataErrors: List[Optional[MetadataError]]
    item: Optional[ObjectWithMetadata]

class PrivateMetadataUpdate(BaseModel):
    metadataErrors: List[Optional[MetadataError]]
    item: Optional[ObjectWithMetadata]

class MenuCreate(BaseModel):
    menuErrors: List[Optional[MenuError]]
    menu: Optional[Menu]

class MenuError(BaseModel):
    field: Optional[str]
    message: str
    code: MenuErrorCode

class MenuDelete(BaseModel):
    menuErrors: List[Optional[MenuError]]
    menu: Optional[Menu]

class MenuBulkDelete(BaseModel):
    count: int
    menuErrors: List[Optional[MenuError]]

class MenuUpdate(BaseModel):
    menuErrors: List[Optional[MenuError]]
    menu: Optional[Menu]

class MenuItemCreate(BaseModel):
    menuErrors: List[Optional[MenuError]]
    menuItem: Optional[MenuItem]

class MenuItemDelete(BaseModel):
    menuErrors: List[Optional[MenuError]]
    menuItem: Optional[MenuItem]

class MenuItemBulkDelete(BaseModel):
    count: int
    menuErrors: List[Optional[MenuError]]

class MenuItemUpdate(BaseModel):
    menuErrors: List[Optional[MenuError]]
    menuItem: Optional[MenuItem]

class MenuItemMove(BaseModel):
    menu: Optional[Menu]
    menuErrors: List[Optional[MenuError]]

class InvoiceRequest(BaseModel):
    order: Optional[Order]
    nauticalOrder: Optional[NauticalOrder]
    refund: Optional[Refund]
    invoiceErrors: List[Optional[InvoiceError]]
    invoice: Optional[Invoice]

class InvoiceError(BaseModel):
    field: Optional[str]
    message: str
    code: InvoiceErrorCode

class InvoiceRequestDelete(BaseModel):
    invoiceErrors: List[Optional[InvoiceError]]
    invoice: Optional[Invoice]

class InvoiceCreate(BaseModel):
    invoiceErrors: List[Optional[InvoiceError]]
    invoice: Optional[Invoice]

class InvoiceDelete(BaseModel):
    invoiceErrors: List[Optional[InvoiceError]]
    invoice: Optional[Invoice]

class InvoiceUpdate(BaseModel):
    invoiceErrors: List[Optional[InvoiceError]]
    invoice: Optional[Invoice]

class InvoiceSendNotification(BaseModel):
    invoiceErrors: List[Optional[InvoiceError]]
    invoice: Optional[Invoice]

class InvoiceRefresh(BaseModel):
    order: Optional[Order]
    nauticalOrder: Optional[NauticalOrder]
    invoiceErrors: List[Optional[InvoiceError]]
    invoice: Optional[Invoice]

class InvoiceFinalize(BaseModel):
    invoiceErrors: List[Optional[InvoiceError]]
    invoice: Optional[Invoice]

class InvoiceCancel(BaseModel):
    invoiceErrors: List[Optional[InvoiceError]]
    invoice: Optional[Invoice]

class PluginUpdate(BaseModel):
    plugin: Optional[Plugin]
    pluginsErrors: List[Optional[PluginError]]

class PluginError(BaseModel):
    field: Optional[str]
    message: str
    code: PluginErrorCode

class CatalogImport(BaseModel):
    ok: Optional[bool]
    plugin: Optional[str]
    pluginsErrors: List[Optional[PluginError]]

class CatalogExport(BaseModel):
    ok: Optional[bool]
    plugin: Optional[str]
    pluginsErrors: List[Optional[PluginError]]

class CustomersExport(BaseModel):
    ok: Optional[bool]
    plugin: Optional[str]
    pluginsErrors: List[Optional[PluginError]]

class PluginFlowUpdate(BaseModel):
    flow: Optional[Flow]
    pluginsErrors: List[Optional[PluginError]]

class PluginFlowDelete(BaseModel):
    pluginsErrors: List[Optional[PluginError]]

class VendorPayoutOnboardingLinkRequest(BaseModel):
    link: Optional[str]
    vendor: Optional[Vendor]
    pluginsErrors: List[Optional[PluginError]]

class ExchangeRatesRefresh(BaseModel):
    pluginsErrors: List[Optional[PluginError]]

class CheckoutEventTriggered(BaseModel):
    checkoutEvent: Optional[CheckoutEvent]
    pluginsErrors: List[Optional[PluginError]]

class JournalEntryCorrect(BaseModel):
    financialErrors: List[Optional[FinancialError]]
    journalEntry: Optional[JournalEntry]

class FinancialError(BaseModel):
    field: Optional[str]
    message: str
    code: FinancialErrorCode

class SaleCreate(BaseModel):
    discountErrors: List[Optional[DiscountError]]
    sale: Optional[Sale]

class DiscountError(BaseModel):
    field: Optional[str]
    message: str
    code: DiscountErrorCode

class SaleDelete(BaseModel):
    discountErrors: List[Optional[DiscountError]]
    sale: Optional[Sale]

class SaleBulkDelete(BaseModel):
    count: int
    discountErrors: List[Optional[DiscountError]]

class SaleUpdate(BaseModel):
    discountErrors: List[Optional[DiscountError]]
    sale: Optional[Sale]

class SaleAddCatalogues(BaseModel):
    sale: Optional[Sale]
    discountErrors: List[Optional[DiscountError]]

class SaleRemoveCatalogues(BaseModel):
    sale: Optional[Sale]
    discountErrors: List[Optional[DiscountError]]

class VoucherCreate(BaseModel):
    discountErrors: List[Optional[DiscountError]]
    voucher: Optional[Voucher]

class VoucherDelete(BaseModel):
    discountErrors: List[Optional[DiscountError]]
    voucher: Optional[Voucher]

class VoucherBulkDelete(BaseModel):
    count: int
    discountErrors: List[Optional[DiscountError]]

class VoucherUpdate(BaseModel):
    discountErrors: List[Optional[DiscountError]]
    voucher: Optional[Voucher]

class VoucherAddCatalogues(BaseModel):
    voucher: Optional[Voucher]
    discountErrors: List[Optional[DiscountError]]

class VoucherRemoveCatalogues(BaseModel):
    voucher: Optional[Voucher]
    discountErrors: List[Optional[DiscountError]]

class DashboardEmbeddingToken(BaseModel):
    token: Optional[str]

class ProductsExport(BaseModel):
    exportFile: Optional[ExportFile]
    exportErrors: List[Optional[ExportError]]

class ExportError(BaseModel):
    field: Optional[str]
    message: str
    code: ExportErrorCode

class ProductsImport(BaseModel):
    importFile: Optional[ImportFile]
    importErrors: List[Optional[ImportError]]

class ImportError(BaseModel):
    field: Optional[str]
    message: str
    code: ImportErrorCode

class CheckoutAddPromoCode(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutError(BaseModel):
    field: Optional[str]
    message: str
    code: CheckoutErrorCode
    variants: Optional[List[Optional[str]]]

class CheckoutBillingAddressUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutComplete(BaseModel):
    order: Optional[NauticalOrder]
    confirmationNeeded: bool
    confirmationData: Optional[str]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutConvertToNauticalQuoteOrder(BaseModel):
    order: Optional[NauticalOrder]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutCreate(BaseModel):
    created: Optional[bool]
    checkoutErrors: List[Optional[CheckoutError]]
    checkout: Optional[Checkout]

class CheckoutCustomerAttach(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutCustomerDetach(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutEmailUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutSetTransactionCurrency(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutNoteUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutLineDelete(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutLinesAdd(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutLinesUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutRemovePromoCode(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutPaymentCreate(BaseModel):
    checkout: Optional[Checkout]
    payment: Optional[Payment]
    paymentErrors: List[Optional[PaymentError]]

class CheckoutShippingAddressUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutSellerShippingMethodsUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutMarketplaceShippingMethodUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutSellerShippingMethodsBulkUpdate(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutSellerShippingMethodsClear(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutDelete(BaseModel):
    checkoutErrors: List[Optional[CheckoutError]]
    checkout: Optional[Checkout]

class CheckoutAddPONumbers(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutRemovePONumbers(BaseModel):
    checkout: Optional[Checkout]
    checkoutErrors: List[Optional[CheckoutError]]

class CheckoutLineAddNote(BaseModel):
    checkoutErrors: List[Optional[CheckoutError]]
    checkoutLine: Optional[CheckoutLine]

class AttributeCreate(BaseModel):
    attribute: Optional[Attribute]
    productErrors: List[Optional[ProductError]]

class AttributeDelete(BaseModel):
    productErrors: List[Optional[ProductError]]
    attribute: Optional[Attribute]

class AttributeBulkDelete(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class AttributeAssign(BaseModel):
    productType: Optional[ProductType]
    productErrors: List[Optional[ProductError]]

class AttributeUnassign(BaseModel):
    productType: Optional[ProductType]
    productErrors: List[Optional[ProductError]]

class AttributeUpdate(BaseModel):
    attribute: Optional[Attribute]
    productErrors: List[Optional[ProductError]]

class CustomAttributeAssign(BaseModel):
    customFieldTemplate: Optional[CustomFieldTemplate]
    attributeErrors: List[Optional[ProductError]]

class CustomAttributeUnassign(BaseModel):
    customFieldTemplate: Optional[CustomFieldTemplate]
    attributeErrors: List[Optional[ProductError]]

class InstanceAttributeUnassign(BaseModel):
    instance: Optional[CustomFieldInstance]
    attributeErrors: List[Optional[AttributeError]]

class AttributeError(BaseModel):
    field: Optional[str]
    message: str
    code: ProductErrorCode
    values: Optional[List[Optional[str]]]

class AttributeValueCreate(BaseModel):
    attribute: Optional[Attribute]
    productErrors: List[Optional[ProductError]]
    attributeValue: Optional[AttributeValue]

class AttributeValueDelete(BaseModel):
    attribute: Optional[Attribute]
    productErrors: List[Optional[ProductError]]
    attributeValue: Optional[AttributeValue]

class AttributeValueBulkCreate(BaseModel):
    count: int
    attributeValues: List[Optional[AttributeValue]]
    attributeErrors: List[Optional[AttributeError]]

class AttributeValueBulkDelete(BaseModel):
    count: int
    productErrors: List[Optional[ProductError]]

class AttributeValueUpdate(BaseModel):
    attribute: Optional[Attribute]
    productErrors: List[Optional[ProductError]]
    attributeValue: Optional[AttributeValue]

class AttributeValuesReorder(BaseModel):
    attribute: Optional[Attribute]
    productErrors: List[Optional[ProductError]]

class AppCreate(BaseModel):
    authToken: Optional[str]
    appErrors: List[Optional[AppError]]
    app: Optional[App]

class AppError(BaseModel):
    field: Optional[str]
    message: str
    code: AppErrorCode
    permissions: Optional[List[Optional[PermissionEnum]]]

class AppUpdate(BaseModel):
    appErrors: List[Optional[AppError]]
    app: Optional[App]

class AppDelete(BaseModel):
    appErrors: List[Optional[AppError]]
    app: Optional[App]

class AppTokenCreate(BaseModel):
    authToken: Optional[str]
    appErrors: List[Optional[AppError]]
    appToken: Optional[AppToken]

class AppTokenDelete(BaseModel):
    appErrors: List[Optional[AppError]]
    appToken: Optional[AppToken]

class AppTokenVerify(BaseModel):
    valid: bool
    appErrors: List[Optional[AppError]]

class AppInstall(BaseModel):
    appErrors: List[Optional[AppError]]
    appInstallation: Optional[AppInstallation]

class AppRetryInstall(BaseModel):
    appErrors: List[Optional[AppError]]
    appInstallation: Optional[AppInstallation]

class AppDeleteFailedInstallation(BaseModel):
    appErrors: List[Optional[AppError]]
    appInstallation: Optional[AppInstallation]

class AppFetchManifest(BaseModel):
    manifest: Optional[Manifest]
    appErrors: List[Optional[AppError]]

class Manifest(BaseModel):
    identifier: str
    version: str
    name: str
    about: Optional[str]
    permissions: Optional[List[Optional[Permission]]]
    appUrl: Optional[str]
    configurationUrl: Optional[str]
    tokenTargetUrl: Optional[str]
    dataPrivacy: Optional[str]
    dataPrivacyUrl: Optional[str]
    homepageUrl: Optional[str]
    supportUrl: Optional[str]

class AppActivate(BaseModel):
    appErrors: List[Optional[AppError]]
    app: Optional[App]

class AppDeactivate(BaseModel):
    appErrors: List[Optional[AppError]]
    app: Optional[App]

class CreateCustomerToken(BaseModel):
    nauticalToken: Optional[str]
    refreshToken: Optional[str]
    authErrors: List[Optional[AuthError]]

class AuthError(BaseModel):
    field: Optional[str]
    message: str
    code: str

class CreateToken(BaseModel):
    token: Optional[str]
    refreshToken: Optional[str]
    csrfToken: Optional[str]
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class AccountError(BaseModel):
    field: Optional[str]
    message: str
    code: AccountErrorCode

class AuthURLGenerate(BaseModel):
    authUrl: Optional[str]
    accountErrors: List[Optional[AccountError]]

class TokenCreateSSO(BaseModel):
    token: Optional[str]
    refreshToken: Optional[str]
    csrfToken: Optional[str]
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class RefreshToken(BaseModel):
    token: Optional[str]
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class VerifyToken(BaseModel):
    user: Optional[User]
    isValid: bool
    payload: Optional[GenericScalar]
    accountErrors: List[Optional[AccountError]]

class DeactivateAllUserTokens(BaseModel):
    accountErrors: List[Optional[AccountError]]

class PasswordRequestReset(BaseModel):
    accountErrors: List[Optional[AccountError]]

class AccountConfirm(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class PasswordSet(BaseModel):
    token: Optional[str]
    refreshToken: Optional[str]
    csrfToken: Optional[str]
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class PasswordChange(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class EmailChangeRequest(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class EmailChangeConfirm(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class AccountAddressCreate(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]
    address: Optional[Address]

class AccountAddressUpdate(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]
    address: Optional[Address]

class AccountAddressDelete(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]
    address: Optional[Address]

class AccountAddressSetDefault(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class AccountRegister(BaseModel):
    requiresConfirmation: Optional[bool]
    accountErrors: List[Optional[AccountError]]
    user: Optional[User]

class AccountUpdate(BaseModel):
    accountErrors: List[Optional[AccountError]]
    user: Optional[User]

class AccountRequestDeletion(BaseModel):
    accountErrors: List[Optional[AccountError]]

class AccountDelete(BaseModel):
    accountErrors: List[Optional[AccountError]]
    user: Optional[User]

class AddressCreate(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]
    address: Optional[Address]

class AddressUpdate(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]
    address: Optional[Address]

class AddressDelete(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]
    address: Optional[Address]

class AddressSetDefault(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class CustomerCreate(BaseModel):
    accountErrors: List[Optional[AccountError]]
    user: Optional[User]

class CustomerUpdate(BaseModel):
    accountErrors: List[Optional[AccountError]]
    user: Optional[User]

class CustomerDelete(BaseModel):
    accountErrors: List[Optional[AccountError]]
    user: Optional[User]

class CustomerBulkDelete(BaseModel):
    count: int
    accountErrors: List[Optional[AccountError]]

class StaffCreate(BaseModel):
    staffErrors: List[Optional[StaffError]]
    user: Optional[User]

class StaffError(BaseModel):
    field: Optional[str]
    message: str
    code: AccountErrorCode
    permissions: Optional[List[Optional[PermissionEnum]]]
    groups: Optional[List[Optional[str]]]
    users: Optional[List[Optional[str]]]

class StaffUpdate(BaseModel):
    staffErrors: List[Optional[StaffError]]
    user: Optional[User]

class StaffDelete(BaseModel):
    staffErrors: List[Optional[StaffError]]
    user: Optional[User]

class StaffBulkDelete(BaseModel):
    count: int
    staffErrors: List[Optional[StaffError]]

class UserAvatarUpdate(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class UserAvatarDelete(BaseModel):
    user: Optional[User]
    accountErrors: List[Optional[AccountError]]

class UserBulkSetActive(BaseModel):
    count: int
    accountErrors: List[Optional[AccountError]]

class PermissionGroupCreate(BaseModel):
    permissionGroupErrors: List[Optional[PermissionGroupError]]
    group: Optional[Group]

class PermissionGroupError(BaseModel):
    field: Optional[str]
    message: str
    code: PermissionGroupErrorCode
    permissions: Optional[List[Optional[PermissionEnum]]]
    users: Optional[List[Optional[str]]]

class PermissionGroupUpdate(BaseModel):
    permissionGroupErrors: List[Optional[PermissionGroupError]]
    group: Optional[Group]

class PermissionGroupDelete(BaseModel):
    permissionGroupErrors: List[Optional[PermissionGroupError]]
    group: Optional[Group]

class EmailTemplateFilterInput(BaseModel):
    title: Optional[str]
    recipientType: Optional[RecipientTypeEnum]
    eventType: Optional[EventTypeEnum]

class EmailTemplateSortingInput(BaseModel):
    direction: OrderDirection
    field: EmailTemplateSortField

class ProductFilterInput(BaseModel):
    isPublished: Optional[bool]
    collections: Optional[List[Optional[str]]]
    categories: Optional[List[Optional[str]]]
    hasCategory: Optional[bool]
    isSimple: Optional[bool]
    attributes: Optional[List[Optional[AttributeInput]]]
    customFields: Optional[List[Optional[AttributeInput]]]
    dates: Optional[CustomDateRangeInput]
    stockAvailability: Optional[StockAvailability]
    productType: Optional[str]
    stocks: Optional[ProductStockFilterInput]
    search: Optional[str]
    sellers: Optional[List[Optional[str]]]
    subStatus: Optional[ProductSubStatusEnum]
    slug: Optional[List[Optional[str]]]
    brand: Optional[List[Optional[str]]]
    features: Optional[FeatureFilterInput]
    price: Optional[PriceRangeInput]
    minimalPrice: Optional[PriceRangeInput]
    createdAt: Optional[DateTimeRangeInput]
    updatedAt: Optional[DateTimeRangeInput]
    publicationDate: Optional[DateRangeInput]
    inCircle: Optional[List[Optional[RadiusSearchInput]]]
    productTypes: Optional[List[Optional[str]]]
    advancedSearch: Optional[ProductSearchInput]
    ids: Optional[List[Optional[str]]]
    isStaff: Optional[bool]
    mpn: Optional[str]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]

class AttributeInput(BaseModel):
    slug: str
    values: Optional[List[Optional[str]]]

class CustomDateRangeInput(BaseModel):
    Pickup: Optional[DateRangeInput]
    Dropoff: Optional[DateRangeInput]

class DateRangeInput(BaseModel):
    gte: Optional[date]
    lte: Optional[date]

class ProductStockFilterInput(BaseModel):
    warehouseIds: Optional[List[Optional[str]]]

class IntRangeInput(BaseModel):
    gte: Optional[int]
    lte: Optional[int]

class FeatureFilterInput(BaseModel):
    connector: FeatureFilterConnector
    operations: Optional[List[Optional[FeatureFilterOperation]]]

class FeatureFilterOperation(BaseModel):
    name: str
    values: Optional[List[Optional[str]]]
    condition: FeatureFilterOperationCondition

class PriceRangeInput(BaseModel):
    gte: Optional[float]
    lte: Optional[float]

class DateTimeRangeInput(BaseModel):
    gte: Optional[datetime]
    lte: Optional[datetime]

class RadiusSearchInput(BaseModel):
    locationType: LocationTypeEnum
    lon: Optional[float]
    lat: Optional[float]
    radius: int
    unit: DistanceUnit

class ProductSearchInput(BaseModel):
    searchTerm: str
    searchFields: Optional[List[Optional[ProductSearchFieldEnum]]]

class MetadataFilterInput(BaseModel):
    key: str
    valueSearchTerm: str

class ProductOrder(BaseModel):
    direction: OrderDirection
    attributeId: Optional[str]
    field: Optional[ProductOrderField]

class AttributeFilterInput(BaseModel):
    valueRequired: Optional[bool]
    isVariantOnly: Optional[bool]
    visibleInStorefront: Optional[bool]
    filterableInStorefront: Optional[bool]
    filterableInDashboard: Optional[bool]
    availableInGrid: Optional[bool]
    search: Optional[str]
    ids: Optional[List[Optional[str]]]
    inCollection: Optional[str]
    inProductSearch: Optional[str]
    inVariantSearch: Optional[str]
    inMicrosite: Optional[str]
    inCategory: Optional[str]
    hasAssignedProductOrVariant: Optional[bool]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    showExternal: Optional[bool]

class ProductVariantFilterInput(BaseModel):
    search: Optional[str]
    sku: Optional[List[Optional[str]]]
    nsn: Optional[List[Optional[str]]]
    subStatus: Optional[ProductVariantSubStatusEnum]
    categories: Optional[List[Optional[str]]]
    price: Optional[PriceRangeInput]
    productTypes: Optional[List[Optional[str]]]
    collections: Optional[List[Optional[str]]]
    isPublished: Optional[bool]
    stockAvailability: Optional[StockAvailability]
    attributes: Optional[List[Optional[AttributeInput]]]
    customFields: Optional[List[Optional[AttributeInput]]]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    features: Optional[FeatureFilterInput]
    advancedSearch: Optional[ProductVariantSearchInput]
    ids: Optional[List[Optional[str]]]
    productIds: Optional[List[Optional[str]]]
    isStaff: Optional[bool]
    sellers: Optional[List[Optional[str]]]
    createdAt: Optional[DateTimeRangeInput]
    updatedAt: Optional[DateTimeRangeInput]

class ProductVariantSearchInput(BaseModel):
    searchTerm: str
    searchFields: Optional[List[Optional[ProductVariantSearchFieldEnum]]]

class VariantSortingInput(BaseModel):
    direction: OrderDirection
    attributeId: Optional[str]
    field: Optional[VariantSortField]

class CustomerOrderFilterInput(BaseModel):
    paymentStatus: Optional[List[Optional[PaymentChargeStatusEnum]]]
    status: Optional[List[Optional[OrderStatusFilter]]]
    customer: Optional[str]
    created: Optional[DateRangeInput]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    ids: Optional[List[Optional[str]]]
    search: Optional[str]
    source: Optional[List[Optional[OrderSourceFilter]]]
    isHistorical: Optional[bool]
    subStatus: Optional[List[Optional[OfferOrderSubStatusFilter]]]
    payoutStatus: Optional[List[Optional[OrderPayoutStatusEnum]]]
    vendorPayouts: Optional[List[Optional[str]]]
    payouts: Optional[List[Optional[str]]]

class OrderSortingInput(BaseModel):
    direction: OrderDirection
    field: OrderSortField

class CustomerNauticalOrderFilterInput(BaseModel):
    paymentStatus: Optional[List[Optional[PaymentChargeStatusEnum]]]
    status: Optional[List[Optional[OrderStatusFilter]]]
    customer: Optional[str]
    created: Optional[DateRangeInput]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    ids: Optional[List[Optional[str]]]
    search: Optional[str]
    source: Optional[List[Optional[OrderSourceFilter]]]
    isHistorical: Optional[bool]
    subStatus: Optional[List[Optional[OfferOrderSubStatusFilter]]]

class WishlistItemInputFilter(BaseModel):
    expiry: Optional[DateRangeInput]

class WishlistItemSortingInput(BaseModel):
    direction: OrderDirection
    field: WishlistItemSortField

class WebhookJobFilterInput(BaseModel):
    status: Optional[List[Optional[WebhookJobStatus]]]
    search: Optional[str]
    source: Optional[List[Optional[WebhookJobSource]]]
    type: Optional[List[Optional[WebhookJobType]]]
    createdAt: Optional[datetime]
    created: Optional[DateRangeInput]

class WebhookJobSortingInput(BaseModel):
    direction: OrderDirection
    field: WebhookJobSortField

class WarehouseFilterInput(BaseModel):
    seller: Optional[str]
    search: Optional[str]
    ids: Optional[List[Optional[str]]]

class WarehouseSortingInput(BaseModel):
    direction: OrderDirection
    field: WarehouseSortField

class StockFilterInput(BaseModel):
    quantity: Optional[Decimal]
    search: Optional[str]

class ContentFilterInput(BaseModel):
    search: Optional[str]

class ContentSortingInput(BaseModel):
    direction: OrderDirection
    field: ContentSortField

class MediaFilterInput(BaseModel):
    search: Optional[str]

class MediaSortingInput(BaseModel):
    direction: OrderDirection
    field: MediaSortField

class ShippingZoneFilterInput(BaseModel):
    seller: Optional[str]
    search: Optional[str]

class SellerFilterInput(BaseModel):
    status: Optional[List[Optional[SellerStatusFilter]]]
    search: Optional[str]
    created: Optional[DateRangeInput]
    storefront: Optional[bool]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]

class SellerSortingInput(BaseModel):
    direction: OrderDirection
    field: SellerSortField

class RefundFilterInput(BaseModel):
    name: Optional[str]
    createdAt: Optional[DateTimeRangeInput]
    updatedAt: Optional[DateTimeRangeInput]
    status: Optional[RefundStatusEnum]
    buyer: Optional[str]
    externalId: Optional[str]
    token: Optional[str]

class RefundSortingInput(BaseModel):
    direction: OrderDirection
    field: RefundSortField

class CategoryFilterInput(BaseModel):
    search: Optional[str]
    ids: Optional[List[Optional[str]]]
    customFields: Optional[List[Optional[AttributeInput]]]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]

class CategorySortingInput(BaseModel):
    direction: OrderDirection
    field: CategorySortField

class CollectionFilterInput(BaseModel):
    published: Optional[CollectionPublished]
    search: Optional[str]
    ids: Optional[List[Optional[str]]]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    isVisible: Optional[CollectionVisible]
    customFields: Optional[List[Optional[AttributeInput]]]

class CollectionSortingInput(BaseModel):
    direction: OrderDirection
    field: CollectionSortField

class ProductTypeFilterInput(BaseModel):
    search: Optional[str]
    productType: Optional[ProductTypeEnum]
    configurable: Optional[ProductTypeConfigurable]
    ids: Optional[List[Optional[str]]]
    showExternal: Optional[bool]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]

class ProductTypeSortingInput(BaseModel):
    direction: OrderDirection
    field: ProductTypeSortField

class PriceBookFilterInput(BaseModel):
    search: Optional[str]
    deleted: Optional[bool]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]

class PriceBookSortingInput(BaseModel):
    direction: OrderDirection
    field: PriceBookSortField

class PriceBookVariantFilterInput(BaseModel):
    search: Optional[str]

class PriceBookVariantSortingInput(BaseModel):
    direction: OrderDirection
    field: PriceBookVariantSortField

class PriceBookProductFilterInput(BaseModel):
    search: Optional[str]

class PriceBookProductSortingInput(BaseModel):
    direction: OrderDirection
    field: PriceBookProductSortField

class PriceBookProductTypeFilterInput(BaseModel):
    search: Optional[str]

class PriceBookProductTypeSortingInput(BaseModel):
    direction: OrderDirection
    field: PriceBookProductTypeSortField

class PriceBookVariantHistoryFilterInput(BaseModel):
    search: Optional[str]

class PriceBookVariantHistorySortingInput(BaseModel):
    direction: OrderDirection
    field: PriceBookVariantHistorySortField

class PriceBookProductHistoryFilterInput(BaseModel):
    search: Optional[str]

class PriceBookProductHistorySortingInput(BaseModel):
    direction: OrderDirection
    field: PriceBookProductHistorySortField

class PriceBookProductTypeHistoryFilterInput(BaseModel):
    search: Optional[str]

class PriceBookProductTypeHistorySortingInput(BaseModel):
    direction: OrderDirection
    field: PriceBookProductTypeHistorySortField

class UserSortingInput(BaseModel):
    direction: OrderDirection
    field: UserSortField

class PluginFilterInput(BaseModel):
    active: Optional[bool]
    search: Optional[str]
    isPaymentGateway: Optional[bool]
    seller: Optional[str]

class PluginSortingInput(BaseModel):
    direction: OrderDirection
    field: PluginSortField

class CatalogImportProcessLogRecordFilterInput(BaseModel):
    taskId: Optional[str]
    objectId: Optional[str]
    operation: Optional[CatalogImportOperation]

class CatalogImportProcessLogRecordSortInput(BaseModel):
    direction: OrderDirection
    field: CatalogImportProcessLogRecordSortField

class CatalogImportProcessFilterInput(BaseModel):
    createdBy: Optional[str]
    seller: Optional[str]

class CatalogImportProcessSortInput(BaseModel):
    direction: OrderDirection
    field: CatalogImportProcessSortField

class StripeClientPaymentData(BaseModel):
    amount: Optional[PositiveDecimal]
    currency: Optional[str]
    token: Optional[str]
    billing: Optional[AddressInput]
    shipping: Optional[AddressInput]
    checkoutId: Optional[str]
    nauticalOrderId: Optional[str]
    customerEmail: Optional[str]
    customerId: Optional[str]
    returnUrl: Optional[str]
    paymentMethodToken: Optional[str]

class AddressInput(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    companyName: Optional[str]
    streetAddress1: Optional[str]
    streetAddress2: Optional[str]
    city: Optional[str]
    cityArea: Optional[str]
    postalCode: Optional[str]
    country: Optional[CountryCode]
    countryArea: Optional[str]
    phone: Optional[str]

class CheckoutEventFilterInput(BaseModel):
    createdAt: Optional[DateTimeRangeInput]
    type: Optional[List[Optional[CheckoutEventType]]]

class CheckoutEventSortInput(BaseModel):
    direction: OrderDirection
    field: CheckoutEventSortField

class PayoutFilterInput(BaseModel):
    status: Optional[List[Optional[PayoutStatusFilter]]]
    search: Optional[str]
    created: Optional[DateRangeInput]
    netSales: Optional[PriceRangeInput]

class PayoutSortingInput(BaseModel):
    direction: OrderDirection
    field: PayoutSortField

class PageSortingInput(BaseModel):
    direction: OrderDirection
    field: PageSortField

class PageFilterInput(BaseModel):
    search: Optional[str]

class OrderFilterInput(BaseModel):
    paymentStatus: Optional[List[Optional[PaymentChargeStatusEnum]]]
    status: Optional[List[Optional[OrderStatusFilter]]]
    customer: Optional[str]
    created: Optional[DateRangeInput]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    ids: Optional[List[Optional[str]]]
    search: Optional[str]
    source: Optional[List[Optional[OrderSourceFilter]]]
    isHistorical: Optional[bool]
    subStatus: Optional[List[Optional[OfferOrderSubStatusFilter]]]
    payoutStatus: Optional[List[Optional[OrderPayoutStatusEnum]]]
    vendorPayouts: Optional[List[Optional[str]]]
    payouts: Optional[List[Optional[str]]]

class NauticalOrderFilterInput(BaseModel):
    paymentStatus: Optional[List[Optional[PaymentChargeStatusEnum]]]
    status: Optional[List[Optional[OrderStatusFilter]]]
    customer: Optional[str]
    created: Optional[DateRangeInput]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    ids: Optional[List[Optional[str]]]
    search: Optional[str]
    source: Optional[List[Optional[OrderSourceFilter]]]
    isHistorical: Optional[bool]
    subStatus: Optional[List[Optional[OfferOrderSubStatusFilter]]]

class OrderDraftFilterInput(BaseModel):
    customer: Optional[str]
    created: Optional[DateRangeInput]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    ids: Optional[List[Optional[str]]]
    search: Optional[str]
    isHistorical: Optional[bool]
    source: Optional[List[Optional[OrderSourceFilter]]]
    subStatus: Optional[List[Optional[OfferOrderSubStatusFilter]]]

class NauticalOrderDraftFilterInput(BaseModel):
    customer: Optional[str]
    created: Optional[DateRangeInput]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    ids: Optional[List[Optional[str]]]
    search: Optional[str]
    isHistorical: Optional[bool]
    source: Optional[List[Optional[OrderSourceFilter]]]
    subStatus: Optional[List[Optional[OfferOrderSubStatusFilter]]]

class NauticalOrderQuoteFilterInput(BaseModel):
    customer: Optional[str]
    created: Optional[DateRangeInput]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    ids: Optional[List[Optional[str]]]
    search: Optional[str]
    isHistorical: Optional[bool]
    subStatus: Optional[List[Optional[QuoteOrderSubStatusFilter]]]
    source: Optional[List[Optional[OrderSourceFilter]]]

class OrderQuoteFilterInput(BaseModel):
    customer: Optional[str]
    created: Optional[DateRangeInput]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]
    ids: Optional[List[Optional[str]]]
    search: Optional[str]
    isHistorical: Optional[bool]
    subStatus: Optional[List[Optional[QuoteOrderSubStatusFilter]]]
    source: Optional[List[Optional[OrderSourceFilter]]]

class ReturnFulfillmentFilterInput(BaseModel):
    status: Optional[List[Optional[FulfillmentStatusFilter]]]
    customer: Optional[str]
    created: Optional[DateRangeInput]
    search: Optional[str]

class ReturnFulfillmentSortingInput(BaseModel):
    direction: OrderDirection
    field: ReturnFulfillmentSortField

class MicrositeFilterInput(BaseModel):
    published: Optional[MicrositePublished]
    search: Optional[str]
    ids: Optional[List[Optional[str]]]
    metadata: Optional[MetadataFilterInput]
    privateMetadata: Optional[MetadataFilterInput]

class MicrositeSortingInput(BaseModel):
    direction: OrderDirection
    field: MicrositeSortField

class MenuSortingInput(BaseModel):
    direction: OrderDirection
    field: MenuSortField

class MenuFilterInput(BaseModel):
    search: Optional[str]
    slug: Optional[List[Optional[str]]]

class MenuItemSortingInput(BaseModel):
    direction: OrderDirection
    field: MenuItemsSortField

class MenuItemFilterInput(BaseModel):
    search: Optional[str]

class EmailEventFilterInput(BaseModel):
    fromEmail: Optional[str]
    toEmail: Optional[str]
    date: Optional[DateTimeRangeInput]
    messageType: Optional[List[Optional[NotifyEventTypeEnum]]]

class EmailEventSortingInput(BaseModel):
    direction: OrderDirection
    field: EmailEventSortField

class JournalEntryFilterInput(BaseModel):
    type: Optional[JournalEntryTypeEnum]
    createdAt: Optional[DateTimeRangeInput]
    fulfillmentLineIds: Optional[List[Optional[str]]]
    nauticalOrderIds: Optional[List[Optional[str]]]
    orderIds: Optional[List[Optional[str]]]
    orderLineIds: Optional[List[Optional[str]]]
    paymentIds: Optional[List[Optional[str]]]
    refundLineIds: Optional[List[Optional[str]]]
    vendorPayoutIds: Optional[List[Optional[str]]]

class JournalEntrySortingInput(BaseModel):
    direction: OrderDirection
    field: JournalEntrySortField

class LedgerEntryFilterInput(BaseModel):
    type: Optional[LedgerTypeEnum]
    sellerIds: Optional[List[Optional[str]]]

class LedgerSortingInput(BaseModel):
    direction: OrderDirection
    field: LedgerSortField

class SaleFilterInput(BaseModel):
    status: Optional[List[Optional[DiscountStatusEnum]]]
    saleType: Optional[DiscountValueTypeEnum]
    started: Optional[DateTimeRangeInput]
    search: Optional[str]

class SaleSortingInput(BaseModel):
    direction: OrderDirection
    field: SaleSortField

class VoucherFilterInput(BaseModel):
    status: Optional[List[Optional[DiscountStatusEnum]]]
    timesUsed: Optional[IntRangeInput]
    discountType: Optional[List[Optional[VoucherDiscountType]]]
    started: Optional[DateTimeRangeInput]
    search: Optional[str]

class VoucherSortingInput(BaseModel):
    direction: OrderDirection
    field: VoucherSortField

class ExportFileFilterInput(BaseModel):
    createdAt: Optional[DateTimeRangeInput]
    updatedAt: Optional[DateTimeRangeInput]
    status: Optional[JobStatusEnum]
    user: Optional[str]
    app: Optional[str]

class ExportFileSortingInput(BaseModel):
    direction: OrderDirection
    field: ExportFileSortField

class AttributeSortingInput(BaseModel):
    direction: OrderDirection
    field: AttributeSortField

class AppFilterInput(BaseModel):
    search: Optional[str]
    isActive: Optional[bool]
    type: Optional[AppTypeEnum]

class AppSortingInput(BaseModel):
    direction: OrderDirection
    field: AppSortField

class AgreementOrder(BaseModel):
    direction: OrderDirection
    field: Optional[AgreementSortField]

class AgreementFilterInput(BaseModel):
    search: Optional[str]

class CustomerFilterInput(BaseModel):
    dateJoined: Optional[DateRangeInput]
    isActive: Optional[bool]
    moneySpent: Optional[PriceRangeInput]
    numberOfOrders: Optional[IntRangeInput]
    placedOrders: Optional[DateRangeInput]
    search: Optional[str]
    customFields: Optional[List[Optional[AttributeInput]]]

class PermissionGroupFilterInput(BaseModel):
    search: Optional[str]

class PermissionGroupSortingInput(BaseModel):
    direction: OrderDirection
    field: PermissionGroupSortField

class StaffUserInput(BaseModel):
    status: Optional[StaffMemberStatus]
    search: Optional[str]
    customFields: Optional[List[Optional[AttributeInput]]]
    isUserActive: Optional[bool]

class EmailTemplateUpdateInput(BaseModel):
    content: Optional[str]
    subject: Optional[str]
    senderEmailAddress: Optional[str]
    isCustom: Optional[bool]

class TenantUpdateInput(BaseModel):
    isActive: Optional[bool]
    name: Optional[str]
    slug: Optional[str]

class DocumentUpdateInput(BaseModel):
    description: Optional[str]

class NauticalConfigurationInputItem(BaseModel):
    configurationName: Optional[str]
    configurationValue: Optional[bool]
    configurationValueDatetime: Optional[datetime]
    configurationValueString: Optional[str]

class MarketplaceConfigurationInput(BaseModel):
    isSellerShippingZoneCreationAllowed: Optional[bool]
    requireProductApproval: Optional[bool]
    requireProductTypes: Optional[bool]
    supportedCurrencies: Optional[List[Optional[str]]]
    defaultCountry: Optional[str]
    supportedCountries: Optional[List[Optional[str]]]
    sellerCanSendQuote: Optional[bool]
    defaultSellerChecklists: Optional[List[Optional[DefaultSellerChecklistInput]]]
    enableStockAllocationForQuotes: Optional[bool]
    enableStockAllocationForOffers: Optional[bool]
    enableStockAllocationForDrafts: Optional[bool]
    validateStockOnOrderPaymentCreation: Optional[bool]
    timezone: Optional[str]
    enableBackorders: Optional[bool]
    automaticFulfillmentDigitalProducts: Optional[bool]
    defaultDigitalMaxDownloads: Optional[int]
    defaultDigitalUrlValidDays: Optional[int]
    trackInventoryByDefault: Optional[bool]
    name: Optional[str]
    description: Optional[str]
    companyAddress: Optional[AddressInput]
    defaultMailSenderName: Optional[str]
    defaultMailSenderAddress: Optional[str]
    defaultMailSupportAddress: Optional[str]
    customerSetPasswordUrl: Optional[str]
    includeTaxesInPrices: Optional[bool]
    chargeTaxesOnShipping: Optional[bool]

class DefaultSellerChecklistInput(BaseModel):
    title: str
    description: str
    completeOn: Optional[SellerChecklistCompletionTriggersEnum]
    isEnabled: bool

class PayoutCreateInput(BaseModel):
    vendorType: Optional[str]
    endDate: date

class PayoutUpdateInput(BaseModel):
    vendorPayouts: List[Optional[VendorPayoutUpdateInput]]

class VendorPayoutUpdateInput(BaseModel):
    vendorId: Optional[str]
    adjustments: Optional[Decimal]
    penalties: Optional[Decimal]
    adjustmentDirection: Optional[str]

class PayoutStatusInput(BaseModel):
    status: str
    vendorPayouts: Optional[List[Optional[VendorPayoutDetails]]]

class VendorPayoutDetails(BaseModel):
    vendor: Optional[str]
    payout: Optional[str]

class PayoutDatesInput(BaseModel):
    endDate: date

class VendorPayoutStatusInput(BaseModel):
    status: str
    payoutAmount: str

class VendorPayoutAddNoteInput(BaseModel):
    message: str

class VendorPayoutUpdateNoteInput(BaseModel):
    message: str

class WishlistInput(BaseModel):
    name: str

class WishlistBuyerInput(BaseModel):
    name: str
    user: str

class WishlistItemUpdateInput(BaseModel):
    note: Optional[str]
    expiryDate: Optional[datetime]
    requestedPriceAmount: Optional[PositiveDecimal]
    quantity: Optional[int]

class MicrositeCreateInput(BaseModel):
    isPublished: Optional[bool]
    name: Optional[str]
    footerText: Optional[str]
    slug: Optional[str]
    description: Optional[str]
    descriptionHtml: Optional[str]
    bannerImage: Optional[Upload]
    bannerImageAlt: Optional[str]
    logoImage: Optional[Upload]
    logoImageAlt: Optional[str]
    seo: Optional[SeoInput]
    publicationDate: Optional[date]
    products: Optional[List[Optional[str]]]
    vendor: str

class SeoInput(BaseModel):
    title: Optional[str]
    description: Optional[str]

class MoveProductInput(BaseModel):
    productId: str
    sortOrder: Optional[int]

class MicrositeInput(BaseModel):
    isPublished: Optional[bool]
    name: Optional[str]
    footerText: Optional[str]
    slug: Optional[str]
    description: Optional[str]
    descriptionHtml: Optional[str]
    bannerImage: Optional[Upload]
    bannerImageAlt: Optional[str]
    logoImage: Optional[Upload]
    logoImageAlt: Optional[str]
    seo: Optional[SeoInput]
    publicationDate: Optional[date]

class AgreementInput(BaseModel):
    slug: Optional[str]
    title: Optional[str]
    content: Optional[str]
    contentHtml: Optional[str]
    isPublished: Optional[bool]
    publicationDate: Optional[str]
    seo: Optional[SeoInput]
    defaultCommission: Optional[Decimal]
    isActive: Optional[bool]
    updatedAt: Optional[str]
    commissionType: Optional[CommissionTypeEnum]
    markupCommissionType: Optional[MarkupCommissionTypeEnum]
    markupCommissionValue: Optional[Decimal]

class AgreementFeeInput(BaseModel):
    agreement: Optional[str]
    feeName: Optional[str]
    feeType: Optional[FeeType]
    feeValue: Optional[Decimal]
    feeScope: Optional[FeeScope]

class AgreementCommissionCreateInput(BaseModel):
    commissionType: Optional[AgreementGranularCommissionType]
    commission: Optional[Decimal]
    instance: Optional[str]
    agreement: Optional[str]

class SellerAgreementAcknowledgeInput(BaseModel):
    agreementDecisionReason: Optional[str]

class SellerAgreementDeclineInput(BaseModel):
    agreementDecisionReason: Optional[str]

class SellerAgreementInput(BaseModel):
    agreement: str
    effectiveAt: date
    seller: str

class DetailedSellerInput(BaseModel):
    companyName: str
    plan: Optional[str]
    metadata: Optional[List[Optional[MetadataInput]]]

class MetadataInput(BaseModel):
    key: str
    value: str

class SellerOwnerCreateInput(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    personalPhone: Optional[str]
    redirectUrl: Optional[str]
    metadata: Optional[List[Optional[MetadataInput]]]

class SellerInput(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    identifiers: Optional[List[Optional[str]]]
    owner: Optional[str]
    plan: Optional[str]
    checklists: Optional[List[Optional[SellerChecklistInput]]]

class SellerChecklistInput(BaseModel):
    title: str
    description: str
    completeOn: Optional[SellerChecklistCompletionTriggersEnum]

class SellerUserInput(BaseModel):
    seller: str
    user: str

class SellerUpdateInput(BaseModel):
    status: Optional[str]
    user: Optional[str]
    plan: Optional[str]
    companyName: Optional[str]
    storeDescription: Optional[str]
    slug: Optional[str]
    identifiers: Optional[List[Optional[str]]]

class SellerNoteInput(BaseModel):
    message: Optional[str]
    user: Optional[str]
    seller: Optional[str]

class SellerSettingsUpdateInput(BaseModel):
    defaultCurrency: Optional[str]
    fulfilledByMarketplace: Optional[bool]

class SellerApplicationUpdateInput(BaseModel):
    formData: Optional[str]
    checkpoint: Optional[SellerApplicationCheckpoint]

class DesignerDataInput(BaseModel):
    name: Optional[str]
    jsonContent: Optional[str]

class WebhookCreateInput(BaseModel):
    name: Optional[str]
    targetUrl: Optional[str]
    events: Optional[List[Optional[WebhookEventTypeEnum]]]
    app: Optional[str]
    isActive: Optional[bool]
    secretKey: Optional[str]
    connectionString: Optional[str]
    queueName: Optional[str]

class WebhookUpdateInput(BaseModel):
    name: Optional[str]
    targetUrl: Optional[str]
    events: Optional[List[Optional[WebhookEventTypeEnum]]]
    app: Optional[str]
    isActive: Optional[bool]
    secretKey: Optional[str]
    connectionString: Optional[str]
    queueName: Optional[str]

class WarehouseCreateInput(BaseModel):
    name: str
    address: Optional[WarehouseAddressInput]
    slug: Optional[str]
    companyName: Optional[str]
    seller: str
    email: Optional[str]
    addShippingZones: Optional[List[Optional[str]]]
    externalId: Optional[str]
    externalSource: Optional[str]
    isAddressSameAsBusiness: Optional[bool]

class WarehouseAddressInput(BaseModel):
    streetAddress1: str
    streetAddress2: Optional[str]
    city: str
    cityArea: Optional[str]
    postalCode: Optional[str]
    country: CountryCode
    countryArea: Optional[str]
    phone: Optional[str]

class WarehouseUpdateInput(BaseModel):
    name: Optional[str]
    address: Optional[WarehouseAddressInput]
    slug: Optional[str]
    companyName: Optional[str]
    seller: Optional[str]
    email: Optional[str]
    addShippingZones: Optional[List[Optional[str]]]
    externalId: Optional[str]
    externalSource: Optional[str]
    isAddressSameAsBusiness: Optional[bool]
    removeShippingZones: Optional[List[Optional[str]]]

class ContentPageDataCreateInput(BaseModel):
    contentId: str
    seoTitle: Optional[str]
    seoDescription: Optional[str]

class ContentPageDataUpdateInput(BaseModel):
    seoTitle: Optional[str]
    seoDescription: Optional[str]

class ContentCreateInput(BaseModel):
    slug: str
    isPage: bool

class ContentSaveInput(BaseModel):
    previousRevision: int
    data: str

class ContentPublishInput(BaseModel):
    previousRevision: int
    data: str
    publicationDate: Optional[date]

class ContentDuplicateInput(BaseModel):
    newSlug: str

class MediaCreateInput(BaseModel):
    alt: Optional[str]
    title: str
    image: Upload

class MediaUpdateInput(BaseModel):
    alt: Optional[str]
    title: Optional[str]
    image: Optional[Upload]

class SiteDomainInput(BaseModel):
    domain: Optional[str]
    name: Optional[str]
    apiUrl: Optional[str]
    dashboardUrl: Optional[str]

class ShopSettingsInput(BaseModel):
    headerText: Optional[str]
    description: Optional[str]
    includeTaxesInPrices: Optional[bool]
    chargeTaxesOnShipping: Optional[bool]
    trackInventoryByDefault: Optional[bool]
    defaultWeightUnit: Optional[WeightUnitsEnum]
    automaticFulfillmentDigitalProducts: Optional[bool]
    defaultDigitalMaxDownloads: Optional[int]
    defaultDigitalUrlValidDays: Optional[int]
    defaultMailSenderName: Optional[str]
    defaultMailSenderAddress: Optional[str]
    defaultMailSupportAddress: Optional[str]
    customerSetPasswordUrl: Optional[str]

class CheckoutThemeCreateInput(BaseModel):
    confirmationUrl: str

class CheckoutThemeInput(BaseModel):
    confirmationUrl: Optional[str]

class CustomDomainCreateInput(BaseModel):
    domain: str

class StorefrontThemeInput(BaseModel):
    primaryColor: Optional[str]
    backgroundColor: Optional[str]
    logo: Optional[Upload]
    faviconImage: Optional[Upload]
    faviconUrl: Optional[str]
    font: Optional[str]
    fontColor: Optional[str]

class SellerOnboardingSettingsCreateInput(BaseModel):
    isAcceptingNewSellers: bool
    summary: str
    welcomeMessage: Optional[str]
    fulfillmentModel: str
    requiredDocuments: str
    notAcceptingSellersMessage: Optional[str]

class SellerOnboardingSettingsUpdateInput(BaseModel):
    isAcceptingNewSellers: Optional[bool]
    summary: Optional[str]
    welcomeMessage: Optional[str]
    fulfillmentModel: Optional[str]
    requiredDocuments: Optional[str]
    notAcceptingSellersMessage: Optional[str]

class ShippingPriceInput(BaseModel):
    name: Optional[str]
    price: Optional[PositiveDecimal]
    minimumOrderPrice: Optional[PositiveDecimal]
    maximumOrderPrice: Optional[PositiveDecimal]
    minimumOrderWeight: Optional[WeightScalar]
    maximumOrderWeight: Optional[WeightScalar]
    type: Optional[ShippingMethodTypeEnum]
    shippingZone: Optional[str]
    requiresSecondaryAddress: Optional[bool]

class ShippingZoneCreateInput(BaseModel):
    name: Optional[str]
    countries: Optional[List[Optional[str]]]
    addWarehouses: Optional[List[Optional[str]]]
    seller: str
    countryAreas: Optional[List[Optional[ShippingZoneCountryAreaInput]]]

class ShippingZoneCountryAreaInput(BaseModel):
    country: str
    countryAreas: List[Optional[str]]

class ShippingZoneUpdateInput(BaseModel):
    name: Optional[str]
    countries: Optional[List[Optional[str]]]
    addWarehouses: Optional[List[Optional[str]]]
    seller: Optional[str]
    countryAreas: Optional[List[Optional[ShippingZoneCountryAreaInput]]]
    removeWarehouses: Optional[List[Optional[str]]]

class RefundCreateInput(BaseModel):
    description: Optional[str]
    descriptionHtml: Optional[str]
    externalId: Optional[str]
    name: str
    order: str

class RefundUpdateInput(BaseModel):
    description: Optional[str]
    descriptionHtml: Optional[str]
    externalId: Optional[str]
    name: Optional[str]

class RefundLineInput(BaseModel):
    chargedTo: RefundChargeToEnum
    lineType: RefundLineTypeEnum
    refundScope: str
    amount: Optional[PositiveDecimal]
    percentage: Optional[PositiveDecimal]
    quantity: Optional[int]
    quantityFulfilled: Optional[int]
    quantityUnfulfilled: Optional[int]

class RefundLineUpdateInput(BaseModel):
    chargedTo: RefundChargeToEnum
    lineType: RefundLineTypeEnum
    refundScope: str
    amount: Optional[PositiveDecimal]
    percentage: Optional[PositiveDecimal]
    quantity: Optional[int]
    quantityFulfilled: Optional[int]
    quantityUnfulfilled: Optional[int]
    id: str

class RefundPaymentInput(BaseModel):
    id: str
    amount: PositiveDecimal

class RefundPaymentUpdateInput(BaseModel):
    id: str
    amount: PositiveDecimal

class PriceBookCreateInput(BaseModel):
    name: Optional[str]
    description: Optional[str]
    descriptionHtml: Optional[str]

class PriceBookUpdateInput(BaseModel):
    name: Optional[str]
    description: Optional[str]
    descriptionHtml: Optional[str]
    activate: Optional[bool]

class PriceBookVariantCreateInput(BaseModel):
    priceAmount: Optional[Decimal]
    currency: Optional[str]
    percentage: Optional[Decimal]
    variant: str
    priceBook: str
    valueType: PriceBookValueTypeEnum

class PriceBookVariantUpdateInput(BaseModel):
    priceAmount: Optional[Decimal]
    currency: Optional[str]
    percentage: Optional[Decimal]
    valueType: Optional[PriceBookValueTypeEnum]

class PriceBookProductCreateInput(BaseModel):
    priceAmount: Optional[Decimal]
    currency: Optional[str]
    percentage: Optional[Decimal]
    product: str
    priceBook: str
    valueType: PriceBookValueTypeEnum

class PriceBookProductUpdateInput(BaseModel):
    priceAmount: Optional[Decimal]
    currency: Optional[str]
    percentage: Optional[Decimal]
    valueType: Optional[PriceBookValueTypeEnum]

class PriceBookProductTypeCreateInput(BaseModel):
    priceAmount: Optional[Decimal]
    currency: Optional[str]
    percentage: Optional[Decimal]
    productType: str
    priceBook: str
    valueType: PriceBookValueTypeEnum

class PriceBookProductTypeUpdateInput(BaseModel):
    priceAmount: Optional[Decimal]
    currency: Optional[str]
    percentage: Optional[Decimal]
    valueType: Optional[PriceBookValueTypeEnum]

class UserAddToPriceBookInput(BaseModel):
    user: str
    priceBook: str

class CategoryInput(BaseModel):
    description: Optional[str]
    descriptionHtml: Optional[str]
    name: Optional[str]
    slug: Optional[str]
    seo: Optional[SeoInput]
    backgroundImage: Optional[Upload]
    backgroundImageAlt: Optional[str]
    customFields: Optional[List[Optional[AttributeValueInput]]]

class AttributeValueInput(BaseModel):
    id: Optional[str]
    values: Optional[List[Optional[str]]]
    value: Optional[str]
    dateTime: Optional[datetime]
    plainText: Optional[str]
    richText: Optional[str]
    amount: Optional[Decimal]
    currency: Optional[str]
    reference: Optional[str]
    boolean: Optional[bool]
    file: Optional[Upload]
    fileUrl: Optional[str]

class CollectionCreateInput(BaseModel):
    isPublished: Optional[bool]
    isVisible: Optional[bool]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    name: Optional[str]
    slug: Optional[str]
    description: Optional[str]
    descriptionHtml: Optional[str]
    backgroundImage: Optional[Upload]
    backgroundImageAlt: Optional[str]
    seo: Optional[SeoInput]
    publicationDate: Optional[date]
    products: Optional[List[Optional[str]]]
    type: Optional[CollectionTypeEnum]

class CollectionInput(BaseModel):
    isPublished: Optional[bool]
    isVisible: Optional[bool]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    name: Optional[str]
    slug: Optional[str]
    description: Optional[str]
    descriptionHtml: Optional[str]
    backgroundImage: Optional[Upload]
    backgroundImageAlt: Optional[str]
    seo: Optional[SeoInput]
    publicationDate: Optional[date]

class ProductCreateInput(BaseModel):
    attributes: Optional[List[Optional[AttributeValueInput]]]
    productType: Optional[str]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    publicationDate: Optional[date]
    category: Optional[str]
    chargeTaxes: Optional[bool]
    collections: Optional[List[Optional[str]]]
    currency: Optional[str]
    description: Optional[str]
    descriptionHtml: Optional[str]
    isPublished: Optional[bool]
    name: Optional[str]
    slug: Optional[str]
    taxCode: Optional[str]
    seo: Optional[SeoInput]
    weight: Optional[WeightScalar]
    sku: Optional[str]
    trackInventory: Optional[bool]
    basePrice: Optional[PositiveDecimal]
    costPrice: Optional[PositiveDecimal]
    visibleInListings: Optional[bool]
    mpn: Optional[str]
    brand: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    overridePrice: Optional[bool]
    overrideCurrency: Optional[bool]
    subStatus: Optional[ProductSubStatusEnum]
    subStatusReason: Optional[str]
    sortPriorityWeight: Optional[Decimal]
    isShippingRequired: Optional[bool]
    isDigital: Optional[bool]
    isPriceOverrideAllowed: Optional[bool]
    seller: str
    stocks: Optional[List[Optional[StockInput]]]
    isAvailable: Optional[bool]
    allowBackorders: Optional[bool]
    startDate: Optional[date]
    externalSource: Optional[str]
    externalId: Optional[str]

class VariantSizeInput(BaseModel):
    length: Optional[Decimal]
    width: Optional[Decimal]
    height: Optional[Decimal]
    sizeUnits: Optional[DistanceUnitsEnum]

class StockInput(BaseModel):
    warehouse: str
    quantity: Optional[int]

class ProductInput(BaseModel):
    attributes: Optional[List[Optional[AttributeValueInput]]]
    productType: Optional[str]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    publicationDate: Optional[date]
    category: Optional[str]
    chargeTaxes: Optional[bool]
    collections: Optional[List[Optional[str]]]
    currency: Optional[str]
    description: Optional[str]
    descriptionHtml: Optional[str]
    isPublished: Optional[bool]
    name: Optional[str]
    slug: Optional[str]
    taxCode: Optional[str]
    seo: Optional[SeoInput]
    weight: Optional[WeightScalar]
    sku: Optional[str]
    trackInventory: Optional[bool]
    basePrice: Optional[PositiveDecimal]
    costPrice: Optional[PositiveDecimal]
    visibleInListings: Optional[bool]
    mpn: Optional[str]
    brand: Optional[str]
    manufacturer: Optional[str]
    model: Optional[str]
    overridePrice: Optional[bool]
    overrideCurrency: Optional[bool]
    subStatus: Optional[ProductSubStatusEnum]
    subStatusReason: Optional[str]
    sortPriorityWeight: Optional[Decimal]
    isShippingRequired: Optional[bool]
    isDigital: Optional[bool]
    isPriceOverrideAllowed: Optional[bool]

class ProductImageCreateInput(BaseModel):
    alt: Optional[str]
    image: Optional[Upload]
    url: Optional[str]
    product: str
    externalId: Optional[str]
    externalSource: Optional[str]

class ReorderInput(BaseModel):
    id: str
    sortOrder: Optional[int]

class ProductImageUpdateInput(BaseModel):
    alt: Optional[str]

class ProductTypeInput(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    isPriceOverrideAllowed: Optional[bool]
    productAttributes: Optional[List[Optional[str]]]
    variantAttributes: Optional[List[Optional[str]]]
    isShippingRequired: Optional[bool]
    isDigital: Optional[bool]
    weight: Optional[WeightScalar]
    taxCode: Optional[str]
    createdBy: Optional[str]

class DigitalContentUploadInput(BaseModel):
    useDefaultSettings: bool
    maxDownloads: Optional[int]
    urlValidDays: Optional[int]
    automaticFulfillment: Optional[bool]
    contentFile: Upload

class DigitalContentInput(BaseModel):
    useDefaultSettings: bool
    maxDownloads: Optional[int]
    urlValidDays: Optional[int]
    automaticFulfillment: Optional[bool]

class DigitalContentUrlCreateInput(BaseModel):
    content: str

class ProductVariantCreateInput(BaseModel):
    product: str
    attributes: List[Optional[AttributeValueInput]]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    costPrice: Optional[PositiveDecimal]
    description: Optional[str]
    descriptionHtml: Optional[str]
    price: Optional[PositiveDecimal]
    currency: Optional[str]
    sku: Optional[str]
    overrideCurrency: Optional[bool]
    trackInventory: Optional[bool]
    seller: Optional[str]
    seo: Optional[SeoInput]
    weight: Optional[WeightScalar]
    size: Optional[VariantSizeInput]
    name: Optional[str]
    requiresQuote: Optional[bool]
    subStatus: Optional[ProductVariantSubStatusEnum]
    isPublished: Optional[bool]
    publishedAt: Optional[datetime]
    allowBackorders: Optional[bool]
    isShippingRequired: Optional[bool]
    isDigital: Optional[bool]
    isPriceOverrideAllowed: Optional[bool]
    stocks: Optional[List[Optional[StockInput]]]
    externalSource: Optional[str]
    externalId: Optional[str]

class ProductVariantBulkCreateInput(BaseModel):
    product: Optional[str]
    attributes: List[Optional[AttributeValueInput]]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    costPrice: Optional[PositiveDecimal]
    description: Optional[str]
    descriptionHtml: Optional[str]
    price: Optional[PositiveDecimal]
    currency: Optional[str]
    sku: Optional[str]
    overrideCurrency: Optional[bool]
    trackInventory: Optional[bool]
    seller: Optional[str]
    seo: Optional[SeoInput]
    weight: Optional[WeightScalar]
    size: Optional[VariantSizeInput]
    name: Optional[str]
    requiresQuote: Optional[bool]
    subStatus: Optional[ProductVariantSubStatusEnum]
    isPublished: Optional[bool]
    publishedAt: Optional[datetime]
    allowBackorders: Optional[bool]
    isShippingRequired: Optional[bool]
    isDigital: Optional[bool]
    isPriceOverrideAllowed: Optional[bool]
    stocks: Optional[List[Optional[StockInput]]]
    externalSource: Optional[str]
    externalId: Optional[str]

class ProductVariantInput(BaseModel):
    product: Optional[str]
    attributes: Optional[List[Optional[AttributeValueInput]]]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    costPrice: Optional[PositiveDecimal]
    description: Optional[str]
    descriptionHtml: Optional[str]
    price: Optional[PositiveDecimal]
    currency: Optional[str]
    sku: Optional[str]
    overrideCurrency: Optional[bool]
    trackInventory: Optional[bool]
    seller: Optional[str]
    seo: Optional[SeoInput]
    weight: Optional[WeightScalar]
    size: Optional[VariantSizeInput]
    name: Optional[str]
    requiresQuote: Optional[bool]
    subStatus: Optional[ProductVariantSubStatusEnum]
    isPublished: Optional[bool]
    publishedAt: Optional[datetime]
    allowBackorders: Optional[bool]
    isShippingRequired: Optional[bool]
    isDigital: Optional[bool]
    isPriceOverrideAllowed: Optional[bool]

class FeatureCreateInput(BaseModel):
    name: Optional[str]
    description: Optional[str]
    options: Optional[List[Optional[str]]]
    featureType: Optional[FeatureTypeEnum]
    id: str

class FeatureInput(BaseModel):
    name: Optional[str]
    description: Optional[str]
    options: Optional[List[Optional[str]]]
    featureType: Optional[FeatureTypeEnum]

class ProductTypeFeatureCreateInput(BaseModel):
    name: Optional[str]
    description: Optional[str]
    options: Optional[List[Optional[str]]]
    featureType: Optional[FeatureTypeEnum]
    id: str
    isVariantFeature: bool

class ProductTypeFeatureInput(BaseModel):
    name: Optional[str]
    description: Optional[str]
    options: Optional[List[Optional[str]]]
    featureType: Optional[FeatureTypeEnum]

class LocationInput(BaseModel):
    companyName: Optional[str]
    streetAddress1: Optional[str]
    streetAddress2: Optional[str]
    city: Optional[str]
    cityArea: Optional[str]
    postalCode: Optional[str]
    country: Optional[CountryCode]
    countryArea: Optional[str]
    phone: Optional[str]
    lon: Optional[float]
    lat: Optional[float]
    locationKind: Optional[LocationKindEnum]

class PageInput(BaseModel):
    slug: Optional[str]
    title: Optional[str]
    content: Optional[str]
    contentHtml: Optional[str]
    isPublished: Optional[bool]
    publicationDate: Optional[str]
    seo: Optional[SeoInput]

class DraftOrderCreateInput(BaseModel):
    billingAddress: Optional[AddressInput]
    user: Optional[str]
    userEmail: Optional[str]
    shippingAddress: Optional[AddressInput]
    customerNote: Optional[str]
    subStatus: Optional[OrderSubStatusEnum]
    lines: Optional[List[Optional[OrderLineCreateInput]]]
    seller: Optional[str]
    transactionCurrency: Optional[str]

class OrderLineCreateInput(BaseModel):
    quantity: int
    variantId: str

class NauticalDraftOrderCreateInput(BaseModel):
    billingAddress: Optional[AddressInput]
    user: Optional[str]
    userEmail: Optional[str]
    shippingAddress: Optional[AddressInput]
    customerNote: Optional[str]
    subStatus: Optional[OrderSubStatusEnum]
    poNumbers: Optional[List[Optional[str]]]
    lines: Optional[List[Optional[OrderLineCreateInput]]]
    seller: Optional[str]
    transactionCurrency: Optional[str]

class NauticalHistoricalOrderInput(BaseModel):
    billingAddress: Optional[AddressInput]
    shippingAddress: Optional[AddressInput]
    user: Optional[str]
    userEmail: Optional[str]
    discount: Optional[PositiveDecimal]
    shippingPriceNetAmount: Optional[PositiveDecimal]
    shippingPriceGrossAmount: Optional[PositiveDecimal]
    totalNetAmount: Optional[PositiveDecimal]
    totalGrossAmount: Optional[PositiveDecimal]
    currency: Optional[str]
    customerNote: Optional[str]
    lines: Optional[List[Optional[HistoricalOrderLineInput]]]
    seller: Optional[str]
    created: Optional[datetime]
    externalId: Optional[str]
    externalInventoryId: Optional[str]
    externalSource: Optional[str]

class HistoricalOrderLineInput(BaseModel):
    quantity: int
    variantId: str
    unitPriceNetAmount: Optional[PositiveDecimal]
    unitPriceGrossAmount: Optional[PositiveDecimal]
    externalId: Optional[str]

class OrderLineInput(BaseModel):
    quantity: int

class DraftOrderInput(BaseModel):
    billingAddress: Optional[AddressInput]
    user: Optional[str]
    userEmail: Optional[str]
    shippingAddress: Optional[AddressInput]
    customerNote: Optional[str]
    subStatus: Optional[OrderSubStatusEnum]

class NauticalDraftOrderInput(BaseModel):
    billingAddress: Optional[AddressInput]
    user: Optional[str]
    userEmail: Optional[str]
    shippingAddress: Optional[AddressInput]
    customerNote: Optional[str]
    subStatus: Optional[OrderSubStatusEnum]
    poNumbers: Optional[List[Optional[str]]]

class OrderLinePriceOverrideInput(BaseModel):
    overrideAmount: PositiveDecimal
    unitPriceOverriddenNote: str

class OrderAddNoteInput(BaseModel):
    message: str

class NoteInput(BaseModel):
    note: str

class OrderReturnNotificationInput(BaseModel):
    returnStatus: str
    productNames: Optional[str]

class OrderFulfillInput(BaseModel):
    lines: List[Optional[OrderFulfillLineInput]]
    notifyCustomer: Optional[bool]
    allowNullVariants: Optional[bool]
    customFields: Optional[List[Optional[AttributeValueInput]]]

class OrderFulfillLineInput(BaseModel):
    orderLineId: Optional[str]
    stocks: List[Optional[OrderFulfillStockInput]]

class OrderFulfillStockInput(BaseModel):
    quantity: int
    warehouse: str

class DeclineFulfillInput(BaseModel):
    lines: List[Optional[DeclineFulfillLineInput]]

class DeclineFulfillLineInput(BaseModel):
    orderLineId: str
    stocks: List[Optional[DeclineFulfillStockInput]]

class DeclineFulfillStockInput(BaseModel):
    quantityDeclined: int
    warehouse: str

class FulfillmentCancelInput(BaseModel):
    warehouseId: str

class FulfillmentReturnInput(BaseModel):
    fulfillmentLineId: str
    returnQuantity: int

class FulfillmentUpdateTrackingInput(BaseModel):
    trackingNumber: Optional[str]
    trackingUrl: Optional[str]
    trackingCompany: Optional[str]

class FulfillmentUpdateReturnStatusInput(BaseModel):
    status: str

class BulkFulfillmentReturnInput(BaseModel):
    fulfillmentId: str
    lineId: str
    orderLineId: Optional[str]
    quantity: int
    returnRequestedQty: int
    decision: Optional[str]
    returnReason: Optional[str]

class OrderUpdateInput(BaseModel):
    billingAddress: Optional[AddressInput]
    userEmail: Optional[str]
    shippingAddress: Optional[AddressInput]

class NauticalOrderUpdateInput(BaseModel):
    billingAddress: Optional[AddressInput]
    userEmail: Optional[str]
    shippingAddress: Optional[AddressInput]
    poNumbers: Optional[List[Optional[str]]]

class OrderPayoutStatusUpdateInput(BaseModel):
    payoutStatus: OrderPayoutStatusEnum

class OrderUpdateShippingInput(BaseModel):
    shippingMethod: Optional[str]
    isManual: Optional[bool]
    newPrice: Optional[PositiveDecimal]

class NauticalOrderUpdateShippingInput(BaseModel):
    seller: Optional[str]
    shippingMethod: Optional[str]
    isManual: Optional[bool]
    newPrice: Optional[PositiveDecimal]

class NauticalOrderUpdateMarketplaceShippingInput(BaseModel):
    shippingMethod: str
    isManual: Optional[bool]
    newPrice: Optional[PositiveDecimal]

class PaymentInput(BaseModel):
    gateway: str
    token: Optional[str]
    amount: Optional[PositiveDecimal]
    volumeDiscount: Optional[PositiveDecimal]
    billingAddress: Optional[AddressInput]
    returnUrl: Optional[str]

class OrderFeeInput(BaseModel):
    order: str
    name: str
    notes: Optional[str]
    feeValue: Decimal

class MenuCreateInput(BaseModel):
    name: str
    slug: Optional[str]
    items: Optional[List[Optional[MenuItemInput]]]

class MenuItemInput(BaseModel):
    name: Optional[str]
    url: Optional[str]
    category: Optional[str]
    collection: Optional[str]
    page: Optional[str]

class MenuInput(BaseModel):
    name: Optional[str]
    slug: Optional[str]

class MenuItemCreateInput(BaseModel):
    name: str
    url: Optional[str]
    category: Optional[str]
    collection: Optional[str]
    page: Optional[str]
    menu: str
    parent: Optional[str]

class MenuItemMoveInput(BaseModel):
    itemId: str
    parentId: Optional[str]
    relativeOffset: Optional[int]

class InvoiceCreateInput(BaseModel):
    number: str
    url: str

class UpdateInvoiceInput(BaseModel):
    number: Optional[str]
    url: Optional[str]

class PluginUpdateInput(BaseModel):
    active: Optional[bool]
    configuration: Optional[List[Optional[ConfigurationItemInput]]]
    allowSellers: Optional[bool]
    seller: Optional[str]

class ConfigurationItemInput(BaseModel):
    name: str
    value: Optional[GenericScalar]

class PluginFlowInput(BaseModel):
    seller: Optional[str]
    process: str
    mapping: str
    formId: str

class JournalEntryCorrectInput(BaseModel):
    correctingJournalEntry: str
    description: Optional[str]
    ledgerEntries: Optional[List[Optional[LedgerEntryInput]]]

class LedgerEntryInput(BaseModel):
    amount: Decimal
    ledger: str

class SaleInput(BaseModel):
    name: Optional[str]
    type: Optional[DiscountValueTypeEnum]
    value: Optional[PositiveDecimal]
    products: Optional[List[Optional[str]]]
    variants: Optional[List[Optional[str]]]
    categories: Optional[List[Optional[str]]]
    collections: Optional[List[Optional[str]]]
    startDate: Optional[datetime]
    endDate: Optional[datetime]
    minSpentAmount: Optional[PositiveDecimal]
    minCheckoutItemsQuantity: Optional[int]
    saleType: Optional[SaleTypeEnum]

class CatalogueInput(BaseModel):
    products: Optional[List[Optional[str]]]
    variants: Optional[List[Optional[str]]]
    categories: Optional[List[Optional[str]]]
    collections: Optional[List[Optional[str]]]

class VoucherInput(BaseModel):
    type: Optional[VoucherTypeEnum]
    name: Optional[str]
    code: Optional[str]
    startDate: Optional[datetime]
    endDate: Optional[datetime]
    discountValueType: Optional[DiscountValueTypeEnum]
    discountValue: Optional[PositiveDecimal]
    products: Optional[List[Optional[str]]]
    variants: Optional[List[Optional[str]]]
    collections: Optional[List[Optional[str]]]
    categories: Optional[List[Optional[str]]]
    minAmountSpent: Optional[PositiveDecimal]
    minCheckoutItemsQuantity: Optional[int]
    countries: Optional[List[Optional[str]]]
    applyOncePerOrder: Optional[bool]
    applyOncePerCustomer: Optional[bool]
    usageLimit: Optional[int]

class ExportProductsInput(BaseModel):
    scope: ExportScope
    filter: Optional[ProductFilterInput]
    ids: Optional[List[Optional[str]]]
    exportInfo: Optional[ExportInfoInput]
    fileType: FileTypesEnum

class ExportInfoInput(BaseModel):
    attributes: Optional[List[Optional[str]]]
    warehouses: Optional[List[Optional[str]]]
    fields: Optional[List[Optional[ProductFieldEnum]]]

class CheckoutCreateInput(BaseModel):
    lines: List[Optional[CheckoutLineInput]]
    email: Optional[str]
    shippingAddress: Optional[AddressInput]
    billingAddress: Optional[AddressInput]
    currency: Optional[MarketplaceConfigurationCurrencyEnum]

class CheckoutLineInput(BaseModel):
    quantity: int
    variantId: str

class SellerShippingMethodInput(BaseModel):
    seller: str
    shippingMethodSelection: str
    shippingMethodPriceOverrideAmount: Optional[PositiveDecimal]

class AttributeCreateInput(BaseModel):
    inputType: Optional[AttributeInputTypeEnum]
    name: str
    slug: Optional[str]
    values: Optional[List[Optional[AttributeValueCreateInput]]]
    valueRequired: Optional[bool]
    isVariantOnly: Optional[bool]
    visibleInStorefront: Optional[bool]
    filterableInStorefront: Optional[bool]
    filterableInDashboard: Optional[bool]
    storefrontSearchPosition: Optional[int]
    availableInGrid: Optional[bool]
    createdBy: Optional[str]

class AttributeValueCreateInput(BaseModel):
    name: str
    value: Optional[str]
    dateTime: Optional[datetime]
    plainText: Optional[str]
    richText: Optional[str]
    amount: Optional[Decimal]
    currency: Optional[str]
    reference: Optional[str]
    boolean: Optional[bool]
    file: Optional[Upload]
    fileUrl: Optional[str]

class AttributeAssignInput(BaseModel):
    id: str
    type: AttributeTypeEnum

class AttributeUpdateInput(BaseModel):
    name: Optional[str]
    slug: Optional[str]
    removeValues: Optional[List[Optional[str]]]
    addValues: Optional[List[Optional[AttributeValueCreateInput]]]
    valueRequired: Optional[bool]
    isVariantOnly: Optional[bool]
    visibleInStorefront: Optional[bool]
    filterableInStorefront: Optional[bool]
    filterableInDashboard: Optional[bool]
    storefrontSearchPosition: Optional[int]
    availableInGrid: Optional[bool]
    createdBy: Optional[str]

class AppInput(BaseModel):
    name: Optional[str]
    permissions: Optional[List[Optional[PermissionEnum]]]
    user: Optional[str]

class AppTokenInput(BaseModel):
    name: Optional[str]
    app: str

class AppInstallInput(BaseModel):
    appName: Optional[str]
    manifestUrl: Optional[str]
    permissions: Optional[List[Optional[PermissionEnum]]]

class AccountRegisterInput(BaseModel):
    email: str
    password: str
    redirectUrl: Optional[str]
    firstName: Optional[str]
    lastName: Optional[str]
    companyName: Optional[str]
    personalPhone: Optional[str]
    defaultBillingAddress: Optional[AddressInput]
    defaultShippingAddress: Optional[AddressInput]

class AccountInput(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    companyName: Optional[str]
    personalPhone: Optional[str]
    defaultBillingAddress: Optional[AddressInput]
    defaultShippingAddress: Optional[AddressInput]
    vatIdentificationNumber: Optional[str]

class UserCreateInput(BaseModel):
    defaultBillingAddress: Optional[AddressInput]
    defaultShippingAddress: Optional[AddressInput]
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    isActive: Optional[bool]
    isStaff: Optional[bool]
    note: Optional[str]
    companyName: Optional[str]
    personalPhone: Optional[str]
    passwordUrl: Optional[str]
    taxExemptCode: Optional[str]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    vatIdentificationNumber: Optional[str]
    sendCustomerSetPasswordEmail: Optional[bool]
    redirectUrl: Optional[str]

class CustomerInput(BaseModel):
    defaultBillingAddress: Optional[AddressInput]
    defaultShippingAddress: Optional[AddressInput]
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    isActive: Optional[bool]
    isStaff: Optional[bool]
    note: Optional[str]
    companyName: Optional[str]
    personalPhone: Optional[str]
    passwordUrl: Optional[str]
    taxExemptCode: Optional[str]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    vatIdentificationNumber: Optional[str]
    sendCustomerSetPasswordEmail: Optional[bool]

class StaffCreateInput(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    isActive: Optional[bool]
    isStaff: Optional[bool]
    note: Optional[str]
    companyName: Optional[str]
    personalPhone: Optional[str]
    passwordUrl: Optional[str]
    taxExemptCode: Optional[str]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    addGroups: Optional[List[Optional[str]]]
    sellerId: Optional[str]
    redirectUrl: Optional[str]

class StaffUpdateInput(BaseModel):
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    isActive: Optional[bool]
    isStaff: Optional[bool]
    note: Optional[str]
    companyName: Optional[str]
    personalPhone: Optional[str]
    passwordUrl: Optional[str]
    taxExemptCode: Optional[str]
    customFields: Optional[List[Optional[AttributeValueInput]]]
    addGroups: Optional[List[Optional[str]]]
    sellerId: Optional[str]
    removeGroups: Optional[List[Optional[str]]]

class PermissionGroupCreateInput(BaseModel):
    addPermissions: Optional[List[Optional[PermissionEnum]]]
    addUsers: Optional[List[Optional[str]]]
    name: str

class PermissionGroupUpdateInput(BaseModel):
    addPermissions: Optional[List[Optional[PermissionEnum]]]
    addUsers: Optional[List[Optional[str]]]
    name: Optional[str]
    removePermissions: Optional[List[Optional[PermissionEnum]]]
    removeUsers: Optional[List[Optional[str]]]
