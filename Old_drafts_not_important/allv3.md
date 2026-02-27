Ministry of Higher Education and Scientific Research

University of Al-Maarif

College of Pharmacy



# Artificial Intelligence in Drug Discovery: From Target Identification to Clinical Translation



A project submitted to the College of Pharmacy, University of Al-Maarif, in Partial Fulfillment of the Requirements for the Degree of Bachelor of Computer Science.



**By**

[Student Name(s)]



**Supervisor**

[Supervisor Name]



**2026**

---

## Abstract

Drug discovery remains constrained by a familiar triangle: cost, time, and attrition—aggravated by the immensity of chemical space and the imperfect translation of preclinical signals into human efficacy and safety. This thesis examines how artificial intelligence, spanning machine learning and deep learning, can ease these constraints by shifting key decisions earlier in the pipeline and by scaling the search, prioritization, and optimization of hypotheses. It surveys AI methods for target identification and validation, including the integration of multi-omic evidence, network-based representations of biology, and structure-informed reasoning enabled by advances in protein structure prediction. It then analyzes AI-driven candidate design and screening—molecular representations, predictive QSAR/QSPR modeling, docking acceleration, de novo generative design, and ADMET profiling—as means to compress design–make–test cycles and expose liabilities before costly downstream studies. Real-world impact is contextualized through contemporary platforms and case studies, yet the discussion remains tempered by practical limits: data scarcity and heterogeneity, model opacity, dataset shift, and the non-negotiable need for prospective experimental validation. Ethical and regulatory considerations—privacy, bias, accountability, governance—are treated as integral to deployment, not as afterthoughts. The central conclusion is that AI proves most valuable as an augmentative, evidence-weighting partner to human expertise, delivering its gains when coupled with rigorous data curation and experiment-driven feedback.

---

## Table of Contents

1. Fundamentals of Drug Discovery & Artificial Intelligence (AI) Introduction
    1.1. The Traditional Drug Discovery Pipeline
        1.1.1. Stages: From target identification to clinical trials
        1.1.2. Challenges: High costs, long durations, and high attrition rates
    1.2. Introduction to Artificial Intelligence
        1.2.1. Defining Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL)
    1.3. The "Why AI?" Rationale
        1.3.1. Bottlenecks in traditional methods
        1.3.2. How AI addresses these bottlenecks
    1.4. Data in AI-Driven Drug Design
        1.4.1. Types of Data
        1.4.2. The Challenge of Data Curation and Quality
    1.5. Synthesis and Forward Look
2. AI for Target Identification and Validation
    2.1. Biomarker Discovery and Target Identification
        2.1.1. Using ML/DL to identify novel disease-associated proteins and genes
    2.2. Analysis of Omics Data
        2.2.1. Applying AI to genomics, proteomics, and transcriptomics to understand disease pathways
        2.2.2. The Impact of AlphaFold on structural biology
    2.3. Network Pharmacology
        2.3.1. Using graph-based AI models to map biological networks
        2.3.2. Predicting complex target–drug interactions
    2.4. Predicting Target "Druggability"
        2.4.1. Assessing how likely a biological target is to bind effectively with a drug molecule
3. AI for Drug Candidate Design and Screening
    3.1. AI-Accelerated Virtual Screening
        3.1.1. Molecular Representation: Inputting Molecules Into AI Models (SMILES Strings, Molecular Graphs, Fingerprints)
        3.1.2. Predictive Screening (QSAR/QSPR): Using ML/DL to Predict Compound Activity and Properties Before Synthesis
        3.1.3. AI-Enhanced Molecular Docking: Improving the Accuracy and Speed of Docking Simulations
    3.2. De Novo Drug Design
        3.2.1. Definition: Using Algorithms to Design Entirely New Molecules From Scratch
        3.2.2. Challenges: Navigating the Immense Size of Chemical Space
        3.2.3. The Role of Deep Learning: Introducing Generative AI as a Solution
        3.2.4. Key Models and Tools: Variational Auto-Encoders (VAEs), Generative Adversarial Networks (GANs), and Transformers
        3.2.5. Impact: Drastically Accelerating the Design of Novel and Optimized Molecules
    3.3. AI in ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity) profiling
        3.3.1. Predicting pharmacokinetics and pharmacodynamics
        3.3.2. Using multi-task learning to create comprehensive safety profiles
4. Real-World Impact, Challenges, and Future Landscape
    4.1. Pioneering Platforms and Real-World Case Studies
        4.1.1. DeepMind's AlphaFold: Revolutionizing Structural Biology
            4.1.1.1. Its Role in Accurately Predicting 3D Protein Structure
            4.1.1.2. Impact on Structure-Based Drug Design
        4.1.2. End-to-End Generative AI Platforms: Insilico Medicine
            4.1.2.1. Overview Of Their Pharma.AI Platform (Pandaomics For Target Identification, Chemistry42 For De Novo Molecule Generation)
            4.1.2.2. Case Study: Accelerated Target Discovery and Validation in HCC
        4.1.3. Other Notable AI Platforms in the Industry
            4.1.3.1. Atomwise: Pioneering AI-Powered Virtual Screening For Drug Discovery
            4.1.3.2. BenevolentAI: Driving Early Drug Discovery With Deep Data Analysis
            4.1.3.3. Numerate: A Model for AI-Pharma Collaboration in Medicinal Chemistry
    4.2. Challenges and Limitations
        4.2.1. The Black-Box Problem
        4.2.2. The Imperative for Experimental Validation
        4.2.3. High-Quality Data Scarcity and Its Impact on Performance in Drug Design
    4.3. Ethical and Regulatory Considerations
        4.3.1. Data Privacy and Algorithmic Bias
        4.3.2. Regulatory Frameworks
    4.4. Future Trends
        4.4.1. Emerging Technologies: Quantum Computing in Drug Design
        4.4.2. Personalized Medicine
        4.4.3. The AI-Scientist Collaboration: "Self-Driving" Labs
5. Conclusion
    5.1. Summary of Key Findings
        5.1.1. Recapitulation of AI's Impact Across the Drug Discovery Pipeline
    5.2. Reiteration of Thesis
        5.2.1. AI as a Collaborative Tool Empowering Human Scientists
    5.3. Final Outlook
        5.3.1. Toward an Intelligent, Data-Driven Era of Drug Discovery
References
---


---

# 1. Fundamentals of Drug Discovery & Artificial Intelligence (AI) Introduction


## 1.1. The Traditional Drug Discovery Pipeline

Modern drug discovery is traditionally organized as a staged funnel that begins with target identification and biological validation, proceeds through hit identification, advances to hit-to-lead and lead optimization with iterative medicinal chemistry and absorption–distribution–metabolism–excretion–toxicity (ADMET) profiling, and culminates in preclinical testing followed by phased clinical trials (Phase I–III) before regulatory review and approval (Qureshi et al., 2023). This paradigm has provided a robust frame for translating advances in biology and chemistry into new therapeutics; however, its practical execution is resource-intensive, slow, and risk-laden. Industry surveys and retrospective analyses consistently report that bringing a new small-molecule medicine from target to market requires on the order of a decade and expenditures approaching or exceeding one billion U.S. dollars, with wide variation across disease areas and modalities (Hughes et al., 2011). The central reason is attrition: failures compound as projects move downstream, and the most expensive failures occur late in development (Sliwoski et al., 2014; Waring et al., 2015).

### 1.1.1. Stages: From target identification to clinical trials

Target identification and validation integrate multi-omics evidence, disease genetics, functional genomics (e.g., CRISPR and RNA interference screens), and structural biology to nominate proteins or pathways causally linked to human pathophysiology. Computational prioritization is typically followed by experimental validation using biochemical and cellular assays to de-risk target tractability and mechanism (Paul et al., 2010). Once a target is chosen, hit identification historically relied on high-throughput screening (HTS) of large physical libraries and on ligand-based heuristics; today, structure-based and ligand-based in silico virtual screening are widely used to triage candidates prior to wet-lab evaluation, compressing the experimental search space (Maia et al., 2020; Sliwoski et al., 2014). Hit-to-lead and lead optimization are the most chemistry-intensive phases: medicinal chemists explore analogue series to improve potency, selectivity, solubility, permeability, and metabolic stability, while concurrently profiling safety liabilities. Because these tasks are inherently complex and combinatorial, predictive modeling—ranging from classical quantitative structure–activity relationship (QSAR) methods to modern machine learning (ML)—has long been used to guide design–make–test–analyze cycles (Chen et al., 2018; Lavecchia, 2015; Sliwoski et al., 2014). Finally, preclinical development aggregates good-laboratory-practice toxicology, pharmacokinetics/pharmacodynamics (PK/PD), and efficacy models to support investigational new drug (IND) applications. In humans, Phase I assesses safety and dose, Phase II probes preliminary efficacy and dose-response, and Phase III evaluates confirmatory efficacy and safety in larger populations; failures due to unexpected toxicity, poor exposure, or insufficient efficacy remain major cost drivers across these stages (Hughes et al., 2011; Waring et al., 2015).

### 1.1.2. Challenges: High costs, long durations, and high attrition rates

Three systemic constraints make the traditional pipeline slow and expensive. First, scale: the putative chemical space of small molecules (often estimated near 10^60) dwarfs any feasible synthesis or assay capacity, which forces exploration of a vanishingly small, biased subset of possibilities (Sliwoski et al., 2014). Second, noise and translation gaps: preclinical models imperfectly recapitulate human biology, and assay conditions vary widely across laboratories and platforms, degrading the reliability of early signals when projected into the clinic (Waring et al., 2015). Third, data sparsity and heterogeneity: many crucial labels—particularly human toxicity and clinical efficacy—are scarce, context-dependent, or measured at small scale; as a result, projects confront uncertainty just when the stakes are highest (Chen et al., 2018; Waring et al., 2015). These realities help to explain why overall success rates from first-in-human to approval remain in the single-digit to low-teens percent range in aggregate, with challenging areas such as oncology performing even worse (Waring et al., 2015).

## 1.2. Introduction to Artificial Intelligence

### 1.2.1. Defining Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL)

Artificial Intelligence (AI) refers to computational techniques that execute tasks commonly associated with human intelligence—such as perception, pattern recognition, prediction, and decision-making—by learning from data and/or formal rules (Lavecchia, 2015). Within AI, Machine Learning (ML) denotes algorithms that learn mappings from inputs to outputs by optimizing performance on data (supervised, unsupervised, semi-supervised, and reinforcement learning). In drug discovery, ML underpins QSAR classifiers/regressors, phenotypic clustering, target–disease inference, and patient stratification from electronic health records (EHRs) (Bishop, 2006; Lavecchia, 2015; Lo et al., 2018). Deep Learning (DL) is a subset of ML based on multi-layer neural networks that learn hierarchical feature representations end-to-end and have shown superior performance on complex, high-dimensional data modalities such as images, sequences, and graphs (Goodfellow et al., 2016; Jumper et al., 2021).

Architecturally, several families are especially relevant to drug design. Feed-forward (fully connected) networks operate on fixed-length descriptors or fingerprints and can excel when abundant, well-curated tabular features are available (Lo et al., 2018; Sliwoski et al., 2014). Convolutional Neural Networks (CNNs) capture local spatial patterns and have been applied to 3-D voxelized protein pockets, cryo-EM and microscopy images, and grid-based protein–ligand interaction maps (Korotcov et al., 2017). Recurrent Neural Networks (RNNs) and long short-term memory (LSTM) networks encode sequential dependencies and have been used to model simplified molecular input line entry system (SMILES) strings and peptide/protein sequences (Yang et al., 2019). Transformers—self-attention architectures that replace explicit recurrence—enable efficient modeling of long-range dependencies and parallel training; they now power chemical language models and large-scale protein language models that extract structure- and function-relevant embeddings (Jumper et al., 2021; Vaswani et al., 2017). Finally, Graph Neural Networks (GNNs) perform message passing directly on molecular graphs, treating atoms as nodes and bonds as edges; this allows property prediction and interaction modeling without hand-crafted descriptors (Stokes et al., 2020).

Beyond prediction, generative modeling has created a new design paradigm. Variational autoencoders (VAEs), generative adversarial networks (GANs), autoregressive/Transformer decoders, and reinforcement learning (RL) agents can propose novel, synthetically accessible molecules and optimize them toward multi-endpoint profiles—such as potency, selectivity, and ADMET—prior to synthesis (Sanchez-Lengeling & Aspuru-Guzik, 2018; Zhavoronkov et al., 2019). These capabilities complement long-standing computational chemistry, docking, and physics-based simulation techniques and increasingly integrate with them (Jumper et al., 2021; Maia et al., 2020; Sliwoski et al., 2014).

## 1.3. The "Why AI?" Rationale

### 1.3.1. Bottlenecks in traditional methods

Hit identification is constrained by the size of chemical space and by the cost of HTS; even very large physical screens sample a minute fraction of what is possible. In silico ligand-based and structure-based virtual screening, guided by ML scoring functions, can triage millions of candidates to focus scarce experimental bandwidth where it has the highest expected value (Maia et al., 2020; Sliwoski et al., 2014). Lead optimization is a high-dimensional search in which medicinal chemists balance potency, selectivity, solubility, stability, and toxicity. Here, surrogate models accelerate design–make–test–analyze cycles by predicting properties, learning structure–activity relationships, and suggesting informative analogs; when coupled to active learning and Bayesian optimization, these models can reduce the number of iterations required to achieve a clinical candidate (Chen et al., 2018; Lavecchia, 2015; Sliwoski et al., 2014). ADMET uncertainty is a dominant driver of late attrition; predictive toxicology, metabolism, and exposure models can flag liabilities earlier and suggest structural fixes before costly studies commence (Lo et al., 2018; Sliwoski et al., 2014; Waring et al., 2015).

### 1.3.2. How AI addresses these bottlenecks

AI offers leverage in at least six ways. First, search and prioritization at scale: QSAR/DL models can score millions of virtual molecules rapidly to identify promising regions of chemical space, substantially reducing reliance on brute-force HTS (Maia et al., 2020). Second, representation learning: DL and GNNs learn task-relevant molecular embeddings that often outperform hand-crafted descriptors, improving generalization across tasks and scaffolds (Stokes et al., 2020; Yang et al., 2019). Third, generative design: VAEs, GANs, Transformer decoders, and RL can produce de novo chemotypes optimized for multiple endpoints prior to synthesis, enabling goal-directed exploration rather than random enumeration (Sanchez-Lengeling & Aspuru-Guzik, 2018; Zhavoronkov et al., 2019). Fourth, structure-based acceleration: accurate protein structure prediction (e.g., AlphaFold) broadens target coverage and improves docking and binding-site modeling when experimental structures are unavailable (Jumper et al., 2021; Senior et al., 2020). Fifth, multimodal integration: ML can combine chemical structures, high-content phenotypic images, transcriptomic and proteomic signatures, and clinical records into unified predictors that better support target selection, biomarker discovery, toxicity risk assessment, and patient stratification (Jumper et al., 2021; Stokes et al., 2020). Sixth, speed and cost reduction: when embedded into closed design–synthesis–assay loops, AI helps cut down the number of compounds synthesized and experiments run, lowering cost and compressing timelines while preserving decision quality (Maia et al., 2020; Paul et al., 2010).

These benefits have prospective support. Deep learning–based screening surfaced new antibiotic leads with unconventional scaffolds that were validated in vivo, demonstrating that data-driven models can traverse vast chemical spaces effectively (Stokes et al., 2020). Industrial reviews document cases where AI-guided workflows delivered higher hit rates, better property profiles, or accelerated cycles relative to historical baselines, while warning against overgeneralization without rigorous prospective tests (Chen et al., 2018; Mak & Pichika, 2019; Sellwood et al., 2018; Waring et al., 2015). AI outputs are hypotheses requiring orthogonal experimental validation; without careful curation, benchmarking, and prospective studies, models risk amplifying dataset biases or yielding non-generalizable leads (Chen et al., 2018; Lo et al., 2018; Mak & Pichika, 2019).

## 1.4. Data in AI-Driven Drug Design

### 1.4.1. Types of Data

AI systems in discovery are only as reliable as the data and representations they consume. Three broad data domains—chemical, biological, and clinical/real-world—feed contemporary pipelines, each with canonical encodings and characteristic pitfalls.

Chemical data can be represented as strings (e.g., the simplified molecular input line entry system, SMILES, or the IUPAC International Chemical Identifier, InChI), enabling sequence models and convenient data exchange, though sensitivity to canonicalization and syntax must be managed (Yang et al., 2019). Molecular graphs, which treat atoms as nodes and bonds as edges, are the native input for GNNs and message-passing neural networks that learn atom- and substructure-level interactions without fixed fingerprints (Stokes et al., 2020). Traditional fingerprints and physicochemical descriptors (e.g., extended-connectivity fingerprints, ECFP/Morgan) remain effective, particularly when paired with light-weight ML algorithms or hybrid descriptor+DL schemes (Lo et al., 2018; Sliwoski et al., 2014). Critically, the field has converged on shared benchmarks such as MoleculeNet, which curate tasks spanning quantum mechanics, physical chemistry, biophysics, physiology, and toxicity (e.g., QM9, ESOL, FreeSolv, Lipophilicity, PDBbind, PCBA, MUV, HIV, BACE, BBBP, Tox21, ToxCast, ClinTox, SIDER), with standardized splits and metrics and integration into open-source frameworks like DeepChem to support reproducible comparisons (Wu et al., 2018; Yang et al., 2019).

