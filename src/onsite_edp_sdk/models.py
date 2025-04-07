"""Blocks used by the EDP Document."""

from typing import Literal

from pydantic import BaseModel, Field

DATE_REGEX = "[0-9]{2}/[0-9]{2}/[0-9]{4}|[0-9]{2}"


class Order(BaseModel):
    """Order Block."""

    # ID
    external_order_id: str = Field(serialization_alias="ExtOrderID")
    external_source: str | None = Field(None, serialization_alias="ExtSource")
    # Per upstream documentation, date_external is required, but we're currently processing orders without it.
    date_external: str | None = Field(None, pattern=DATE_REGEX, serialization_alias="date_External")
    order_type_id: float = Field(serialization_alias="id_OrderType")

    # Details
    customer_purchase_order: str | None = Field(None, serialization_alias="CustomerPurchaseOrder")
    terms_name: str | None = Field(None, serialization_alias="TermsName")
    customer_service_rep: str | None = Field(None, serialization_alias="CustomerServiceRep")
    customer_type: str | None = Field(None, serialization_alias="CustomerType")
    company_location_id: int | None = Field(None, serialization_alias="id_CompanyLocation")
    sales_status_id: int | None = Field(None, serialization_alias="id_SalesStatus")
    status_allow_commishion: Literal[0, 1] | None = Field(None, serialization_alias="sts_CommishAllow")
    hold_order_text: Literal["Yes", "No"] | None = Field(None, serialization_alias="HoldOrderText")

    # Dates
    date_order_placed: str = Field(pattern=DATE_REGEX, serialization_alias="date_OrderPlaced")
    date_order_requested_to_ship: str | None = Field(None, pattern=DATE_REGEX, serialization_alias="date_OrderRequestedToShip")
    date_order_drop_dead: str | None = Field(None, pattern=DATE_REGEX, serialization_alias="date_OrderDropDead")

    # Sales Tax
    status_order_sales_tax_override: Literal[0, 1] | None = Field(None, serialization_alias="sts_Order_SalesTax_Override")
    status_apply_sales_tax_1: Literal[0, 1] | None = Field(None, serialization_alias="sts_ApplySalesTax01")
    status_apply_sales_tax_2: Literal[0, 1] | None = Field(None, serialization_alias="sts_ApplySalesTax02")
    status_apply_sales_tax_3: Literal[0, 1] | None = Field(None, serialization_alias="sts_ApplySalesTax03")
    status_apply_sales_tax_4: Literal[0, 1] | None = Field(None, serialization_alias="sts_ApplySalesTax04")
    coa_account_sales_tax_1: Literal[0, 1] | None = Field(None, serialization_alias="coa_AccountSalesTax01")
    coa_account_sales_tax_2: Literal[0, 1] | None = Field(None, serialization_alias="coa_AccountSalesTax02")
    coa_account_sales_tax_3: Literal[0, 1] | None = Field(None, serialization_alias="coa_AccountSalesTax03")
    coa_account_sales_tax_4: Literal[0, 1] | None = Field(None, serialization_alias="coa_AccountSalesTax04")
    status_shipping_taxable: Literal[0, 1] | None = Field(None, serialization_alias="sts_ShippingTaxable")

    # Shipping
    address_description: str | None = Field(None, serialization_alias="AddressDescription")
    address_company: str | None = Field(None, serialization_alias="AddressCompany")
    address1: str | None = Field(None, serialization_alias="Address1")
    address2: str | None = Field(None, serialization_alias="Address2")
    address_city: str | None = Field(None, serialization_alias="AddressCity")
    address_state: str | None = Field(None, serialization_alias="AddressState")
    address_zip: str | None = Field(None, serialization_alias="AddressZip")
    address_country: str | None = Field(None, serialization_alias="AddressCountry")
    ship_method: str | None = Field(None, serialization_alias="ShipMethod")
    status_shipping_taxable_field: Literal[0, 1] | None = Field(None, serialization_alias="sts_ShippingTaxableField")
    cur_shipping: float | None = Field(None, serialization_alias="cur_Shipping")
    status_order_shipping_address_add: Literal[0, 1] | None = Field(None, serialization_alias="sts_Order_ShipAddress_Add")

    # Notes
    notes_to_art: str | None = Field(None, serialization_alias="NotesToArt")
    notes_to_production: str | None = Field(None, serialization_alias="NotesToProduction")
    notes_to_receiving: str | None = Field(None, serialization_alias="NotesToReceiving")
    notes_to_purchasing: str | None = Field(None, serialization_alias="NotesToPurchasing")
    notes_to_shipping: str | None = Field(None, serialization_alias="NotesToShipping")
    notes_to_accounting: str | None = Field(None, serialization_alias="NotesToAccounting")
    notes_to_purchasing_sub: str | None = Field(None, serialization_alias="NotesToPurchasingSub")


