from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class FileMetadata:
    """
    Structured filesystem metadata for one analyzed sample.

    The model contains descriptive file information collected before
    executable-specific parsing begins.
    """

    file_name: str
    file_stem: str
    extension: str
    suffixes: tuple[str, ...]
    absolute_path: str
    size_bytes: int
    modified_time_utc: str
    accessed_time_utc: str
    filesystem_change_time_utc: str
    birth_time_utc: str | None
    detected_file_type: str

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the metadata model into a JSON-serializable dictionary.

        Returns:
            Dictionary containing all metadata fields.
        """
        return {
            "file_name": self.file_name,
            "file_stem": self.file_stem,
            "extension": self.extension,
            "suffixes": list(self.suffixes),
            "absolute_path": self.absolute_path,
            "size_bytes": self.size_bytes,
            "modified_time_utc": self.modified_time_utc,
            "accessed_time_utc": self.accessed_time_utc,
            "filesystem_change_time_utc": self.filesystem_change_time_utc,
            "birth_time_utc": self.birth_time_utc,
            "detected_file_type": self.detected_file_type,
        }