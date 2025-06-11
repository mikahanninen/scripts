import requests
from datetime import datetime
import pytz
from rich.console import Console
from rich.table import Table


def get_electricity_prices():
    """Get and format electricity prices from the API

    Returns:
        list: List of dictionaries containing formatted price data
    """
    url = "https://api.porssisahko.net/v1/latest-prices.json"
    response = requests.get(url).json()

    # Get current datetime at the start of the hour in Helsinki timezone
    helsinki_tz = pytz.timezone("Europe/Helsinki")
    current_datetime = datetime.now(helsinki_tz).replace(
        minute=0, second=0, microsecond=0
    )

    formatted_prices = []
    for price_data in response["prices"]:
        # Convert UTC timestamps to Helsinki time
        start_time = datetime.fromisoformat(
            price_data["startDate"].replace("Z", "+00:00")
        ).astimezone(helsinki_tz)

        # Skip if the time is in the past
        if start_time < current_datetime:
            continue

        rounded_price = round(price_data["price"], 2)
        if rounded_price < 5:
            text_style = "bold green"
        elif rounded_price < 10:
            text_style = "bold yellow"
        else:
            text_style = "bold red"

        formatted_prices.append(
            {
                "price": rounded_price,
                "time": start_time.strftime("%Y-%m-%d %H:%M"),
                "datetime": start_time,  # Keep datetime object for sorting
                "style": text_style,
            }
        )

    # Sort by datetime
    formatted_prices.sort(key=lambda x: x["datetime"])

    table = Table(title="Sähkön hinta (cents/kWh)")
    table.add_column("Aika", justify="left")
    table.add_column("Hinta", justify="left")
    for entry in formatted_prices:
        table.add_row(
            str(entry["time"]),
            f"[{entry['style']}] {entry['price']} [/{entry['style']}]",
        )

    console = Console()
    console.print("\n")
    console.print(table)
    return formatted_prices


if __name__ == "__main__":
    get_electricity_prices()
