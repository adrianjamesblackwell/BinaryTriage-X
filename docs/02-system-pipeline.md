# System Pipeline

## Purpose

This document describes the complete execution flow of BinaryTriage-X.

While the System Architecture document explains how the platform is organized, this document explains how a binary moves through the analysis pipeline from user input to the final report.

The pipeline is deterministic.

Every execution of the same binary under the same configuration should produce the same observable results.

---

# Pipeline Philosophy

BinaryTriage-X follows a staged processing model.

Each stage has exactly one responsibility.

Each stage receives structured input.

Each stage validates its own assumptions.

Each stage enriches the central Sample object.

Each stage forwards the Sample object to the next stage.

The pipeline is intentionally linear in Version 1 to maximize:

* Predictability
* Simplicity
* Debuggability
* Testability

Future versions may parallelize independent stages without changing the logical pipeline.

---

# Pipeline Overview

```text
User
 │
 ▼
CLI
 │
 ▼
Input Validation
 │
 ▼
File Type Detection
 │
 ▼
Hash Engine
 │
 ▼
Sample Creation
 │
 ▼
Metadata Engine
 │
 ▼
Executable Parser
 │
 ▼
Static Analysis
 │
 ▼
IOC Extraction
 │
 ▼
Detection Engine
 │
 ▼
Threat Intelligence
 │
 ▼
Threat Scoring
 │
 ▼
Reporting
 │
 ▼
JSON
HTML
Case Bundle
```

---

# Stage 1 — User Input

## Purpose

Receive the analysis request.

Example:

```bash
binarytriage analyze suspicious.exe
```

Input:

* File path
* Optional configuration
* CLI arguments

Output:

Validated analysis request.

---

# Stage 2 — Input Validation

Module

```text
binarytriage/core/intake.py
```

Responsibilities

* Verify file existence
* Verify permissions
* Verify file size
* Normalize path
* Reject invalid input

Input

Raw file path.

Output

Validated Path object.

Failure

Pipeline stops immediately.

---

# Stage 3 — File Type Detection

Module

```text
binarytriage/core/filetype.py
```

Responsibilities

* Read magic bytes
* Detect executable format
* Reject unsupported formats

Input

Validated file.

Output

PE

ELF

Mach-O

UNKNOWN

Failure

Pipeline continues only for supported formats.

---

# Stage 4 — Hash Engine

Module

```text
binarytriage/core/hashing.py
```

Responsibilities

* Generate MD5
* Generate SHA1
* Generate SHA256

Input

Validated executable.

Output

Cryptographic identity.

The hash values become part of the Sample object.

---

# Stage 5 — Sample Creation

Module

```text
binarytriage/models/sample.py
```

Purpose

Create the central analysis object.

Responsibilities

Store:

* File identity
* Metadata
* Findings
* Evidence
* Scores
* Reports

Every subsequent stage updates this object.

No stage creates an independent analysis result.

---

# Stage 6 — Metadata Engine

Module

```text
binarytriage/core/metadata.py
```

Responsibilities

Extract:

* Filename
* Extension
* File size
* Creation time
* Modification time
* Executable type
* Hashes

The Sample object now represents the binary's identity.

---

# Stage 7 — Executable Parsing

Modules

```text
formats/pe.py
formats/elf.py
formats/macho.py
```

Responsibilities

Interpret executable-specific structures.

Examples

PE

* DOS Header
* PE Header
* Optional Header
* Section Table
* Import Table
* Export Table

ELF

* ELF Header
* Program Headers
* Section Headers
* Dynamic Symbols

Mach-O

* Mach Header
* Load Commands
* Segments
* Sections

Output

Executable structure attached to the Sample object.

---

# Stage 8 — Static Analysis

Responsibilities

Collect observable characteristics.

Modules may include:

* Strings
* Entropy
* Imports
* Exports
* Sections
* Symbols

Output

Static evidence.

No conclusions are produced at this stage.

---

# Stage 9 — IOC Extraction

Purpose

Extract Indicators of Compromise.

Examples

URLs

Domains

IP addresses

Email addresses

Registry paths

Filesystem paths

Mutex names

Output

Structured IOC collection.

---

# Stage 10 — Detection

Responsibilities

Evaluate suspicious indicators.

Capabilities

* Suspicious APIs
* Packers
* YARA
* Sigma mapping
* Blackwell signatures

Output

Findings.

Every finding must include supporting evidence.

---

# Stage 11 — Threat Intelligence

Responsibilities

Provide operational context.

Examples

* MITRE ATT&CK techniques
* Threat context
* Indicator categorization

Output

Contextual information.

The pipeline still does not classify malware.

---

# Stage 12 — Threat Scoring

Purpose

Help analysts prioritize work.

Inputs

* Findings
* IOC count
* Detection results
* Metadata
* Static evidence

Outputs

* Threat Score
* Confidence Score
* Investigation Priority

Important

Scores are recommendations.

They are not verdicts.

---

# Stage 13 — Reporting

Responsibilities

Generate analyst-friendly output.

Formats

JSON

HTML Dashboard

Case Bundle

Analyst Summary

Reports must be:

* Structured
* Reproducible
* Explainable
* Machine-readable
* Human-readable

---

# Sample Evolution

During execution the Sample object grows continuously.

```text
Stage 1

Sample

↓

Stage 2

Sample + File Type

↓

Stage 3

Sample + Hashes

↓

Stage 4

Sample + Metadata

↓

Stage 5

Sample + Executable Structure

↓

Stage 6

Sample + Static Evidence

↓

Stage 7

Sample + IOC

↓

Stage 8

Sample + Findings

↓

Stage 9

Sample + Threat Context

↓

Stage 10

Sample + Scores

↓

Stage 11

Sample + Reports
```

The Sample object is never replaced.

It is enriched throughout the pipeline.

---

# Error Handling Strategy

BinaryTriage-X uses stage-local error handling.

Each module raises domain-specific exceptions.

Examples

* FileIntakeError
* FileTypeError
* HashingError

Errors stop the pipeline only when the current stage cannot produce valid output.

Future versions may support partial analysis recovery where appropriate.

---

# Pipeline Design Rules

The following rules apply to every stage.

1. One responsibility per stage.
2. Never modify previous evidence.
3. Never discard evidence silently.
4. Every output must be deterministic.
5. Every finding must be explainable.
6. Every module must be independently testable.
7. Every stage must have dedicated unit tests.
8. Every stage updates the Sample object instead of creating new analysis containers.

--- 

# Pipeline Summary

BinaryTriage-X is designed as a deterministic evidence-generation pipeline.

The platform does not attempt to replace analyst expertise.

Instead, it reduces the time required to understand an unknown executable by collecting evidence, organizing information, and producing explainable outputs that support technical decision-making.
