# BinaryTriage-X System Pipeline

BinaryTriage-X is organized as a staged binary triage pipeline.

Each stage receives structured input, performs one clear responsibility, and passes normalized output to the next stage.

## Pipeline Overview

```text
CLI
 │
 ▼
File Intake
 │
 ▼
File Type Detection
 │
 ▼
Hash Engine
 │
 ▼
Metadata Engine
 │
 ▼
Format Analysis
 ├── PE
 ├── ELF
 └── Mach-O
 │
 ▼
Static Analysis Core
 ├── Strings
 ├── Entropy
 ├── Sections
 ├── Imports
 └── Symbols
 │
 ▼
IOC Extraction
 │
 ▼
Detection Layer
 ├── Suspicious Indicators
 ├── Packer Detection
 ├── YARA Matching
 ├── Sigma Mapping
 └── Blackwell Signatures
 │
 ▼
Intelligence Layer
 ├── MITRE ATT&CK Mapping
 └── Threat Context
 │
 ▼
Scoring Layer
 ├── Threat Score
 ├── Confidence Score
 └── Triage Priority
 │
 ▼
Reporting Layer
 ├── JSON Report
 ├── HTML Dashboard
 ├── Analyst Summary
 └── Case Bundle