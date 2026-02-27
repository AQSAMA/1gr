# To-Do

## Section 3 - Completed
- [x] Restructure Section 3 headings and prune clutter
- [x] Curate ~20--30 keeper sources and generate APA-style reference list
- [x] Replace legacy oversized bibliography in Section 3
- [x] Normalize in-text citations to match the curated reference list

## Section 4 - Completed
- [x] Curate references (82 → 29)
- [x] Standardize heading hierarchy (proper markdown headings)
- [x] Fix paragraph formatting (unwrap hard line breaks)
- [x] Remove orphaned text fragments ("disease targets:**", "EXAMPLE**", "Model Decisions**", etc.)
- [x] Fix escape characters (\\", \\*, 1\\.)
- [x] Fix special notation (IC₅₀)
- [x] Fix missing spaces after citations (e.g., ")." → "). ")
- [x] Remove curly brace artifacts

## Abstract (New)
- [x] Draft thesis abstract based on `allv2.md` scope (AI across the drug discovery pipeline)
- [x] Ensure tone: academic, clear, non-generic; avoid hype and marketing language
- [x] Cover: target identification/validation, candidate design/screening, ADMET, real-world platforms/case studies, limits (data quality, black-box), ethics/regulation, and future outlook
- [x] Keep length moderate (typically ~150–250 words unless thesis guidelines require otherwise)
- [x] Save as `abstraction_head.md` in the project root (`1gr/abstraction_head.md`)
- [x] Quick pass: verify terminology consistency (AI/ML/DL, QSAR/QSPR, ADMET) and avoid introducing new claims not supported by the thesis text

## Review
**Section 3:**
- Updated section content in section3.md to reduce clutter and keep the scope academically focused.
- Replaced the previous extremely long reference list with a curated 28-item alphabetized APA-style list.
- Normalized in-text citations (including disambiguating two 2024 "Li et al." works using initials).
- Kept the ADMET subsection in place (as requested).

**Section 4:**
- Reduced references from 82 to 29 high-quality APA7 sources
- Fixed paragraph formatting: lines were hard-wrapped at ~70-80 chars, now proper paragraphs (500-900+ chars)
- Line count reduced from 1079 → 550 (word count preserved: 7142)
- Removed 4 orphaned text fragments that were artifacts from the original document
- Fixed all escaped characters and special notations
- Added missing spaces after citation parentheses
- Removed curly brace artifacts

**Abstract:**
- Added `1gr/abstraction_head.md` containing an academically toned abstract aligned to `allv2.md` (targets → design/screening → ADMET → real-world impact), explicitly noting core limitations (data quality, opacity, dataset shift) and the requirement for prospective experimental validation, with ethics/regulation positioned as deployment-critical.

## Final Stats
| Section | Lines | Words |
|---------|-------|-------|
| Section 3 | 234 | 6,205 |
| Section 4 | 550 | 7,142 |

## Notes / Open Question
- "No search links" was interpreted as "no Google/search-result links". The final references include DOI and arXiv URLs, which are standard for APA 7. If you want *no URLs at all*, I can convert them to plain DOI/arXiv identifiers.