class Customer(BaseModel):
    """Customer Block."""

    # Details
    external_customer_id: str | None = Field(None, serialization_alias="ExtCustomerID")
    customer_id: int | None = Field(None, serialization_alias="id_Customer")
    company: str | None = Field(None, serialization_alias="Company")
    company_location_id: int | None = Field(None, serialization_alias="id_CompanyLocation")
    terms: str | None = Field(None, serialization_alias="Terms")
    website_url: str | None = Field(None, serialization_alias="WebsiteURL")
    email_main: str | None = Field(None, serialization_alias="EmailMain")

    # Address
    address_description: str | None = Field(None, serialization_alias="AddressDescription")
    address_company: str | None = Field(None, serialization_alias="AddressCompany")
    address1: str | None = Field(None, serialization_alias="Address1")
    address2: str | None = Field(None, serialization_alias="Address2")
    address_city: str | None = Field(None, serialization_alias="AddressCity")
    address_state: str | None = Field(None, serialization_alias="AddressState")
    address_zip: str | None = Field(None, serialization_alias="AddressZip")
    address_country: str | None = Field(None, serialization_alias="AddressCountry")

    # Sales Tax
    sts_apply_sales_tax_1: Literal[0, 1] | None = Field(None, serialization_alias="sts_ApplySalesTax01")
    sts_apply_sales_tax_2: Literal[0, 1] | None = Field(None, serialization_alias="sts_ApplySalesTax02")
    sts_apply_sales_tax_3: Literal[0, 1] | None = Field(None, serialization_alias="sts_ApplySalesTax03")
    sts_apply_sales_tax_4: Literal[0, 1] | None = Field(None, serialization_alias="sts_ApplySalesTax04")
    coa_account_sale_tax_1: str | None = Field(None, serialization_alias="coa_AccountSalesTax01")
    coa_account_sale_tax_2: str | None = Field(None, serialization_alias="coa_AccountSalesTax02")
    coa_account_sale_tax_3: str | None = Field(None, serialization_alias="coa_AccountSalesTax03")
    coa_account_sale_tax_4: str | None = Field(None, serialization_alias="coa_AccountSalesTax04")
    tax_exempt_number: str | None = Field(None, serialization_alias="TaxExemptNumber")

    # Price Calculator
    discount_level_id: int | None = Field(None, serialization_alias="id_DiscountLevel")
    default_calculator_1_id: str | None = Field(None, serialization_alias="id_DefaultCalculator1")
    default_calculator_2_id: str | None = Field(None, serialization_alias="id_DefaultCalculator2")

    # Profile
    customer_server_rep: str | None = Field(None, serialization_alias="CustomerServiceRep")
    customer_type: str | None = Field(None, serialization_alias="CustomerType")
    customer_source: str | None = Field(None, serialization_alias="CustomerSource")
    reference_from: str | None = Field(None, serialization_alias="ReferenceFrom")
    sic_code: str | None = Field(None, serialization_alias="SICCode")
    sic_description: str | None = Field(None, serialization_alias="SICDescription")
    employee_count: int | None = Field(None, serialization_alias="n_EmployeeCount")

    # Custom Fields
    custom_field_1: str | None = Field(None, serialization_alias="CustomField01")
    custom_field_2: str | None = Field(None, serialization_alias="CustomField02")
    custom_field_3: str | None = Field(None, serialization_alias="CustomField03")
    custom_field_4: str | None = Field(None, serialization_alias="CustomField04")
    custom_field_5: str | None = Field(None, serialization_alias="CustomField05")
    custom_field_6: str | None = Field(None, serialization_alias="CustomField06")
    custom_field_7: str | None = Field(None, pattern=DATE_REGEX, serialization_alias="CustomField07")
    custom_field_8: str | None = Field(None, pattern=DATE_REGEX, serialization_alias="CustomField08")
    custom_field_9: str | None = Field(None, pattern=DATE_REGEX, serialization_alias="CustomField09")
    custom_field_10: str | None = Field(None, pattern=DATE_REGEX, serialization_alias="CustomField10")


