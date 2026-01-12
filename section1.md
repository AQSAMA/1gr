**1. Fundamentals of Drug Discovery & Artificial Intelligence (AI)
Introduction**

**Abbreviations**

Artificial Intelligence (AI); Machine Learning (ML); Deep Learning (DL);
quantitative structure--activity relationship (QSAR);
absorption--distribution--metabolism--excretion--toxicity (ADMET);
electronic health records (EHRs); Graph Neural Networks (GNNs);
Variational Autoencoder (VAE); Generative Adversarial Network (GAN);
Reinforcement Learning (RL); pharmacokinetics/pharmacodynamics (PK/PD);
high-throughput screening (HTS); investigational new drug (IND).

**1.1. The Traditional Drug Discovery Pipeline**

Modern drug discovery is traditionally organized as a staged funnel that
begins with target identification and biological validation, proceeds
through hit identification, advances to hit-to-lead and lead
optimization with iterative medicinal chemistry and
absorption--distribution--metabolism--excretion--toxicity (ADMET)
profiling, and culminates in preclinical testing followed by phased
clinical trials (Phase I--III) before regulatory review and approval
(Qureshi et al., 2023). This paradigm has provided a robust frame for
translating advances in biology and chemistry into new therapeutics;
however, its practical execution is resource-intensive, slow, and
risk-laden. Industry surveys and retrospective analyses consistently
report that bringing a new small-molecule medicine from target to market
requires on the order of a decade and expenditures approaching or
exceeding one billion U.S. dollars, with wide variation across disease
areas and modalities (Hughes, Rees, Kalindjian, & Philpott, 2011). The
central reason is attrition: failures compound as projects move
downstream, and the most expensive failures occur late in development
(Sliwoski, Kothiwale, Meiler, & Lowe, 2014; Waring et al., 2015).

**1.1.1. Stages: From target identification to clinical trials**

Target identification and validation integrate multi-omics evidence,
disease genetics, functional genomics (e.g., CRISPR and RNA interference
screens), and structural biology to nominate proteins or pathways
causally linked to human pathophysiology. Computational prioritization
is typically followed by experimental validation using biochemical and
cellular assays to de-risk target tractability and mechanism (Paul et
al., 2010). Once a target is chosen, hit identification historically
relied on high-throughput screening (HTS) of large physical libraries
and on ligand-based heuristics; today, structure-based and ligand-based
in silico virtual screening are widely used to triage candidates prior
to wet-lab evaluation, compressing the experimental search space (Maia,
Assis, de Oliveira, da Silva, & Taranto, 2020; Sliwoski, Kothiwale,
Meiler, & Lowe, 2014). Hit-to-lead and lead optimization are the most
chemistry-intensive phases: medicinal chemists explore analogue series
to improve potency, selectivity, solubility, permeability, and metabolic
stability, while concurrently profiling safety liabilities. Because
these tasks are inherently complex and combinatorial, predictive
modeling---ranging from classical quantitative structure--activity
relationship (QSAR) methods to modern machine learning (ML)---has long
been used to guide design--make--test--analyze cycles (Chen, Engkvist,
Wang, Olivecrona, & Blaschke, 2018; Lavecchia, 2015; Sliwoski,
Kothiwale, Meiler, & Lowe, 2014). Finally, preclinical development
aggregates good-laboratory-practice toxicology,
pharmacokinetics/pharmacodynamics (PK/PD), and efficacy models to
support investigational new drug (IND) applications. In humans, Phase I
assesses safety and dose, Phase II probes preliminary efficacy and
dose-response, and Phase III evaluates confirmatory efficacy and safety
in larger populations; failures due to unexpected toxicity, poor
exposure, or insufficient efficacy remain major cost drivers across
these stages (Hughes, Rees, Kalindjian, & Philpott, 2011; Waring et al.,
2015).

**1.1.2. Challenges: High costs, long durations, and high attrition
rates**

