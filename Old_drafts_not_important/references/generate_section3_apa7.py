import json
import subprocess
from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass(frozen=True)
class Work:
    doi: str


def _curl_json(url: str) -> dict:
    result = subprocess.run(
        ["curl", "-sL", url],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return json.loads(result.stdout)


def _authors_apa7(authors: list) -> str:
    def one(author: dict) -> str:
        family = " ".join((author.get("family") or "").split())
        given = " ".join((author.get("given") or "").split())
        initials = "".join([part.strip()[0] + "." for part in given.replace("-", " ").split() if part.strip()])
        if not family:
            return initials.strip() or ""
        if not initials:
            return family
        return f"{family}, {initials}"

    formatted = [one(a) for a in authors if a]
    formatted = [a for a in formatted if a]

    if not formatted:
        return ""

    # APA7: list up to 20 authors; if 21+, list first 19, …, last
    if len(formatted) <= 20:
        if len(formatted) == 1:
            return formatted[0]
        return ", ".join(formatted[:-1]) + ", & " + formatted[-1]

    first_19 = formatted[:19]
    last = formatted[-1]
    return ", ".join(first_19) + ", …, " + last


def _year(message: dict) -> Optional[int]:
    for key in ("published-print", "issued", "published-online"):
        parts = (message.get(key, {}).get("date-parts") or [])
        if parts and parts[0] and parts[0][0]:
            return int(parts[0][0])
    return None


def _title_sentence_case(title: str) -> str:
    # Crossref titles are usually already sentence/title case; keep as-is but strip trailing periods.
    return title.strip().rstrip(".")


def apa7_from_doi(doi: str) -> str:
    data = _curl_json(f"https://api.crossref.org/works/{doi}")
    message = data.get("message", {})

    authors = _authors_apa7(message.get("author") or [])
    year = _year(message)
    title = _title_sentence_case(" ".join(((message.get("title") or [""])[0]).split()))

    container = " ".join(((message.get("container-title") or [""])[0]).split())
    volume = (message.get("volume") or "").strip()
    issue = (message.get("issue") or "").strip()
    page = (message.get("page") or "").strip()
    article_number = (message.get("article-number") or "").strip()

    doi_url = f"https://doi.org/{doi}"

    year_str = str(year) if year else "n.d."

    # Journal/booktitle formatting (minimal Markdown, APA-like)
    parts: List[str] = []

    if authors:
        parts.append(f"{authors} ({year_str}). {title}.")
    else:
        parts.append(f"{title}. ({year_str}).")

    if container:
        vol_issue = ""
        if volume:
            vol_issue += volume
        if issue:
            vol_issue += f"({issue})" if volume else f"({issue})"

        locator = ""
        if page:
            locator = page
        elif article_number:
            locator = article_number

        if vol_issue and locator:
            parts.append(f"{container}, {vol_issue}, {locator}.")
        elif vol_issue:
            parts.append(f"{container}, {vol_issue}.")
        else:
            parts.append(f"{container}.")

    parts.append(doi_url)

    return " ".join([p for p in parts if p])


def main() -> None:
    # Keep list for Section 3 (20–30 range target)
    dois: Iterable[str] = [
        "10.1186/s13321-015-0109-z",  # ChemDes
        "10.1093/nar/gkv951",  # PubChem
        "10.1093/nar/gky1075",  # ChEMBL
        "10.1021/acs.jcim.0c00675",  # ZINC20
        "10.1093/bib/bbae294",  # Image-based survey
        "10.1002/wcms.1603",  # Wigh review
        "10.1021/ci00057a005",  # SMILES
        "10.3390/biom14010072",  # Protein-ligand fingerprinting
        "10.1038/s41586-021-03819-2",  # AlphaFold
        "10.1038/s41592-022-01488-1",  # ColabFold
        "10.1002/jcc.21334",  # AutoDock Vina
        "10.1021/jm0306430",  # Glide
        "10.1186/s13321-018-0285-8",  # P2Rank
        "10.1093/bioinformatics/btx350",  # DeepSite
        "10.1021/acs.jcim.0c00411",  # Crossdocked 3D-CNN
        "10.1021/acs.molpharmaceut.0c00326",  # DILI
        "10.3389/fphar.2020.00639",  # Cardiotoxicity
        "10.1093/bioinformatics/bty707",  # admetSAR 2.0
        "10.1016/j.sbi.2023.102546",  # PK prediction
        "10.1007/s10822-013-9672-4",  # size of chemical space
        "10.1038/nrd.2017.232",  # Automating drug discovery
        "10.1186/s13321-017-0235-x",  # de novo RL
        "10.1021/acscentsci.7b00512",  # RNN focused libraries
        "10.1021/acs.jmedchem.1c00927",  # Generative models review
        "10.1162/neco.1997.9.8.1735",  # LSTM
        "10.1016/j.drudis.2020.10.010",  # AI in drug discovery (Drug Discov Today)
    ]

    entries: List[str] = []

    for doi in dois:
        entries.append(f"- {apa7_from_doi(doi)}")

    # arXiv entries (Crossref 404 in this environment):
    entries.append(
        "- Corso, G., Stärk, H., Jing, B., Barzilay, R., & Jaakkola, T. (2022). DiffDock: Diffusion steps, twists, and turns for molecular docking (arXiv:2210.01776). arXiv. https://arxiv.org/abs/2210.01776"
    )
    entries.append(
        "- Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes (arXiv:1312.6114). arXiv. https://arxiv.org/abs/1312.6114"
    )

    for entry in sorted(entries, key=lambda s: s.lower()):
        print(entry)


if __name__ == "__main__":
    main()
