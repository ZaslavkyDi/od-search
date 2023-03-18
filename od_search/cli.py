import typing

from typer import Typer, Option

from od_search.config.constants import (
    TransactionDirection,
    TransactionTypeIdCliFormat,
    TransactionFilterNameOrderfulFormat,
)

app = Typer()


@app.command()
def search(
    direction: typing.Optional[TransactionDirection] = Option(
        None,
        "--direction",
        "-d",
        help="Transaction direction.",
        rich_help_panel="Filters",
    ),
    ttype: typing.Optional[TransactionTypeIdCliFormat] = Option(
        None,
        "--ttype",
        "-tt",
        help="Transaction type.",
        rich_help_panel="Filters",
    ),
    content_filters: list[TransactionFilterNameOrderfulFormat] = Option(
        None,
        "--content-filter",
        "-cf",
        help="Filter by transaction content.",
        rich_help_panel="Filters",
    ),
) -> None:
    print(f"Hello {direction.name}")