Three systemic constraints make the traditional pipeline slow and
expensive. First, scale: the putative chemical space of small molecules
(often estimated near 10\^60) dwarfs any feasible synthesis or assay
capacity, which forces exploration of a vanishingly small, biased subset
of possibilities (Sliwoski, Kothiwale, Meiler, & Lowe, 2014). Second,
noise and translation gaps: preclinical models imperfectly recapitulate
human biology, and assay conditions vary widely across laboratories and
platforms, degrading the reliability of early signals when projected
into the clinic (Waring et al., 2015). Third, data sparsity and
heterogeneity: many crucial labels---particularly human toxicity and
clinical efficacy---are scarce, context-dependent, or measured at small
scale; as a result, projects confront uncertainty just when the stakes
are highest (Chen, Engkvist, Wang, Olivecrona, & Blaschke, 2018; Waring
et al., 2015). These realities help to explain why overall success rates
from first-in-human to approval remain in the single-digit to low-teens
percent range in aggregate, with challenging areas such as oncology
performing even worse (Waring et al., 2015).

**1.2. Introduction to Artificial Intelligence**

Artificial Intelligence (AI) refers to computational techniques that
execute tasks commonly associated with human intelligence---such as
perception, pattern recognition, prediction, and decision-making---by
learning from data and/or formal rules (Lavecchia, 2015). Within AI,
Machine Learning (ML) denotes algorithms that learn mappings from inputs
to outputs by optimizing performance on data (supervised, unsupervised,
semi-supervised, and reinforcement learning). In drug discovery, ML
underpins QSAR classifiers/regressors, phenotypic clustering,
target--disease inference, and patient stratification from electronic
health records (EHRs) (Bishop, 2006; Lavecchia, 2015; Lo, Rensi, Torng,
& Altman, 2018). Deep Learning (DL) is a subset of ML based on
multi-layer neural networks that learn hierarchical feature
representations end-to-end and have shown superior performance on
complex, high-dimensional data modalities such as images, sequences, and
graphs (Goodfellow, Bengio, & Courville, 2016; Jumper et al., 2021).

Architecturally, several families are especially relevant to drug
design. Feed-forward (fully connected) networks operate on fixed-length
descriptors or fingerprints and can excel when abundant, well-curated
tabular features are available (Lo, Rensi, Torng, & Altman, 2018;
Sliwoski, Kothiwale, Meiler, & Lowe, 2014). Convolutional Neural
Networks (CNNs) capture local spatial patterns and have been applied to
3-D voxelized protein pockets, cryo-EM and microscopy images, and
grid-based protein--ligand interaction maps (Korotcov, Tkachenko, Russo,
& Ekins, 2017). Recurrent Neural Networks (RNNs) and long short-term
memory (LSTM) networks encode sequential dependencies and have been used
to model simplified molecular input line entry system (SMILES) strings
and peptide/protein sequences (Yang et al., 2019).
Transformers---self-attention architectures that replace explicit
recurrence---enable efficient modeling of long-range dependencies and
parallel training; they now power chemical language models and
large-scale protein language models that extract structure- and
function-relevant embeddings (Jumper et al., 2021; Vaswani et al.,
2017). Finally, Graph Neural Networks (GNNs) perform message passing
directly on molecular graphs, treating atoms as nodes and bonds as
edges; this allows property prediction and interaction modeling without
hand-crafted descriptors (Stokes et al., 2020).

Beyond prediction, generative modeling has created a new design
paradigm. Variational autoencoders (VAEs), generative adversarial
networks (GANs), autoregressive/Transformer decoders, and reinforcement
learning (RL) agents can propose novel, synthetically accessible
molecules and optimize them toward multi-endpoint profiles---such as
potency, selectivity, and ADMET---prior to synthesis (Sanchez-Lengeling
& Aspuru-Guzik, 2018; Zhavoronkov et al., 2019). These capabilities
complement long-standing computational chemistry, docking, and
physics-based simulation techniques and increasingly integrate with them
(Jumper et al., 2021; Maia, Assis, de Oliveira, da Silva, & Taranto,
2020; Sliwoski, Kothiwale, Meiler, & Lowe, 2014).

