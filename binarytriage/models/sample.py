from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from binarytriage.models.metadata import FileMetadata


@dataclass
class Sample:
    """
    Central analysis object for BinaryTriage-X.

    A Sample represents one file being analyzed.
    Pipeline stages enrich this object with structured evidence.
    """

    path: Path
    file_type: str = "UNKNOWN"
    hashes: dict[str, str] = field(default_factory=dict)
    metadata: FileMetadata | None = None
    strings: list[str] = field(default_factory=list)
    entropy: dict[str, Any] = field(default_factory=dict)
    iocs: dict[str, list[str]] = field(default_factory=dict)
    findings: list[dict[str, Any]] = field(default_factory=list)
    mitre: list[dict[str, Any]] = field(default_factory=list)
    score: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the Sample object into a JSON-serializable dictionary.

        Returns:
            Dictionary representation of the complete analysis state.
        """
        return {
            "path": str(self.path),
            "file_name": self.path.name,
            "file_type": self.file_type,
            "hashes": self.hashes,
            "metadata": (
                self.metadata.to_dict()
                if self.metadata is not None
                else None
            ),
            "strings": self.strings,
            "entropy": self.entropy,
            "iocs": self.iocs,
            "findings": self.findings,
            "mitre": self.mitre,
            "score": self.score,
        }