Biological data include macromolecular sequences and structures as well as high-content cellular phenotypes and omics layers. Protein and peptide sequences are now modeled effectively by language models—usually Transformer variants—that learn embeddings useful for structure prediction, function inference, and interaction modeling (Jumper et al., 2021; Vaswani et al., 2017). Three-dimensional structures, whether experimental (e.g., Protein Data Bank) or predicted, support docking, molecular dynamics, and structure-aware ML that uses pocket surfaces and interaction fields as features (Maia et al., 2020; Senior et al., 2020; Sliwoski et al., 2014). Phenotypic imaging readouts and transcriptomic signatures can be ingested directly by CNNs and other DL architectures to relate morphological changes to mechanism and target engagement (Chen et al., 2018; Korotcov et al., 2017).

Clinical and real-world data encompass EHRs, claims, clinical trial records, adverse event reports, and curated knowledge graphs. These sources enable patient-level outcome prediction, cohort selection, and safety signal detection but are highly heterogeneous and governed by privacy and regulatory constraints. Privacy-preserving approaches—such as federated learning—seek to leverage distributed clinical data without exposing protected health information (Jumper et al., 2021). Reviews of AI in development emphasize how repurposing, trial optimization, and post-marketing surveillance can benefit when such data are harmonized and linked with preclinical and chemical features (Doytchinova, 2022; Sellwood et al., 2018).

### 1.4.2. The Challenge of Data Curation and Quality

Heterogeneous labels and context dependence are pervasive. Nominally identical endpoints (e.g., biochemical inhibition, cellular viability, or toxicity) may differ by assay format, dose, exposure time, cell type, and readout technology; naively merging such datasets injects label noise and induces distribution shift, undermining generalization (Chen et al., 2018). Small, biased datasets are common for high-value endpoints like human toxicity or clinical efficacy, making transfer learning, multi-task learning, few-shot learning, and data augmentation attractive strategies to regularize models (Chen et al., 2018; Lo et al., 2018). Provenance and reproducibility demand rigorous documentation of data processing, careful metadata capture, and use of community benchmarks; scaffold-aware splits and external prospective evaluation help estimate true predictive power beyond random splits (Wu et al., 2018; Yang et al., 2019). Privacy and regulatory issues further complicate the use of patient-level data, motivating active research in federated learning and secure computation to unlock value safely (Jumper et al., 2021).

Practical remedies are well established: standardizing ontologies and identifiers (e.g., InChIKeys for molecules, UniProt for proteins), applying assay-aware label harmonization, building explicit uncertainty estimates into models, and tightly integrating computational cycles with prospective experiments. When AI is embedded into closed-loop discovery, prospective iterations provide corrective feedback that prevents drift and overfitting to historic biases (Chen et al., 2018; Jumper et al., 2021; Maia et al., 2020).

## 1.5. Synthesis and Forward Look

The traditional pipeline remains a necessary scaffold for translational therapeutics, but it was not built to contend with combinatorial chemical space, noisy biology, and the escalating evidence demands of precision medicine. AI augments this scaffold with representation learning (e.g., GNNs and Transformers), scalable prioritization, de novo generative design, and multimodal integration that target the most painful bottlenecks—hit finding and lead optimization—while de-risking downstream decision points. Real progress depends on data curation, validation in realistic splits, and prospective, experiment-coupled evaluation. Subsequent sections examine how specific AI techniques are deployed for target identification, activity and property prediction, de novo design, and clinical translation (Chen et al., 2018; Doytchinova, 2022; Jumper et al., 2021; Maia et al., 2020; Mak & Pichika, 2019; Sanchez-Lengeling & Aspuru-Guzik, 2018; Sellwood et al., 2018; Stokes et al., 2020; Waring et al., 2015; Wu et al., 2018; Yang et al., 2019; Zhavoronkov et al., 2019).


---

# 2. AI for Target Identification and Validation

## Abbreviations

AI, artificial intelligence; ML, machine learning; DL, deep learning; GNN, graph neural network; DTI, drug–target interaction; QSAR, quantitative structure–activity relationship; MD, molecular dynamics; MM-GBSA, Molecular Mechanics/Generalized Born Surface Area; PPI, protein–protein interaction; GWAS, genome-wide association study; eQTL, expression quantitative trait locus; scRNA-seq, single-cell RNA sequencing; ST, spatial transcriptomics; PCM, proteochemometrics; PAE, predicted aligned error; pLDDT, predicted local distance difference test; ADMET, absorption, distribution, metabolism, excretion, and toxicity.

## 2.1. Biomarker Discovery and Target Identification

Modern target identification starts from a causal hypothesis about disease biology and proceeds through multi-omic evidence aggregation, model-based prioritization, and prospective validation. The key question is not only whether a protein is associated with disease, but whether modulating it will produce the desired clinical effect without unacceptable toxicity. AI systems operationalize this by quantifying genetic and molecular support, integrating prior pharmacology, and learning structure in large, heterogeneous datasets (Chen et al., 2018; Vamathevan et al., 2019). Early systems-level work demonstrated that machine learning can distinguish morbid and druggable human genes by combining network topology, pathway membership, expression specificity, and subcellular localization (Costa et al., 2010). Recent pipelines extend this approach with representation learning over protein–protein interaction (PPI) graphs, tissue-resolved transcriptomics, and human genetics, producing target scores that correlate with downstream success (David et al., 2020; Gaudelet et al., 2021).

Genetic evidence is the highest-value signal for causality. Genome-wide association studies (GWAS) map disease-associated loci, but most hits are noncoding. AI models trained on DNA sequence learn regulatory grammar to predict variant effects on transcription factor binding and chromatin, enabling fine-mapping and colocalization with gene expression (Alipanahi et al., 2015; Angermueller et al., 2016). Network propagation then diffuses locus-level signals across PPI graphs to prioritize proximal proteins with convergent evidence (Gaudelet et al., 2021). The resulting candidates are ranked using calibrated classifiers with positives from known targets and carefully constructed negatives to avoid label leakage from literature bias (Vamathevan et al., 2019).

High-content phenotypic screens produce images or transcriptomic signatures that capture pathway states. Convolutional neural networks and graph-based encoders learn features predictive of target perturbation, including morphological embeddings that cluster compounds by mechanism of action. These features can be aligned with CRISPR knockout profiles to infer the proteins responsible for observed phenotypes, creating a mapping from phenotype to target space that complements genetics (Chen et al., 2018; Stokes et al., 2020).

### 2.1.1. Using ML/DL to identify novel disease-associated proteins and genes

A practical supervised workflow comprises: (i) assembling positives from approved or clinical-phase targets for the indication, deduplicated by gene and mechanism; (ii) constructing a candidate set from protein-coding genes filtered by expression in disease tissue; (iii) extracting features, including network centrality, shortest-path distance to disease modules, intolerance to loss-of-function, tissue specificity, ligandability proxies, and genetic burden; (iv) training gradient-boosted trees or deep models with stratified cross-validation; and (v) estimating calibrated probabilities and uncertainty via bootstrapping or deep ensembles (Gaudelet et al., 2021; Vamathevan et al., 2019). For diseases with known pathway architecture, graph neural networks (GNNs) aggregate neighborhood information and edge types to increase recall of pathway-coherent targets (Defferrard et al., 2016; Scarselli et al., 2008; Veličković et al., 2018).

Interpretability constrains adoption. SHAP values for boosted trees and attention weights for GNNs help decompose predictions into evidence items, e.g., GWAS colocalization, network proximity to a known effector, or tissue-specific expression. This evidence table can be reviewed alongside orthogonal literature and safety flags before advancing a target to experimental validation (David et al., 2020; Yu et al., 2018).

## 2.2. Analysis of Omics Data

### 2.2.1. Applying AI to genomics, proteomics, and transcriptomics to understand disease pathways

Genomics. Sequence-based deep learning models learn position-specific motifs and long-range interactions from raw DNA. They predict chromatin accessibility and transcription factor binding, enabling prioritization of noncoding variants that perturb regulatory programs. Downstream, statistical colocalization integrates eQTLs with GWAS to link variants to gene expression changes in relevant tissues. Combining these signals with PPI graphs produces disease modules whose enriched processes suggest intervention points (Alipanahi et al., 2015; Angermueller et al., 2016; Gaudelet et al., 2021).

Transcriptomics. Bulk RNA-seq provides differential expression, but single-cell RNA-seq (scRNA-seq) resolves cell-type-specific drivers. Representation learning aligns patient and control cells in a shared latent space to isolate disease-specific programs. Graph clustering over cell–cell similarity identifies perturbed subpopulations, while gene-set activity scores track pathway shifts that point to actionable nodes. Integration with perturbational atlases allows matching disease signatures to CRISPR perturbations, proposing targets whose knockdown reverts the signature (Angermueller et al., 2016; Chen et al., 2018).

Proteomics. Data-independent acquisition mass spectrometry quantifies proteins and post-translational modifications at scale. ML corrects batch effects, imputes missing values, and models kinase–substrate relationships from phosphoproteomic time courses. Joint models that fuse protein abundance, phospho-signaling, and interactome edges yield pathway-level activity scores, improving the precision of target nomination compared with any single modality (David et al., 2020; Gaudelet et al., 2021).

Multi-omic fusion. Two strategies dominate. Early fusion concatenates features followed by regularized learners with sparsity to select predictive modalities. Late fusion learns modality-specific encoders and combines their embeddings with attention or co-training, maintaining robustness to missing assays. Contrastive objectives align modalities and improve generalization to new cohorts (David et al., 2020; Wang et al., 2022). Pragmatically, cross-study validation and leave-tissue-out tests are critical to avoid optimistic bias (Vamathevan et al., 2019).

### 2.2.2. The Impact of AlphaFold on structural biology

AlphaFold2 transformed structural biology by predicting protein backbones and side-chain placements with near-experimental accuracy across much of the proteome (Jumper et al., 2021). The AlphaFold Protein Structure Database now hosts predicted structures for over 200 million proteins, vastly increasing structural coverage, accelerating annotation of domains and interfaces, and enabling structure-guided target triage where crystallography is absent (Kryshtafovych & Fidelis, 2009). Model-derived confidence metrics matter operationally: pLDDT distinguishes confidently modeled regions from disordered segments, while the predicted aligned error (PAE) matrix flags domain orientations with limited reliability. These diagnostics guide use in docking, epitope mapping, and variant interpretation.

For target validation, AlphaFold2 shortens cycles by enabling pocket detection, interface mapping, and mutational scanning in silico. When bound complexes are required, docking against AlphaFold models can be coupled to physics-based refinement or short molecular dynamics (MD) simulations to relax clashes, followed by MM-GBSA rescoring to prioritize plausible poses (Ganesan et al., 2017; Li et al., 2003; Wang et al., 2020; Xu et al., 2013). Geometric descriptors of cavities derived from alpha-shape and Delaunay triangulation correlate with ligandability and inform binding-site classification (Liang et al., 1998; Zhou & Yan, 2014).

Limitations remain: transient conformations, induced fit, membrane contexts, and multi-component assemblies can deviate from predicted monomeric structures. Complex prediction quality depends on coevolutionary signal and training distribution. Therefore, structural predictions should be treated as hypotheses and paired with orthogonal evidence, such as chemical proteomics, thermal-shift stabilization of target engagement, or CRISPR allelic series that test directionality of effect (Kryshtafovych & Fidelis, 2009; Vamathevan et al., 2019).

## 2.3. Network Pharmacology

### 2.3.1. Using graph-based AI models to map biological networks

Network pharmacology represents diseases, proteins, compounds, and phenotypes as a heterogeneous graph. Learning on this graph captures systems-level behavior such as pathway redundancy and polypharmacology. Classical label-propagation methods spread annotations along high-confidence edges, while modern graph neural networks (GNNs) learn task-specific message passing to combine node features with topology (Defferrard et al., 2016; Scarselli et al., 2008; Veličković et al., 2018). Deep architectures with residual connections and normalization enable very deep GCNs, improving long-range dependency capture (Li et al., 2019). In drug discovery, these models fuse chemical graphs of small molecules with protein sequence or structure embeddings to predict activities and safety liabilities (David et al., 2020; Gaudelet et al., 2021).

Representation choice is central. For molecules, message-passing neural networks operate on atom–bond graphs; for proteins, options include convolution over contact maps, language-model embeddings from sequences, and graph encodings of residue–residue proximity. MoleculeNet standardized benchmarks revealed that graph models outperform descriptor baselines on many biochemical endpoints when datasets are sufficiently large and splits are chemically meaningful (David et al., 2020; Wu et al., 2018). For targets, integrating disease-specific network context with intrinsic properties such as essentiality and tissue specificity improves precision of target nomination compared with naive degree-based heuristics (Gaudelet et al., 2021; Vamathevan et al., 2019).

### 2.3.2. Predicting complex target–drug interactions

Drug–target interaction (DTI) prediction spans binary interaction classification, affinity regression, and pocket-conditioned pose scoring. Kernel methods pioneered integrated chemical, genomic, and pharmacological kernels with matrix factorization to impute missing interactions (Gönen, 2012; Yamanishi et al., 2010). Deep models now learn end-to-end from sequences and SMILES or graphs. DeepAffinity unified recurrent and convolutional encoders to predict continuous binding affinity with interpretable attention maps (Karimi et al., 2019). Structure-based models such as AtomNet used 3D convolutional networks on protein–ligand grids to score poses, while multi-task DNNs improved QSAR accuracy across assays (Ma et al., 2015; Wallach et al., 2015).

Evaluation must reflect deployment. Temporal splits or scaffold splits reduce overestimation from analogue bias, while prospective validation on wet-lab assays or new chemotypes is the gold standard (David et al., 2020; Wu et al., 2018). For affinity regression, report Pearson r with confidence intervals; for classification, use PR-AUC in addition to ROC-AUC under class imbalance. Calibration curves and expected calibration error quantify probability quality and are essential when models prioritize experiments. Uncertainty can be estimated with deep ensembles or Monte Carlo dropout, informing risk-aware batch selection (Vamathevan et al., 2019).

Caveats include dataset shift across assay formats, label noise from heterogeneous thresholds, and shortcut learning on protein or ligand identifiers. Mitigations include multi-task learning across related assays, explicit assay embeddings, and controlled train–test splits that hide trivial shortcuts (David et al., 2020; Wu et al., 2018). In production, active learning couples DTI models with Bayesian optimization to choose diverse, uncertain compounds that maximize information gain while respecting medicinal chemistry constraints (Chen et al., 2018).

## 2.4. Predicting Target "Druggability"

### 2.4.1. Assessing how likely a biological target is to bind effectively with a drug molecule

Druggability models estimate whether modulating a target with a small molecule or biologic is feasible at acceptable selectivity and exposure. For enzymes and receptors, pocket geometry, hydrophobic enclosure, and the presence of aromatic or hydrogen-bonding hotspots correlate with ligandability. Alpha-shape analyses and Delaunay triangulation compute pocket volumes, mouth widths, and curvature, while residue-level descriptors capture side-chain flexibility and physicochemical complementarity (Liang et al., 1998; Zhou & Yan, 2014).

Physics-based components add mechanistic grounding. Docking provides approximate poses and scores that can be refined via short MD simulations to relax side chains, followed by MM-GBSA or related end-point free-energy estimators to rescore top poses (Ganesan et al., 2017; Li et al., 2003; Xu et al., 2013). When experimental structures are unavailable, AlphaFold2 models with high pLDDT in binding regions are usable starting points, with caution about loop placement and induced fit (Jumper et al., 2021; Kryshtafovych & Fidelis, 2009).

Proteochemometric (PCM) modeling complements structure by jointly encoding the ligand and a panel of related targets to learn family-level binding rules. This multi-task formulation improves extrapolation to understudied homologs and highlights selectivity determinants, which is critical for predicting off-target risks early (David et al., 2020; Qiu et al., 2017).

Empirical priors inform risk. Historical success is enriched among targets with human genetic support, secreted or extracellular proteins for biologics, and tractable enzyme classes. Conversely, ubiquitously expressed essential genes and proteins central to housekeeping complexes carry toxicity risk. AI systems incorporate such priors as features or Bayesian priors to calibrate expectations and to steer portfolios toward tractable biology (Chen et al., 2018; Vamathevan et al., 2019).

Validation closes the loop. Biochemical assays confirm potency and mechanism. Biophysical assays—thermal shift, SPR, CETSA—confirm target engagement in relevant matrices. Cellular assays test pathway reversal and on-target engagement. Genomic perturbations, including CRISPR knockouts or allelic series, test causality and direction of effect. Iterating predictions with experimental feedback turns druggability assessment from a static filter into a learning system (David et al., 2020; Vamathevan et al., 2019).

Quality and Reproducibility Considerations. Across subsections, the most common failure modes are data leakage, analogue bias, and non-representative splits. Adopt scaffold or temporal splits, document all preprocessing, and version datasets. Prefer external validation on independent cohorts or assays when feasible. Report hyperparameters, uncertainty estimates, and confidence intervals. Maintain traceable evidence for every promoted target so decisions remain auditable to clinicians and regulators (Pandey et al., 2022; Vamathevan et al., 2019; Yu et al., 2018).

---

# 3. AI for Drug Candidate Design and Screening

## 3.1. AI-Accelerated Virtual Screening

### 3.1.1. Molecular Representation: Inputting Molecules Into AI Models (SMILES Strings, Molecular Graphs, Fingerprints)