**1.3. The "Why AI?" Rationale**

**1.3.1. Bottlenecks in traditional methods**

Hit identification is constrained by the size of chemical space and by
the cost of HTS; even very large physical screens sample a minute
fraction of what is possible. In silico ligand-based and structure-based
virtual screening, guided by ML scoring functions, can triage millions
of candidates to focus scarce experimental bandwidth where it has the
highest expected value (Maia, Assis, de Oliveira, da Silva, & Taranto,
2020; Sliwoski, Kothiwale, Meiler, & Lowe, 2014). Lead optimization is a
high-dimensional search in which medicinal chemists balance potency,
selectivity, solubility, stability, and toxicity. Here, surrogate models
accelerate design--make--test--analyze cycles by predicting properties,
learning structure--activity relationships, and suggesting informative
analogs; when coupled to active learning and Bayesian optimization,
these models can reduce the number of iterations required to achieve a
clinical candidate (Chen, Engkvist, Wang, Olivecrona, & Blaschke, 2018;
Lavecchia, 2015; Sliwoski, Kothiwale, Meiler, & Lowe, 2014). ADMET
uncertainty is a dominant driver of late attrition; predictive
toxicology, metabolism, and exposure models can flag liabilities earlier
and suggest structural fixes before costly studies commence (Lo, Rensi,
Torng, & Altman, 2018; Sliwoski, Kothiwale, Meiler, & Lowe, 2014; Waring
et al., 2015).

**1.3.2. How AI addresses these bottlenecks**

AI offers leverage in at least six ways. First, search and
prioritization at scale: QSAR/DL models can score millions of virtual
molecules rapidly to identify promising regions of chemical space,
substantially reducing reliance on brute-force HTS (Maia, Assis, de
Oliveira, da Silva, & Taranto, 2020). Second, representation learning:
DL and GNNs learn task-relevant molecular embeddings that often
outperform hand-crafted descriptors, improving generalization across
tasks and scaffolds (Stokes et al., 2020; Yang et al., 2019). Third,
generative design: VAEs, GANs, Transformer decoders, and RL can produce
de novo chemotypes optimized for multiple endpoints prior to synthesis,
enabling goal-directed exploration rather than random enumeration
(Sanchez-Lengeling & Aspuru-Guzik, 2018; Zhavoronkov et al., 2019).
Fourth, structure-based acceleration: accurate protein structure
prediction (e.g., AlphaFold) broadens target coverage and improves
docking and binding-site modeling when experimental structures are
unavailable (Jumper et al., 2021; Senior et al., 2020). Fifth,
multimodal integration: ML can combine chemical structures, high-content
phenotypic images, transcriptomic and proteomic signatures, and clinical
records into unified predictors that better support target selection,
biomarker discovery, toxicity risk assessment, and patient
stratification (Jumper et al., 2021; Stokes et al., 2020). Sixth, speed
and cost reduction: when embedded into closed design--synthesis--assay
loops, AI helps cut down the number of compounds synthesized and
experiments run, lowering cost and compressing timelines while
preserving decision quality (Maia, Assis, de Oliveira, da Silva, &
Taranto, 2020; Paul et al., 2010).

