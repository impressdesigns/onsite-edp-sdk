"""Test models."""

from datetime import date

from onsite_edp_sdk import Customer, Design, DesignLocation, EDPDocument, Order

SAMPLE_DOCUMENT = EDPDocument(
    order=Order(
        external_order_id="TEST",
        date_external=date(2022, 8, 5),
        order_type_id=1,
        date_order_placed=date(2022, 8, 5),
        on_hold=True,
        status_allow_commission=True,
    ),
    customer=Customer(
        customer_id=1,
    ),
    designs=[
        (
            Design(
                design_name="Design1",
            ),
            [
                DesignLocation(
                    location="Test Location",
                ),
            ],
        ),
    ],
)

SAMPLE_OUTPUT = """\
---- Start Order ----
ExtOrderID: TEST
date_External: 08/05/2022
id_OrderType: 1.0
sts_CommishAllow: 1
HoldOrderText: Yes
date_OrderPlaced: 08/05/2022
---- End Order ----
---- Start Customer ----
id_Customer: 1
---- End Customer ----
---- Start Design ----
DesignName: Design1
---- Start Location ----
Location: Test Location
---- End Location ----
---- End Design ----
"""


def test_can_create_order() -> None:
    """Sanity check."""
    assert SAMPLE_DOCUMENT.to_edp() == SAMPLE_OUTPUT


def test_a_location_with_a_list_of_colours_writes_one_color_line_per_colour() -> None:
    """Each colour in the list gets its own ``Color`` line, in order, inside the location."""
    document = EDPDocument(
        order=Order(external_order_id="TEST", order_type_id=1, date_order_placed=date(2022, 8, 5)),
        customer=Customer(customer_id=1),
        designs=[
            (
                Design(design_name="Design1"),
                [DesignLocation(location="Front", total_colors=2, color=["_", "Navy", "White"], map="Line 1\nLine 2")],
            ),
        ],
    )

    assert document.to_edp().endswith(
        """\
---- Start Design ----
DesignName: Design1
---- Start Location ----
Location: Front
ColorsTotal: 2
Color: _
Color: Navy
Color: White
Map: Line 1<cr>Line 2
---- End Location ----
---- End Design ----
""",
    )


def test_a_location_with_one_colour_writes_one_color_line() -> None:
    """A single colour still writes as a plain ``Color`` line."""
    document = EDPDocument(
        order=Order(external_order_id="TEST", order_type_id=1, date_order_placed=date(2022, 8, 5)),
        customer=Customer(customer_id=1),
        designs=[(Design(design_name="Design1"), [DesignLocation(location="Front", color="Navy")])],
    )

    assert "---- Start Location ----\nLocation: Front\nColor: Navy\n---- End Location ----\n" in document.to_edp()


def test_line_breaks_inside_a_listed_colour_become_carriage_return_markers() -> None:
    """A newline inside one of the colours is written with the carriage return marker, like any other text."""
    document = EDPDocument(
        order=Order(external_order_id="TEST", order_type_id=1, date_order_placed=date(2022, 8, 5)),
        customer=Customer(customer_id=1),
        designs=[(Design(design_name="Design1"), [DesignLocation(location="Front", color=["Navy\nBlue"])])],
    )

    assert "Color: Navy<cr>Blue\n" in document.to_edp()