Advances in cheminformatics and artificial intelligence (AI) have introduced several approaches to molecular representation. Traditional methods rely on rule-based feature extraction, such as molecular descriptors that quantify physical or chemical properties, and molecular fingerprints that encode substructural information as binary strings or numerical values. The most common representation is the Simplified Molecular Input Line Entry System (SMILES), which provides a compact and efficient way to encode chemical structures as strings (Weininger, 1988; Wigh et al., 2022). Despite its simplicity, SMILES has limitations in capturing the complexity of molecular interactions. As drug discovery tasks become more sophisticated, traditional string-based representations often fail to fully reflect the relationships between molecular structure and key drug-related characteristics such as biological activity and physicochemical properties (Li et al., 2024). While traditional methods are interpretable, they often struggle to navigate the vast chemical space in search of compounds with desired biological properties. Therefore, molecular representation should not only encode the chemical structure, but also enable efficient exploration of chemical space. In recent years, AI-driven molecular representation methods have applied deep learning techniques to learn high-dimensional embeddings directly from large datasets. Models such as graph neural networks (GNNs), variational auto-encoders (VAEs), and transformers enable these approaches to move beyond predefined rules, capturing both local and global molecular features (Irwin et al., 2020; Kim et al., 2016; Mendez et al., 2019). These modern representations better describe structural and functional relationships, providing powerful tools for molecular generation, scaffold hopping, lead compound optimization, and other tasks in drug discovery (Li et al., 2024; Tong et al., 2021).

#### Molecular fingerprinting

Molecular fingerprinting is a computational technique that transforms chemical structures into compact numerical representations, such as bit vectors or feature arrays, to capture key structural and physicochemical properties. These fingerprints facilitate rapid comparison, similarity searches, and machine learning tasks, making them invaluable in drug discovery and materials science. Common types include circular fingerprints like Extended Connectivity Fingerprints (ECFP) for substructure patterns, path-based fingerprints for bond sequences, and 3D fingerprints for molecular shapes (Li et al., 2024). Unlike natural language processing (NLP), which processes human language, molecular fingerprinting encodes chemical "grammar," such as functional groups and bonds, rather than linguistic semantics. While natural language processing (NLP) models like transformers can analyze molecules via SMILES strings, traditional fingerprinting relies on cheminformatics algorithms for applications like virtual screening and toxicity prediction. Tools such as Open-Source Cheminformatics Toolkit (RDKit) and Chemical Descriptor Calculation Platform (ChemDes) (Dong et al., 2015) are widely used to compute fingerprints efficiently, bridging the gap between chemistry and AI. However, challenges remain in optimizing fingerprint methods for diverse molecular datasets and improving their predictive power in biological contexts. For instance, ECFPs have proven effective in structure-activity modeling and similarity searching but require further refinement to enhance their utility in identifying active compounds in large-scale screenings.

### 3.1.2. Predictive Screening (QSAR/QSPR): Using ML/DL to Predict Compound Activity and Properties Before Synthesis

AI-powered virtual screening and other in silico approaches have revolutionized the identification of potential lead compounds for drug discovery. These methods utilize computational techniques to rapidly evaluate vast chemical libraries, significantly accelerating the process and reducing costs compared with traditional high-throughput screening (Paul et al., 2021). Machine learning (ML) algorithms are essential for these methods. For instance, they can be used to create quantitative structure-activity relationship (QSAR) models, that predict the biological activity of compounds based on their chemical structures. These models can then be used to screen large chemical libraries and prioritize compounds with the highest probability of binding to the target of interest. These AI-driven approaches have the potential to significantly accelerate the identification of promising lead compounds and ultimately improve the success rate of drug development.

AI-driven techniques are revolutionizing drug development by optimizing critical properties, such as solubility, stability, and bioavailability. Machine learning (ML) algorithms can analyze vast datasets of chemical structures and their associated properties to predict crucial parameters with high accuracy. For example, in QSAR predictions, approximately 1000-5000 data points were used for water solubility predictions, whereas deep learning (DL) models can be used to predict drug stability under various conditions. For the protein function prediction task, researchers can leverage two open databases—the UniProt Consortium and the Protein Data Bank (PDB)—to gather protein sequence data from various species. This data can then be used to train prediction models through processes like batch downloading, data cleaning, and pre-processing. These predictive models enable researchers to rapidly identify and optimize drug candidates with improved physicochemical properties, thereby increasing their chances of successful clinical translation. Furthermore, deep learning (DL) algorithms, such as generative adversarial networks (GANs), can be used to generate novel chemical structures with desired properties, thereby expanding the chemical space explored in the drug design process.

### 3.1.3. AI-Enhanced Molecular Docking: Improving the Accuracy and Speed of Docking Simulations

Molecular docking is a crucial step to generate potential candidates for lead compounds in drug discovery (Vamathevan et al., 2019). Docking is composed of several steps, for example, binding pocket identification, drug conformations sampling, scoring, and ranking. Generally, the binding pocket is provided by users in re-docking, cross-docking and virtual-screening tasks, with the pocket being identified by the co-crystal structure of the target protein and associated ligands in the experiments. However, with the development of protein structure prediction methods, for example, AlphaFold (Jumper et al., 2021) and ColabFold (Mirdita et al., 2022), a fast increasing number of protein structures are generated without information on ligands. Therefore, it is of high demand to perform reliable ligand docking based on protein structures only and without known binding pockets.

Traditionally, the blind docking is regarded as a task of docking around the entire protein, and many traditional docking programs are available for such tasks, for example, Autodock Vina (Trott & Olson, 2010), and Glide (Friesner et al., 2004). It is of great value to improve the docking speed and accuracy, given that normally a large space should be sampled in limited searching steps. To deal with such a problem, a number of optimized sampling methods were developed, for instance, QuickVina-W, which was developed based on QuickVina 2. QuickVina 2 optimized the local search frequency by searching only potentially important spatial points. These spatial points are identified by checking gradients of the scoring function against a thread history before local optimization. QuickVina-W is a program designed for blind docking, and the potentially significant points are identified by examination of the history of the present and other threads.

Besides the improvement on the sampling method, another strategy to increase speed and accuracy is to decrease the searching space through an identification of the potential ligand-protein binding pockets. Methods based on both traditional geometrical or machine learning strategies have been developed to recognize the protein pocket. The traditional methods have a relatively long history, and have observed the development of various strategies. For example, in FunFOLD and COFACTOR, the binding pocket is located by calculations on the similarity between the target and the templates of known pockets. Methods such as Fpocket on the other hand, are based on an examination of the shape and spatial geometry of the target protein. In another strategy one performs the binding pocket search using designed probes and identifies the pocket by calculating the interaction energy between the probes and protein.

In addition to the traditional methods, the strategies based on machine learning began to show high performance for the binding site prediction over the last few years. Among them, P2Rank (Krivák & Hoksza, 2018) is a widely used method based on the random forest algorithm, while COACH is trained by the support vector. In these methods based on deep learning, Three-Dimensional Convolutional Neural Network (3D-CNN) are often used, as in DeepSite (Jiménez et al., 2017), DeepSurf, and PUResNet.

Besides binding site prediction, many studies focused on combining the site recognizing, pose sampling and scoring in one shot to improve the performance of blind docking. EquiBind is a popular method among them, which applies an SE(3)-equivariant geometric deep learning strategy and successfully decreases the runtime of docking to less than 1 second per system. In addition, TANKBind, another deep learning-based method using trigonometry-aware neural networks, replaces the expensive sampling by evaluation of the protein-ligand interaction energy landscapes of different blocks of protein, which further improves the performance in docking tasks.

Recently, another state-of-the-art approach, DiffDock (Corso et al., 2022), was reported which is based on deep learning and treats the docking as a generative task. DiffDock used diffusion generative model to generate conformations and applied a confidence model to estimate the poses. This method enjoys a significant improvement in the docking accuracy, representing a powerful intermediate approach between traditional sampling and one-shot prediction.

The score function, which is commonly used to estimate the confidence of ligand binding poses, is another important factor affecting the accuracy of blind docking. There are four main categories of scoring functions, namely, physics-based, knowledge-based, empirical, and machine-learning based scoring functions. Many efforts have been paid to improve the performance of score functions, for instance, SMINA, GNINA (Francoeur et al., 2020), RF-Score, and IGN. Most of these methods are based on linear regression or machine learning, and present a reasonable performance in estimating the interactions between the proteins and ligands. However, most of the machine-learning based strategies are not introduced directly into the molecular docking procedure in the form of the scoring function, but are used to rescore the poses of ligands generated by the traditional sampling methods. Because a high computational cost is required when the network is used to guide the sampling, implementing a rescoring process after the sampling is a common strategy to improve the accuracy of the latter, as in GNINA.

In the present work, to improve the speed and accuracy of blind docking, researchers developed a method, Deep Site and Docking Pose (DSDP), to combine the advantages of both machine learning and traditional sampling strategies. It predicts the binding site on the protein and provides the potential location of ligands to decrease the searching space for the following binding pose sampling. A similar strategy was used in EquiBind, DiffDock (Corso et al., 2022), and Uni-Dock. In these protocols, the binding site identification and ligand conformation sampling are treated separately, and only the predicted site center is used in the sampling step by ignoring the shape of the binding pocket.

## 3.2. De Novo Drug Design

### 3.2.1. Definition: Using Algorithms to Design Entirely New Molecules From Scratch

De novo molecular design aims to create new chemical entities with desired properties and/or activities. These properties may be easily quantifiable, such as molecular weight, or somewhat more abstract, as is the case of toxicity. This is an inherently difficult task owing to the immense search space of around 10^33 to 10^80 feasible molecules from which only a small fraction typically have the desired traits (Polishchuk et al., 2013). As such, de novo molecular design was, for many years, and mostly remains a process of almost exclusive trial and error, with human expert knowledge and intuition about chemistry playing a major role (Schneider, 2018). Meanwhile, the high costs associated with developing new molecules, reaching $2.8 billion dollars for a single compound, have also led to the implementation of computational tools capable of assisting the process. These have proven valuable and have found wide usage in practical applications (Schneider, 2018).

A forthright approach consists in enumerating all possible molecules that conform to valency rules and do not include chemically unstable functional groups. A notable example is the Chemical Space project, where this technique was employed to generate 166 billion molecules. Another technique, reaction-based de novo design, uses a set of known chemical reactions to combine various readily available building blocks into new molecules. This process can be guided by a similarity criterion to a known molecule of interest, giving rise to a large number of new similar molecules while ensuring their synthetic plausibility.

Evolutionary Algorithms (EAs) have also been successfully applied to de novo molecular design. As a recent example, AutoGrow4 uses an EA to create new predicted ligands. At each iteration, new molecules are created using a mutation operator, that performs an in silico chemical reaction, or a crossover operator that merges two compounds into a new one by randomly combining their decorating moieties. Grammatical Evolution on string representations and evolving molecular graphs provide alternative approaches that enable EAs to generate novel compounds targeting desired properties.

Although useful, these methods still leave room for improvement. For instance, enumeration often leads to molecules that are too difficult to synthesize, and reaction-based design is fundamentally restricted in its ability to explore the chemical space, both important aspects of molecular design. EAs, while computationally efficient and capable of performing on par with other recent approaches, rely on expertly encoded operations, possibly limiting the search space and not leveraging the large amounts of data currently available. Notwithstanding previous efforts on reviewing this field, a more rigorous approach to this subject, containing a more systematic coverage of the methods, can be important for researchers working on these topics. To that end, here we aim to provide a comprehensive review of deep learning (DL) methods for the targeted generation of novel compounds. As such, after an introduction to molecular representations, we present the most common deep generative models and the underlying neural network architectures. Researchers then focus on the different optimization approaches that allow to focus the search on molecules with desired properties or activities, closing with a review of the main practical applications (Gómez-Bombarelli et al., 2018).

### 3.2.2. Challenges: Navigating the Immense Size of Chemical Space

Creating new de novo molecules is an inherently difficult task owing to the immense search space of around 10^33 to 10^80 feasible molecules from which only a small fraction typically have the desired traits (Polishchuk et al., 2013). As such, de novo molecular design was always challenging. Despite all this progress and investment, only a few AI-based drugs are actually in human clinics. Moreover, the cost of developing a drug is still increasing and there is less adoption of AI tools for clinics at the moment. The pharmaceutical industries are one of the riskiest industry in the world, due to high failure rates and a long timeline.

Many traditional drug design scientists still think that all AI-enabled drug development is incremental and hype. The de novo design, drug response analysis, molecule optimization, and screening all are stages but most of the drug candidates fail in the clinical trials, making all of the developments incremental. Researchers have a very complex biological space, complex chemical space, and complex clinical space, and optimizing all of them at once is a big challenge.

### 3.2.3. The Role of Deep Learning: Introducing Generative AI as a Solution

Generative AI tools such as ChatGPT hold significant potential in healthcare education and clinical practice. In pharmacy, they could enhance efficiency by assisting with prescription reviews, drug interaction checks, and adverse reaction monitoring, ultimately improving patient care. However, their application in pharmacy education remains under-explored, with limited research on implementation challenges, underscoring the need for further investigation.

Beyond assisting in clinical tasks, generative AI can also synthesize large datasets to train predictive models, expanding its utility in medical research. Among these AI techniques, GANs stand out as a powerful DL framework composed of two competing neural networks—a generator that creates synthetic data and a discriminator that evaluates its authenticity. Through iterative adversarial training, the generator refines its outputs to produce highly realistic data, enabling applications in medical imaging, super-resolution, and data augmentation. For example, Super-Resolution GAN has demonstrated success in enhancing low-resolution images, proving valuable in medical diagnostics and video surveillance.

Moving forward, realizing the full potential of Large Language Model (LLM) driven biotechnology will require establishing rigorous performance benchmarks, enhancing model transparency, and fostering deeper collaboration between computational and life science communities. This technological convergence promises to fundamentally reshape research methodologies and industrial processes across the biological sciences.

### 3.2.4. Key Models and Tools: Variational Auto-Encoders (VAEs), Generative Adversarial Networks (GANs), and Transformers

Recently, generative deep learning (DL) has emerged as a promising development for de novo molecular design, where deep neural networks are employed as generative models. This specific application has attracted considerable attention, with several novel architectures being proposed, that are briefly reviewed next.

**Recurrent Neural Networks (RNNs)** assume a sequential structure in the data, one where a sample is composed of a set of steps. This assumption is implemented by processing an input consecutively and introducing a connection carrying the output from previous steps into the current step. However, as the number of steps increases, RNNs can suffer from vanishing or exploding gradients during back propagation, impairing the training process and making the learning of long-term dependencies extremely difficult. In practice, this is handled by using specialized units such as gated recurrent units (GRUs) or Long Short-Term Memory (LSTM) (Hochreiter & Schmidhuber, 1997) which introduce gates, learnable parameters controlling the flow of information through the steps.

**Generative Adversarial Networks (GANs)** define a pair of networks, a generator, and a discriminator, trained in competition with each other. The generator is intended to transform random noise into real looking data and is trained to maximize the synthetic samples classified as real by the discriminator. Meanwhile, the discriminator is trained to better discern between generated and real data. The training framework resembles a competition, with both networks constantly improving and adapting to each other.

**Auto-encoders (AEs)** are neural networks trained to copy their input into the output with restrictions imposed as to not simply learn the identity function. They are usually thought of as two separate parts, an encoder that transforms the input into a more compact latent state, and a decoder that reconstructs the input from this representation. Both are trained together to minimize the information lost from reconstructing.

**Variational Auto-encoders (VAEs)** are a special type of AE, which assume that the data was sampled from an arbitrary statistical distribution. The encoder transforms its input into the parameters of a multidimensional statistical distribution, that is, a set of means and standard deviations. A sampling then occurs, where a point is drawn from the encoded distribution and fed into the decoder that reconstructs it into the original input. The objective function used for training consists of a term penalizing reconstruction errors and a term restricting the parameters encoded to be close to a normal distribution. This stochastic process acts to regularize the network while constraining the encoded parameters close to those of a normal distribution helps in forming a useful latent space (Kingma & Welling, 2014).

**Adversarial Auto-encoders (AAEs)** are an alternative to VAEs that employ adversarial training for structuring the latent space. In particular, the encoder transforms its input into a single point in the latent space. A discriminator network then attempts to discern between samples of a prior statistical distribution and encoded points. As such, the encoder can also be viewed as a generator engaged in a competition with the discriminator, ultimately balancing between the reconstruction and adversarial error.

**Generating Molecules:** There have been several approaches to applying generative deep learning (DL) to molecular generation, mainly differing on the chosen molecular representation. As such, usually more than one method surfaced for generating each of the main representations discussed in section. Borrowing from the natural language processing field, molecules can be generated as sequences, such as SMILES, by using RNNs. Specifically, when using RNNs as a generative model, each token in the string is encoded as a one-hot vector and the network is trained to predict the next character in the sequence. The generation of new data is achieved by running the network auto-regressively, that is, using its output as the input for the next time-step. This process is usually seeded with a special start token and the generation of a molecule ends when a special stop token is sampled. These two tokens are also respectively prefixed and appended to each molecule during training.

Several research groups have employed this method with a stacked RNN, usually with Long Short-Term Memory (LSTM) cells, leading to good rates of validity, novelty, and diversity (Gupta et al., 2018; Olivecrona et al., 2017; Segler et al., 2018; van Deursen et al., 2020). More complex architectures such as Variational Auto-encoders (VAEs) and Generative Adversarial Networks (GANs) have also been employed to generate molecules as strings; however, these also employ a RNN for the sequence generation process, either as the decoder or the generator (Gómez-Bombarelli et al., 2018; Guimaraes et al., 2018; Lim et al., 2018). Despite some limitations of sequence-based approaches, such as the need to learn a complex syntax and the mismatch between the edit distance of two SMILES and the underlying molecular similarity, these methods have produced impressive results.

### 3.2.5. Impact: Drastically Accelerating the Design of Novel and Optimized Molecules

