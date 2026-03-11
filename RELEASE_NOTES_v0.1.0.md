# Release v0.1.0

Initial public release of the OpenClaw OCR skill.

## Highlights
- Installable Python package with command-line entrypoint: openclaw-ocr.
- Extract text from scanned PDFs using Tesseract OCR.
- Default language configured for Spanish OCR (spa) with optional multi-language usage (spa+eng).
- Server-friendly options for custom tesseract and poppler paths.
- Included OpenClaw skill definition and practical usage examples.
- CI workflow for basic validation on push and pull requests.

## Core command
openclaw-ocr input.pdf -o output.txt -l spa

## System requirements
- Tesseract OCR installed on the host.
- Poppler installed on the host.
- Tesseract language data for Spanish (spa) installed on the host.
