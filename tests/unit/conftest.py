"""Shared test fixtures."""

import pytest
from rich.console import Console


@pytest.fixture
def recording_console() -> Console:
    return Console(record=True, width=80)