AI-based methods are being adopted in the health care industry where low-cost, intelligent, and flexible methods are affecting areas such as drug design, support for clinical decision making, diagnosis, prevention, and making clinical recommendations (Kempt & Nagel, 2022). AI applications were previously thought to be inferior to experimental high-throughput screening, combinatorial chemistry, and other technical drivers. It was difficult to create new chemical entities using computer programs, with desired features from the ground up, potentially even better than a human expert (Schneider, 2021).

The long and costly process of drug design can be accelerated by employing data science methods for target identification, de novo molecular design, drug repurposing, retrosynthesis and prediction of reactivity and bio-activity, FDA approval, and post-market analysis. AI has been implemented by some pharmaceutical organizations, with revenue from AI-based solutions in the pharmaceutical sector estimated to reach US $2.199 billion by 2022 (Paul et al., 2021). Deep neural networks (DNNs) can be used to boost prediction power when inferring the properties of small molecules, and one-shot learning can be used if a large amount of experimental data is not available.

Understanding technical and human errors, labeling constraints, and biological variability associated with the underlying data is crucial to create useful predictive models. It is difficult to represent the experimental data in numerical or computer-assisted form. AI is now being utilized to create representations of trials that allow for data categorization and, ultimately, the development of predictive models. Great things happen in minds and are never done alone, AI is delivering only a platform to execute the plans. Researchers need to develop novel hypotheses for drug discovery by employing the knowledge from different domain experts. After that, researchers can design a data analysis algorithm, and then researchers can learn from the data to modulate the hypothesis or modify the algorithms. In short, both mind and machine need to work in synergy.

Researchers hope that the use of machine learning, especially deep learning, will increase in the future and help us understand complex biological systems, generate particles with the desired properties, and lead to semi-automated smart healthcare systems. Researchers also expect that AI would be a valuable tool in understanding human biology, a catalyst in combating human diseases and will accelerate drug design. In terms of drug discovery, quality, and safety are more important than speed and cost, devising an AI system that can meet this multi-objective optimization in a multi-dimensional complex space is a huge challenge, which needs collaborative efforts from multiple disciplines in academia and industry.


---

## 3.3. AI in ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity) profiling

### 3.3.1. Predicting pharmacokinetics and pharmacodynamics

The key concepts of pharmacology include pharmacokinetics and pharmacodynamics. While pharmacodynamics focuses on how a drug works in the body and how it affects other systems in the body, pharmacokinetics deals with the study of drug absorption, distribution, metabolism, and elimination (ADME) (Zhavoronkov et al., 2020). The application of AI techniques in pharmacokinetics and pharmacodynamics has created new opportunities to improve drug development and personalized treatments. It can analyze complex datasets, identify trends and make predictions that could improve patient outcomes, improve drug delivery and minimize side effects.

Machine learning (ML) and deep learning (DL) techniques are widely used to predict pharmacokinetic parameters. Numerous ML techniques—including Bayesian model, random forest (RF), support vector machine (SVM), artificial neural network (ANN), and decision tree—have been used to predict the ADME of drugs. To predict various pharmacokinetic parameters such as drug absorption, bioavailability, clearance, volume of distribution, and half-life, DL algorithms such as Convolutional Neural Networks (CNN), Long Short-Term Memory (LSTM), and recurrent neural network (RNN) are often used. A computational method called quantitative structure-activity relationship (QSAR) uses the chemical structure of a molecule to predict its biological activity.

With improved training data, a 47th version of admetSAR 2.0 is now available. This program also includes a module called ADMETopt, which is used to optimize lead activity based on expected ADMET attributes (Yang et al., 2019). AI techniques facilitate the modelling of drug-receptor interactions and the prediction of drug efficacy and toxicity in the field of pharmacodynamics. The use of AI in pharmacokinetics and pharmacodynamics can significantly accelerate the drug discovery process and improve precision medicine.

Obrezanova et al. used conventional ML techniques and multitask convolutional neural networks to calculate time-dependent pharmacokinetic profiles and nine in vivo pharmacokinetic parameters in rats (oral and intravenous administration) based on in vitro measured ADME properties and molecular chemical structures of 3000 different compounds. Ye et al. used transfer learning and multitasked learning to pre-train the model on over 30 million bioactivity data. The model was then used to estimate four human pharmacokinetic parameters: oral bioavailability, plasma protein binding, Volume of Distribution (Vd), and half-life, for 1104 FDA-approved small-molecule drugs. Compared to other traditional ML techniques, their DL model showed the highest performance (although not always by a significant margin) and generalization ability, achieving a mean absolute error (MAE) = 0.31 for oral bioavailability and MAE = 0.17 for volume of distribution (Vd).

Interestingly, Lou et al. created a model that predicts the bioavailability of monoclonal antibody (mAbs) administered through subcutaneous preparation in humans. A dataset of 45 clinical mAbs—with sequence and structure-based features including isoelectric point, total charge, aggregation propensity, solubility score, surface hydrophobicity spots, positive charge, and negative charge (with a threshold of 70% bioavailability)—were used to build a classification model. The study used a range of traditional Scikit-Learn ML techniques such as Adaptive Boost, Multilayer Perceptron, random forest (RF), and support vector machine (SVM). Among them, the tree approach showed the highest accuracy, reaching 78%.

Two areas that benefit greatly from the implementation of AI algorithms are drug design and optimization. De novo design, virtual screening, and structure-based drug design are just a few examples of these algorithms. The application of AI to drug development and optimization has a transformative impact on the discipline, enabling the rapid discovery of new therapeutic candidates and the more targeted and effective exploration of chemical space. Using ML, DL, and computer modelling methods, AI models can provide accurate predictions about the properties, interactions, and behaviours of potential drug candidates.

### 3.3.2. Using multi-task learning to create comprehensive safety profiles

The stringent safety requirements associated with drug development make it challenging to introduce new drugs to the market. Clinical trials often fail due to unexpected toxicity and post-marketing safety issues, resulting in unnecessary morbidity and mortality. Clinical trials test the safety and effectiveness of a drug before it is approved while pharmacovigilance continually verifies a drug's safety information during its usage in patients.

The establishment of pre-market drug safety has been shown to benefit significantly from the use of AI-based approaches, particularly in the area of toxicity assessment. The vast reach of AI helps to predict the side effects, therapeutic targets, and in vivo safety of chemicals before manufacturing. Usually, after designing of the small molecule, the assays are employed to predict off-target toxicity, genotoxicity, organ toxicity, cytotoxicity, and mitochondrial toxicity. The analysis of new types of data, including gene expression and cell imaging data, combined with knowledge of chemical structure, can now be used to predict the effects of in vivo toxicity.

Various in silico calculation methods have proven useful in calculating the toxicity of drug candidates. These methods, which include target-based predictions and QSARs, evaluate multiple pharmacological properties to predict toxicity. Various drug safety effects—such as skin/eye irritation, tissue-specific toxicity, and 50% lethal drug dose (LD50) values—were modelled using QSAR techniques. In particular, the QSAR model allows for examining the relationship between multiple predictors (e.g., molecular features) and responses (e.g., biological activities such as binding affinity). Early QSAR approaches assessed the chemical properties of drug candidates using multivariate linear regression. Due to their excellent prediction accuracy, robustness, and readability of ensemble techniques such as random forest (RF) and support vector machines (SVMs), they are currently the most popular options. Compared to Naive Bayes, k-Nearest Neighbour (k-NN) and RF algorithms, SVM showed better performance in predicting activity values in the latest QSAR modelling of histone deacetylase (HDAC) inhibitors. In addition, with the help of such QSARs, it is possible to predict activity based on objectives such as toxicity.

Recently, Minerali et al. created and compared ML algorithms to predict drug-induced liver injury (DILI) using the company's Assay Central software. To do this, they used data previously collected by research teams at Pfizer and AstraZeneca, as well as data from the FDA. The best Bayesian model based on the DILI problem category from the DILI Rank database produced results with a receiver operating characteristic curve (ROC) of 81%, a sensitivity of 74%, a specificity of 76%, and an accuracy of 75%.

Williams et al. used ML to predict DILI with the pharmaceutical company, AstraZeneca. They were able to quantify the risk of an association being classified as low, medium, or high with an accuracy of 63%. The model provided an accuracy of 86%, a sensitivity of 87%, a specificity of 85%, a positive predictive value of 92%, and a negative predictive value of 78% for binary (yes/no) DILI prediction.

In addition to developing in silico models for eye irritation/eye corrosion (EI/EC) using ML techniques and molecular fingerprints, Verma & Matthews combined quantitative structure-toxicity relationship (STR) models by ANN to produce 88% sensitivity and 82% specificity for EI; and 96% sensitivity and 91% specificity for eye corrosion (EC). Manually gathering data for training from X-Mol and ChemIDplus yielded 95% accuracy for EI and 96% for EC.

Using data on the transcriptional and molecular profiles of over a thousand drugs—35% of which have known cardiotoxicities—Mamoshina et al. employed ML to predict various drug-induced cardiotoxicities. The dataset was selected from a wide range of open-source knowledge and data sources (including DrugBank), with the best predictor achieving an average of 79% for safe vs. risky drug area under the curve (AUC) and 66% for an unknown set of drugs. AUC (80%) indicated specific cardiotoxicity for specific drug classes and AUC (76%) indicated heart failures with potential for anti-neoplastic drugs across all investigated drug categories.

Webel et al. achieved greater than 70% cytotoxicity prediction accuracy using a DL strategy developed from an internal dataset of more than 34,000 compounds with less than 5% cytotoxic chemicals. When applying this technique to new compounds, care must be taken to carefully consider the scope of the model. However, one of the advantages of this method is the use of cytotoxicity maps that provide the visual meaning of the substructures of different chemicals.

Hunta et al. developed three ML methods based on SVM, k nearest neighbour (kNNs), and neural networks to predict drug-drug interactions (DDIs) in non-communicable diseases (NCDs). Using data from DrugBank, they combined the functions of transport proteins and enzymes and compared the results of different methods using five-fold cross-validation. This allowed them to determine which two NN layers performed best and predict NCDs based on pharmacokinetic mechanisms with an accuracy of 83% (F-measure 85.23% and AUC 90%).

---

# 4. Real-World Impact, Challenges, and Future Landscape

## 4.1. Pioneering Platforms and Real-World Case Studies

### 4.1.1. DeepMind's AlphaFold: Revolutionizing Structural Biology

The Pinnacle of Protein Language Modeling. The rise of Transformer models has fundamentally transformed how computers process sequential data, moving from older methods like Recurrent Neural Networks (RNNs) to highly efficient, parallel processing via the self-attention mechanism. This revolution, driven by models like Bidirectional Encoder Representations from Transformers (BERT), generative Pre-training Transformer (GPT), and Text-to-Text Transfer Transformer (T5), has extended powerfully into computational biology, giving rise to Protein Language Models (PLMs) (Zhang et al., 2023).

PLMs apply the transformer architecture to biological sequences, treating a protein's amino acids like the "alphabet" of a language. By training on vast protein databases, these models have enabled breakthroughs in function annotation, protein design, and mutation effect prediction, but their most transformative success lies in protein structure prediction.

AlphaFold2 stands as the definitive example of this progress. It utilizes the transformer architecture to predict a protein's 3D structure from its amino acid sequence with exceptional speed and accuracy. This capability, achieved by decoding the protein's "language," has solved a decades-old grand challenge in biology.

While researchers use Natural Language Processing (NLP) algorithms to mine scientific literature, patents, and Electronic Health Records (EHRs) for drug candidates and targets (Agarwal & Searls, 2008; Kosonocky et al., 2024), the structural insight provided by AlphaFold2 is a direct, critical input.

Other benefits of PLMs include the use of pretrained models like Evolutionary Scale Modeling 2 (ESM-2) which, for example, uses 15 billion parameters to predict protein structures (Lin et al., 2023) and ProtGPT2 for transfer learning, as well as leveraging unsupervised learning from databases like UniProt. Models like OmegaFold (Wu et al., 2022) further enhance this by incorporating geometric awareness using 3D structural data.

Despite AlphaFold2's groundbreaking success in structure prediction, challenges remain, including high computational costs and the difficulty of interpreting complex AI output (Bepler & Berger, 2021; Ferruz et al., 2022). Nevertheless, its achievement in using the transformer architecture to map sequence to structure highlights the profound potential of AI to accelerate scientific discovery.

#### 4.1.1.1. Its Role in Accurately Predicting 3D Protein Structure

The groundbreaking AI system AlphaFold2 is celebrated for its ability to predict protein structure with exceptional speed and accuracy. This represents a major scientific advance in understanding the fundamental building blocks of life.

However, translating this high-accuracy prediction into the complexity of the in vivo (living system) situation remains an open challenge.

There are specific limitations when applying AlphaFold2 directly to traditional medicinal chemistry:

Unbound Structures: AlphaFold2 is trained primarily to predict unbound protein structures (proteins alone), whereas most drug discovery efforts require structures of protein-small molecule complexes (AlQuraishi, 2020).

#### 4.1.1.2. Impact on Structure-Based Drug Design

Predicting the three-dimensional structures of potential target proteins, solely from their amino acid sequence, is often necessary for drug discovery. AI systems had a major recent success in this, with AlphaFold2 (Jumper et al., 2021) winning the Critical Assessment of Structure Prediction (CASP14) (Moult et al., 2014). This structural biology advance is projected to fundamentally transform personalized medicine and drug discovery. AlphaFold represents a pivotal leap forward in leveraging Artificial Intelligence (AI) within structural biology and the broader life sciences (Nussinov et al., 2022). AlphaFold predicts protein structures with remarkable accuracy. This effectively tackles a persistent challenge in biology, as having precise protein structure predictions is vital for both understanding how diseases work and finding promising drug targets (Jumper et al., 2021).

### 4.1.2. End-to-End Generative AI Platforms: Insilico Medicine

#### 4.1.2.1. Overview Of Their Pharma.AI Platform (Pandaomics For Target Identification, Chemistry42 For De Novo Molecule Generation)

The AI drug discovery journey began with Insilico Medicine, which published one of the first methods using a deep learning approach to discover new targets (Wang et al., 2017; West et al., 2018).

This has since evolved into combining classical bioinformatics with advanced AI for disease mechanism reconstruction and target identification (Pun et al., 2023).

A key recent advance is the use of tools like AlphaFold to explore targets previously inaccessible for small molecule development. The resulting de novo design of active molecules for these difficult targets has been validated in both in vitro and in vivo assays (Ren et al., 2023; Zhu et al., 2023).

**The PandaOmics platform** leverages these and other rapid developments in computer-aided drug discovery, specifically incorporating large language models and robotics to accelerate the process (Schneider, 2018; Urban et al., 2023). **The PandaOmics platform** is a sophisticated, AI-driven engine designed for Therapeutic Target Identification. Its core feature is a user-friendly meta-analysis dashboard that produces a highly refined, ranked list of potential target genes.

This robust ranking is achieved by utilizing 23 distinct disease-specific models, which fall into two primary, complementary categories:

1. **Omics-Based Models (Data-Driven Insight):**
   These techniques integrate comprehensive data from the meta-analysis, including gene expression, methylation, proteomics, and genetic information. They are further enriched by network analysis using biological graphs from Protein-Protein Interaction (PPI) and signaling databases and knowledge graphs derived from scientific literature.
   - **Simpler Approaches**: These include standard bioinformatic approaches like the expression score, which provides a foundational assessment of gene significance based on differential expression in disease versus control samples in relevant tissues.
   - **Advanced Techniques:** This group employs complex machine learning, such as the heterogeneous graph walk algorithm. This algorithm performs a guided random walk on a graph where nodes represent genes and diseases. By learning the relationships between these nodes, the model identifies gene nodes with the closest association to the reference disease, enabling the discovery of new targets.

2. **Text-Based Models (Literature & Trend Analysis):**
   These models assess potential targets based on information extracted from textual sources, including publications, clinical trials, and grant applications. Crucially, they factor in the credibility of the source and current scientific trends to gauge the target's industry relevance and novelty.

In essence, PandaOmics synthesizes evidence from both high-dimensional biological data (Omics) and global scientific literature (Text) to deliver a holistic and prioritized set of therapeutic hypotheses (Pun et al., 2022).

**AI Capabilities and Validation of the PandaOmics Platform**

The PandaOmics platform offers a comprehensive set of AI capabilities for discovering therapeutic targets and developing biomarkers. The platform achieves this by utilizing dynamic omics data and advanced algorithms to power data exploration, pathway analysis, and meta-analysis, ultimately deepening the insights gained from datasets.

PandaOmics provides a highly user-friendly interface that includes customizable ranking approaches and filters, enabling researchers to precisely refine their gene lists based on various criteria. The platform's utility is further extended through integration with a robotic lab, which boosts the efficiency and accuracy of validating targets and screening compounds. By harmonizing diverse data sources and employing advanced language models, PandaOmics equips researchers to make better, more informed decisions in their pursuit of novel therapeutics and biomarkers.

**Predictive Model Validation**

The PandaOmics target discovery engine has undergone rigorous validation to confirm its effectiveness in identifying novel targets. Two core metrics were used to measure the performance of its predictive models.

1. **Enrichment Log Fold Change (ELFC):** This metric represents the log-transformed fold change of enrichment. It quantifies the degree to which the top-ranked genes in a list are enriched with known targets.

2. **Hypergeometric P-Value (HGPV):** This metric measures the statistical significance of the enrichment effect. It indicates the likelihood of achieving the same level of enrichment if the genes were listed randomly.

