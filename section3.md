## 3. AI for Drug Candidate Design and Screening

### 3.1 AI-Accelerated Virtual Screening

#### 3.1.1 Molecular representation: inputting molecules into AI models (SMILES strings, molecular graphs, fingerprints)

Advances in cheminformatics and artificial intelligence (AI) have
introduced several approaches to molecular representation. Traditional
methods rely on rule-based feature extraction, such as molecular
descriptors that quantify physical or chemical properties, and molecular
fingerprints that encode substructural information as binary strings or
numerical values. The most common representation is the Simplified
Molecular Input Line Entry System (SMILES), which provides a compact and
efficient way to encode chemical structures as strings (Wigh et al., 2022;
Weininger, 1988). Despite its simplicity, SMILES has limitations in
capturing the complexity of molecular interactions. As drug discovery
tasks become more sophisticated, traditional string-based
representations often fail to fully reflect the relationships between
molecular structure and key drug-related characteristics such as
biological activity and physicochemical properties (Y. Li et al., 2024). While
traditional methods are interpretable, they often struggle to navigate
the vast chemical space in search of compounds with desired biological
properties. Therefore, molecular representation should not only encode
the chemical structure, but also enable efficient exploration of
chemical space. In recent years, AI-driven molecular representation
methods have applied deep learning techniques to learn high-dimensional
embeddings directly from large datasets. Models such as graph neural
networks (GNNs), variational auto-encoders (VAEs), and transformers
enable these approaches to move beyond predefined rules, capturing both
local and global molecular features (Kim et al., 2016; Mendez et al., 2019;
Irwin et al., 2020). These modern representations better
describe structural and functional relationships, providing powerful
tools for molecular generation, scaffold hopping, lead compound
optimization, and other tasks in drug discovery (Tong et al., 2021; Z. Li et al., 2024).

##### Molecular fingerprinting

Molecular fingerprinting is a
computational technique that transforms chemical structures into compact
numerical representations, such as bit vectors or feature arrays, to
capture key structural and physicochemical properties. These
fingerprints facilitate rapid comparison, similarity searches, and
machine learning tasks, making them invaluable in drug discovery and
materials science. Common types include circular fingerprints like
Extended Connectivity Fingerprints (ECFP) for substructure patterns,
path-based fingerprints for bond sequences, and 3D fingerprints for
molecular shapes (Z. Li et al., 2024). Unlike natural language processing
(NLP), which processes human language, molecular fingerprinting encodes
chemical \"grammar,\" such as functional groups and bonds, rather than
linguistic semantics. While natural language processing (NLP) models
like transformers can analyze molecules via SMILES strings, traditional
fingerprinting relies on cheminformatics algorithms for applications
like virtual screening and toxicity prediction. Tools such as
Chemical Descriptor Calculation Platform (ChemDes) (Dong et al., 2015)
are widely used to compute fingerprints efficiently, bridging the gap
between chemistry and AI. However, challenges
remain in optimizing fingerprint methods for diverse molecular datasets
and improving their predictive power in biological contexts. For
instance, ECFPs have proven effective in structure-activity modeling and
similarity searching.

#### 3.1.2 Predictive screening (QSAR/QSPR): using ML/DL to predict compound activity and properties before synthesis

AI-powered virtual screening and other in silico approaches accelerate
lead identification by enabling rapid prioritization of compounds before
synthesis and experimental testing (Paul et al., 2021). A common
strategy is to build quantitative structure--activity relationship
(QSAR/QSPR) models that learn relationships between chemical structure
and activity or physicochemical properties.

In practice, model reliability depends strongly on the quality and
coverage of training data. Public resources such as PubChem, ChEMBL, and
ZINC provide large-scale compound and bioactivity datasets that support
predictive modeling workflows (Kim et al., 2016; Mendez et al., 2019;
Irwin et al., 2020).

#### 3.1.3 AI-enhanced molecular docking: improving the accuracy and speed of docking simulations

Molecular docking is widely used to prioritize potential lead compounds
by predicting plausible binding poses and estimating binding affinity.
Docking workflows typically include binding pocket identification,
conformational sampling, scoring, and ranking.

