# BinaryTriage-X Architecture

## Purpose

BinaryTriage-X is designed as a modular static binary triage platform.

The system follows a staged analysis pipeline where each module has one clearly defined responsibility.

Every stage receives structured input, performs one task, enriches the analysis object, and forwards it to the next stage.

This architecture prioritizes:

* Explainability
* Modularity
* Testability
* Reproducibility
* Maintainability

rather than monolithic analysis.

---

# Architectural Principles

BinaryTriage-X follows the following architectural principles.

## Single Responsibility

Every module performs exactly one logical task.

Examples:

* Intake validates input.
* FileType identifies executable format.
* Hash Engine calculates cryptographic hashes.
* Metadata Engine extracts identity information.
* IOC Extraction discovers indicators.
* Reporting generates analyst output.

No module should perform unrelated work.

---

## Pipeline Architecture

The entire system is implemented as a sequential analysis pipeline.

Each stage enriches the central Sample object.

No stage should duplicate work already completed by previous stages.

---

## Sample-Centric Design

The Sample object is the core entity of the platform.

Every module receives the same Sample instance.

Every module appends new evidence.

No module creates a separate analysis object.

---

## Explainable Analysis

BinaryTriage-X never produces unexplained scores.

Every score must be backed by findings.

Every finding must be backed by observable evidence.

---

## Security First

Unknown binaries are never trusted.

Input validation is mandatory.

Unsafe assumptions are avoided.

All analysis is deterministic and reproducible.

---

# System Layers

## Layer 1

Command Interface

Responsible for:

* User interaction
* Argument parsing
* Pipeline execution

---

## Layer 2

Input Validation

Responsible for:

* File existence
* Permissions
* File size
* Input normalization

Implemented by:

```text
core/intake.py
```

---

## Layer 3

File Identification

Responsible for:

* Magic bytes
* Executable format detection

Supported formats:

* PE
* ELF
* Mach-O

Implemented by:

```text
core/filetype.py
```

---

## Layer 4

Identity Generation

Responsible for:

* MD5
* SHA1
* SHA256

Implemented by:

```text
core/hashing.py
```

---

## Layer 5

Sample Model

Responsible for storing every analysis result generated throughout the pipeline.

Implemented by:

```text
models/sample.py
```

---

## Layer 6

Metadata Extraction

Responsible for:

* Filename
* Extension
* Size
* Creation time
* Modification time
* File type
* Hashes

---

## Layer 7

Format Analysis

Responsible for executable-specific parsing.

Modules:

* PE
* ELF
* Mach-O

---

## Layer 8

Static Analysis

Responsible for:

* Strings
* Entropy
* Sections
* Imports
* Exports
* Symbols

---

## Layer 9

Detection

Responsible for:

* Suspicious Indicators
* Packer Detection
* YARA Matching
* Sigma Mapping
* Blackwell Signatures

---

## Layer 10

Threat Intelligence

Responsible for:

* IOC Extraction
* MITRE ATT&CK Mapping
* Threat Context

---

## Layer 11

Threat Scoring

Responsible for:

* Threat Score
* Confidence Score
* Investigation Priority

---

## Layer 12

Reporting

Responsible for:

* JSON
* HTML Dashboard
* Analyst Summary
* Case Bundle

---

# Data Flow

```text
CLI

↓

Intake

↓

File Type Detection

↓

Hash Engine

↓

Sample Model

↓

Metadata

↓

Format Parser

↓

Static Analysis

↓

IOC Extraction

↓

Detection

↓

Threat Intelligence

↓

Threat Scoring

↓

Reporting
```

---

# Design Goals

BinaryTriage-X is designed to achieve the following goals.

* Fast binary triage.
* Reproducible analysis.
* Modular implementation.
* Explainable findings.
* Analyst-friendly output.
* Testable architecture.
* Easy future expansion.

---

# Long-Term Evolution

Future versions may include:

* Dynamic analysis
* Plugin framework
* REST API
* Distributed analysis
* Parallel processing
* Sandbox orchestration
* Threat intelligence connectors
* Digital signature validation
* Certificate analysis
* ML-assisted prioritization
* Multi-sample correlation

The core architecture is intentionally designed to support these future capabilities without requiring fundamental redesign.
