import hashlib
from pathlib import Path


class HashingError(Exception):
    """Raised when hashing a file fails."""
    pass


DEFAULT_CHUNK_SIZE = 1024 * 1024


def calculate_file_hashes(file_path: str, chunk_size: int = DEFAULT_CHUNK_SIZE) -> dict[str, str]:
    """
    Calculate MD5, SHA1, and SHA256 hashes for a file.

    Args:
        file_path: Path to the file.
        chunk_size: Number of bytes to read per iteration.

    Returns:
        A dictionary containing md5, sha1, and sha256 hex digests.

    Raises:
        HashingError: If the file cannot be read or hashed.
    """
    path = Path(file_path)

    md5_hasher = hashlib.md5()
    sha1_hasher = hashlib.sha1()
    sha256_hasher = hashlib.sha256()

    try:
        with path.open("rb") as file:
            while True:
                chunk = file.read(chunk_size)

                if not chunk:
                    break

                md5_hasher.update(chunk)
                sha1_hasher.update(chunk)
                sha256_hasher.update(chunk)

    except OSError as error:
        raise HashingError(f"Could not calculate hashes for file: {error}") from error

    return {
        "md5": md5_hasher.hexdigest(),
        "sha1": sha1_hasher.hexdigest(),
        "sha256": sha256_hasher.hexdigest(),
    }