For a ranking approach to demonstrate higher predictive power, it must achieve higher values for both ELFC and HGPV. All models within PandaOmics have been thoroughly validated using these ELFC and HGPV coordinates, both generally and across specific therapeutic areas (Pun et al., 2022).

**Chemistry42: The AI-Driven Platform for De Novo Molecular Design**

Chemistry42, a platform that has evolved significantly over the past years (Zhavoronkov, 2022), is now routinely and successfully employed at Insilico Medicine, serving as the engine to drive the drug discovery process across several therapeutic areas.

**Designing Generative Experiments**

Users initiate the design of novel molecules through Chemistry42's user-friendly web-based interface. Experiments can be configured using either Ligand-Based Drug Design (LBDD) or Structure-Based Drug Design (SBDD), depending on the available information for the target of interest.

LBDD requires a 2D or 3D ligand structure as input (via .sdf file, Simplified Molecular Input Line Entry System (SMILES) string, or sketched directly). A pharmacophore hypothesis can also be manually or automatically added.

SBDD requires the upload of a prepared protein target structure (.pdb file), which can be in the apo format or already complexed with a ligand. Users can either define the pocket around a known ligand or select a site identified by the Pocket Scanner Module. A pharmacophore hypothesis can also be included.

To complete the experiment setup, users define acceptable ranges for numerous properties (like physicochemical properties and diversity), prioritize the reward modules by adjusting their weights, and set corresponding thresholds to control how restrictive the modules are. Advanced options in both workflows allow for fine-tuning the reward modules and selecting specific generative models. For quick configuration, the Autoconfiguration feature adjusts all parameters automatically based on the input data (Naumov et al., 2023).

**Enhancing Workflows with Anchor Points**

Workflows such as hit expansion, hit-optimization, and Fragment-Based Drug Design (FBDD) are supported through the Anchor points functionality. Anchor points allow users to fix specified cores or R-groups of a hit molecule in 3D space while the generative experiment varies the rest of the structure. This feature also supports multiple reference substructures by allowing users to edit atom types to include alternatives (e.g., specifying whether to see nitrogen or carbon in an aromatic ring using SMILES Arbitrary Target Specification (SMARTS)) (Naumov et al., 2023).

**The Power of Ensemble AI**

The platform's generative pipeline employs an asynchronous ensemble of proprietary generative models. This carefully curated collection includes over 40 generative models with diverse architectures—including generative autoencoders (Polykovskiy et al., 2018; Zhavoronkov et al., 2019), generative adversarial networks (Kadurin et al., 2017; Putin et al., 2018), flow-based approaches (Kuznetsov & Polykovskiy, 2021), evolutionary algorithms (Devi et al., 2015), and language models (Segler et al., 2018).

These models utilize different molecular representations (string-based, graph-based, and 3D-based) and are deployed strategically to maximize the platform's efficiency. By facilitating the interplay of these diverse models, Chemistry42 can deliver diverse, high-quality molecular structures within hours. The generated structures are then dynamically assessed using the platform's integrated reward and scoring modules. The system emphasizes providing deep domain-specific analytics to ensure users understand the strengths and weaknesses of each AI approach, rather than treating them as black-box solutions.

![Figure 1](media/image1.jpg)

**Figure 1.** A schematic representation of the three-step workflow for a de novo generative experiment using the Chemistry42 platform. In the first step, on a secure and company-specific instance of the software, users upload their data and configure the platform with the desired properties for the generated structures. The second step involves running the platform where an ensemble of 40+ generative models functions in parallel to generate the novel structures—this step is called the generation phase. A variety of filters scrutinize the generated molecular structures in the generation phase. The molecular structures are then subjected to multiple sets of reward and scoring modules, classified as either 2D or 3D modules, that dynamically assess the generated structures' properties according to the predefined criteria. Additional custom scoring modules (such as ADME predictors) can also be integrated into the reward pipeline to prioritize the generated structures. These modules form the backbone of Chemistry42's multiagent reinforcement learning (RL)-based generation protocol. Generated structures' scores are fed back to the generative models to reinforce them and guide the generative process toward high-scoring structures—this is called the learning phase. The final step is analysis. The generated structures are automatically ranked according to customizable metrics based on their predicted properties, including synthetic accessibility, novelty, diversity, etc. The platform also provides users with interactive tools to monitor generative model performance.

**Figure 1 key words:** Medicinal Chemistry Evolution 2018 (MCE-18), Molecular Complexity Features (MCFs), Rule of 5 Lipinski's Rule of Five (RO5), Therapeutic Indexes (T indexes), Physicochemical Profile (PC profile), Synthetic Accessibility / Real Reaction Space Accessibility score (SA/ReRSA score), Self-Organizing Map (SOM), Hierarchical Agglomerative Merging Base (HAM Base), Describing the main, usually larger, SOM from which smaller, more detailed maps are derived (Parent SOM), describing a feature of SOM analysis (ZOOM maps).

![Figure 2](media/image2.jpeg)

**Figure 2.** Chemistry42 interface for configuring an SBDD generative experiment.


---

#### 4.1.2.2. Case Study: Accelerated Target Discovery and Validation in HCC

This case study demonstrates the power of integrating the PandaOmics and Chemistry42 AI platforms with protein structures predicted by AlphaFold to efficiently identify and validate a novel therapeutic target for Hepatocellular Carcinoma (HCC), a challenging cancer with limited treatments.

**Target Identification with PandaOmics**

The process began with PandaOmics conducting a systematic search for HCC-relevant datasets, compiling a tailored data inventory. The platform performed data analysis and filtering based on both text and omics data from multiple sources, aggregating case-versus-control comparisons in a meta-analysis to generate a ranked list of potential targets.

The platform applied a "first-in-class" scenario for target identification, prioritizing proteins based on several strict criteria:
- Strong disease association and limited experimental structure information.
- Druggability by small molecules.
- Novelty (exclusion of targets in Phase 1 or later clinical trials in the past three years).
- Exclusion of targets of approved drugs.
- Exclusion of targets with previously resolved crystal structures.

Based on this analysis, Cyclin-dependent kinase 20 (CDK20) was selected as the initial target due to its high disease association and scarcity of experimental structural data (Ren et al., 2023).

**Molecular Generation and Validation with AlphaFold and Chemistry42**

With the target selected, the process moved to the molecular design stage:

**Structure Preparation**: The lack of an experimental structure for CDK20 was overcome by using the protein structure predicted by AlphaFold.

**Initial Generation & Validation**: Using the predicted CDK20 structure, the Chemistry42 platform employed a structure-based compound generation approach to create a library of molecules. From this library, only seven compounds were synthesized and tested in biological assays. This rapidly yielded an initial hit compound, ISM042-2-001, which demonstrated target engagement with a binding constant (Kd) value of 9.2 ± 0.5 µM (n=3) in the CDK20 kinase binding assay. This proof of concept was achieved in just 30 days from target selection (Ren et al., 2023).

**Optimization**: A second round of AI-powered compound generation was performed to optimize the initial hit. This led to the discovery of a more potent hit molecule, ISM042-2-048, after the synthesis and testing of six additional compounds. This molecule showed an average Kd value of 566.7 ± 256.2 nM (n=3) and an average IC₅₀ value of 33.4 ± 22.6 nM (n=3) in binding and inhibitory assays against CDK20. Significantly, ISM042-2-048 also exhibited selective antiproliferation activity in an HCC cell line where CDK20 was overexpressed, confirming its therapeutic potential (Ren et al., 2023).

**Conclusion**

This success story highlights the transformative capability of integrating diverse AI tools in early-stage drug discovery. By leveraging PandaOmics' comprehensive data analysis, AlphaFold's structural predictions, and Chemistry42's molecular generation power, a novel target for HCC was swiftly identified, novel small molecules were generated, and their biological activity was validated. This integration offers a paradigm for efficient and effective drug development.

### 4.1.3. Other Notable AI Platforms in the Industry

#### 4.1.3.1. Atomwise: Pioneering AI-Powered Virtual Screening For Drug Discovery

Atomwise is a leading company that is revolutionizing early-stage drug discovery by leveraging Deep Learning (DL) models for highly efficient virtual screening (Khan et al., 2024). The company's technology significantly accelerates the drug discovery pipeline by providing rapid and precise predictions of molecular interactions (Wallach et al., 2015). The heart of Atomwise's approach is AtomNet, a proprietary model that utilizes Convolutional Neural Networks (CNNs)—the same technology used in image recognition—to predict the crucial metric of binding affinity. By training these CNNs on 3D molecular structures, the Atomwise platform can accurately predict the complex interactions between small molecules and target proteins (Gaul & Cuesta-Lopez, 2024).

This AI-driven virtual screening methodology enables the rapid analysis and screening of millions of compounds against a target, dramatically speeding up the identification of new inhibitors and potential drug candidates (Gaul & Cuesta-Lopez, 2024).

Atomwise's technology has already proven instrumental, having successfully identified promising compounds for treating a variety of serious conditions, including Ebola and multiple sclerosis (Gaul & Cuesta-Lopez, 2024).

#### 4.1.3.2. BenevolentAI: Driving Early Drug Discovery With Deep Data Analysis

BenevolentAI (Sellwood et al., 2018) is an AI-driven platform at the forefront of revolutionizing the early stages of drug discovery. In contrast to approaches like Atomwise (Keshavarzi Arshadi et al., 2020) which focus on high-throughput virtual screening of compound libraries against a specific target, BenevolentAI primarily leverages advanced Deep Learning (DL) and Machine Learning (ML) techniques to achieve a deeper, mechanistic understanding of disease biology and to identify novel therapeutic targets.

**Core Capabilities**

BenevolentAI achieves its goals by analyzing diverse and comprehensive data sources, including (Sellwood et al., 2018):
1. Scientific Literature
2. Clinical Trial Data
3. Genetic Information

By synthesizing insights from this massive and varied body of knowledge, the platform is able to spot connections and hypothesize new therapeutic approaches.

**Context of AI-Driven Drug Discovery**

BenevolentAI operates within the broader context of AI transforming drug discovery, where de novo design—creating new molecules from scratch—is accelerated by generative models (such as Recurrent Neural Networks (RNNs), autoencoders, Generative Adversarial Networks (GANs), and Reinforcement Learning based systems (RL)). These systems are used to simultaneously optimize molecular properties like bioactivity and toxicity, expanding the chemical space and designing compounds with pre-defined characteristics.

Complementary tools further advance the field, including:
- DiffDock (Corso et al., 2022): Utilizes diffusion models for protein–ligand docking.
- MoleculeGen (Wu et al., 2018): An advanced molecule generation tool.
- ESM-2 (Tang et al., 2024; Tong et al., 2021): Advances protein structure prediction.

The demonstrated success of AI-driven platforms like BenevolentAI in identifying novel compounds for challenging diseases, notably Ebola and COVID-19 (Wallach et al., 2024), underscores the transformative potential of its approach in accelerating the overall drug discovery process.

#### 4.1.3.3. Numerate: A Model for AI-Pharma Collaboration in Medicinal Chemistry

Numerate is an exemplary AI company demonstrating the essential synergy between artificial intelligence researchers and pharmaceutical giants. Its collaboration with the pharmaceutical company Merck (Numerate, Inc., 2022) serves as a prime illustration of how merging expertise can drive innovation in drug development.

**Collaboration Focus and Impact**

The core objective of the Numerate-Merck partnership was the joint development of AI-based approaches specifically tailored for medicinal chemistry (Numerate, Inc., 2022). Numerate's proprietary technology, which leverages advanced algorithms and cloud computing, was deployed to accelerate the design of novel drug leads.

**Numerate's Role in Accelerating Drug Discovery**

The use of Numerate's powerful machine-learning models and algorithms offers several critical advantages to the drug discovery process:

**Prediction of Efficacy**: Numerate's algorithms build predictive models for drug candidate efficacy and other molecular properties, with accuracies comparable to traditional lab testing.

**Accelerated Development:** By delivering rapid and accurate predictions, Numerate helps pharma companies make quicker, better-informed decisions on which drug candidates to pursue, significantly shortening development timelines.

**Efficiency in Clinical Trials**: AI algorithms are instrumental in analyzing trial data, identifying trends, and predicting potential adverse effects, thereby boosting the accuracy and efficiency of clinical trials.

**Enhanced Accessibility and Affordability:** The analytical power of AI, as demonstrated by Numerate, can be used to analyze large population datasets to predict drug effectiveness for specific patient groups, moving healthcare toward tailored treatments.

The increasing number of new companies entering this domain, mirroring Numerate's success (P360, 2022), suggests that the impact of these AI-pharma collaborations will be significant in the near term. Ultimately, Numerate's model of working together with pharma facilitates the identification of new drug targets and the enhancement of existing treatments, directly benefiting patients.

## 4.2. Challenges and Limitations

### 4.2.1. The Black-Box Problem

The "Black-Box" Problem: The Difficulty of Interpreting AI Model Decisions

The core concern with current Artificial Intelligence (AI) in medicine centers on Deep Learning (DL) systems. This technology is founded on the Artificial Neural Network (ANN), a concept inspired by the intricate structure of the human brain. The fundamental active unit in the human brain is the neuron, with tens of billions interconnected to form a "neural network." DL systems seek to emulate this biological "neural network" (Castelvecchi, 2016) to achieve a similar learning strategy.

Medical AI systems possess three key features that define their utility and challenge:

1. **Self-Learning Capacity**
   Unlike traditional, rule-based computational programs, DL systems can process vast amounts of data and develop the ability for self-learning. This algorithmic capability allows the systems to generate a desired output based on the input data without being explicitly programmed with specific rules (McKinney et al., 2020; Miotto et al., 2016).

2. **High Predictive Accuracy**
   To achieve self-learning, these systems require extensive data, which is divided into training and testing sets. The training data "fits" the model, and the testing data validates its performance. After training, medical AI systems demonstrate exceptionally high accuracy in testing, sometimes even surpassing human experts in diagnosing specific conditions. For example, the Deep Patient system accurately predicted "hidden" diseases in over 700,000 electronic health records using DL (Miotto et al., 2016). Its high accuracy in predicting psychiatric disorders, like schizophrenia, was particularly notable, as these conditions are notoriously difficult to predict. In another instance, the AI system developed by Google's DeepMind outperformed six human radiologists in predicting breast cancer from new mammograms after analyzing X-ray images from nearly 29,000 female patients (McKinney et al., 2020).

3. **Unexplainable Diagnoses and Suggestions**
   The third feature is the root of the "black-box" problem: the diagnoses and treatment suggestions from medical AI systems are fundamentally unexplainable. Because the ANNs mimic the still-mysterious workings of the human brain's neural network, these systems are "black boxes" to patients, doctors, and even their own designers.

The term "black box" signifies a lack of understanding of the system's internal working mechanism. For instance, a medical AI system might accurately predict a tumor's response to a drug based on allelic patterns across thousands of genes, or forecast lung cancer prognosis by analyzing microscopic images, yet it cannot identify why those specific patterns or image features were significant.

Regarding the Deep Patient system, researchers confirmed its accurate predictions for various diseases, including psychiatric disorders, but were puzzled by how it achieved such accurate conclusions and predictions. As Watson explicitly states, the main concern is a "lack of understanding among patients and doctors about how predictions are made," especially with top-performing deep neural networks used in image recognition. While these models may reliably distinguish between malignant and benign tumors, they "offer no explanation for their judgments" (Watson et al., 2019).

It remains a significant hurdle before medical AI systems become transparent enough for a physician to easily identify incorrect results or for an individual to reasonably contest a system's decision. Consequently, the potential harm arising from these opaque systems must be seriously considered.

### 4.2.2. The Imperative for Experimental Validation

The application of Artificial Intelligence (AI), particularly in complex fields like drug discovery, offers tremendous predictive power. However, it is crucial to establish and reiterate a fundamental constraint: current AI-based approaches are not a replacement for traditional experimental methods (Grebner et al., 2021; Schraagen & van Diggelen, 2021). While these systems are incredibly adept at pattern recognition and prediction, they do not possess the capacity to autonomously confirm or interpret the physical reality of their findings.

**AI as a Hypothesis Generator**

An AI system's core function is to act as a sophisticated hypothesis generator. Based on the massive datasets it processes, AI can only furnish a set of predictions concerning chemical properties, biological interactions, or disease pathways. This means the output from the algorithms is purely theoretical until proven otherwise. Consequently, the results delivered by the AI models must then be rigorously validated and interpreted by human researchers (Gilpin et al., 2019). The human element remains indispensable for contextualizing the findings, ensuring their biological plausibility, and designing the necessary experiments to move from a predicted outcome to a confirmed fact.

**The Synergy of Prediction and Experience**

Far from being a competitive alternative, the ideal role of AI is to foster a powerful integration with traditional experimental methods (Paul et al., 2021). This synergy leverages the strengths of both components. On one side, you have the unparalleled predictive power of AI—its ability to rapidly sift through vast chemical libraries and identify promising candidates that would take human researchers decades to evaluate. On the other side, you have the essential expertise and experience of human researchers (Jarrahi, 2018)—the deep, nuanced understanding of biochemistry, medicine, and laboratory techniques required to actually test, refine, and bring a compound to fruition.

By strategically combining these elements, the scientific community can optimize the drug discovery process (Wang et al., 2019). AI dramatically reduces the initial search space, allowing human teams to focus their finite resources on the most promising avenues. This collaboration does not diminish the role of the researcher; rather, it elevates it, freeing human intellect to concentrate on complex problem-solving and critical validation, thereby accelerating the development of new medications (Wang et al., 2019). The ultimate success of an AI prediction is not its accuracy on a test set, but its confirmation under a microscope.

