import json
from pathlib import Path

REPORT = Path("/app/report.json")

# Ground truth for the fixed /app/access.log fixture (6 request lines):
#   requests : 6
#   IPs      : 192.168.0.1, 192.168.0.2, 10.0.0.5      -> 3 distinct
#   paths    : /index.html x3, /about.html x2, /api/login x1 -> top /index.html
EXPECTED_TOTAL = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _load():
    return json.loads(REPORT.read_text())


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and parses as a single JSON object."""
    assert REPORT.exists(), "no /app/report.json found"
    data = json.loads(REPORT.read_text())
    assert isinstance(data, dict), "report.json must contain a single JSON object"


def test_total_requests():
    """Criterion 2: total_requests counts every request line in the log."""
    assert _load()["total_requests"] == EXPECTED_TOTAL


def test_unique_ips():
    """Criterion 3: unique_ips counts the distinct client IP addresses."""
    assert _load()["unique_ips"] == EXPECTED_UNIQUE_IPS


def test_top_path():
    """Criterion 4: top_path is the most-requested path."""
    assert _load()["top_path"] == EXPECTED_TOP_PATH
