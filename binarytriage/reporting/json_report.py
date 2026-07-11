import json
from pathlib import Path

from binarytriage.models.sample import Sample


class JsonReportError(Exception):
    """Raised when a JSON report cannot be generated or written."""


def generate_json_report(
    sample: Sample,
    *,
    pretty: bool = True,
) -> str:
    """
    Serialize a Sample object into JSON.

    Args:
        sample: Completed or partially enriched analysis object.
        pretty: Whether to format the output with indentation.

    Returns:
        JSON string containing the sample analysis.

    Raises:
        JsonReportError: If serialization fails.
    """
    try:
        indentation = 2 if pretty else None

        return json.dumps(
            sample.to_dict(),
            indent=indentation,
            sort_keys=True,
            ensure_ascii=False,
        )
    except (TypeError, ValueError) as error:
        raise JsonReportError(
            "Could not serialize sample analysis to JSON."
        ) from error


def write_json_report(
    sample: Sample,
    output_path: Path,
    *,
    pretty: bool = True,
) -> Path:
    """
    Write a Sample analysis report to a JSON file.

    Args:
        sample: Completed or partially enriched analysis object.
        output_path: Destination path for the report.
        pretty: Whether to format the output with indentation.

    Returns:
        Resolved path to the generated report.

    Raises:
        JsonReportError: If the report cannot be written.
    """
    json_content = generate_json_report(
        sample,
        pretty=pretty,
    )

    try:
        resolved_output = output_path.expanduser().resolve()

        resolved_output.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        resolved_output.write_text(
            json_content,
            encoding="utf-8",
        )

        return resolved_output

    except OSError as error:
        raise JsonReportError(
            f"Could not write JSON report: {output_path}"
        ) from error