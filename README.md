# OCR Tool (OpenClaw Skill)

Proyecto Python para extraer texto de PDFs escaneados usando Tesseract OCR, pensado para instalarse en servidor y exponer un comando reutilizable por un agente OpenClaw.

## Estructura

- ocr.py: wrapper de compatibilidad
- ocr_tool/cli.py: CLI principal
- pyproject.toml: paquete instalable con comando `openclaw-ocr`
- requirements.txt: dependencias Python
- openclaw-skill/SKILL.md: definicion del skill para OpenClaw
- examples/: ejemplos de uso

## Requisitos del sistema

Ademas de dependencias Python, necesitas instalar:

- Tesseract OCR
- Poppler (para pdf2image)

### Windows

1. Instala Tesseract OCR (por ejemplo desde UB Mannheim o instalador oficial).
2. Instala Poppler para Windows y ubica la carpeta `bin`.
3. Si Tesseract no queda en PATH, configura su ruta en variables de entorno.

### Linux (Debian/Ubuntu)

```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-spa poppler-utils
```

## Instalacion Python (desarrollo local)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Instalacion en servidor (para OpenClaw)

Instala el proyecto como paquete en el entorno Python del agente:

```bash
pip install .
```

Esto expone el comando global:

```bash
openclaw-ocr --help
```

## Uso basico

```bash
openclaw-ocr input.pdf -o salida.txt -l spa
```

## Opciones utiles

```bash
openclaw-ocr input.pdf -o salida.txt -l spa+eng --dpi 300 --first-page 1 --last-page 5 --poppler-path "C:\\poppler\\Library\\bin"
```

Si Tesseract no esta en `PATH`:

```bash
openclaw-ocr input.pdf -o salida.txt -l spa --tesseract-cmd "/usr/bin/tesseract"
```

## Nota sobre idioma

- `-l spa` para espanol
- `-l eng` para ingles
- `-l spa+eng` para ambos
