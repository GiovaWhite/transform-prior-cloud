"""I percorsi e il nome dei file, e basta: la versione per il cloud di tp/comune.py."""
import hashlib
import re
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
CORPUS = RADICE / "corpus"
LETTI = CORPUS / "letti"


def doi_normale(doi):
    if not doi:
        return None
    d = doi.strip().lower()
    d = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", d)
    return d or None


def nome_file(doi):
    d = doi_normale(doi)
    prefisso, _, resto = d.partition("/")
    corto = re.sub(r"[^a-z0-9._-]+", "_", resto)[:120].strip("._") or "x"
    return f"{prefisso}/{corto}_{hashlib.sha1(d.encode()).hexdigest()[:8]}"
