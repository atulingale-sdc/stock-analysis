import enum


class ResponseTypeEnum(str, enum.Enum):
    success: str = "SUCCESS"
    error: str = "ERROR"
    warning: str = "WARNING"
    info: str = "INFO"


class UserTypeEnum(str, enum.Enum):
    cashier: str = "CASHIER"
    admin: str = "ADMIN"
    ticket_agent: str = "TICKET_AGENT"
    manager: str = "MANAGER"
    toast_user: str = "TOAST_USER"


class UserStatusEnum(str, enum.Enum):
    active: str = "ACTIVE"
    inactive: str = "INACTIVE"


class OrderEnum(str, enum.Enum):
    desc: str = "DESC"
    asc: str = "ASC"


class SearchFieldOperatorEnum(str, enum.Enum):
    between: str = "BETWEEN"
    gt: str = ">"
    lt: str = "<"
    eq: str = "="
    ne: str = "!="
    gteq: str = ">="
    lteq: str = "<="


class GCActions(enum.Enum):
    # This will be used when the endpoint does not require any specific action access
    any: str = "*"

    # Masters
    store_master = "master_store"
    taxes_charges_master = "master_taxes_charges"
    ticket_roll_master = "master_ticket_roll"
    location_master = "master_location"
    general_ledger_code_master = "master_general_ledger_code"
    event_category_master = "master_event_category"

    # Reports
    reports_host_bar: str = "report_host_bar"
    reports_beverage_by_store: str = "report_beverage_by_store"
    reports_bar_snack_gift_summary: str = "report_bar_snack_gift_summary"
    reports_tax_exempt: str = "report_tax_exempt"
    reports_non_gc_trip_location: str = "report_non_gc_trip_location"
    reports_charter_advance_payments: str = "report_charter_advance_payments"
    reports_tripsheet_details: str = "report_tripsheet_details"
    reports_daily_monthly_credit_card_log: str = "report_daily_monthly_credit_card_log"
    reports_daily_revenue: str = "report_daily_revenue"
    reports_cash_over_short: str = "report_cash_over_short"
    reports_gift_card_activation_or_redeemed: str = "report_gift_card_activation_or_redeemed"
    reports_accounts_receivables: str = "report_accounts_receivables"
    reports_daily_revenue_miscellaneous: str = "report_daily_revenue_miscellaneous"
    reports_shuttle_ticket_recon: str = "report_shuttle_ticket_recon"
    # User Management
    user_read: str = "user_read"
    user_write: str = "user_write"

    # Dashboard
    dashboard_weekly_trip_due_amt: str = "dashboard_weekly_trip_due_amt"
    dashboard_daily_trips_revenue: str = "dashboard_daily_trips_revenue"
    dashboard_daily_no_of_trips: str = "dashboard_daily_no_of_trips"
    dashboard_revenue_report: str = "dashboard_revenue_report"
    dashboard_eventwise_report: str = "dashboard_eventwise_report"
    dashboard_activity_status: str = "dashboard_activity_status"
    dashboard_advance_deposit_total: str = "dashboard_advance_deposit_total"

    # Transactions
    shuttle_payment_collection_verification: str = "transaction_shuttle_payment_collection_verification"
    public_event_recon_write: str = "transaction_public_event_recon_write"
    public_event_recon_read: str = "transaction_public_event_recon_read"
    private_event_recon_write: str = "transaction_private_event_recon_write"
    private_event_recon_read: str = "transaction_private_event_recon_read"
    shuttle_event_recon_write: str = "transaction_shuttle_event_recon_write"
    shuttle_event_recon_read: str = "transaction_shuttle_event_recon_read"
    gift_card_recon_read: str = "transaction_gift_card_recon_read"
    gift_card_recon_write: str = "transaction_gift_card_recon_write"
    payment_refund: str = "transaction_payment_refund"
    payment_collection: str = "transaction_payment_collection"
    ticket_booking_entry: str = "transaction_ticket_booking_entry"
    ticket_booking_entry_verification: str = "transaction_ticket_booking_entry_verification"
    ticket_roll_assignment: str = "transaction_ticket_roll_assignment"
    sage_integration: str = "transaction_sage_integration"


class MasterStoreTypeEnum(str, enum.Enum):
    vessel: str = "VESSEL"
    cafe: str = "CAFE"
    dock: str = "DOCK"


class MasterStoreStatusEnum(str, enum.Enum):
    active: str = "ACTIVE"
    inactive: str = "INACTIVE"


class MasterTaxTypeEnum(str, enum.Enum):
    percent: str = "PERCENT"
    amount: str = "AMOUNT"


class MasterTaxStatusEnum(str, enum.Enum):
    inactive: str = "INACTIVE"
    active: str = "ACTIVE"


class JourneyTypeEnum(str, enum.Enum):
    ONE_WAY: str = "ONE_WAY"
    ROUND_TRIP: str = "ROUND_TRIP"


class MasterTicketStatusEnum(str, enum.Enum):
    active: str = "ACTIVE"
    archive: str = "ARCHIVE"
    in_use: str = "IN_USE"


class LocationMasterStatusEnum(str, enum.Enum):
    active: str = "ACTIVE"
    inactive: str = "INACTIVE"


class TransactionShuttlePaymentEntryStatusEnum(str, enum.Enum):
    pending: str = "PENDING"
    verified: str = "VERIFIED"


class TicketSaleEventTypeEnum(str, enum.Enum):
    transaction_shuttle_payment_Entry: str = "TransactionShuttlePaymentEntry"
    fareharbor: str = "FareHarborTicket"
    toast: str = "ToastTicket"


class WebhookEventStatus(str, enum.Enum):
    pending: str = "PENDING"
    processed: str = "PROCESSED"


