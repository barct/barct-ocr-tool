# OpenClaw Skill: OCR PDF

## Purpose

Extraer texto de PDFs escaneados mediante OCR usando el comando `openclaw-ocr`.

## Command

```bash
openclaw-ocr <input_pdf> -o <output_txt> -l spa
```

## Typical usage

```bash
openclaw-ocr /data/invoice.pdf -o /data/invoice.txt -l spa+eng --dpi 300
```

## Parameters

- `input_pdf`: ruta al PDF de entrada.
- `-o, --output`: archivo de salida (por defecto: `texto_extraido.txt`).
- `-l, --lang`: idioma(s) de OCR (`spa`, `eng`, `spa+eng`, etc).
- `--dpi`: resolucion de renderizado del PDF.
- `--first-page`: pagina inicial a procesar.
- `--last-page`: pagina final a procesar.
- `--poppler-path`: ruta a binarios de Poppler (Windows).
- `--tesseract-cmd`: ruta a ejecutable de Tesseract si no esta en `PATH`.
- `--preview-chars`: caracteres de vista previa impresos en stdout.

## Server install

1. Instalar dependencias de sistema en el servidor:
   - Tesseract OCR (+ idioma espanol)
   - Poppler
2. Instalar este skill en entorno Python del agente:

```bash
pip install /path/to/ocr-tool
```

3. Verificar comando:

```bash
openclaw-ocr --help
```
