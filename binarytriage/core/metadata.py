import os
from datetime import datetime, timezone
from pathlib import Path

from binarytriage.models.metadata import FileMetadata


class MetadataError(Exception):
    """Raised when file metadata cannot be extracted."""


def _timestamp_to_utc_iso(timestamp: float) -> str:
    """
    Convert a filesystem timestamp into an ISO 8601 UTC string.

    Args:
        timestamp: POSIX timestamp expressed as seconds since the epoch.

    Returns:
        UTC timestamp formatted as an ISO 8601 string.
    """
    utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    return utc_time.isoformat().replace("+00:00", "Z")


def _get_birth_time_utc(stat_result: os.stat_result) -> str | None:
    """
    Return the filesystem birth time when supported by the platform.

    Args:
        stat_result: Filesystem stat result for the analyzed file.

    Returns:
        ISO 8601 UTC birth timestamp, or None when unavailable.
    """
    birth_timestamp = getattr(stat_result, "st_birthtime", None)

    if birth_timestamp is not None:
        return _timestamp_to_utc_iso(birth_timestamp)

    if os.name == "nt":
        return _timestamp_to_utc_iso(stat_result.st_ctime)

    return None


def extract_file_metadata(
    file_path: Path,
    detected_file_type: str,
) -> FileMetadata:
    """
    Extract structured filesystem metadata for one analyzed file.

    Args:
        file_path: Validated path to the file.
        detected_file_type: Format identified through magic bytes.

    Returns:
        Immutable FileMetadata object.

    Raises:
        MetadataError: If metadata extraction fails.
    """
    try:
        resolved_path = file_path.expanduser().resolve(strict=True)

        if not resolved_path.is_file():
            raise MetadataError(
                f"Metadata target is not a regular file: {resolved_path}"
            )

        stat_result = resolved_path.stat()

    except MetadataError:
        raise
    except OSError as error:
        raise MetadataError(
            f"Could not extract metadata from file: {file_path}"
        ) from error

    normalized_suffixes = tuple(
        suffix.lower() for suffix in resolved_path.suffixes
    )

    return FileMetadata(
        file_name=resolved_path.name,
        file_stem=resolved_path.stem,
        extension=resolved_path.suffix.lower(),
        suffixes=normalized_suffixes,
        absolute_path=str(resolved_path),
        size_bytes=stat_result.st_size,
        modified_time_utc=_timestamp_to_utc_iso(stat_result.st_mtime),
        accessed_time_utc=_timestamp_to_utc_iso(stat_result.st_atime),
        filesystem_change_time_utc=_timestamp_to_utc_iso(stat_result.st_ctime),
        birth_time_utc=_get_birth_time_utc(stat_result),
        detected_file_type=detected_file_type,
    )