class EventTypeEnum(str, enum.Enum):
    public: str = "PUBLIC"
    private: str = "PRIVATE"
    shuttle: str = "SHUTTLE"


class BookingStatus(str, enum.Enum):
    booked: str = "booked"
    cancelled: str = "cancelled"


class TicketType(str, enum.Enum):
    adult: str = "Adult"
    child: str = "Child"
    infant: str = "Infant"


class BookingPaymentStatus(str, enum.Enum):
    paid: str = "PAID"
    pending: str = "PENDING"
    refunded: str = "REFUNDED"
    partially_paid: str = "PARTIALLY_PAID"


class PaymentStatus(str, enum.Enum):
    success: str = "success"


class PublicEventReconciliationStatus(str, enum.Enum):
    pending: str = "PENDING"
    cancelled: str = "CANCELLED"
    reconciled: str = "RECONCILED"


class ShuttleEventReconciliationStatus(str, enum.Enum):
    pending: str = "PENDING"
    cancelled: str = "CANCELLED"
    reconciled: str = "RECONCILED"


class IsReconciled(enum.Enum):
    TRUE = True
    FALSE = False


class ToastOrderPaymentModesEnum(str, enum.Enum):
    cash: str = "CASH"
    credit_card: str = "CREDIT_CARD"


class ToastOrderPaymentStatusEnum(str, enum.Enum):
    captured: str = "CAPTURED"
    denied: str = "DENIED"
    voided: str = "VOIDED"
    pending: str = "PENDING"


class TaxCodes(str, enum.Enum):
    # SERVICE_CHARGE_PUBLIC_SIGHTSEEING: str = "SC_PUB_SIG"
    AMUSEMENT_TAX_PUBLIC_SIGHTSEEING: str = "AT_PUB_SIG"
    # PA_SALES_TAX_PUBLIC_SIGHTSEEING: str = "PA_PUB_SIGH"
    ALCOHOLIC_BEVERAGE_TAX_PUBLIC_SIGHTSEEING: str = "AB_PUB_SIGH"
    FOOD_TAX_PUBLIC_SIGHTSEEING: str = "FD_PUB_SIGH"
    # GROSS_RECEIPT_TAX_PUBLIC_SIGHTSEEING: str = "GR_PUB_SIGH"

    SERVICE_CHARGE_PUBLIC_AFTERNOON_DINING: str = "SC_PUB_AFDI"
    AMUSEMENT_TAX_PUBLIC_AFTERNOON_DINING: str = "AT_PUB_AFDI"
    PA_SALES_TAX_PUBLIC_AFTERNOON_DINING: str = "PA_PUB_AFDI"
    ALCOHOLIC_BEVERAGE_TAX_PUBLIC_AFTERNOON_DINING: str = "AB_PUB_AFDI"
    FOOD_TAX_PUBLIC_AFTERNOON_DINING: str = "FD_PUB_AFDI"
    # GROSS_RECEIPT_PUBLIC_AFTERNOON_DINING: str = "GR_PUB_AFDI"

    SERVICE_CHARGE_PUBLIC_EVENING_DINING: str = "SC_PUB_EVDI"
    AMUSEMENT_TAX_PUBLIC_EVENING_DINING: str = "AT_PUB_EVDI"
    PA_SALES_TAX_PUBLIC_EVENING_DINING: str = "PA_PUB_EVDI"
    ALCOHOLIC_BEVERAGE_TAX_PUBLIC_EVENING_DINING: str = "AB_PUB_EVDI"
    FOOD_TAX_PUBLIC_EVENING_DINING: str = "FD_PUB_EVDI"
    # GROSS_RECEIPT_PUBLIC_EVENING_DINING: str = "GR_PUB_EVDI"

    SERVICE_CHARGE_PUBLIC_DANCE_TRIP: str = "SC_PUB_DATR"
    AMUSEMENT_TAX_PUBLIC_DANCE_TRIP: str = "AT_PUB_DATR"
    PA_SALES_TAX_PUBLIC_DANCE_TRIP: str = "PA_PUB_DATR"
    ALCOHOLIC_BEVERAGE_TAX_PUBLIC_DANCE_TRIP: str = "AB_PUB_DATR"
    FOOD_TAX_PUBLIC_DANCE_TRIP: str = "FD_PUB_DATR"
    GROSS_RECEIPT_PUBLIC_DANCE_TRIP: str = "GR_PUB_DATR"

    # SERVICE_CHARGE_SHUTTLE: str = "SC_SHUT"
    # AMUSEMENT_TAX_SHUTTLE: str = "AT_SHUT"
    # PA_SALES_TAX_SHUTTLE: str = "PA_SHUT"
    # ALCOHOLIC_BEVERAGE_TAX_SHUTTLE: str = "AB_SHUT"
    # BEVERAGE_TAX_SHUTTLE: str = "BV_SHUT"
    GROSS_RECEIPT_SHUTTLE: str = "GR_SHUT"


class PaymentSourceEnum(str, enum.Enum):
    cash: str = "CASH"
    cheque: str = "CHEQUE"
    green_apple: str = "GREEN_APPLE"


class PaymentTypeEnum(str, enum.Enum):
    event: str = "EVENT"
    misc: str = "MISC"
    store: str = "STORE"


class PaymentCollectionEventTypeEnum(str, enum.Enum):
    public: str = "PUBLIC"
    private: str = "PRIVATE"


class PaymentCollectionStatus(str, enum.Enum):
    pending: str = "PENDING"
    reconciled: str = "RECONCILED"


class EntityTypeEnum(str, enum.Enum):
    transaction_shuttle_payment_Entry: str = "TransactionShuttlePaymentEntry"
    payment_collection: str = "PaymentCollectionModel"
    toast_payment: str = "ToastPaymentModel"