These benefits have prospective support. Deep learning--based screening
surfaced new antibiotic leads with unconventional scaffolds that were
validated in vivo, demonstrating that data-driven models can traverse
vast chemical spaces effectively (Stokes et al., 2020). Industrial
reviews document cases where AI-guided workflows delivered higher hit
rates, better property profiles, or accelerated cycles relative to
historical baselines, while warning against overgeneralization without
rigorous prospective tests (Chen, Engkvist, Wang, Olivecrona, &
Blaschke, 2018; Mak & Pichika, 2019; Sellwood et al., 2018; Waring et
al., 2015). AI outputs are hypotheses requiring orthogonal experimental
validation; without careful curation, benchmarking, and prospective
studies, models risk amplifying dataset biases or yielding
non-generalizable leads (Chen, Engkvist, Wang, Olivecrona, & Blaschke,
2018; Lo, Rensi, Torng, & Altman, 2018; Mak & Pichika, 2019).

**1.4. Data in AI-Driven Drug Design**

**1.4.1. Types of Data**

AI systems in discovery are only as reliable as the data and
representations they consume. Three broad data domains---chemical,
biological, and clinical/real-world---feed contemporary pipelines, each
with canonical encodings and characteristic pitfalls.

Chemical data can be represented as strings (e.g., the simplified
molecular input line entry system, SMILES, or the IUPAC International
Chemical Identifier, InChI), enabling sequence models and convenient
data exchange, though sensitivity to canonicalization and syntax must be
managed (Yang et al., 2019). Molecular graphs, which treat atoms as
nodes and bonds as edges, are the native input for GNNs and
message-passing neural networks that learn atom- and substructure-level
interactions without fixed fingerprints (Stokes et al., 2020).
Traditional fingerprints and physicochemical descriptors (e.g.,
extended-connectivity fingerprints, ECFP/Morgan) remain effective,
particularly when paired with light-weight ML algorithms or hybrid
descriptor+DL schemes (Lo, Rensi, Torng, & Altman, 2018; Sliwoski,
Kothiwale, Meiler, & Lowe, 2014). Critically, the field has converged on
shared benchmarks such as MoleculeNet, which curate tasks spanning
quantum mechanics, physical chemistry, biophysics, physiology, and
toxicity (e.g., QM9, ESOL, FreeSolv, Lipophilicity, PDBbind, PCBA, MUV,
HIV, BACE, BBBP, Tox21, ToxCast, ClinTox, SIDER), with standardized
splits and metrics and integration into open-source frameworks like
DeepChem to support reproducible comparisons (Wu et al., 2018; Yang et
al., 2019).

Biological data include macromolecular sequences and structures as well
as high-content cellular phenotypes and omics layers. Protein and
peptide sequences are now modeled effectively by language
models---usually Transformer variants---that learn embeddings useful for
structure prediction, function inference, and interaction modeling
(Jumper et al., 2021; Vaswani et al., 2017). Three-dimensional
structures, whether experimental (e.g., Protein Data Bank) or predicted,
support docking, molecular dynamics, and structure-aware ML that uses
pocket surfaces and interaction fields as features (Maia, Assis, de
Oliveira, da Silva, & Taranto, 2020; Senior et al., 2020; Sliwoski,
Kothiwale, Meiler, & Lowe, 2014). Phenotypic imaging readouts and
transcriptomic signatures can be ingested directly by CNNs and other DL
architectures to relate morphological changes to mechanism and target
engagement (Chen, Engkvist, Wang, Olivecrona, & Blaschke, 2018;
Korotcov, Tkachenko, Russo, & Ekins, 2017).

Clinical and real-world data encompass EHRs, claims, clinical trial
records, adverse event reports, and curated knowledge graphs. These
sources enable patient-level outcome prediction, cohort selection, and
safety signal detection but are highly heterogeneous and governed by
privacy and regulatory constraints. Privacy-preserving approaches---such
as federated learning---seek to leverage distributed clinical data
without exposing protected health information (Jumper et al., 2021).
Reviews of AI in development emphasize how repurposing, trial
optimization, and post-marketing surveillance can benefit when such data
are harmonized and linked with preclinical and chemical features
(Doytchinova, 2022; Sellwood et al., 2018).

**1.4.2. The Challenge of Data Curation and Quality**

