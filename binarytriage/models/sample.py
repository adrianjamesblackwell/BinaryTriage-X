from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Sample:
    """
    Central analysis object for BinaryTriage-X.

    A Sample represents one file being analyzed.
    All pipeline stages enrich this object with additional evidence.
    """

    path: Path
    file_type: str = "UNKNOWN"
    hashes: dict[str, str] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    strings: list[str] = field(default_factory=list)
    entropy: dict[str, Any] = field(default_factory=dict)
    iocs: dict[str, list[str]] = field(default_factory=dict)
    findings: list[dict[str, Any]] = field(default_factory=list)
    mitre: list[dict[str, Any]] = field(default_factory=list)
    score: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the Sample object into a serializable dictionary.

        Returns:
            Dictionary representation of the sample.
        """
        return {
            "path": str(self.path),
            "filename": self.path.name,
            "file_type": self.file_type,
            "hashes": self.hashes,
            "metadata": self.metadata,
            "strings": self.strings,
            "entropy": self.entropy,
            "iocs": self.iocs,
            "findings": self.findings,
            "mitre": self.mitre,
            "score": self.score,
        }