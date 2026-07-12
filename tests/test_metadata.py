from pathlib import Path

import pytest

from binarytriage.core.metadata import (
    MetadataError,
    extract_file_metadata,
)


def test_extract_file_metadata(tmp_path: Path) -> None:
    test_file = tmp_path / "sample.EXE"
    test_data = b"BinaryTriage-X metadata test"
    test_file.write_bytes(test_data)

    metadata = extract_file_metadata(
        file_path=test_file,
        detected_file_type="PE",
    )

    assert metadata.file_name == "sample.EXE"
    assert metadata.file_stem == "sample"
    assert metadata.extension == ".exe"
    assert metadata.suffixes == (".exe",)
    assert metadata.size_bytes == len(test_data)
    assert metadata.detected_file_type == "PE"
    assert metadata.absolute_path == str(test_file.resolve())


def test_extract_multiple_suffixes(tmp_path: Path) -> None:
    test_file = tmp_path / "invoice.pdf.exe"
    test_file.write_bytes(b"MZ-test")

    metadata = extract_file_metadata(
        file_path=test_file,
        detected_file_type="PE",
    )

    assert metadata.file_name == "invoice.pdf.exe"
    assert metadata.file_stem == "invoice.pdf"
    assert metadata.extension == ".exe"
    assert metadata.suffixes == (".pdf", ".exe")


def test_metadata_timestamps_are_utc(tmp_path: Path) -> None:
    test_file = tmp_path / "sample.bin"
    test_file.write_bytes(b"test")

    metadata = extract_file_metadata(
        file_path=test_file,
        detected_file_type="UNKNOWN",
    )

    assert metadata.modified_time_utc.endswith("Z")
    assert metadata.accessed_time_utc.endswith("Z")
    assert metadata.filesystem_change_time_utc.endswith("Z")

    if metadata.birth_time_utc is not None:
        assert metadata.birth_time_utc.endswith("Z")


def test_metadata_rejects_directory(tmp_path: Path) -> None:
    with pytest.raises(
        MetadataError,
        match="not a regular file",
    ):
        extract_file_metadata(
            file_path=tmp_path,
            detected_file_type="UNKNOWN",
        )


def test_metadata_rejects_missing_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.bin"

    with pytest.raises(MetadataError):
        extract_file_metadata(
            file_path=missing_file,
            detected_file_type="UNKNOWN",
        )


def test_metadata_to_dict_is_serializable(tmp_path: Path) -> None:
    test_file = tmp_path / "sample.bin"
    test_file.write_bytes(b"sample")

    metadata = extract_file_metadata(
        file_path=test_file,
        detected_file_type="UNKNOWN",
    )

    result = metadata.to_dict()

    assert isinstance(result, dict)
    assert isinstance(result["suffixes"], list)
    assert result["file_name"] == "sample.bin"