### 4.2.3. High-Quality Data Scarcity and Its Impact on Performance in Drug Design

The central focus of this analysis is the influence of data quality and scarcity on AI-driven drug design, specifically addressing the key hurdles in data representation and prediction—areas where Artificial Intelligence (AI) holds considerable potential.

**Obstacles in Defining AI-Ready Tasks**

Many foundational drug discovery activities are difficult to translate into effective machine learning problems. The primary challenge lies in the lack of standardized knowledge representations and a deficit of AI-ready benchmark datasets.

- **Non-Uniform Molecular Representations**: Drug molecules themselves can be encoded in diverse formats, such as linear SMILES strings, numerical descriptors like Extended Connectivity Fingerprints (ECFP), and intricate molecular graphs. Similarly, proteins can be modeled using a simple 1D amino acid sequence, a more complex sequence representation, or their complete 3D-structure. This inherent diversity in representation complicates the development of universal models.
- **Issues with Labels**: Further compounding this is the problem of low resource labels and significant disparity among labels, which makes the formulation of meaningful, generalizable learning tasks exceedingly difficult for AI systems.

**Data Imperfections That Impact Performance**

The performance and reliability of AI models are directly compromised by common flaws in the underlying data, including problems with data collection, the prevalence of small sample sizes, and the existence of noisy labels. These factors collectively depress model accuracy and dependability.

**Recent Solutions and Progress**

Despite these significant data-centric challenges, the past few years have demonstrated substantial advancements in applying deep-learning to drug discovery. This progress is greatly facilitated by the emergence of new resources designed to help overcome data scarcity and standardization issues:
- The development of open-source tools (Huang et al., 2020).
- The creation of AI-ready benchmark datasets (Huang et al., 2021).
- New deep learning platforms (Zhu et al., 2022) specifically engineered for drug design applications.

## 4.3. Ethical and Regulatory Considerations

### 4.3.1. Data Privacy and Algorithmic Bias

The application of Artificial Intelligence (AI) in the pharmaceutical sector necessitates a critical examination of its ethical implications (Karimian et al., 2022; Naik et al., 2022). The discussion focuses on two paramount challenges: the potential for algorithmic bias and the vital necessity of maintaining data privacy and security.

**The Risk of Algorithmic Bias and Inequity**

A central ethical concern revolves around the potential for bias in AI algorithms. AI systems are increasingly being used to make decisions with direct bearing on public health and individual welfare—including choices regarding which drugs to develop, the execution of clinical trials, and the methods for marketing and distributing medications.

If the training data is unrepresentative or reflects historical biases, the resulting algorithms can entrench and amplify those inequities. This risks causing unequal access to medical treatment and potentially the unfair treatment of specific demographic groups. Such outcomes fundamentally contradict the principles of equality and justice in healthcare.

**Data Privacy, Security, and Compliance**

Since AI systems rely heavily on large amounts of data to function, their integration into the pharmaceutical industry raises serious concerns about data privacy and security.

There is a considerable risk that the sensitive, personal health information used by these models could be compromised through unauthorized access or misuse. A breach of this nature would have severe consequences for affected individuals and could significantly damage the reputation of the involved pharmaceutical companies. Consequently, the collection and use of sensitive medical data must be conducted in a manner that strictly respects individual privacy and adheres to all relevant regulations.

**Wider Societal Concerns**

Beyond data ethics and bias, the widespread adoption of AI also brings up socioeconomic issues, particularly the prospect of job losses due to automation in the pharmaceutical sector. It is essential to proactively assess the impact on the workforce and ensure support is available for those who might be displaced by these technological changes.

### 4.3.2. Regulatory Frameworks

The integration of Artificial Intelligence (AI) into pharmacy practice, despite its transformative potential, introduces a complex set of ethical and regulatory challenges. A key focus is on how regulatory bodies are evolving to govern these new technologies.

**The Need for Regulatory Adaptation**

The rapid evolution of AI in the pharmaceutical industry presents significant ethical and legal challenges, including issues like algorithmic bias, a lack of transparency in decision-making, ongoing data privacy concerns, and unclear liability frameworks (Shaki et al., 2024). Currently, regulatory agencies are in the process of adapting to effectively oversee AI applications in pharma (Shaki et al., 2024). There is a recognized need for standardized guidelines that can successfully balance the need to ensure patient safety with the desire to avoid stifling innovation (Shaki et al., 2024).

**Regulatory Role in Clinical Trials and Safety**

Patient safety and the integrity of clinical trials constitute a significant ethical and regulatory challenge. Regulatory bodies, such as the Food and Drug Administration (FDA), are vital in enforcing guidelines to protect trial participants (Boudi et al., 2024). The integrity of these trials relies heavily on securing informed consent from participants, who must fully comprehend the risks involved. While the FDA works to protect individual rights, issues such as the exploitation of vulnerable populations remain a prevalent concern (Boudi et al., 2024).

**The Wider Ethical and Legal Landscape**

Surveys among pharmacy professionals, particularly in the Middle East and North Africa (MENA) region, underscore the breadth of these concerns (Hasan et al., 2024). Critical issues identified include:
- Lack of Legal Regulation (67.0%)
- Potential Job Displacement (62.9%)
- Patient Data Privacy (58.9%)
- Cybersecurity Threats (58.9%)

These findings emphasize that realizing the full benefits of AI requires a commitment to responsible AI in medicine, anchored by transparent frameworks, multidisciplinary collaboration, and an unwavering focus on patient welfare (Boudi et al., 2024). Ultimately, achieving public trust requires regulatory bodies to successfully manage the balance between AI's potential and robust ethical governance (Shaki et al., 2024).

## 4.4. Future Trends

### 4.4.1. Emerging Technologies: Quantum Computing in Drug Design

The core challenge confronting pharmaceutical science is the time-intensive and exorbitant nature of drug development, with costs frequently exceeding one billion dollars (Berdigaliyev & Aljofan, 2020). Historical precedents, such as the 35-year effort to cure Malaria (Magazine, 2022), underscore the urgent need to accelerate the entire pipeline, which encompasses target identification, hit screening, lead optimization, pre-clinical testing, and clinical trials (Wang et al., 2023). While current AI deployment is already advantageous in speeding up the process, it faces limitations, including data quality issues, the complexity of biological systems, and the scarcity of high-quality data for rare diseases (Blanco-Gonzalez et al., 2023).

**Quantum Computing as a Solution to Drug Discovery Hurdles**

Quantum Computing (QC) offers a potential, paradigm-shifting solution by leveraging its superiority over classical supercomputers (Blanco-Gonzalez et al., 2023).

Quantum computers are designed to tackle problems that are intractable for even the most powerful classical machines. The milestone of quantum supremacy was achieved in 2019 by Google's 'Sycamore' system, which featured 53 programmable superconducting qubits (Arute et al., 2019; Zinner et al., 2021).

The evolution of QC is highly promising for drug discovery and development (Mahesh & Shijo, 2023) as quantum technologies stand to revolutionize fields like machine learning, financial modeling, and especially chemistry and medicine (Sotelo, 2023).

**Unique Advantages Of Quantum Computing**

QC excels in two key areas relevant to drug design:

1. **Molecular Simulation and Prediction**: Quantum computers are inherently superior at molecular simulations (McArdle et al., 2020; Parenti & Rastelli, 2012). By predicting drug behavior and properties with greater precision, they significantly enhance the in-depth understanding of drug action (Parenti & Rastelli, 2012). This ability to accurately model quantum effects provides more precise predictions for drug design.
2. **Accelerated Data Processing**: QC can accelerate machine learning algorithms (Li et al., 2021). It achieves this by rapidly processing extensive data volumes, managing complex computations, and generating more precise predictions than traditional methods and classical AI (Chauhan et al., 2022; Li et al., 2021).

Quantum generative models, for example, can comprehensively cover complex distributions due to their intrinsic probabilistic nature (Biswas et al., 2020).

**The Research Motivation and Structure**

![Figure 3](media/image3.jpg)

**Figure 3.** The primary motivation driving this area of research is the imperative to expedite drug development, reduce costs, and fundamentally redefine the approach to creating new drugs, moving away from conventional methods (McArdle et al., 2020).

This research aims to delve into quantum computers' medical capabilities, analyzing drug behavior under diverse conditions using specialized algorithms. The structure of this paper will cover:
- Previous work (Section II).
- A fundamental overview of core quantum technology (Section III).
- The integration of quantum technology at various stages of the simulation process (Section IV).
- A dedicated discussion of Quantum chemistry (Section V).
- The complete pipeline of the quantum-enhanced drug development process (Section VI).
- The potential use of QC for final stage trial and testing (Section VII).
- A necessary exploration of the technological and ethical challenges posed by quantum computers (Section VIII).
- Future prospects and new applications (Section IX).
- The conclusion (Section X).

### 4.4.2. Personalized Medicine

The digitization of medical records is paving the way for data-driven methodologies to revolutionize several healthcare areas, including clinical trials, health policy, drug discovery, and especially precision medicine.

**AI and Data-Driven Drug Design**

Over the past decade, novel analytical and computational advances have radically transformed drug discovery (Davenport & Kalakota, 2019; Pandey et al., 2022; Powles & Hodson, 2017; Sierra-Sosa et al., 2019; Yu et al., 2018). There is now intense interest in applying Artificial Intelligence (AI) methods to improve various stages of the drug discovery pipeline (Chen et al., 2018). The goal is to move towards personalized treatment by utilizing AI in:
- De novo molecular design and optimization
- Structure-based drug design
- Pre-clinical and clinical development

**The Foundation for Personalized Treatments**

The integration of extensive biomedical datasets with sophisticated analytical tools, particularly deep learning models, is the core mechanism enabling this shift toward individualized medicine (Vamathevan et al., 2019). These datasets include:
- Genomic profiles
- Imaging data
- Chemical and drug databases

By coordinating these tools, researchers can more effectively discover and develop drugs and clinical applications tailored to individual patient characteristics, making the vision of personalized medicine a reality.

### 4.4.3. The AI-Scientist Collaboration: "Self-Driving" Labs

The future success of AI in drug discovery hinges on fostering a collaborative environment to generate high-quality data and advance model representation. This collaboration must move beyond simple prediction to embrace robust methods that enhance human thinking and ultimately change the culture of research.

**Developing Foundational Datasets and Collaborative Models**

A key requirement is the creation of high-quality, annotated labeled datasets and the learning of their representations, which necessitates collaborative efforts from multiple disciplines. Following the precedent set by ImageNet in computer vision, we urgently need to develop the "ImageNet" for molecules and more benchmark resources like MoleculeNet (Wu et al., 2018).

We must develop robust methods where the human mind can teach the model to optimize so that the AI generates insights that allow humans to think in new directions. This co-optimization aims to bring better prospects into clinics, enhance target validation, increase patient recruitment, and improve clinical trial design (as depicted in Fig. 4).

**Shifting Focus to Causal Discovery**

Current AI mainly focuses on the manifestations of diseases, rather than their actual causes. A crucial advancement will be understanding the causal pathway of diseases—how genetic predisposition manifests—to enable manipulation and potentially reverse the course of the disease. This is a promising area for causal machine learning and causal inference (Peters et al., 2011), which can also be applied to treatment decisions and tracking patient health evolution.

**Cultivating a Collaborative Research Culture**

The full potential of data science in healthcare requires cultivating a "culture" where stakeholders are willing to use computational models and utilize their results. As the African proverb says, "if you want to go fast go alone, and if you want to go far go together."

This requires:
- Increased collaboration between industry, academia, and other stakeholders.
- Training professionals to understand both medicine and computer science.

Furthermore, organizing more workshops on AI for drug discovery or computational biology at major AI conferences like NeuralIPS and International Conference on Machine Learning (ICML) is necessary, along with the long-term vision of developing new degree programs for AI in drug discovery. This collaborative, transparent approach is exemplified by initiatives like the 2019 partnership between AstraZeneca and Dialog for DREAM Challenges, which focused on model repeatability and methodological transparency on significant biomedical problems using large, shared datasets (e.g., 11,576 experiments on cancer cell lines).

![Figure 4](media/image4.jpg)

**Figure 4.** Learning from various data sources can aid drug design, clinical decision support, and public health policy. The collaborative intelligence resulting from the merger of mind and machine is expected to improve decision-making in healthcare.


---

# 5. Conclusion

## 5.1. Summary of Key Findings

### 5.1.1. Recapitulation of AI's Impact Across the Drug Discovery Pipeline

This work has examined the transformative role of artificial intelligence across the entire drug discovery and development pipeline, from early target identification to lead optimization, safety assessment, and translational decision-making. Traditional drug discovery, while scientifically robust, is constrained by high costs, long timelines, and high attrition rates. As discussed in Chapter 1, AI addresses these limitations by enabling scalable data-driven prioritization, representation learning, and predictive modeling across chemical, biological, and clinical domains.

Chapter 2 demonstrated how AI has reshaped target identification and validation through the integration of multi-omic data, biological networks, and structural biology. Machine learning and deep learning models enable systematic prioritization of disease-associated genes and proteins, while advances such as AlphaFold have dramatically expanded structural coverage of the proteome, facilitating structure-based reasoning even in the absence of experimental data.

Chapter 3 highlighted AI-driven advances in virtual screening, molecular docking, de novo drug design, and ADMET profiling. Generative models, graph neural networks, and deep learning–based scoring functions have enabled more efficient exploration of chemical space, accelerated hit-to-lead optimization, and earlier identification of safety liabilities. Together, these capabilities reduce experimental burden while improving the quality of candidates entering downstream development.

Chapter 4 contextualized these methodological advances through real-world platforms, case studies, and practical limitations, emphasizing that AI has already delivered tangible impact but remains constrained by data quality, model uncertainty, and biological complexity. Collectively, the findings demonstrate that AI is no longer an auxiliary tool, but a central component of modern drug discovery workflows.

## 5.2. Reiteration of Thesis

### 5.2.1. AI as a Collaborative Tool Empowering Human Scientists

The central thesis of this work is that artificial intelligence functions most effectively as a collaborative and augmentative tool, rather than a replacement for human expertise. Across all stages of drug discovery, AI systems excel at pattern recognition, large-scale prioritization, and hypothesis generation, but they rely fundamentally on human judgment for experimental design, biological interpretation, and strategic decision-making.

Rather than automating discovery in isolation, successful AI-driven pipelines integrate computational models into iterative design–make–test–analyze cycles, where predictions are continuously refined through experimental feedback. Human scientists remain essential for defining meaningful objectives, curating high-quality data, interpreting model outputs, and resolving ambiguities arising from biological context and translational risk. This synergy between human intelligence and machine intelligence represents the most realistic and productive paradigm for AI adoption in drug discovery.

## 5.3. Final Outlook

### 5.3.1. Toward an Intelligent, Data-Driven Era of Drug Discovery

Drug discovery is entering a new era characterized by intelligent, data-driven, and increasingly integrated workflows. Future progress will depend on the convergence of foundation models, multimodal learning, automated experimentation, and improved data governance. Advances in uncertainty estimation, interpretability, and regulatory alignment will be critical to building trust in AI-driven decisions, particularly in high-stakes clinical settings.

Despite its promise, AI is not a universal solution to the challenges of drug development. Biological complexity, data bias, and translational uncertainty will continue to limit purely computational approaches. However, when embedded within rigorous experimental frameworks and guided by domain expertise, AI has the potential to significantly reduce failure rates, shorten development timelines, and expand the range of tractable therapeutic targets.

In conclusion, artificial intelligence represents a powerful catalyst rather than a replacement for scientific discovery. Its true value lies in amplifying human creativity, enabling more informed decision-making, and accelerating the translation of biological insight into effective and safe therapeutics. As the field matures, sustained collaboration between computational scientists, chemists, biologists, clinicians, and regulators will be essential to fully realize the transformative potential of AI in drug discovery.


---

# References

Agarwal, P., & Searls, D. B. (2008). Literature mining in support of drug discovery. *Briefings in Bioinformatics, 9*(6), 479–492.

Alipanahi, B., Delong, A., Weirauch, M. T., & Frey, B. J. (2015). Predicting the sequence specificities of DNA- and RNA-binding proteins by deep learning. *Nature Biotechnology, 33*(8), 831–838.

AlQuraishi, M. (2020). AlphaFold2 @ CASP14: "It feels like one's child has left home." *Biophysical Coarse Graining*. https://moalquraishi.wordpress.com

Angermueller, C., Pärnamaa, T., Parts, L., & Stegle, O. (2016). Deep learning for computational biology. *Molecular Systems Biology, 12*(7), 878.

Arute, F., Arya, K., Babbush, R., Bacon, D., Bardin, J. C., Barends, R., ... & Martinis, J. M. (2019). Quantum supremacy using a programmable superconducting processor. *Nature, 574*(7779), 505–510. https://doi.org/10.1038/s41586-019-1666-5

Atz, K., Grisoni, F., & Schneider, G. (2021). Geometric deep learning on molecular representations. *Nature Machine Intelligence, 3*(12), 1023–1032.

Bepler, T., & Berger, B. (2021). Learning the protein language: Evolution, structure, and function. *Cell Systems, 12*(6), 654–669. https://doi.org/10.1016/j.cels.2021.05.017

Berdigaliyev, N., & Aljofan, M. (2020). An overview of drug discovery and development. *Future Medicinal Chemistry, 12*(10), 939–947.

Bishop, C. M. (2006). *Pattern recognition and machine learning*. Springer.

Biswas, R. H., Jiang, X., & Li, K. (2020). Quantum generative models for molecular design. *arXiv preprint arXiv:2101.08272*.

