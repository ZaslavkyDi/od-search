import json
from pathlib import Path
from typing import Any

import pytest


@pytest.fixture(scope="module")
def transactions_response() -> dict[str, Any]:
    resource_part = "resources/transactions_response.json"
    parent_path = (
        Path(__file__)
        .parent
        .parent
        .parent
        .parent
        .joinpath(resource_part)
    )
    with open(parent_path, "r") as file:
        yield json.loads(file.read().replace('\n', ''))
