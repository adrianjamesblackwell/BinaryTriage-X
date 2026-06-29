from pathlib import Path


class FileTypeError(Exception):
    """Raised when file type detection fails."""
    pass


PE_MAGIC = b"MZ"
ELF_MAGIC = b"\x7fELF"

MACHO_MAGICS = {
    b"\xfe\xed\xfa\xce",
    b"\xfe\xed\xfa\xcf",
    b"\xce\xfa\xed\xfe",
    b"\xcf\xfa\xed\xfe",
    b"\xca\xfe\xba\xbe",
    b"\xca\xfe\xba\xbf",
}


def read_magic_bytes(file_path: str, length: int = 4) -> bytes:
    """
    Read the first bytes of a file.

    Args:
        file_path: Path to the file.
        length: Number of bytes to read.

    Returns:
        The first length bytes from the file.

    Raises:
        FileTypeError: If the file cannot be read.
    """
    try:
        path = Path(file_path)
        with path.open("rb") as file:
            return file.read(length)
    except OSError as error:
        raise FileTypeError(f"Could not read file magic bytes: {error}") from error


def detect_file_type(file_path: str) -> str:
    """
    Detect executable file type using magic bytes.

    Args:
        file_path: Path to the file.

    Returns:
        One of: "PE", "ELF", "MACHO", "UNKNOWN".
    """
    magic = read_magic_bytes(file_path, length=4)

    if magic.startswith(PE_MAGIC):
        return "PE"

    if magic.startswith(ELF_MAGIC):
        return "ELF"

    if magic in MACHO_MAGICS:
        return "MACHO"

    return "UNKNOWN"