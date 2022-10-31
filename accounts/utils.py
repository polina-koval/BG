from datetime import datetime

from django.db.models import Sum
from django.template.loader import render_to_string
from weasyprint import HTML, CSS


def make_receipt(obj):
    context = {
        "number": obj.unique_number,
        "date": datetime.now().strftime("%b %d %Y %H:%M:%S"),
        "games": obj.cart.games.all(),
        "total": obj.cart.games.all().aggregate(total=Sum("price"))[
            "total"
        ],
    }

    html_string = render_to_string(
        template_name="accounts/receipt.html", context=context
    )
    doc = HTML(string=html_string).write_pdf(
        stylesheets=[CSS("accounts/templates/accounts/receipt.css")]
    )
    return doc
