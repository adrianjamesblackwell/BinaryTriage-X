from binarytriage.core.filetype import detect_file_type, read_magic_bytes


def test_detect_pe_file(tmp_path):
    test_file = tmp_path / "sample.exe"
    test_file.write_bytes(b"MZ\x90\x00fake-pe-data")

    assert detect_file_type(str(test_file)) == "PE"


def test_detect_elf_file(tmp_path):
    test_file = tmp_path / "sample.elf"
    test_file.write_bytes(b"\x7fELFfake-elf-data")

    assert detect_file_type(str(test_file)) == "ELF"


def test_detect_macho_file(tmp_path):
    test_file = tmp_path / "sample_macho"
    test_file.write_bytes(b"\xcf\xfa\xed\xfefake-macho-data")

    assert detect_file_type(str(test_file)) == "MACHO"


def test_detect_unknown_file(tmp_path):
    test_file = tmp_path / "sample.txt"
    test_file.write_bytes(b"hello world")

    assert detect_file_type(str(test_file)) == "UNKNOWN"


def test_read_magic_bytes(tmp_path):
    test_file = tmp_path / "sample.bin"
    test_file.write_bytes(b"ABCDEFG")

    assert read_magic_bytes(str(test_file), length=4) == b"ABCD"