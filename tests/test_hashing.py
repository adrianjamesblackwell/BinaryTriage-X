import hashlib

from binarytriage.core.hashing import calculate_file_hashes


def test_calculate_file_hashes(tmp_path):
    test_file = tmp_path / "sample.bin"
    test_data = b"BinaryTriage-X test data"
    test_file.write_bytes(test_data)

    result = calculate_file_hashes(str(test_file))

    assert result["md5"] == hashlib.md5(test_data).hexdigest()
    assert result["sha1"] == hashlib.sha1(test_data).hexdigest()
    assert result["sha256"] == hashlib.sha256(test_data).hexdigest()


def test_calculate_file_hashes_with_small_chunks(tmp_path):
    test_file = tmp_path / "sample.bin"
    test_data = b"ABCDEFGHIJK"
    test_file.write_bytes(test_data)

    result = calculate_file_hashes(str(test_file), chunk_size=3)

    assert result["sha256"] == hashlib.sha256(test_data).hexdigest()