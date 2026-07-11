import json
from pathlib import Path

from binarytriage.cli import (
    EXIT_ANALYSIS_ERROR,
    EXIT_SUCCESS,
    main,
)


def test_cli_prints_json_report(
    tmp_path: Path,
    capsys,
) -> None:
    test_file = tmp_path / "sample.exe"
    test_file.write_bytes(b"MZ\x90\x00test")

    exit_code = main([
        "analyze",
        str(test_file),
    ])

    captured = capsys.readouterr()
    parsed_output = json.loads(captured.out)

    assert exit_code == EXIT_SUCCESS
    assert parsed_output["file_type"] == "PE"


def test_cli_writes_json_report(
    tmp_path: Path,
    capsys,
) -> None:
    test_file = tmp_path / "sample.elf"
    test_file.write_bytes(b"\x7fELFtest")

    output_file = tmp_path / "reports" / "report.json"

    exit_code = main([
        "analyze",
        str(test_file),
        "--output",
        str(output_file),
    ])

    captured = capsys.readouterr()

    assert exit_code == EXIT_SUCCESS
    assert output_file.exists()
    assert "Report written to:" in captured.out


def test_cli_returns_error_for_missing_file(
    tmp_path: Path,
    capsys,
) -> None:
    missing_file = tmp_path / "missing.exe"

    exit_code = main([
        "analyze",
        str(missing_file),
    ])

    captured = capsys.readouterr()

    assert exit_code == EXIT_ANALYSIS_ERROR
    assert "error:" in captured.err