class Contact(BaseModel):
    """Contact Block."""

    first_name: str | None = Field(None, serialization_alias="NameFirst")
    last_name: str | None = Field(None, serialization_alias="NameLast")
    department: str | None = Field(None, serialization_alias="Department")
    title: str | None = Field(None, serialization_alias="Title")
    phone: str | None = Field(None, serialization_alias="Phone")
    fax: str | None = Field(None, serialization_alias="Fax")
    email: str | None = Field(None, serialization_alias="Email")
    status_enable_bulk_email: Literal[0, 1] | None = Field(None, serialization_alias="sts_EnableBulkEmail")
    status_contact_add: Literal[0, 1] | None = Field(None, serialization_alias="sts_Contact_Add")


class Design(BaseModel):
    """Design Block."""

    # Design
    external_design_id: str | None = Field(None, serialization_alias="ExtDesignID")
    design_id: int | None = Field(None, serialization_alias="id_Design")
    design_type_id: int | None = Field(None, serialization_alias="id_DesignType")
    design_name: str | None = Field(None, serialization_alias="DesignName")


class DesignLocation(BaseModel):
    """Design Location Block."""

    # Location
    location: str = Field(serialization_alias="Location")
    total_colors: int | None = Field(None, serialization_alias="ColorsTotal")
    total_flashes: int | None = Field(None, serialization_alias="FlashesTotal")
    total_stitches: int | None = Field(None, serialization_alias="StitchesTotal")
    design_code: str | None = Field(None, serialization_alias="DesignCode")

    # Color
    # Per upstream documentation, color is required, but we're currently processing orders without it.
    color: str | None = Field(None, serialization_alias="Color")
    map: str | None = Field(None, serialization_alias="Map")


