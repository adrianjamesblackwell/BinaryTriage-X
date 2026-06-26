import pytest

from binarytriage.core.intake import FileIntakeError, validate_input_file


def test_validate_existing_file(tmp_path):
    test_file = tmp_path / "sample.bin"
    test_file.write_bytes(b"hello")

    result = validate_input_file(str(test_file))

    assert result.exists()
    assert result.is_file()


def test_reject_missing_file():
    with pytest.raises(FileIntakeError):
        validate_input_file("missing-file.bin")


def test_reject_empty_file(tmp_path):
    test_file = tmp_path / "empty.bin"
    test_file.write_bytes(b"")

    with pytest.raises(FileIntakeError):
        validate_input_file(str(test_file))


def test_reject_directory(tmp_path):
    with pytest.raises(FileIntakeError):
        validate_input_file(str(tmp_path))


def test_reject_large_file(tmp_path):
    test_file = tmp_path / "large.bin"
    test_file.write_bytes(b"A" * 11)

    with pytest.raises(FileIntakeError):
        validate_input_file(str(test_file), max_size=10)