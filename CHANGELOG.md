# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2026-03-11

### Added
- Python package structure for an installable OpenClaw OCR skill.
- CLI command: openclaw-ocr.
- OCR pipeline for scanned PDFs using pdf2image + pytesseract.
- CLI options for language, DPI, page range, poppler path, and tesseract executable path.
- OpenClaw skill definition at openclaw-skill/SKILL.md.
- Usage examples at examples/uso.txt.
- GitHub Actions CI workflow to validate package install and CLI help.
- Python-oriented .gitignore.

### Notes
- Spanish OCR support uses Tesseract language data spa, which must be installed at OS level.
- Python dependencies are managed via pyproject.toml and requirements.txt.
