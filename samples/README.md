cat > samples/README.md <<'EOF'
# Local Samples Policy

This directory is reserved for local analysis workflows.

Live malware samples must never be committed to this repository.

## Permitted Local Content

- legally obtained analysis samples
- benign executable fixtures
- private research artifacts
- temporary files used during isolated analysis

## Prohibited Repository Content

- live malware
- weaponized binaries
- unauthorized samples
- stolen files
- credentials
- private customer data
- restricted or improperly licensed datasets

All unknown or malicious samples must be handled only inside controlled, isolated, and legally authorized environments.

The contents of this directory are ignored by Git except for this policy document.
EOF
