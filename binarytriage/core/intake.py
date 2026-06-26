from pathlib import Path


class FileIntakeError(Exception):
    """Raised when an input file fails validation."""
    pass


DEFAULT_MAX_FILE_SIZE = 100 * 1024 * 1024


def validate_input_file(file_path: str, max_size: int = DEFAULT_MAX_FILE_SIZE) -> Path:
    if not file_path:
        raise FileIntakeError("No input file path provided.")

    path = Path(file_path).expanduser()

    if not path.exists():
        raise FileIntakeError(f"Input path does not exist: {path}")

    if not path.is_file():
        raise FileIntakeError(f"Input path is not a regular file: {path}")

    if not os_access_readable(path):
        raise FileIntakeError(f"Input file is not readable: {path}")

    file_size = path.stat().st_size

    if file_size == 0:
        raise FileIntakeError(f"Input file is empty: {path}")

    if file_size > max_size:
        raise FileIntakeError(
            f"Input file is too large: {file_size} bytes. "
            f"Maximum allowed size is {max_size} bytes."
        )

    return path.resolve()


def os_access_readable(path: Path) -> bool:
    try:
        with path.open("rb"):
            return True
    except OSError:
        return False