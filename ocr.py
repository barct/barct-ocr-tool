#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compat wrapper para ejecutar la CLI empaquetada."""

from ocr_tool.cli import main


if __name__ == "__main__":
    raise SystemExit(main())