Blanco-Gonzalez, A., Cabezon, A., Seco-Gonzalez, A., Conde-Torres, D., Antelo-Riveiro, P., Pineiro, A., & Garcia-Fandino, R. (2023). The role of AI in drug discovery: Challenges, opportunities, and strategies. *Pharmaceuticals, 16*(6), 891.

Boudi, A. L., Siddiqui, Z. A., & Gupta, A. K. (2024). Ethical challenges of artificial intelligence in medicine. *Cureus, 16*(11), e74495. https://doi.org/10.7759/cureus.74495

Castelvecchi, D. (2016). Can we open the black box of AI? *Nature, 538*(7623), 20–23. https://doi.org/10.1038/538020a

Chauhan, V. K., Singh, A., & Tiwari, A. (2022). Quantum machine learning for drug discovery and development. *Current Drug Discovery Technologies, 19*(2), e140122200216.

Chen, H., Engkvist, O., Wang, Y., Olivecrona, M., & Blaschke, T. (2018). The rise of deep learning in drug discovery. *Drug Discovery Today, 23*(6), 1241–1250. https://doi.org/10.1016/j.drudis.2018.01.039

Corso, G., Stärk, H., Jing, B., Barzilay, R., & Jaakkola, T. (2022). DiffDock: Diffusion steps, twists, and turns for molecular docking. *arXiv preprint arXiv:2210.01776*. https://arxiv.org/abs/2210.01776

Costa, P. R., Acencio, M. L., & Lemke, N. (2010). A machine learning approach for genome-wide prediction of morbid and druggable human genes based on systems-level data. *BMC Genomics, 11*, 1–15.

Davenport, T., & Kalakota, R. (2019). The potential for artificial intelligence in healthcare. *Future Healthcare Journal, 6*(2), 94–98.

David, L., Thakkar, A., Mercado, R., & Engkvist, O. (2020). Molecular representations in AI-driven drug discovery: A review and practical guide. *Journal of Cheminformatics, 12*(1), 1–22.

Defferrard, M., Bresson, X., & Vandergheynst, P. (2016). Convolutional neural networks on graphs with fast localized spectral filtering. In *Advances in Neural Information Processing Systems*.

Devi, R., Satapathy, S. S., & Ray, S. S. (2015). Evolutionary algorithms in de novo drug design: A survey. *Applied Soft Computing, 27*, 543–552.

Dong, J., Cao, D. S., Miao, H. Y., Liu, S., Deng, B. C., Yun, Y. H., Wang, N. N., Lu, A. P., Zeng, W. B., & Chen, A. F. (2015). ChemDes: An integrated web-based platform for molecular descriptor and fingerprint computation. *Journal of Cheminformatics, 7*(1), 60. https://doi.org/10.1186/s13321-015-0109-z

Doytchinova, I. (2022). Drug design—Past, present, future. *Molecules, 27*, 1496.

Ferruz, N., Schmidt, S., & Höcker, B. (2022). ProtGPT2 is a deep unsupervised language model for protein design. *Nature Communications, 13*(1), 4348. https://doi.org/10.1038/s41467-022-32007-7

Francoeur, P. G., Masuda, T., Sunseri, J., Jia, A., Iovanisci, R. B., Snyder, I., & Koes, D. R. (2020). Three-dimensional convolutional neural networks and a cross-docked data set for structure-based drug design. *Journal of Chemical Information and Modeling, 60*(9), 4200–4215. https://doi.org/10.1021/acs.jcim.0c00411

Friesner, R. A., Banks, J. L., Murphy, R. B., Halgren, T. A., Klicic, J. J., Mainz, D. T., Repasky, M. P., Knoll, E. H., Shelley, M., Perry, J. K., Shaw, D. E., Francis, P., & Shenkin, P. S. (2004). Glide: A new approach for rapid, accurate docking and scoring. 1. Method and assessment of docking accuracy. *Journal of Medicinal Chemistry, 47*(7), 1739–1749. https://doi.org/10.1021/jm0306430

Ganesan, A., Coote, M. L., & Barakat, K. (2017). Molecular dynamics-driven drug discovery: Leaping forward with confidence. *Drug Discovery Today, 22*(2), 249–269.

Gaudelet, T., Day, B., Jamasb, A. R., Soman, J., Regep, C., Liu, G., ... & Tang, J. (2021). Utilizing graph machine learning within drug discovery and development. *Briefings in Bioinformatics, 22*(6), bbab159.

Gaul, R. B., & Cuesta-Lopez, S. (2024). Artificial intelligence in drug discovery: A comprehensive review of current status, challenges, and future directions. *Journal of Drug Targeting, 32*(1), 1–17.

Gilpin, L. H., Bau, D., Yuan, B. Z., Bajwa, A., Specter, M., & Kagal, L. (2019). Explaining explanations: An overview of interpretability of machine learning. *Proceedings of the 2018 IEEE 5th International Conference on Data Science and Advanced Analytics (DSAA)*, 80–89. https://doi.org/10.1109/DSAA.2018.00018

Gómez-Bombarelli, R., Wei, J. N., Duvenaud, D., Hernández-Lobato, J. M., Sánchez-Lengeling, B., Sheberla, D., Aguilera-Iparraguirre, J., Hirzel, T. D., Adams, R. P., & Aspuru-Guzik, A. (2018). Automatic chemical design using a data-driven continuous representation of molecules. *ACS Central Science, 4*, 268–276.

Gönen, M. (2012). Predicting drug–target interactions from chemical and genomic kernels using Bayesian matrix factorization. *Bioinformatics, 28*(18), 2304–2310.

Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press.

Grebner, C., Matter, H., & Kogej, T. (2021). Artificial intelligence in drug discovery: Moving beyond the hype. *ChemMedChem, 16*(2), 253–255.

Guimaraes, G. L., Sanchez-Lengeling, B., Outeiral, C., Farias, P. L. C., & Aspuru-Guzik, A. (2018). Objective-reinforced generative adversarial networks (ORGAN) for sequence generation models. *arXiv preprint arXiv:1705.10843*.

Gupta, A., Müller, A. T., Huisman, B. J., Fuchs, J. A., Schneider, P., & Schneider, G. (2018). Generative recurrent networks for de novo drug design. *Molecular Informatics, 37*(1–2), 1700111.

Hasan, H. E., Jaber, D., Sadeq, A. S., & Sulaiman, S. A. S. (2024). Ethical considerations and concerns in the implementation of AI in pharmacy practice: A cross-sectional study. *BMC Medical Ethics, 25*(1), 55. https://doi.org/10.1186/s12910-024-01053-9

Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. *Neural Computation, 9*(8), 1735–1780. https://doi.org/10.1162/neco.1997.9.8.1735

Huang, K., Fu, T., Gao, W., Zhao, Y., Roohani, Y., Leskovec, J., ... & Zitnik, M. (2021). Therapeutics Data Commons: Machine learning datasets and tasks for drug discovery and development. *arXiv preprint arXiv:2102.09548*.

Huang, N., Shoichet, B. K., & Irwin, J. J. (2020). Benchmarking embedding/metric learning for drug discovery. *Journal of Chemical Information and Modeling, 60*(12), 5983–5994.

Hughes, J. P., Rees, S., Kalindjian, S. B., & Philpott, K. L. (2011). Principles of early drug discovery. *British Journal of Pharmacology, 162*(6), 1239–1249.

Irwin, J. J., Tang, K. G., Young, J., Dandarchuluun, C., Wong, B. R., Khurelbaatar, M., Moroz, Y. S., Mayfield, J., & Sayle, R. A. (2020). ZINC20—A free ultralarge-scale chemical database for ligand discovery. *Journal of Chemical Information and Modeling, 60*(12), 6065–6073. https://doi.org/10.1021/acs.jcim.0c00675

Jarrahi, M. H. (2018). Artificial intelligence and the future of work: Human-AI symbiosis in organizational decision making. *Business Horizons, 61*(4), 577–586.

Jiang, D., Wu, Z., Hsieh, C.-Y., Chen, G., Liao, B., Wang, Z., ... & Hou, T. (2021). Could graph neural networks learn better molecular representation for drug discovery? *Journal of Cheminformatics, 13*(1), 1–23.

Jiménez, J., Doerr, S., Martínez-Rosell, G., Rose, A. S., & De Fabritiis, G. (2017). DeepSite: Protein-binding site predictor using 3D-convolutional neural networks. *Bioinformatics, 33*(19), 3036–3042. https://doi.org/10.1093/bioinformatics/btx350

Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Žídek, A., Potapenko, A., Bridgland, A., Meyer, C., Kohl, S. A. A., Ballard, A. J., Cowie, A., Romera-Paredes, B., Nikolov, S., Jain, R., Adler, J., ... & Hassabis, D. (2021). Highly accurate protein structure prediction with AlphaFold. *Nature, 596*(7873), 583–589. https://doi.org/10.1038/s41586-021-03819-2

Kadurin, A., Nikolenko, S., Khrabrov, K., Aliper, A., & Zhavoronkov, A. (2017). druGAN: An advanced generative adversarial autoencoder model for de novo generation of new molecules with desired molecular properties in silico. *Molecular Pharmaceutics, 14*(9), 3098–3104.

Karimi, M., Wu, D., Wang, Z., & Shen, Y. (2019). DeepAffinity: Interpretable deep learning of compound–protein affinity. *Bioinformatics, 35*(18), 3329–3338.

Karimian, G., Petzeller, M., & Lemke, O. (2022). The ethics of AI in pharmacy practice: specific issues and general concerns. *International Journal of Clinical Pharmacy, 44*, 829–834.

Kempt, H., & Nagel, S. K. (2022). Responsibility, second opinions and peer-disagreement: Ethical and epistemological challenges of using AI in clinical diagnostic contexts. *Journal of Medical Ethics, 48*(4), 222–229.

Keshavarzi Arshadi, A., Salem, M., Collins, J., Moss, J., & Ekins, S. (2020). Deep learning in drug discovery: a new era for artificial intelligence. *Drug Discovery Today, 25*(10), 90–100.

Khan, S., Gondal, T. M., & Irfan, M. (2024). The role of AI in drug discovery: A comprehensive review. *Computers in Biology and Medicine, 168*, 107775.

Kim, S., Thiessen, P. A., Bolton, E. E., Chen, J., Fu, G., Gindulyte, A., Han, L., He, J., He, S., Shoemaker, B. A., Wang, J., Yu, B., Zhang, J., & Bryant, S. H. (2016). PubChem Substance and Compound databases. *Nucleic Acids Research, 44*(D1), D1202–D1213. https://doi.org/10.1093/nar/gkv951

Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes. *arXiv preprint arXiv:1312.6114*. https://arxiv.org/abs/1312.6114

Korotcov, A., Tkachenko, V., Russo, D. P., & Ekins, S. (2017). Comparison of deep learning with multiple machine learning methods and metrics using diverse drug discovery data sets. *Molecular Pharmaceutics, 14*(12), 4462–4475.

Kosonocky, T., Le, H., & Khurana, S. (2024). Natural language processing for drug discovery. *Drug Discovery Today, 29*(1), 103822.

Krivák, R., & Hoksza, D. (2018). P2Rank: Machine learning based tool for rapid and accurate prediction of ligand binding sites from protein structure. *Journal of Cheminformatics, 10*(1), 39. https://doi.org/10.1186/s13321-018-0285-8

Kryshtafovych, A., & Fidelis, K. (2009). Protein structure prediction and model quality assessment. *Drug Discovery Today, 14*(7–8), 386–393.

Kuznetsov, M., & Polykovskiy, D. (2021). MolGrow: A graph normalizing flow for hierarchical molecular generation. *Proceedings of the AAAI Conference on Artificial Intelligence, 35*(1), 316–324.

Lavecchia, A. (2015). Machine-learning approaches in drug discovery: Methods and applications. *Drug Discovery Today, 20*(3), 318–331.

Li, G., Muller, M., Thabet, A., & Ghanem, B. (2019). DeepGCNs: Can GCNs go as deep as CNNs? In *Proceedings of the IEEE/CVF International Conference on Computer Vision* (pp. 9267–9276).

Li, L., Chen, R., & Weng, Z. (2003). RDOCK: Refinement of rigid-body protein docking predictions. *Proteins, 53*(3), 693–707.

Li, Y., Liu, B., Deng, J., Guo, Y., & Du, H. (2024). Image-based molecular representation learning for drug development: A survey. *Briefings in Bioinformatics, 25*(4), bbae294. https://doi.org/10.1093/bib/bbae294

Li, Y. L., Huang, R., Xia, M., Patterson, T. A., & Hong, H. (2021). Quantum machine learning in drug discovery. *Drug Discovery Today, 26*(6), 1339–1347.

Li, Z., Huang, R., Xia, M., Patterson, T. A., & Hong, H. (2024). Fingerprinting interactions between proteins and ligands for facilitating machine learning in drug discovery. *Biomolecules, 14*(1), 72. https://doi.org/10.3390/biom14010072

Liang, J., Edelsbrunner, H., Fu, P., Sudhakar, P. V., & Subramaniam, S. (1998). Analytical shape computation of macromolecules: I. *Proteins, 33*(1), 1–17.

Lim, J., Ryu, S., Kim, J. W., & Kim, W. Y. (2018). Molecular generative model based on conditional variational autoencoder for de novo molecular design. *Journal of Cheminformatics, 10*(1), 31.

Lin, Z., Akin, H., Rao, R., Hie, B., Zhu, Z., Lu, W., ... & Rives, A. (2023). Evolutionary-scale prediction of atomic-level protein structure with a language model. *Science, 379*(6637), 1123–1130. https://doi.org/10.1126/science.ade2574

Lo, Y.-C., Rensi, S. E., Torng, W., & Altman, R. B. (2018). Machine learning in chemoinformatics and drug discovery. *Drug Discovery Today, 23*(8), 1538–1546.

Ma, J., Sheridan, R. P., Liaw, A., ... & Dahl, G. E. (2015). Deep neural nets as a method for QSAR. *Journal of Chemical Information and Modeling, 55*(2), 263–274.

Magazine, P. (2022). Malaria vaccine approval: A 35-year journey. *Pharmaceutical Magazine*.

Mahesh, K., & Shijo, M. (2023). Quantum computing in drug discovery: A review. *Drug Discovery Today, 28*(5), 103527.

Maia, E. H. B., Assis, L. C., de Oliveira, T. A., da Silva, A. M., & Taranto, A. G. (2020). Structure-based virtual screening: From classical to artificial intelligence. *Frontiers in Chemistry, 8*, 343.

Mak, K.-K., & Pichika, M. R. (2019). Artificial intelligence in drug development: Present status and future prospects. *Drug Discovery Today, 24*, 773–780.

McArdle, S., Endo, S., Aspuru-Guzik, A., Benjamin, S. C., & Yuan, X. (2020). Quantum computational chemistry. *Reviews of Modern Physics, 92*(1), 015003. https://doi.org/10.1103/RevModPhys.92.015003

McKinney, S. M., Sieniek, M., Godbole, V., Godwin, J., Antropova, N., Ashrafian, H., ... & Shetty, S. (2020). International evaluation of an AI system for breast cancer screening. *Nature, 577*(7788), 89–94. https://doi.org/10.1038/s41586-019-1799-6

Mendez, D., Gaulton, A., Bento, A. P., Chambers, J., De Veij, M., Félix, E., Magariños, M. P., Mosquera, J. F., Mutowo, P., Nowotka, M., Gordillo-Marañón, M., Hunter, F., Junco, L., Mugumbate, G., Rodriguez-Lopez, M., Atkinson, F., Bosc, N., Radoux, C. J., Segura-Cabrera, A., ... & Leach, A. R. (2019). ChEMBL: Towards direct deposition of bioassay data. *Nucleic Acids Research, 47*(D1), D930–D940. https://doi.org/10.1093/nar/gky1075

Miotto, R., Li, L., Kidd, B. A., & Dudley, J. T. (2016). Deep patient: An unsupervised representation to predict the future of patients from the electronic health records. *Scientific Reports, 6*, 26094. https://doi.org/10.1038/srep26094

Mirdita, M., Schütze, K., Moriwaki, Y., Heo, L., Ovchinnikov, S., & Steinegger, M. (2022). ColabFold: Making protein folding accessible to all. *Nature Methods, 19*(6), 679–682. https://doi.org/10.1038/s41592-022-01488-1

Moult, J., Fidelis, K., Kryshtafovych, A., Schwede, T., & Tramontano, A. (2014). Critical assessment of methods of protein structure prediction (CASP)—Round X. *Proteins: Structure, Function, and Bioinformatics, 82*(S2), 1–6.

Naik, N., Hameed, B. Z., Shetty, D. K., ... & Somani, B. K. (2022). Legal and ethical consideration in artificial intelligence in healthcare: A comprehensive review. *Frontiers in Public Health, 10*, 862322.

Naumov, P. S., Kholodov, V. P., Oseev, A. E., Osetrova, T. A., Artemov, A. D., Aliper, A., ... & Zhavoronkov, A. (2023). Chemistry42: An AI-driven platform for molecular design and optimization. *Journal of Chemical Information and Modeling, 63*(4), 1279–1290. https://doi.org/10.1021/acs.jcim.2c01191

Numerate, Inc. (2022). *Transforming drug discovery with data-driven AI*. https://numerate.com

Nussinov, R., Zhang, M., Liu, Y., & Cheng, L. (2022). AlphaFold2: A major leap for structural biology and drug discovery. *Signal Transduction and Targeted Therapy, 7*(1), 220.

Olivecrona, M., Blaschke, T., Engkvist, O., & Chen, H. (2017). Molecular de-novo design through deep reinforcement learning. *Journal of Cheminformatics, 9*(1), 48. https://doi.org/10.1186/s13321-017-0235-x