class Product(BaseModel):
    """Product Block."""

    # Product
    part_number: str = Field(serialization_alias="PartNumber")
    part_color_range: str | None = Field(None, serialization_alias="PartColorRange")
    part_color: str | None = Field(None, serialization_alias="PartColor")
    part_description: str | None = Field(None, serialization_alias="PartDescription")
    cur_unit_price_user_entered: float | None = Field(None, serialization_alias="cur_UnitPriceUserEntered")
    order_instructions: str | None = Field(None, serialization_alias="OrderInstructions")

    size1_required: int | None = Field(None, serialization_alias="Size01_Req")
    size2_required: int | None = Field(None, serialization_alias="Size02_Req")
    size3_required: int | None = Field(None, serialization_alias="Size03_Req")
    size4_required: int | None = Field(None, serialization_alias="Size04_Req")
    size5_required: int | None = Field(None, serialization_alias="Size05_Req")
    size6_required: int | None = Field(None, serialization_alias="Size06_Req")

    status_production_product_override: Literal[0, 1] | None = Field(None, serialization_alias="sts_Prod_Product_Override")
    cur_unit_cost: float | None = Field(None, serialization_alias="cur_UnitCost")
    status_enable_commission: Literal[0, 1] | None = Field(None, serialization_alias="sts_EnableCommission")
    product_class_id: int | None = Field(None, serialization_alias="id_ProductClass")

    # Sales Tax
    status_production_sales_tax_override: Literal[0, 1] | None = Field(None, serialization_alias="sts_Prod_SalesTax_Override")
    status_enable_tax_1: Literal[0, 1] | None = Field(None, serialization_alias="sts_EnableTax01")
    status_enable_tax_2: Literal[0, 1] | None = Field(None, serialization_alias="sts_EnableTax02")
    status_enable_tax_3: Literal[0, 1] | None = Field(None, serialization_alias="sts_EnableTax03")
    status_enable_tax_4: Literal[0, 1] | None = Field(None, serialization_alias="sts_EnableTax04")

    # Secondary Units
    status_production_secondary_units_override: Literal[0, 1] | None = Field(
        None,
        serialization_alias="sts_Prod_SecondaryUnits_Override",
    )
    status_use_secondary_units: Literal[0, 1] | None = Field(None, serialization_alias="sts_UseSecondaryUnits")
    units_quantity: int | None = Field(None, serialization_alias="Units_Qty")
    units_type: (
        Literal[
            "Linear Feet",
            "Linear Inches",
            "Linear Centimeters",
            "Linear Meters",
            "Linear Yards",
            "Square Feet",
            "Square Inches",
            "Square Yards",
            "Square Meters",
            "Square Centimeters",
            "Units",
            "Pieces",
            "Count",
        ]
        | None
    ) = Field(None, serialization_alias="Units_Type")
    units_area1: int | None = Field(None, serialization_alias="Units_Area1")
    units_area2: int | None = Field(None, serialization_alias="Units_Area2")
    status_units_pricing: Literal[0, 1] | None = Field(None, serialization_alias="sts_UnitsPricing")
    status_units_purchasing: Literal[0, 1] | None = Field(None, serialization_alias="sts_UnitsPurchasing")
    status_units_purchasing_extra_percent: float | None = Field(None, serialization_alias="sts_UnitsPurchasingExtraPercent")
    status_units_purchasing_extra_round: Literal[1] | None = Field(None, serialization_alias="sts_UnitsPurchasingExtraRound")

    # Behavior
    status_production_behavior_override: Literal[0, 1] | None = Field(None, serialization_alias="sts_Prod_Behavior_Override")
    status_product_source_supplied: Literal[0, 1] | None = Field(None, serialization_alias="sts_ProductSource_Supplied")
    status_product_source_purchase: Literal[0, 1] | None = Field(None, serialization_alias="sts_ProductSource_Purchase")
    status_product_source_inventory: Literal[0, 1] | None = Field(None, serialization_alias="sts_ProductSource_Inventory")

    status_production_designs: Literal[0, 1] | None = Field(None, serialization_alias="sts_Production_Designs")
    status_production_subcontract: Literal[0, 1] | None = Field(None, serialization_alias="sts_Production_Subcontract")
    status_production_components: Literal[0, 1] | None = Field(None, serialization_alias="sts_Production_Components")

    status_storage_ship: Literal[0, 1] | None = Field(None, serialization_alias="sts_Storage_Ship")
    status_storage_inventory: Literal[0, 1] | None = Field(None, serialization_alias="sts_Storage_Inventory")

    status_invoicing_invoice: Literal[0, 1] | None = Field(None, serialization_alias="sts_Invoicing_Invoice")


class Payment(BaseModel):
    """Payment Block."""

    date_payment: str = Field(pattern=DATE_REGEX, serialization_alias="date_Payment")
    cur_payment: float | None = Field(None, serialization_alias="cur_Payment")
    payment_type: str | None = Field(None, serialization_alias="PaymentType")
    payment_number: str | None = Field(None, serialization_alias="PaymentNumber")
    card_name_first: str | None = Field(None, serialization_alias="Card_Name_First")
    card_name_last: str | None = Field(None, serialization_alias="Card_Name_Last")
    card_expiration_date: str | None = Field(None, serialization_alias="Card_Exp_Date")
    notes: str | None = Field(None, serialization_alias="Notes")


class EDPDocument(BaseModel):
    """EDP Document."""

    order: Order
    customer: Customer
    contact: Contact | None = Field(None)
    designs: list[tuple[Design, list[DesignLocation]]] | None = Field(None)
    products: list[Product] | None = Field(None)
    payment: Payment | None = Field(None)

    def to_edp(self, tag_bracket: str = "----", data_seperator: str = ": ", carriage_return: str = "<cr>") -> str:
        """Serialize to EDP format."""
        data = self.model_dump(by_alias=True, exclude_unset=True)
        text = ""

        for block_name in data:
            block_data = data[block_name]
            if not isinstance(block_data, list):
                block_data = [block_data]

            for block in block_data:
                block_text = ""
                block_text += f"{tag_bracket} Start {block_name.removesuffix("s").title()} {tag_bracket}\n"

                for key, value in block.items():
                    if isinstance(value, str):
                        value = value.replace("\n", carriage_return)  # noqa: PLW2901
                    block_text += f"{key}{data_seperator}{value}\n"

                block_text += f"{tag_bracket} End {block_name.removesuffix("s").title()} {tag_bracket}\n"

                text += block_text

        return text
