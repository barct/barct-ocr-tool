#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI para extraer texto de un PDF escaneado usando OCR (Tesseract)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extrae texto de un PDF escaneado usando OCR (Tesseract)."
    )
    parser.add_argument("input_pdf", type=Path, help="Ruta al PDF de entrada")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("texto_extraido.txt"),
        help="Archivo de salida para el texto extraido",
    )
    parser.add_argument(
        "-l",
        "--lang",
        default="spa",
        help="Idioma OCR de Tesseract (ej: spa, eng, spa+eng)",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="Resolucion en DPI para renderizar el PDF a imagenes",
    )
    parser.add_argument(
        "--first-page",
        type=int,
        default=None,
        help="Primera pagina a procesar (1-indexado)",
    )
    parser.add_argument(
        "--last-page",
        type=int,
        default=None,
        help="Ultima pagina a procesar (1-indexado)",
    )
    parser.add_argument(
        "--poppler-path",
        type=Path,
        default=None,
        help="Ruta a la carpeta bin de Poppler (util en Windows)",
    )
    parser.add_argument(
        "--preview-chars",
        type=int,
        default=500,
        help="Cantidad de caracteres a mostrar por consola como vista previa",
    )
    parser.add_argument(
        "--tesseract-cmd",
        type=Path,
        default=None,
        help="Ruta al ejecutable tesseract si no esta en PATH",
    )
    return parser.parse_args()


def run_ocr(args: argparse.Namespace) -> str:
    if not args.input_pdf.exists():
        raise FileNotFoundError(f"No existe el PDF de entrada: {args.input_pdf}")

    if args.tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = str(args.tesseract_cmd)

    poppler_path = str(args.poppler_path) if args.poppler_path else None

    images = convert_from_path(
        str(args.input_pdf),
        dpi=args.dpi,
        first_page=args.first_page,
        last_page=args.last_page,
        poppler_path=poppler_path,
    )

    if not images:
        raise RuntimeError("No se pudieron obtener imagenes desde el PDF")

    extracted = []
    total = len(images)
    for idx, image in enumerate(images, start=1):
        print(f"Procesando pagina {idx}/{total}...")
        extracted.append(pytesseract.image_to_string(image, lang=args.lang))

    return "\n\n".join(extracted)


def main() -> int:
    args = parse_args()

    try:
        text = run_ocr(args)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")

        print(f"OCR completado. Archivo generado: {args.output}")
        if args.preview_chars > 0:
            print("\n--- Vista previa ---")
            print(text[: args.preview_chars])
        return 0
    except Exception as exc:  # pragma: no cover
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