With the availability of large numbers of predicted protein structures
from methods such as AlphaFold and ColabFold, docking is increasingly
performed when no co-crystal ligand (and sometimes no binding pocket
annotation) is available (Jumper et al., 2021; Mirdita et al., 2022).

Traditional docking engines such as AutoDock Vina and Glide remain
widely used (Friesner et al., 2004; Trott & Olson, 2010). A practical
strategy to improve runtime is to reduce the search space by predicting
likely ligand-binding sites. Examples include P2Rank and DeepSite
(Jiménez et al., 2017; Krivák & Hoksza, 2018).

Learning-based methods can also model docking directly. DiffDock, for
example, treats docking as a generative problem using diffusion models
(Corso et al., 2022). Curated datasets and benchmarking remain
important for robust learning and evaluation in docking and rescoring
(Francoeur et al., 2020).

### 3.2 De Novo Drug Design

#### 3.2.1 Definition: using algorithms to design entirely new molecules from scratch

De novo molecular design aims to create new chemical entities with
desired properties and/or activities. This is an inherently difficult
task owing to the immense search space of feasible molecules, from which
only a small fraction typically have the desired traits (Polishchuk et
al., 2013). As such, de novo molecular design has historically relied
heavily on expert knowledge and iterative experimentation (Schneider,
2018). Recent reviews emphasize that generative modeling can be used to
propose candidate structures that are subsequently filtered and
prioritized using predictive models and screening pipelines (Tong et
al., 2021).

#### 3.2.2 Challenges: navigating the immense size of chemical space

The chemical search space is extremely large, and practical success
requires balancing exploration with constraints such as
synthesizability, drug-likeness, and downstream developability
(Polishchuk et al., 2013; Schneider, 2018).

#### 3.2.3 Key models and tools

Deep generative models have become central to modern de novo design.
Recurrent neural networks (RNNs), often implemented with Long
Short-Term Memory (LSTM) units, support sequence-based generation such
as SMILES (Hochreiter & Schmidhuber, 1997). RNN-based approaches have
been used to generate focused libraries in drug discovery (Segler et
al., 2018), and reinforcement learning has been applied to steer
generation toward desirable objectives (Olivecrona et al., 2017).

Variational auto-encoders (VAEs) provide an alternative framework that
learns a continuous latent representation that can be sampled and
optimized (Kingma & Welling, 2014). Overall, current generative
approaches are frequently combined with property predictors and
screening to improve the quality of proposed candidates (Tong et al.,
2021).

#### 3.2.4 Impact

In principle, de novo design can accelerate early-stage ideation and
optimization by proposing novel candidates and enabling rapid
iteration; however, the value of these methods depends on data quality,
model validation, and integration with experimental workflows
(Paul et al., 2021; Schneider, 2018).

### 3.3 AI in ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity) profiling

#### 3.3.1 Predicting pharmacokinetics and pharmacodynamics

The key concepts of pharmacology include pharmacokinetics and
pharmacodynamics. While pharmacodynamics focuses on how a drug affects
biological systems, pharmacokinetics studies absorption, distribution,
metabolism, and elimination (ADME). In this context, AI can support
earlier estimation of ADME-related parameters and enable prioritization
of candidates during lead optimization.

With improved training data and model development, tools such as
admetSAR 2.0 support prediction and optimization of ADMET properties
(Yang et al., 2019). In addition, work on AI for compound
pharmacokinetics prediction highlights opportunities and limitations for
practical use in drug discovery pipelines (Obrezanova, 2023).

#### 3.3.2 Using multi-task learning to create comprehensive safety profiles

The stringent safety requirements associated with drug development make
it challenging to introduce new drugs to the market. Clinical trials can
fail due to unexpected toxicity, and post-marketing surveillance may
reveal safety issues not detected earlier.

AI-based toxicity prediction can support earlier risk assessment by
learning from historical compound and assay data. For example, Minerali
et al. compared machine learning models for predicting drug-induced
liver injury (DILI) (Minerali et al., 2020). Mamoshina et al. used
machine learning to predict major clinical forms of drug cardiotoxicity
(Mamoshina et al., 2020).

## References

