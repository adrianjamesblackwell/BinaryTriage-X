from pathlib import Path

from binarytriage.models.metadata import FileMetadata
from binarytriage.models.sample import Sample


def test_create_sample_with_path() -> None:
    sample = Sample(path=Path("sample.exe"))

    assert sample.path == Path("sample.exe")
    assert sample.file_type == "UNKNOWN"
    assert sample.hashes == {}
    assert sample.metadata is None
    assert sample.findings == []


def test_sample_to_dict_without_metadata() -> None:
    sample = Sample(
        path=Path("sample.exe"),
        file_type="PE",
        hashes={"sha256": "abc123"},
    )

    result = sample.to_dict()

    assert result["path"] == "sample.exe"
    assert result["file_name"] == "sample.exe"
    assert result["file_type"] == "PE"
    assert result["hashes"]["sha256"] == "abc123"
    assert result["metadata"] is None


def test_sample_to_dict_with_metadata() -> None:
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

    sample = Sample(
        path=Path("/tmp/sample.exe"),
        file_type="PE",
        metadata=metadata,
    )

    result = sample.to_dict()

    assert result["metadata"] is not None
    assert result["metadata"]["size_bytes"] == 128
    assert result["metadata"]["detected_file_type"] == "PE"


def test_sample_lists_are_not_shared() -> None:
    sample_a = Sample(path=Path("a.exe"))
    sample_b = Sample(path=Path("b.exe"))

    sample_a.findings.append({"title": "test finding"})

    assert len(sample_a.findings) == 1
    assert len(sample_b.findings) == 0