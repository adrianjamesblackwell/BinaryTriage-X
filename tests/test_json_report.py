import json
from pathlib import Path

from binarytriage.models.metadata import FileMetadata
from binarytriage.models.sample import Sample
from binarytriage.reporting.json_report import (
    generate_json_report,
    write_json_report,
)


def build_test_sample() -> Sample:
    metadata = FileMetadata(
        file_name="sample.exe",
        file_stem="sample",
        extension=".exe",
        suffixes=(".exe",),
        absolute_path="/tmp/sample.exe",
        size_bytes=128,
        modified_time_utc="2026-07-10T12:00:00Z",
        accessed_time_utc="2026-07-10T12:00:00Z",
        filesystem_change_time_utc="2026-07-10T12:00:00Z",
        birth_time_utc=None,
        detected_file_type="PE",
    )

    return Sample(
        path=Path("/tmp/sample.exe"),
        file_type="PE",
        hashes={"sha256": "abc123"},
        metadata=metadata,
    )


def test_generate_json_report() -> None:
    sample = build_test_sample()

    report = generate_json_report(sample)
    parsed_report = json.loads(report)

    assert parsed_report["file_type"] == "PE"
    assert parsed_report["hashes"]["sha256"] == "abc123"
    assert parsed_report["metadata"]["size_bytes"] == 128


def test_generate_compact_json_report() -> None:
    sample = build_test_sample()

    report = generate_json_report(
        sample,
        pretty=False,
    )

    assert "\n" not in report


def test_write_json_report(tmp_path: Path) -> None:
    sample = build_test_sample()
    output_path = tmp_path / "reports" / "sample.json"

    result_path = write_json_report(
        sample,
        output_path,
    )

    assert result_path.exists()
    assert result_path == output_path.resolve()

    parsed_report = json.loads(
        result_path.read_text(encoding="utf-8")
    )

    assert parsed_report["file_name"] == "sample.exe"