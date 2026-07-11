import argparse
import sys
from pathlib import Path
from typing import Sequence

from binarytriage.core.filetype import FileTypeError
from binarytriage.core.hashing import HashingError
from binarytriage.core.intake import FileIntakeError
from binarytriage.core.metadata import MetadataError
from binarytriage.pipeline import analyze_file
from binarytriage.reporting.json_report import (
    JsonReportError,
    generate_json_report,
    write_json_report,
)


EXIT_SUCCESS = 0
EXIT_ANALYSIS_ERROR = 1
EXIT_USAGE_ERROR = 2


def build_parser() -> argparse.ArgumentParser:
    """
    Build the BinaryTriage-X command-line argument parser.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="binarytriage",
        description=(
            "Static binary triage for PE, ELF, and Mach-O files."
        ),
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    analyze_parser = subparsers.add_parser(
        "analyze",
        help="Analyze one file.",
    )

    analyze_parser.add_argument(
        "file",
        help="Path to the file that should be analyzed.",
    )

    analyze_parser.add_argument(
        "--output",
        type=Path,
        help="Write the JSON report to this path.",
    )

    analyze_parser.add_argument(
        "--compact",
        action="store_true",
        help="Generate compact JSON without indentation.",
    )

    return parser


def run_analyze_command(args: argparse.Namespace) -> int:
    """
    Execute the analyze command.

    Args:
        args: Parsed command-line arguments.

    Returns:
        Process exit code.
    """
    sample = analyze_file(args.file)

    if args.output is not None:
        report_path = write_json_report(
            sample,
            args.output,
            pretty=not args.compact,
        )

        print(f"Report written to: {report_path}")
        return EXIT_SUCCESS

    report = generate_json_report(
        sample,
        pretty=not args.compact,
    )

    print(report)
    return EXIT_SUCCESS


def main(argv: Sequence[str] | None = None) -> int:
    """
    Run the BinaryTriage-X command-line interface.

    Args:
        argv: Optional argument sequence used primarily by tests.

    Returns:
        Process exit code.
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "analyze":
            return run_analyze_command(args)

        parser.error(f"Unsupported command: {args.command}")
        return EXIT_USAGE_ERROR

    except (
        FileIntakeError,
        FileTypeError,
        HashingError,
        MetadataError,
        JsonReportError,
    ) as error:
        print(
            f"error: {error}",
            file=sys.stderr,
        )

        return EXIT_ANALYSIS_ERROR


if __name__ == "__main__":
    raise SystemExit(main())