Heterogeneous labels and context dependence are pervasive. Nominally
identical endpoints (e.g., biochemical inhibition, cellular viability,
or toxicity) may differ by assay format, dose, exposure time, cell type,
and readout technology; naively merging such datasets injects label
noise and induces distribution shift, undermining generalization (Chen,
Engkvist, Wang, Olivecrona, & Blaschke, 2018). Small, biased datasets
are common for high-value endpoints like human toxicity or clinical
efficacy, making transfer learning, multi-task learning, few-shot
learning, and data augmentation attractive strategies to regularize
models (Chen, Engkvist, Wang, Olivecrona, & Blaschke, 2018; Lo, Rensi,
Torng, & Altman, 2018). Provenance and reproducibility demand rigorous
documentation of data processing, careful metadata capture, and use of
community benchmarks; scaffold-aware splits and external prospective
evaluation help estimate true predictive power beyond random splits (Wu
et al., 2018; Yang et al., 2019). Privacy and regulatory issues further
complicate the use of patient-level data, motivating active research in
federated learning and secure computation to unlock value safely (Jumper
et al., 2021).

Practical remedies are well established: standardizing ontologies and
identifiers (e.g., InChIKeys for molecules, UniProt for proteins),
applying assay-aware label harmonization, building explicit uncertainty
estimates into models, and tightly integrating computational cycles with
prospective experiments. When AI is embedded into closed-loop discovery,
prospective iterations provide corrective feedback that prevents drift
and overfitting to historic biases (Chen, Engkvist, Wang, Olivecrona, &
Blaschke, 2018; Jumper et al., 2021; Maia, Assis, de Oliveira, da Silva,
& Taranto, 2020).

**Synthesis and Forward Look**

The traditional pipeline remains a necessary scaffold for translational
therapeutics, but it was not built to contend with combinatorial
chemical space, noisy biology, and the escalating evidence demands of
precision medicine. AI augments this scaffold with representation
learning (e.g., GNNs and Transformers), scalable prioritization, de novo
generative design, and multimodal integration that target the most
painful bottlenecks---hit finding and lead optimization---while
de-risking downstream decision points. Real progress depends on data
curation, validation in realistic splits, and prospective,
experiment-coupled evaluation. Subsequent sections examine how specific
AI techniques are deployed for target identification, activity and
property prediction, de novo design, and clinical translation (Chen,
Engkvist, Wang, Olivecrona, & Blaschke, 2018; Doytchinova, 2022; Jumper
et al., 2021; Maia, Assis, de Oliveira, da Silva, & Taranto, 2020; Mak &
Pichika, 2019; Sanchez-Lengeling & Aspuru-Guzik, 2018; Sellwood et al.,
2018; Stokes et al., 2020; Waring et al., 2015; Wu et al., 2018; Yang et
al., 2019; Zhavoronkov et al., 2019).

**References**

Bishop, C. M. (2006). \*Pattern recognition and machine learning\*.
Springer.

Chen, H., Engkvist, O., Wang, Y., Olivecrona, M., & Blaschke, T. (2018).
The rise of deep learning in drug discovery. \*Drug Discovery Today,
23\*(6), 1241--1250.

Doytchinova, I. (2022). Drug design---Past, present, future.
\*Molecules, 27\*, 1496.

Goodfellow, I., Bengio, Y., & Courville, A. (2016). \*Deep learning\*.
MIT Press.

Hughes, J. P., Rees, S., Kalindjian, S. B., & Philpott, K. L. (2011).
Principles of early drug discovery. \*British Journal of Pharmacology,
162\*(6), 1239--1249.

Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M.,
Ronneberger, O., et al. (2021). Highly accurate protein structure
prediction with AlphaFold. \*Nature, 596\*(7873), 583--589.

Korotcov, A., Tkachenko, V., Russo, D. P., & Ekins, S. (2017).
Comparison of deep learning with multiple machine learning methods and
metrics using diverse drug discovery data sets. \*Molecular
Pharmaceutics, 14\*(12), 4462--4475.

