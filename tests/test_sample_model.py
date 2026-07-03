from pathlib import Path

from binarytriage.models.sample import Sample


def test_create_sample_with_path():
    sample = Sample(path=Path("sample.exe"))

    assert sample.path == Path("sample.exe")
    assert sample.file_type == "UNKNOWN"
    assert sample.hashes == {}
    assert sample.findings == []


def test_sample_to_dict():
    sample = Sample(
        path=Path("sample.exe"),
        file_type="PE",
        hashes={"sha256": "abc123"},
    )

    result = sample.to_dict()

    assert result["path"] == "sample.exe"
    assert result["filename"] == "sample.exe"
    assert result["file_type"] == "PE"
    assert result["hashes"]["sha256"] == "abc123"


def test_sample_lists_are_not_shared():
    sample_a = Sample(path=Path("a.exe"))
    sample_b = Sample(path=Path("b.exe"))

    sample_a.findings.append({"title": "test finding"})

    assert len(sample_a.findings) == 1
    assert len(sample_b.findings) == 0