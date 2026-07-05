# Module Index

## Purpose

This document provides a centralized index of every module in BinaryTriage-X.

It serves as the primary navigation document for developers, reviewers, and future contributors.

Each module is documented using a standardized format describing:

* Responsibility
* Position within the analysis pipeline
* Inputs
* Outputs
* Dependencies
* Consumers
* Current implementation status

The goal is to allow engineers to understand the purpose of every module before reading its implementation.

---

# Module Classification

BinaryTriage-X is organized into the following logical categories.

| Category     | Purpose                         |
| ------------ | ------------------------------- |
| CLI          | User interaction                |
| Core         | Fundamental pipeline operations |
| Models       | Shared analysis objects         |
| Formats      | Executable format parsing       |
| Detection    | Suspicious indicator analysis   |
| Intelligence | Threat intelligence enrichment  |
| Scoring      | Risk evaluation                 |
| Reporting    | Report generation               |
| Integrations | External services               |

---

# Module Documentation Template

Every module should follow the documentation structure below.

---

## Module Name

Module Path

Mission

Pipeline Position

Primary Responsibility

Inputs

Outputs

Dependencies

Consumers

Exceptions

Current Status

Future Extensions

---

# CLI

---

## Module

binarytriage/cli.py

Mission

Provide the primary command-line interface for BinaryTriage-X.

Pipeline Position

Entry Point

Responsibilities

* Parse CLI arguments
* Validate commands
* Initialize analysis pipeline
* Handle execution flow
* Display user feedback

Input

* Command-line arguments
* File path
* Configuration options

Output

Pipeline execution request.

Dependencies

* core/
* reporting/

Consumers

End users.

Status

Planned

---

# Core Modules

---

## Module

binarytriage/core/intake.py

Mission

Validate that a file is safe to analyze.

Pipeline Position

Stage 1

Responsibilities

* Validate file existence
* Validate permissions
* Validate size
* Normalize path
* Reject invalid input

Input

User-supplied file path.

Output

Validated Path object.

Dependencies

pathlib

Consumers

All subsequent pipeline stages.

Status

Implemented

---

## Module

binarytriage/core/filetype.py

Mission

Determine the actual executable format using magic bytes.

Pipeline Position

Stage 2

Responsibilities

* Read magic bytes
* Detect executable format
* Reject unsupported formats

Input

Validated file path.

Output

PE

ELF

Mach-O

UNKNOWN

Dependencies

pathlib

Consumers

Metadata Engine

Executable Parsers

Status

Implemented

---

## Module

binarytriage/core/hashing.py

Mission

Generate cryptographic identities.

Pipeline Position

Stage 3

Responsibilities

* Calculate MD5
* Calculate SHA1
* Calculate SHA256

Input

Validated executable.

Output

Hash collection.

Dependencies

hashlib

Consumers

Metadata

Reporting

Threat Intelligence

VirusTotal Integration

Status

Implemented

---

## Module

binarytriage/core/metadata.py

Mission

Build the identity profile of the analyzed sample.

Pipeline Position

Stage 4

Responsibilities

* Extract filename
* Extract extension
* Extract file size
* Extract timestamps
* Store executable type
* Store hashes

Input

Validated Sample.

Output

Updated Sample object.

Status

Planned

---

# Models

---

## Module

binarytriage/models/sample.py

Mission

Represent the central analysis object used throughout the platform.

Pipeline Position

Shared Object

Responsibilities

* Store metadata
* Store hashes
* Store findings
* Store scores
* Store IOC collection
* Store reporting information

Input

Pipeline results.

Output

Unified analysis object.

Status

Implemented

---

# Format Parsers

---

## Module

binarytriage/formats/pe.py

Mission

Parse Portable Executable files.

Status

Planned

---

## Module

binarytriage/formats/elf.py

Mission

Parse ELF executables.

Status

Planned

---

## Module

binarytriage/formats/macho.py

Mission

Parse Mach-O executables.

Status

Planned

---

# Detection Modules

---

## Module

binarytriage/detection/indicators.py

Mission

Evaluate suspicious static characteristics.

Status

Planned

---

## Module

binarytriage/detection/packers.py

Mission

Identify packed executables.

Status

Planned

---

## Module

binarytriage/detection/yara_matcher.py

Mission

Execute YARA rules against extracted evidence.

Status

Planned

---

## Module

binarytriage/detection/sigma_mapper.py

Mission

Map analysis findings to Sigma detection logic.

Status

Planned

---

## Module

binarytriage/detection/blackwell_signatures.py

Mission

Apply project-specific heuristic signatures.

Status

Planned

---

# Intelligence Modules

---

## Module

binarytriage/intel/ioc_extractor.py

Mission

Extract Indicators of Compromise.

Status

Planned

---

## Module

binarytriage/intel/mitre_mapper.py

Mission

Map findings to MITRE ATT&CK techniques.

Status

Planned

---

## Module

binarytriage/intel/threat_context.py

Mission

Provide operational context for findings.

Status

Planned

---

# Scoring Modules

---

## Module

binarytriage/scoring/engine.py

Mission

Calculate investigation priority.

Status

Planned

---

## Module

binarytriage/scoring/weights.py

Mission

Store configurable scoring weights.

Status

Planned

---

## Module

binarytriage/scoring/confidence.py

Mission

Calculate confidence levels for findings.

Status

Planned

---

# Reporting Modules

---

## Module

binarytriage/reporting/json_report.py

Mission

Generate structured JSON reports.

Status

Planned

---

## Module

binarytriage/reporting/html_report.py

Mission

Generate analyst-friendly HTML reports.

Status

Planned

---

## Module

binarytriage/reporting/summary.py

Mission

Generate concise investigation summaries.

Status

Planned

---

## Module

binarytriage/reporting/case_bundle.py

Mission

Package all analysis artifacts into a portable investigation bundle.

Status

Planned

---

# Integration Modules

---

## Module

binarytriage/integrations/virustotal.py

Mission

Query external hash intelligence sources.

Status

Planned

---

## Module

binarytriage/integrations/sandbox.py

Mission

Prepare optional sandbox integration for future workflow enrichment.

Status

Planned

---

# Module Development Rules

Every new module added to BinaryTriage-X must:

1. Have a clearly defined mission.
2. Perform exactly one primary responsibility.
3. Define its inputs and outputs.
4. Document its dependencies.
5. Include unit tests.
6. Update the System Pipeline document if its position changes.
7. Update this Module Index.
8. Follow the project's coding standards.

---

# Summary

The Module Index acts as the navigation map of BinaryTriage-X.

It ensures that every component has a documented purpose, a defined place in the architecture, and a consistent interface with the rest of the platform.

As the project evolves, this document should remain synchronized with the implementation to preserve architectural clarity.