Lavecchia, A. (2015). Machine-learning approaches in drug discovery:
Methods and applications. \*Drug Discovery Today, 20\*(3), 318--331.

Lo, Y.-C., Rensi, S. E., Torng, W., & Altman, R. B. (2018). Machine
learning in chemoinformatics and drug discovery. \*Drug Discovery Today,
23\*(8), 1538--1546.

Maia, E. H. B., Assis, L. C., de Oliveira, T. A., da Silva, A. M., &
Taranto, A. G. (2020). Structure-based virtual screening: From classical
to artificial intelligence. \*Frontiers in Chemistry, 8\*, 343.

Mak, K.-K., & Pichika, M. R. (2019). Artificial intelligence in drug
development: Present status and future prospects. \*Drug Discovery
Today, 24\*, 773--780.

Paul, S. M., Mytelka, D. S., Dunwiddie, C. T., Persinger, C. C., Munos,
B. H., Lindborg, S. R., & Schacht, A. L. (2010). How to improve R&D
productivity: The pharmaceutical industry's grand challenge. \*Nature
Reviews Drug Discovery, 9\*(3), 203--214.

Qureshi, R., Irfan, M., Gondal, T. M., Khan, S., Wu, J., Hadi, M. U., et
al. (2023). AI in drug discovery and its clinical relevance. \*Heliyon,
9\*(5), e16214.

Sanchez-Lengeling, B., & Aspuru-Guzik, A. (2018). Inverse molecular
design using machine learning: Generative models for matter engineering.
\*Science, 361\*(6400), 360--365.

Sellwood, M. A., Ahmed, M., Segler, M., Brown, N., Heifets, A., et al.
(2018). Artificial intelligence in drug discovery. \*Future Medicinal
Chemistry, 10\*(17), 2025--2028.

Senior, A. W., Evans, R., Jumper, J., Kirkpatrick, J., Sifre, L., Green,
T., et al. (2020). Improved protein structure prediction using
potentials from deep learning. \*Nature, 577\*(7792), 706--710.

Sliwoski, G., Kothiwale, S., Meiler, J., & Lowe, E. W. (2014).
Computational methods in drug discovery. \*Pharmacological Reviews,
66\*(1), 334--395.

Stokes, J. M., Yang, K., Swanson, K., Jin, W., Cubillos-Ruiz, A.,
Donghia, N. M., et al. (2020). A deep learning approach to antibiotic
discovery. \*Cell, 180\*(4), 688--702.e13.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez,
A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need.
In \*Advances in Neural Information Processing Systems\*.

Waring, M. J., Arrowsmith, J., Leach, A. R., Leeson, P. D., Mandrell,
S., Owen, R. M., et al. (2015). An analysis of the attrition of drug
candidates from four major pharmaceutical companies. \*Nature Reviews
Drug Discovery, 14\*(7), 475--486.

Wu, Z., Ramsundar, B., Feinberg, E. N., Gomes, J., Geniesse, C., Pappu,
A. S., et al. (2018). MoleculeNet: A benchmark for molecular machine
learning. \*Chemical Science, 9\*(2), 513--530.

Yang, K., Swanson, K., Jin, W., Coley, C., Eiden, P., Gao, H.,
Guzman-Perez, A., Hopper, T., Kelley, B., Mathew, R., Palmer, A.,
Settels, V., Jaakkola, T., Jensen, K., & Barzilay, R. (2019). Analyzing
learned molecular representations for property prediction. \*Journal of
Chemical Information and Modeling, 59\*(8), 3370--3388.

Zhavoronkov, A., Ivanenkov, Y. A., Aliper, A., Veselov, M. S.,
Aladinskiy, V. A., et al. (2019). Deep learning enables rapid
identification of potent DDR1 kinase inhibitors. \*Nature Biotechnology,
37\*(9), 1038--1040.
