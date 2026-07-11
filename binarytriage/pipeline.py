from pathlib import Path

from binarytriage.core.filetype import detect_file_type
from binarytriage.core.hashing import calculate_file_hashes
from binarytriage.core.intake import validate_input_file
from binarytriage.core.metadata import extract_file_metadata
from binarytriage.models.sample import Sample


class PipelineError(Exception):
    """Raised when the analysis pipeline cannot complete."""


def analyze_file(file_path: str) -> Sample:
    """
    Run the foundational BinaryTriage-X analysis pipeline.

    Args:
        file_path: User-supplied path to the file being analyzed.

    Returns:
        A Sample object enriched with file type, hashes, and metadata.

    Raises:
        FileIntakeError: If the input file is invalid.
        FileTypeError: If file type detection fails.
        HashingError: If hashes cannot be calculated.
        MetadataError: If filesystem metadata cannot be extracted.
    """
    validated_path = validate_input_file(file_path)

    detected_file_type = detect_file_type(str(validated_path))

    hashes = calculate_file_hashes(str(validated_path))

    metadata = extract_file_metadata(
        file_path=validated_path,
        detected_file_type=detected_file_type,
    )

    return Sample(
        path=validated_path,
        file_type=detected_file_type,
        hashes=hashes,
        metadata=metadata,
    )