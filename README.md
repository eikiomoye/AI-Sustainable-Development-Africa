# AI for Sustainable Development in Low-Resource African Contexts

A research companion to:

**Ikiomoye Douglas Emmanuel and Ebenezer Esenogho (2026). Artificial Intelligence for Sustainable Development in Low-Resource African Contexts: A Structured Review and Adaptive Deployment Framework.** *Sustainability*, 18(15), 7835.

**Paper:** https://doi.org/10.3390/su18157835

## Purpose

This companion organises the paper's conceptual framework, resource constraints, sectoral themes and bibliography into reusable documentation and machine-readable resources. It was newly prepared from the published PDF supplied by co-author Ikiomoye Douglas Emmanuel.

The central distinction is between an AI system's technical potential and the conditions needed to deploy, maintain, govern and adapt it. The proposed framework is a synthesis-based conceptual model. It has not been empirically validated as a deployment instrument, and the worksheet in this repository is a new discussion aid, not a validated readiness score.

## Resources

| Path | Contents |
| --- | --- |
| `catalogue/references.csv` and `.json` | 72 bibliography entries extracted from the article |
| `catalogue/framework_layers.csv` | Four interacting framework layers from Section 8 |
| `catalogue/deployment_dimensions.csv` | Six resource/context dimensions from Table 4 |
| `catalogue/sectoral_domains.csv` | Five synthesis domains described in Section 4 |
| `catalogue/research_priorities.csv` | Five future-work priorities from Section 9 |
| `catalogue/reported_selection_counts.csv` | Article-reported PRISMA-stage counts |
| `catalogue/reported_exclusion_reasons.csv` | Article-reported full-text exclusion categories |
| `templates/deployment_discussion.csv` | Editable, unscored discussion worksheet |
| `docs/FRAMEWORK.md` | Framework explanation and simplified Mermaid diagram |
| `docs/PROVENANCE.md` | Sources, derivations and extraction limits |
| `docs/SOURCE_NOTES.md` | Bibliography/citation and evidence limitations |
| `tools/companion.py` | New standard-library utility for reference search and worksheet summaries |
| `CITATION.cff` and `paper.bib` | Citation files crediting both paper authors |

## Framework overview

Section 8 connects four layers:

1. **Structural enablers:** technical foundations and deployment conditions.
2. **Sectoral applications:** healthcare, agriculture, education and environmental management.
3. **Potential outcomes:** service delivery, productivity, inclusion, resilience and monitoring.
4. **Adaptive feedback:** evaluation, user feedback and learning that inform changes to enablers and applications.

See [docs/FRAMEWORK.md](docs/FRAMEWORK.md). Governance/infrastructure is also one of the five analytical synthesis domains in Section 4; it is not presented as a fifth sectoral application in Section 8.

## Reference inventory and study-selection counts

The article reports **26 included studies** in its structured synthesis. Its bibliography contains **72 entries**, which include background and methodological sources. These counts describe different things.

The reported selection sequence is 144 identified, 15 duplicates removed, 129 screened, 48 excluded at screening, 81 sought for retrieval, 16 not retrieved, 65 assessed for eligibility, 39 excluded at full text and 26 included. The arithmetic reconciles. Original record-level screening decisions, search exports and extraction sheets were not supplied, so this repository does not reconstruct a 26-row included-study dataset.

Some names and bracketed citation numbers in Table 2 differ from the final bibliography. Examples are recorded in [docs/SOURCE_NOTES.md](docs/SOURCE_NOTES.md). The companion does not silently repair the article or infer an authoritative study-membership list from these references.

## Use the companion

Requires Python 3.10 or later. No third-party packages are needed for the utility.

```bash
python tools/companion.py references --query "Africa" --limit 10
python tools/companion.py references --number 24 --json
python tools/companion.py worksheet --file templates/deployment_discussion.csv --json
```

The worksheet starts with all six dimensions marked `not_assessed`. Complete it with locally sourced evidence and stakeholder discussion. Valid descriptive states are `present`, `weak`, `absent` and `not_assessed`. These states are a new companion convention. The utility only summarises entries and identifies missing evidence. It produces no score, ranking, deployment recommendation or pass/fail decision.

## Provenance and authorship

The title page names Ikiomoye Douglas Emmanuel and Ebenezer Esenogho and states that they contributed equally. The contribution statement credits both for conceptualisation, methodology, validation, investigation, review/editing and visualisation; original-draft preparation is credited to Emmanuel and supervision to Esenogho. Citation files preserve the published author order.

All companion resources and utilities were prepared after publication. They are not original screening files, a new experiment, or evidence that the framework has been validated. Source page numbers use the printed article numbering; the supplied PDF has an additional cover sheet.

## Reuse

The source article states CC BY licensing. Article-derived summaries and reference extractions retain attribution and are labelled as adapted material. See [LICENSE.md](LICENSE.md) for reuse terms and the separate MIT licence for the newly written utility.