- Corso, G., Stärk, H., Jing, B., Barzilay, R., & Jaakkola, T. (2022). DiffDock: Diffusion steps, twists, and turns for molecular docking (arXiv:2210.01776). arXiv. https://arxiv.org/abs/2210.01776
- Dong, J., Cao, D.S., Miao, H.Y., Liu, S., Deng, B.C., Yun, Y.H., Wang, N.N., Lu, A.P., Zeng, W.B., & Chen, A.F. (2015). ChemDes: an integrated web-based platform for molecular descriptor and fingerprint computation. Journal of Cheminformatics, 7(1), 60. https://doi.org/10.1186/s13321-015-0109-z
- Francoeur, P.G., Masuda, T., Sunseri, J., Jia, A., Iovanisci, R.B., Snyder, I., & Koes, D.R. (2020). Three-Dimensional Convolutional Neural Networks and a Cross-Docked Data Set for Structure-Based Drug Design. Journal of Chemical Information and Modeling, 60(9), 4200-4215. https://doi.org/10.1021/acs.jcim.0c00411
- Friesner, R.A., Banks, J.L., Murphy, R.B., Halgren, T.A., Klicic, J.J., Mainz, D.T., Repasky, M.P., Knoll, E.H., Shelley, M., Perry, J.K., Shaw, D.E., Francis, P., & Shenkin, P.S. (2004). Glide: A New Approach for Rapid, Accurate Docking and Scoring. 1. Method and Assessment of Docking Accuracy. Journal of Medicinal Chemistry, 47(7), 1739-1749. https://doi.org/10.1021/jm0306430
- Hochreiter, S., & Schmidhuber, J. (1997). Long Short-Term Memory. Neural Computation, 9(8), 1735-1780. https://doi.org/10.1162/neco.1997.9.8.1735
- Irwin, J.J., Tang, K.G., Young, J., Dandarchuluun, C., Wong, B.R., Khurelbaatar, M., Moroz, Y.S., Mayfield, J., & Sayle, R.A. (2020). ZINC20—A Free Ultralarge-Scale Chemical Database for Ligand Discovery. Journal of Chemical Information and Modeling, 60(12), 6065-6073. https://doi.org/10.1021/acs.jcim.0c00675
- Jiménez, J., Doerr, S., Martínez-Rosell, G., Rose, A.S., & De Fabritiis, G. (2017). DeepSite: protein-binding site predictor using 3D-convolutional neural networks. Bioinformatics, 33(19), 3036-3042. https://doi.org/10.1093/bioinformatics/btx350
- Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Žídek, A., Potapenko, A., Bridgland, A., Meyer, C., Kohl, S.A.A., Ballard, A.J., Cowie, A., Romera-Paredes, B., Nikolov, S., Jain, R., Adler, J., …, Hassabis, D. (2021). Highly accurate protein structure prediction with AlphaFold. Nature, 596(7873), 583-589. https://doi.org/10.1038/s41586-021-03819-2
- Kim, S., Thiessen, P.A., Bolton, E.E., Chen, J., Fu, G., Gindulyte, A., Han, L., He, J., He, S., Shoemaker, B.A., Wang, J., Yu, B., Zhang, J., & Bryant, S.H. (2016). PubChem Substance and Compound databases. Nucleic Acids Research, 44(D1), D1202-D1213. https://doi.org/10.1093/nar/gkv951
- Kingma, D. P., & Welling, M. (2014). Auto-encoding variational Bayes (arXiv:1312.6114). arXiv. https://arxiv.org/abs/1312.6114
- Krivák, R., & Hoksza, D. (2018). P2Rank: machine learning based tool for rapid and accurate prediction of ligand binding sites from protein structure. Journal of Cheminformatics, 10(1), 39. https://doi.org/10.1186/s13321-018-0285-8
- Li, Y., Liu, B., Deng, J., Guo, Y., & Du, H. (2024). Image-based molecular representation learning for drug development: a survey. Briefings in Bioinformatics, 25(4), bbae294. https://doi.org/10.1093/bib/bbae294
- Li, Z., Huang, R., Xia, M., Patterson, T.A., & Hong, H. (2024). Fingerprinting Interactions between Proteins and Ligands for Facilitating Machine Learning in Drug Discovery. Biomolecules, 14(1), 72. https://doi.org/10.3390/biom14010072
- Mamoshina, P., Bueno-Orovio, A., & Rodriguez, B. (2020). Dual Transcriptomic and Molecular Machine Learning Predicts all Major Clinical Forms of Drug Cardiotoxicity. Frontiers in Pharmacology, 11, 639. https://doi.org/10.3389/fphar.2020.00639
- Mendez, D., Gaulton, A., Bento, A.P., Chambers, J., De Veij, M., Félix, E., Magariños, M.P., Mosquera, J.F., Mutowo, P., Nowotka, M., Gordillo-Marañón, M., Hunter, F., Junco, L., Mugumbate, G., Rodriguez-Lopez, M., Atkinson, F., Bosc, N., Radoux, C.J., Segura-Cabrera, A., …, Leach, A.R. (2019). ChEMBL: towards direct deposition of bioassay data. Nucleic Acids Research, 47(D1), D930-D940. https://doi.org/10.1093/nar/gky1075
- Minerali, E., Foil, D.H., Zorn, K.M., Lane, T.R., & Ekins, S. (2020). Comparing Machine Learning Algorithms for Predicting Drug-Induced Liver Injury (DILI). Molecular Pharmaceutics, 17(7), 2628-2637. https://doi.org/10.1021/acs.molpharmaceut.0c00326
- Mirdita, M., Schütze, K., Moriwaki, Y., Heo, L., Ovchinnikov, S., & Steinegger, M. (2022). ColabFold: making protein folding accessible to all. Nature Methods, 19(6), 679-682. https://doi.org/10.1038/s41592-022-01488-1
- Obrezanova, O. (2023). Artificial intelligence for compound pharmacokinetics prediction. Current Opinion in Structural Biology, 79, 102546. https://doi.org/10.1016/j.sbi.2023.102546
- Olivecrona, M., Blaschke, T., Engkvist, O., & Chen, H. (2017). Molecular de-novo design through deep reinforcement learning. Journal of Cheminformatics, 9(1), 48. https://doi.org/10.1186/s13321-017-0235-x
- Paul, D., Sanap, G., Shenoy, S., Kalyane, D., Kalia, K., & Tekade, R.K. (2021). Artificial intelligence in drug discovery and development. Drug Discovery Today, 26(1), 80-93. https://doi.org/10.1016/j.drudis.2020.10.010
- Polishchuk, P.G., Madzhidov, T.I., & Varnek, A. (2013). Estimation of the size of drug-like chemical space based on GDB-17 data. Journal of Computer-Aided Molecular Design, 27(8), 675-679. https://doi.org/10.1007/s10822-013-9672-4
- Schneider, G. (2018). Automating drug discovery. Nature Reviews Drug Discovery, 17(2), 97-113. https://doi.org/10.1038/nrd.2017.232
- Segler, M.H.S., Kogej, T., Tyrchan, C., & Waller, M.P. (2018). Generating Focused Molecule Libraries for Drug Discovery with Recurrent Neural Networks. ACS Central Science, 4(1), 120-131. https://doi.org/10.1021/acscentsci.7b00512
- Tong, X., Liu, X., Tan, X., Li, X., Jiang, J., Xiong, Z., Xu, T., Jiang, H., Qiao, N., & Zheng, M. (2021). Generative Models for De Novo Drug Design. Journal of Medicinal Chemistry, 64(19), 14011-14027. https://doi.org/10.1021/acs.jmedchem.1c00927
- Trott, O., & Olson, A.J. (2010). AutoDock Vina: Improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. Journal of Computational Chemistry, 31(2), 455-461. https://doi.org/10.1002/jcc.21334
- Weininger, D. (1988). SMILES, a chemical language and information system. 1. Introduction to methodology and encoding rules. Journal of Chemical Information and Computer Sciences, 28(1), 31-36. https://doi.org/10.1021/ci00057a005
- Wigh, D.S., Goodman, J.M., & Lapkin, A.A. (2022). A review of molecular representation in the age of machine learning. WIREs Computational Molecular Science, 12(5), e1603. https://doi.org/10.1002/wcms.1603
- Yang, H., Lou, C., Sun, L., Li, J., Cai, Y., Wang, Z., Li, W., Liu, G., & Tang, Y. (2019). admetSAR 2.0: web-service for prediction and optimization of chemical ADMET properties. Bioinformatics, 35(6), 1067-1069. https://doi.org/10.1093/bioinformatics/bty707