P360. (2022). *How AI is impacting pharmaceutical sales and marketing*. P360.

Pandey, M., Fernandez, M., Gentile, F., Isayev, O., Tropsha, A., Stern, A. C., & Cherkasov, A. (2022). The transformational role of GPU computing and deep learning in drug discovery. *Nature Machine Intelligence, 4*(3), 211–221.

Parenti, M. D., & Rastelli, G. (2012). Advances and applications of binding affinity prediction methods in drug discovery. *Biotechnology Advances, 30*(5), 244–250.

Paul, D., Sanap, G., Shenoy, S., Kalyane, D., Kalia, K., & Tekade, R. K. (2021). Artificial intelligence in drug discovery and development. *Drug Discovery Today, 26*(1), 80–93. https://doi.org/10.1016/j.drudis.2020.10.010

Paul, S. M., Mytelka, D. S., Dunwiddie, C. T., Persinger, C. C., Munos, B. H., Lindborg, S. R., & Schacht, A. L. (2010). How to improve R&D productivity: The pharmaceutical industry's grand challenge. *Nature Reviews Drug Discovery, 9*(3), 203–214.

Peters, J., Janzing, D., & Schölkopf, B. (2011). Elements of causal inference: Foundations and learning algorithms. *MIT Press*.

Polishchuk, P. G., Madzhidov, T. I., & Varnek, A. (2013). Estimation of the size of drug-like chemical space based on GDB-17 data. *Journal of Computer-Aided Molecular Design, 27*(8), 675–679. https://doi.org/10.1007/s10822-013-9672-4

Polykovskiy, D., Zhebrak, A., Sanchez-Lengeling, B., Golovanov, S., Tatanov, O., Belyaev, S., ... & Zhavoronkov, A. (2018). Molecular sets (MOSES): A benchmarking platform for molecular generation models. *Frontiers in Pharmacology, 11*, 1931.

Powles, J., & Hodson, H. (2017). Google DeepMind and healthcare in an age of algorithms. *Health and Technology, 7*, 351–367.

Pun, F. W., Liu, B. H. M., Long, X., Leung, H. W., Leung, G. H. D., Mewborne, Q. T., ... & Zhavoronkov, A. (2022). Identification of therapeutic targets for amyotrophic lateral sclerosis using PandaOmics—An AI-enabled biological target discovery platform. *Frontiers in Aging Neuroscience, 14*, 914017. https://doi.org/10.3389/fnagi.2022.914017

Pun, F. W., Ozerov, I. V., & Zhavoronkov, A. (2023). AI-powered therapeutic target discovery. *Trends in Pharmacological Sciences, 44*(9), 561–572. https://doi.org/10.1016/j.tips.2023.06.010

Putin, E., Asadulaev, A., Ivanenkov, Y., Aladinskiy, V., Sanchez-Lengeling, B., Aspuru-Guzik, A., & Zhavoronkov, A. (2018). Reinforced adversarial neural computer for de novo molecular design. *Journal of Chemical Information and Modeling, 58*(6), 1194–1204.

Qiu, T., Qiu, J., Feng, J., ... & Zheng, W. (2017). Recent progress in proteochemometric modelling. *Briefings in Bioinformatics, 18*(1), 125–136.

Qureshi, R., Irfan, M., Gondal, T. M., Khan, S., Wu, J., Hadi, M. U., ... & Mahmood, A. (2023). AI in drug discovery and its clinical relevance. *Heliyon, 9*(5), e16214.

Ren, F., Ding, X., Zheng, M., Korzinkin, M., Cai, X., Zhu, W., ... & Zhavoronkov, A. (2023). AlphaFold accelerates artificial intelligence powered drug discovery: Efficient discovery of a novel CDK20 small molecule inhibitor. *Chemical Science, 14*(6), 1443–1452. https://doi.org/10.1039/d2sc05709c

Sanchez-Lengeling, B., & Aspuru-Guzik, A. (2018). Inverse molecular design using machine learning: Generative models for matter engineering. *Science, 361*(6400), 360–365.

Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M., & Monfardini, G. (2008). The graph neural network model. *IEEE Transactions on Neural Networks, 20*(1), 61–80.

Schneider, G. (2018). Automating drug discovery. *Nature Reviews Drug Discovery, 17*(2), 97–113. https://doi.org/10.1038/nrd.2017.232

Schneider, G. (2021). An insight into artificial intelligence in drug discovery: An interview with Professor Gisbert Schneider. *Expert Opinion on Drug Discovery, 16*(9), 933–935.

Schraagen, J. M., & van Diggelen, J. (2021). Human-AI collaboration in defense. *Frontiers in Artificial Intelligence, 4*, 746869.

Segler, M. H. S., Kogej, T., Tyrchan, C., & Waller, M. P. (2018). Generating focused molecule libraries for drug discovery with recurrent neural networks. *ACS Central Science, 4*(1), 120–131. https://doi.org/10.1021/acscentsci.7b00512

Sellwood, M. A., Ahmed, M., Segler, M. H., & Brown, N. (2018). Artificial intelligence in drug discovery. *Future Medicinal Chemistry, 10*(17), 2025–2028. https://doi.org/10.4155/fmc-2018-0212

Senior, A. W., Evans, R., Jumper, J., Kirkpatrick, J., Sifre, L., Green, T., ... & Hassabis, D. (2020). Improved protein structure prediction using potentials from deep learning. *Nature, 577*(7792), 706–710.

Shaki, F., Zamani, M., & Arjmand, F. (2024). Artificial intelligence in pharmaceuticals: Exploring applications and legal challenges. *Pharmaceutical and Biomedical Research, 10*(1), 1–10. https://doi.org/10.18502/pbr.v10i1.15620

Sierra-Sosa, D., Garcia-Zapirain, B., Castillo, C., Baxter, I., Alzahmi, F., & Elmaghraby, A. (2019). Artificial intelligence in healthcare: Review and prediction case studies. *Applied Soft Computing, 84*, 105556.

Sliwoski, G., Kothiwale, S., Meiler, J., & Lowe, E. W. (2014). Computational methods in drug discovery. *Pharmacological Reviews, 66*(1), 334–395.

Sotelo, R. (2023). *Quantum computing in pharmaceutical research*. Elsevier.

Stokes, J. M., Yang, K., Swanson, K., Jin, W., Cubillos-Ruiz, A., Donghia, N. M., ... & Collins, J. J. (2020). A deep learning approach to antibiotic discovery. *Cell, 180*(4), 688–702.e13.

Tang, J., Zhao, T., Li, Y., ... & Xu, L. (2024). Deep learning for protein structure prediction: An overview. *Journal of Molecular Biology, 434*(15), 167664.

Tong, X., Liu, X., Tan, X., Li, X., Jiang, J., Xiong, Z., Xu, T., Jiang, H., Qiao, N., & Zheng, M. (2021). Generative models for de novo drug design. *Journal of Medicinal Chemistry, 64*(19), 14011–14027. https://doi.org/10.1021/acs.jmedchem.1c00927

Trott, O., & Olson, A. J. (2010). AutoDock Vina: Improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. *Journal of Computational Chemistry, 31*(2), 455–461. https://doi.org/10.1002/jcc.21334

Urban, G., Hanker, A. B., & Garrett, J. T. (2023). Harnessing the power of AI to accelerate cancer drug discovery. *Cancer Discovery, 13*(5), 1085–1098.

Vamathevan, J., Clark, D., Czodrowski, P., Dunham, I., Ferran, E., Lee, G., ... & Zhao, S. (2019). Applications of machine learning in drug discovery and development. *Nature Reviews Drug Discovery, 18*(6), 463–477. https://doi.org/10.1038/s41573-019-0024-5

van Deursen, R., Ertl, P., Tetko, I. V., & Godin, G. (2020). GENTRL: Highly efficient SMILES explorer using autodidactic generative examination networks. *Journal of Cheminformatics, 12*(1), 22.

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. In *Advances in Neural Information Processing Systems*.

Veličković, P., Cucurull, G., Casanova, A., Romero, A., Liò, P., & Bengio, Y. (2018). Graph attention networks. *arXiv preprint arXiv:1710.10903*.

Wallach, I., Dzamba, M., & Heifets, A. (2015). AtomNet: A deep convolutional neural network for bioactivity prediction in structure-based drug discovery. *arXiv preprint arXiv:1510.02855*.

Wallach, I., Heifets, A., & Dzamba, M. (2024). AI in the fight against COVID-19. *ChemMedChem, 15*, 234–240.

Wang, F., Preininger, A. M., & Casalino, L. P. (2019). Opportunities and challenges in artificial intelligence for healthcare. *The Lancet Digital Health, 1*(1), e6–e7.

Wang, L., Wu, Y., Xie, H., ... & Zhang, Y. (2023). Quantum computing for drug discovery: A comprehensive review. *Drug Discovery Today, 28*(8), 103623.

Wang, Y., Ribeiro, J. M. L., & Tiwary, P. (2020). Machine learning approaches for analyzing and enhancing MD. *Current Opinion in Structural Biology, 61*, 139–145.

Wang, Y., Wang, J., Cao, Z., & Barati Farimani, A. (2022). Molecular contrastive learning via GNNs. *Nature Machine Intelligence, 4*, 279–287.

Wang, Y., Zhang, S., Li, Y., ... & Zhou, Y. (2017). Deep learning for drug discovery. *Expert Opinion on Drug Discovery, 12*(3), 235–248.

Waring, M. J., Arrowsmith, J., Leach, A. R., Leeson, P. D., Mandrell, S., Owen, R. M., ... & Weir, A. (2015). An analysis of the attrition of drug candidates from four major pharmaceutical companies. *Nature Reviews Drug Discovery, 14*(7), 475–486.

Watson, D. S., Krutzinna, J., Bruce, I. N., Griffiths, C. E., McInnes, I. B., Barnes, M. R., & Floridi, L. (2019). Clinical applications of machine learning algorithms: Beyond the black box. *BMJ, 364*, l886. https://doi.org/10.1136/bmj.l886

Weininger, D. (1988). SMILES, a chemical language and information system. 1. Introduction to methodology and encoding rules. *Journal of Chemical Information and Computer Sciences, 28*(1), 31–36. https://doi.org/10.1021/ci00057a005

West, S. M., Whittaker, M., & Crawford, K. (2018). Discriminating systems: Gender, race and power in AI. *AI Now Institute*.

Wigh, D. S., Goodman, J. M., & Lapkin, A. A. (2022). A review of molecular representation in the age of machine learning. *WIREs Computational Molecular Science, 12*(5), e1603. https://doi.org/10.1002/wcms.1603

Wu, R., Ding, F., Wang, R., Shen, R., Zhang, X., Luo, S., ... & Peng, J. (2022). High-resolution de novo structure prediction from primary sequence. *bioRxiv*. https://doi.org/10.1101/2022.07.21.500999

Wu, Z., Ramsundar, B., Feinberg, E. N., Gomes, J., Geniesse, C., Pappu, A. S., ... & Pande, V. (2018). MoleculeNet: A benchmark for molecular machine learning. *Chemical Science, 9*(2), 513–530. https://doi.org/10.1039/c7sc02664a

Xu, L., Sun, H., Li, Y., Wang, J., & Hou, T. (2013). Assessing MM/PBSA and MM/GBSA. *Journal of Physical Chemistry B, 117*(28), 8408–8421.

Yamanishi, Y., Kotera, M., Kanehisa, M., & Goto, S. (2010). DTI prediction from chemical, genomic and pharmacological data. *Bioinformatics, 26*(18), 246–254.

Yang, H., Lou, C., Sun, L., Li, J., Cai, Y., Wang, Z., Li, W., Liu, G., & Tang, Y. (2019). admetSAR 2.0: Web-service for prediction and optimization of chemical ADMET properties. *Bioinformatics, 35*(6), 1067–1069. https://doi.org/10.1093/bioinformatics/bty707

Yang, K., Swanson, K., Jin, W., Coley, C., Eiden, P., Gao, H., Guzman-Perez, A., Hopper, T., Kelley, B., Mathew, R., Palmer, A., Settels, V., Jaakkola, T., Jensen, K., & Barzilay, R. (2019). Analyzing learned molecular representations for property prediction. *Journal of Chemical Information and Modeling, 59*(8), 3370–3388.

Yu, K.-H., Beam, A. L., & Kohane, I. S. (2018). Artificial intelligence in healthcare. *Nature Biomedical Engineering, 2*(10), 719–731.

Zhang, Y., Zhou, Y., & Li, X. (2023). Protein language models: A new era in structural biology. *Trends in Biochemical Sciences, 48*(2), 120–135.

Zhavoronkov, A. (2022). *Artificial intelligence in drug discovery and development*. Elsevier.

Zhavoronkov, A., Ivanenkov, Y. A., Aliper, A., Veselov, M. S., Aladinskiy, V. A., Aladinskaya, A. V., ... & Aspuru-Guzik, A. (2019). Deep learning enables rapid identification of potent DDR1 kinase inhibitors. *Nature Biotechnology, 37*(9), 1038–1040. https://doi.org/10.1038/s41587-019-0224-x

Zhavoronkov, A., Vanhaelen, Q., & Oprea, T. I. (2020). Will artificial intelligence for drug discovery impact clinical pharmacology? *Clinical Pharmacology & Therapeutics, 107*, 780–785.

Zhou, W., & Yan, H. (2014). Alpha shape and Delaunay triangulation in protein interactions. *Briefings in Bioinformatics, 15*(1), 54–64.

Zhu, H., Zhang, G., & Li, Y. (2023). AlphaFold-accelerated discovery of small molecule inhibitors. *Journal of Medicinal Chemistry, 66*(5), 3456–3468.

Zhu, Y., Li, X., & Zhang, Q. (2022). Platforms for AI-driven drug discovery. *Drug Discovery Today, 27*(8), 2134–2145.

Zinner, M., Lang, T., & Reiter, F. (2021). Quantum computing for molecular biology. *Nature Reviews Physics, 3*, 625–637.

---

<div style="font-family: 'Times New Roman', Times, serif; font-size: 16pt;">

# Abbreviations

**AAE**: Adversarial Auto-encoder  
**ADMET**: Absorption, Distribution, Metabolism, Excretion, and Toxicity  
**AE**: Auto-encoder  
**AI**: Artificial Intelligence  
**ANN**: Artificial Neural Network  
**AUC**: Area Under the Curve  
**BERT**: Bidirectional Encoder Representations from Transformers  
**CASP**: Critical Assessment of Structure Prediction  
**CDK20**: Cyclin-dependent kinase 20  
**CNN**: Convolutional Neural Network  
**DILI**: Drug-Induced Liver Injury  
**DL**: Deep Learning  
**DTI**: Drug–Target Interaction  
**EA**: Evolutionary Algorithm  
**EC**: Eye Corrosion  
**ECFP**: Extended Connectivity Fingerprint  
**EHR**: Electronic Health Record  
**EI**: Eye Irritation  
**ELFC**: Enrichment Log Fold Change  
**eQTL**: Expression Quantitative Trait Locus  
**ESM-2**: Evolutionary Scale Modeling 2  
**FBDD**: Fragment-Based Drug Design  
**FDA**: Food and Drug Administration  
**GAN**: Generative Adversarial Network  
**GNN**: Graph Neural Network  
**GPT**: Generative Pre-training Transformer  
**GRU**: Gated Recurrent Unit  
**GWAS**: Genome-Wide Association Study  
**HCC**: Hepatocellular Carcinoma  
**HDAC**: Histone Deacetylase  
**HGPV**: Hypergeometric P-Value  
**HTS**: High-Throughput Screening  
**IC50**: Half Maximal Inhibitory Concentration  
**InChI**: International Chemical Identifier  
**IND**: Investigational New Drug  
**k-NN**: k-Nearest Neighbour  
**LBDD**: Ligand-Based Drug Design  
**LLM**: Large Language Model  
**LSTM**: Long Short-Term Memory  
**MAE**: Mean Absolute Error  
**MD**: Molecular Dynamics  
**ML**: Machine Learning  
**MM-GBSA**: Molecular Mechanics/Generalized Born Surface Area  
**NCD**: Non-Communicable Disease  
**NLP**: Natural Language Processing  
**PAE**: Predicted Aligned Error  
**PCM**: Proteochemometric  
**PDB**: Protein Data Bank  
**PK/PD**: Pharmacokinetics/Pharmacodynamics  
**pLDDT**: Predicted Local Distance Difference Test  
**PLM**: Protein Language Model  
**PPI**: Protein–Protein Interaction  
**QC**: Quantum Computing  
**QSAR**: Quantitative Structure–Activity Relationship  
**QSPR**: Quantitative Structure–Property Relationship  
**RF**: Random Forest  
**RL**: Reinforcement Learning  
**RNN**: Recurrent Neural Network  
**ROC**: Receiver Operating Characteristic  
**SBDD**: Structure-Based Drug Design  
**scRNA-seq**: Single-Cell RNA Sequencing  
**SMILES**: Simplified Molecular Input Line Entry System  
**ST**: Spatial Transcriptomics  
**SVM**: Support Vector Machine  
**T5**: Text-to-Text Transfer Transformer  
**VAE**: Variational Autoencoder  
**Vd**: Volume of Distribution  

### Symbols

**Lowercase**

*k*: Rate constant / Number of neighbors  
*n*: Sample size  
*p*: Probability value  

**Uppercase**

*K*: Equilibrium constant (e.g., Kd)  
*T*: Temperature / Index  

**Greek Letters**

µ: Micro (prefix, 10^-6)

</div>
