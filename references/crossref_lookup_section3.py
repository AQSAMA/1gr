import json
import sys
import urllib.parse
import urllib.request


def crossref_title_lookup(title: str, rows: int = 1) -> dict:
    query = urllib.parse.urlencode({"query.title": title, "rows": str(rows)})
    url = f"https://api.crossref.org/works?{query}"
    with urllib.request.urlopen(url, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    titles = [
        "ZINC20-A Free Ultralarge-scale chemical database for ligand discovery",
        "Three-Dimensional Convolutional Neural Networks and a Crossdocked Data Set for Structure-Based Drug Design",
        "GNINA 1.0: Molecular Docking with Deep Learning",
        "PubChem substance and compound databases",
        "ChEMBL: towards direct deposition of bioassay data",
        "BindingDB: a web-accessible database of experimentally determined protein-ligand binding affinities",
        "Fingerprinting interactions between proteins and ligands for facilitating machine learning in drug discovery",
        "admetSAR 2.0: Web-service for prediction and optimization of chemical ADMET properties",
        "Revealing cytotoxic substructures in molecules using deep learning",
        "Comparing machine learning algorithms for predicting drug-induced liver injury (DILI)",
        "Dual transcriptomic and molecular machine learning predicts all major clinical forms of drug cardiotoxicity",
        "An Overview of Machine Learning and Big Data for Drug Toxicity Evaluation",
        "Artificial intelligence for compound pharmacokinetics prediction",
        "Integrative computational approaches for discovery and evaluation of lead compound for drug design",
    ]

    for title in titles:
        try:
            data = crossref_title_lookup(title)
            item = (data.get("message", {}).get("items") or [{}])[0]
            doi = item.get("DOI")
            year = ((item.get("issued", {}).get("date-parts") or [[None]])[0][0])
            journal = (item.get("container-title") or [""])[0]
            match_title = (item.get("title") or [""])[0]

            print(f"- {title}")
            print(f"  -> {year} | {journal}")
            print(f"  DOI: {doi}")
            print(f"  match: {match_title}")
        except Exception as exc:
            print(f"- {title}")
            print(f"  ERR: {exc}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
