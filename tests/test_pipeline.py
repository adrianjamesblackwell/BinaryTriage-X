from pathlib import Path

from binarytriage.pipeline import analyze_file


def test_analyze_file_builds_sample(tmp_path: Path) -> None:
    test_file = tmp_path / "sample.exe"
    test_data = b"MZ\x90\x00BinaryTriage-X"
    test_file.write_bytes(test_data)

    sample = analyze_file(str(test_file))

    assert sample.path == test_file.resolve()
    assert sample.file_type == "PE"
    assert sample.hashes["sha256"]
    assert len(sample.hashes["sha256"]) == 64
    assert sample.metadata is not None
    assert sample.metadata.file_name == "sample.exe"
    assert sample.metadata.size_bytes == len(test_data)


def test_analyze_unknown_file_type(tmp_path: Path) -> None:
    test_file = tmp_path / "sample.txt"
    test_file.write_bytes(b"ordinary text")

    sample = analyze_file(str(test_file))

    assert sample.file_type == "UNKNOWN"
    assert sample.metadata is not None
    assert sample.metadata.detected_file_type == "UNKNOWN"