> **CHAPTER4: REAL-WORLD IMPACT, CHALLENGES, AND FUTURE LANDSCAPE**
>
> 4.1. **PIONEERING PLATFORMS AND REAL-WORLD CASE STUDIES**
>
> 4.1.1. **Deepmind's Alphafold: Revolutionizing Structural Biology**:
>
> The Pinnacle of Protein Language Modeling. The rise of Transformer
> models has fundamentally transformed how computers process sequential
> data, moving from older methods like Recurrent Neural Networks (RNNs)
> to highly efficient, parallel processing via the self-attention
> mechanism. This revolution, driven by models like Bidirectional
> Encoder Representations from Transformers (BERT), generative
> Pre-training Transformer (GPT), and Text-to-Text Transfer Transformer
> (T5), has extended powerfully into computational biology, giving rise
> to Protein Language Models (PLMs) (Zhang, S., et al. 2023).
>
> PLMs apply the transformer architecture to biological sequences,
> treating a protein\'s amino acids like the \"alphabet\" of a language.
> By training on vast protein databases, these models have enabled
> breakthroughs in function annotation, protein design, and mutation
> effect prediction, but their most transformative success lies in
> protein structure prediction.
>
> AlphaFold2 stands as the definitive example of this progress. It
> utilizes the transformer architecture to predict a protein\'s 3D
> structure from its amino acid sequence with exceptional speed and
> accuracy. This capability, achieved by decoding the protein\'s
> \"language,\" has solved a decades-old grand challenge in biology.
>
> While researchers use Natural Language Processing (NLP) algorithms to
> mine scientific literature, patents, and Electronic Health Records
> (EHRs) for drug candidates and targets (Agarwal, P., & Searls, D. B.
> 2008); (Kosonocky, C. W., et al. 2024), the structural insight provided
> by AlphaFold2 is a direct, critical input.
>
> Other benefits of PLMs include the use of pretrained models like
> Evolutionary Scale Modeling 2 (ESM-2) which, for example, uses 15
> billion parameters to predict protein structures (Lin, Z., et al.
> 2023) and ProtGPT2 for transfer learning, as well as leveraging
> unsupervised learning from databases like UniProt. Models like
> OmegaFold (Wu, R., et al. 2022). further enhance this by incorporating
> geometric awareness using 3D structural data.
>
> Despite AlphaFold2\'s groundbreaking success in structure prediction,
> challenges remain, including high computational costs and the
> difficulty of interpreting complex AI output (Bepler, T., & Berger, B.
> 2021); (Ferruz et al. 2022). Nevertheless, its achievement in using
> the transformer architecture to map sequence to structure highlights
> the profound potential of AI to accelerate scientific discovery.
>
> 4.1.1.1. **Its Role In Accurately Predicting The 3D Structure Of
> Proteins:**
>
> The groundbreaking AI system AlphaFold2 is celebrated for its ability
> to predict protein structure with exceptional speed and accuracy. This
> represents a major scientific advance in understanding the fundamental
> building blocks of life.
>
> However, translating this high-accuracy prediction into the complexity
> of the in vivo (living system) situation remains an open challenge.
>
> There are specific limitations when applying AlphaFold2 directly to
> traditional medicinal chemistry:
>
> Unbound Structures: AlphaFold2 is trained primarily to predict unbound
> protein structures (proteins alone), whereas most drug discovery
> efforts require structures of protein-small molecule complexes
> (AlQuraishi, M. 2020).
>
> 4.1.1.2. **The impact on structure-based drug design and understanding
> disease targets:**
>
> Predicting the three-dimensional structures of potential target
> proteins, solely from their amino acid sequence, is often necessary
> for drug discovery. AI systems had a major recent success in this,
> with AlphaFold2 (Jumper et al., 2021).winning the Critical Assessment
> of Structure Prediction (CASP14) (Moult et al., 2014). This structural
> biology advance is projected to fundamentally transform personalized
> medicine and drug discovery. AlphaFold represents a pivotal leap
> forward in leveraging Artificial Intelligence (AI) within structural
> biology and the broader life sciences  (Nussinov et al., 2022).
> AlphaFold, predicts protein structures with remarkable accuracy. This
> effectively tackles a persistent challenge in biology, as having
> precise protein structure predictions is vital for both understanding
> how diseases work and finding promising drug targets (Jumper et al.,
> 2021).
>
> 4.1.2. **END-TO-END GENERATIVE AI PLATFORMS: THE INSILICO MEDICINE
> EXAMPLE**
>
> **4.1.2.1. Overview Of Their Pharma. AI Platform (Pandaomics For Target
> Identification, Chemistry42 For De Novo Molecule Generation):**
>
> The AI drug discovery journey began with Insilico Medicine, which
> published one of the first methods using a deep learning approach to
> discover new targets (Wang et al., 2017); (West et al., 2018).
>
> This has since evolved into combining classical bioinformatics with
> advanced AI for disease mechanism reconstruction and target
> identification (Pun et al., 2023).
>
> A key recent advance is the use of tools like AlphaFold to explore
> targets previously inaccessible for small molecule development. The
> resulting de novo design of active molecules for these difficult
> targets has been validated in both in vitro and in vivo assays (Ren et
> al., 2023); ( Zhu et al., 2023).
>
> **The PandaOmics platform** leverages these and other rapid
> developments in computer-aided drug discovery, specifically
> incorporating large language models and robotics to accelerate the
> process (Schneider, G. 2018); (Urban et al., 2023)..**The PandaOmics
> platform** is a sophisticated, AI-driven engine designed for
> Therapeutic Target Identification. Its core feature is a user-friendly
> meta-analysis dashboard that produces a highly refined, ranked list of
> potential target genes.
>
> This robust ranking is achieved by utilizing 23 distinct
> disease-specific models, which fall into two primary, complementary
> categories:
>
> 1-Omics-Based Models (Data-Driven Insight):
>
> These techniques integrate comprehensive data from the meta-analysis,
> including gene expression, methylation, proteomics, and genetic
> information. They are further enriched by network analysis using
> biological graphs from Protein-Protein Interaction (PPI) and signaling
> databases and knowledge graphs derived from scientific literature.
>
> **Simpler Approaches**: These include standard bioinformatic
> approaches like the expression score, which provides a foundational
> assessment of gene significance based on differential expression in
> disease versus control samples in relevant tissues.
>
> **Advanced Techniques:** This group employs complex machine learning,
> such as the heterogeneous graph walk algorithm. This algorithm
> performs a guided random walk on a graph where nodes represent genes
> and diseases. By learning the relationships between these nodes, the
> model identifies gene nodes with the closest association to the
> reference disease, enabling the discovery of new targets.
>
> 2-Text-Based Models (Literature & Trend Analysis):
>
> These models assess potential targets based on information extracted
> from textual sources, including publications, clinical trials, and
> grant applications. Crucially, they factor in the credibility of the
> source and current scientific trends to gauge the target\'s industry
> relevance and novelty.
>
> In essence, PandaOmics synthesizes evidence from both high-dimensional
> biological data (Omics) and global scientific literature (Text) to
> deliver a holistic and prioritized set of therapeutic hypotheses (Pun
> et al., 2022).
>
> **AI Capabilities and Validation of the PandaOmics Platform**
>
> The PandaOmics platform offers a comprehensive set of AI capabilities
> for discovering therapeutic targets and developing biomarkers. The
> platform achieves this by utilizing dynamic omics data and advanced
> algorithms to power data exploration, pathway analysis, and
> meta-analysis, ultimately deepening the insights gained from datasets.
>
> PandaOmics provides a highly user-friendly interface that includes
> customizable ranking approaches and filters, enabling researchers to
> precisely refine their gene lists based on various criteria. The
> platform\'s utility is further extended through integration with a
> robotic lab, which boosts the efficiency and accuracy of validating
> targets and screening compounds. By harmonizing diverse data sources
> and employing advanced language models, PandaOmics equips researchers
> to make better, more informed decisions in their pursuit of novel
> therapeutics and biomarkers.
>
> **Predictive Model Validation**
>
> The PandaOmics target discovery engine has undergone rigorous
> validation to confirm its effectiveness in identifying novel targets.
> Two core metrics were used to measure the performance of its
> predictive models.
>
> **1-** **Enrichment Log Fold Change (ELFC):** This metric represents
> the log-transformed fold change of enrichment. It quantifies the
> degree to which the top-ranked genes in a list are enriched with known
> targets.
>
> **2- Hypergeometric P-Value (HGPV):** This metric measures the
> statistical significance of the enrichment effect. It indicates the
> likelihood of achieving the same level of enrichment if the genes were
> listed randomly.
>
> For a ranking approach to demonstrate higher predictive power, it must
> achieve higher values for both ELFC and HGPV. All models within
> PandaOmics have been thoroughly validated using these ELFC and HGPV
> coordinates, both generally and across specific therapeutic areas (Pun
> et al., 2022).
>
> **Chemistry42: The AI-Driven Platform for De Novo Molecular Design**
>
> Chemistry42, a platform that has evolved significantly over the past
> years (Zhavoronkov, A. 2022), is now routinely and successfully
> employed at Insilico Medicine, serving as the engine to drive the drug
> discovery process across several therapeutic areas.
>
> **Designing Generative Experiments**
>
> Users initiate the design of novel molecules through Chemistry42\'s
> user-friendly web-based interface. Experiments can be configured using
> either Ligand-Based Drug Design (LBDD) or Structure-Based Drug Design
> (SBDD), depending on the available information for the target of
> interest.
>
> LBDD requires a 2D or 3D ligand structure as input (via .sdf file,
> Simplified Molecular Input Line Entry System (SMILES) string, or
> sketched directly). A pharmacophore hypothesis can also be manually or
> automatically added.
>
> SBDD requires the upload of a prepared protein target structure (.pdb
> file), which can be in the apo format or already complexed with a
> ligand. Users can either define the pocket around a known ligand or
> select a site identified by the Pocket Scanner Module. A pharmacophore
> hypothesis can also be included.
>
> To complete the experiment setup, users define acceptable ranges for
> numerous properties (like physicochemical properties and diversity),
> prioritize the reward modules by adjusting their weights, and set
> corresponding thresholds to control how restrictive the modules are.
> Advanced options in both workflows allow for fine-tuning the reward
> modules and selecting specific generative models. For quick
> configuration, the Autoconfiguration feature adjusts all parameters
> automatically based on the input data  (Naumov et al., 2023).
>
> **Enhancing Workflows with Anchor Points**
>
> Workflows such as hit expansion, hit-optimization, and Fragment-Based
> Drug Design (FBDD) are supported through the Anchor points
> functionality. Anchor points allow users to fix specified cores or
> R-groups of a hit molecule in 3D space while the generative experiment
> varies the rest of the structure. This feature also supports multiple
> reference substructures by allowing users to edit atom types to
> include alternatives (e.g., specifying whether to see nitrogen or
> carbon in an aromatic ring using SMILES Arbitrary Target Specification
> (SMARTS)  (Naumov et al., 2023).
>
> **The Power of Ensemble AI**
>
> The platform\'s generative pipeline employs an asynchronous ensemble
> of proprietary generative models. This carefully curated collection
> includes over 40 generative models with diverse
> architectures---including generative autoencoders (Zhavoronkov et al.,
> 2019); (Polykovskiy et al., 2018). generative adversarial networks
>  (Kadurin et al., 2017); (Kadurin et al., 2017); (Putin et al.,
> 2018), flow-based approaches (Kuznetsov, M., & Polykovskiy, D.
> 2021), evolutionary algorithms (Devi et al., 2015) and language models
> (Segler et al., 2018).
>
> These models utilize different molecular representations
> (string-based, graph-based, and 3D-based) and are deployed
> strategically to maximize the platform\'s efficiency. By facilitating
> the interplay of these diverse models, Chemistry42 can deliver
> diverse, high-quality molecular structures within hours. The generated
> structures are then dynamically assessed using the platform\'s
> integrated reward and scoring modules. The system emphasizes providing
> deep domain-specific analytics to ensure users understand the
> strengths and weaknesses of each AI approach, rather than treating
> them as black-box solutions.
>
> ![](media/image1.jpg){width="6.040512904636921in"
> height="5.697916666666667in"}
>
> **Figure 1.** A schematic representation of the three-step workflow for a de novo generative experiment using the Chemistry42 platform. In the
> first step, on a secure and company-specific instance of the software, users
>
> upload their data and configure the platform with the desired
> properties for the generated structures. The second step involves running the
>
> platform where an ensemble of 40+ generative models functions in
>
> parallel to generate the novel structures this step is called the
>
> generation phase. A variety of filters scrutinize the generated
> molecular structures in the generation phase. The molecular structures are then
>
> subjected to multiple sets of reward and scoring modules, classified
> as either 2D or 3D modules, that dynamically assess the generated
>
> structures' properties according to the predefined criteria.
> Additional
>
> custom scoring modules (such as ADME predictors) can also be
>
> integrated into the reward pipeline to prioritize the generated
>
> structures. These modules form the backbone of Chemistry42's
>
> multiagent reinforcement learning (RL)-based generation protocol.
>
> Generated structures' scores are fed back to the generative models to
>
> reinforce them and guide the generative process toward high-scoring
>
> structures this is called the learning phase. The final step is
> analysis.
>
> The generated structures are automatically ranked according to
>
> customizable metrics based on their predicted properties, including
>
> synthetic accessibility, novelty, diversity, etc. The platform also
>
> provides users with interactive tools to monitor generative model
>
> performance.
>
> Figure(1) key words:
>
> Medicinal Chemistry Evolution 2018 (MCE-18), Molecular Complexity
> Features (MCFs), Rule of 5 Lipinski\'s Rule of Five (RO5), Therapeutic
> Indexes (T indexes), Physicochemical Profile (PC profile), Synthetic
> Accessibility / Real Reaction Space Accessibility score (SA/ReRSA
> score), Self-Organizing Map (SOM), Hierarchical Agglomerative Merging
> Base (HAM Base), Describing the main, usually larger, SOM from which
> smaller, more detailed maps are derived (Parent SOM), describing a
> feature of SOM analysis (ZOOM maps).
>
> ![](media/image2.jpeg){width="6.635416666666667in" height="3.34375in"}

> **Figure 2.** Chemistry42 interface for configuring an SBDD generative
experiment

> **4.1.2.2. Case Study: Accelerated Target Discovery And Validation In
> Hepatocellular Carcinoma (HCC) Using Pandaomics, Alphafold, And
> Chemistry42**
>
> This case study demonstrates the power of integrating the PandaOmics
> and Chemistry42 AI platforms with protein structures predicted by
> AlphaFold to efficiently identify and validate a novel therapeutic
> target for Hepatocellular Carcinoma (HCC), a challenging cancer with
> limited treatments.
>
> Target Identification with PandaOmics
>
> The process began with PandaOmics conducting a systematic search for
> HCC-relevant datasets, compiling a tailored data inventory. The
> platform performed data analysis and filtering based on both text and
> omics data from multiple sources, aggregating case-versus-control
> comparisons in a meta-analysis to generate a ranked list of potential
> targets.
>
> The platform applied a \"first-in-class\" scenario for target
> identification, prioritizing proteins based on several strict
> criteria:
>
> \* Strong disease association and limited experimental structure
> information.
>
> \* Druggability by small molecules.
>
> \* Novelty (exclusion of targets in Phase 1 or later clinical trials
> in the past three years).
>
> \* Exclusion of targets of approved drugs.
>
> \* Exclusion of targets with previously resolved crystal structures.
>
> Based on this analysis, Cyclin-dependent kinase 20 (CDK20) was
> selected as the initial target due to its high disease association and
> scarcity of experimental structural data  (Ren et al., 2023).
>
> Molecular Generation and Validation with AlphaFold and Chemistry42
>
> With the target selected, the process moved to the molecular design
> stage:
>
> **Structure Preparation**: The lack of an experimental structure for
> CDK20 was overcome by using the protein structure predicted by
> AlphaFold.
>
> Initial Generation & Validation: Using the predicted CDK20 structure,
> the Chemistry42 platform employed a structure-based compound
> generation approach to create a library of molecules. From this
> library, only seven compounds were synthesized and tested in
> biological assays. This rapidly yielded an initial hit compound,
> ISM042-2-001, which demonstrated target engagement with a binding
> constant (Kd) value of 9.2 ± 0.5 µM (
>
> n=3) in the CDK20 kinase binding assay. This proof of concept was
> achieved in just {30 days} from target selection (Ren et
> al., 2023).
>
> **Optimization**: A second round of AI-powered compound generation was
> performed to optimize the initial hit. This led to the discovery of a
> more potent hit molecule, ISM042-2-048, after the synthesis and
> testing of six additional compounds. This molecule showed an average
> Kd value of 566.7 ± 256.2 nM (n=3) and an average IC\_{50} value of
> 33.4 ± 22.6 nM (n=3) in binding and inhibitory assays against CDK20.
> Significantly, ISM042-2-048 also exhibited selective antiproliferation
> activity in an HCC cell line where CDK20 was overexpressed, confirming
> its therapeutic potential (Ren et al., 2023).
>
> **Conclusion**
>
> This success story highlights the transformative capability of
> integrating diverse AI tools in early-stage drug discovery. By
> leveraging PandaOmics\' comprehensive data analysis, AlphaFold\'s
> structural predictions, and Chemistry42\'s molecular generation power,
> a novel target for HCC was swiftly identified, novel small molecules
> were generated, and their biological activity was validated. This
> integration offers a paradigm for efficient and effective drug
> development.
>
> 4.1.3. **Other Notable AI Platforms in the Industry**
>
> **4.1.3.1. Atomwise: Pioneering AI-Powered Virtual Screening For Drug
> Discovery**
>
> Atomwise is a leading company that is revolutionizing early-stage drug
> discovery by leveraging Deep Learning (DL) models for highly efficient
> virtual screening (Khan et al., 2024). The company\'s technology
> significantly accelerates the drug discovery pipeline by providing
> rapid and precise predictions of molecular interactions  (Wallach et
> al., 2015). The heart of Atomwise\'s approach is AtomNet, a
> proprietary model that utilizes Convolutional Neural Networks
> (CNNs)---the same technology used in image recognition---to predict
> the crucial metric of binding affinity. By training these CNNs on 3D
> molecular structures, the Atomwise platform can accurately predict the
> complex interactions between small molecules and target proteins
> (Gaul, C., & Cuesta-Lopez, S. 2024)
>
> This AI-driven virtual screening methodology enables the rapid
> analysis and screening of millions of compounds against a target,
> dramatically speeding up the identification of new inhibitors and
> potential drug candidates (Gaul, C., & Cuesta-Lopez, S. 2024).
>
> Atomwise's technology has already proven instrumental, having
> successfully identified promising compounds for treating a variety of
> serious conditions, including Ebola and multiple sclerosis (Gaul, C.,
> & Cuesta-Lopez, S. 2024)
>
> **4.1.3.2. Benevolentai: Driving Early Drug Discovery With Deep Data
> Analysis**
>
> BenevolentAI (Sellwood et al., 2018).is an AI-driven platform at the
> forefront of revolutionizing the early stages of drug discovery. In
> contrast to approaches like Atomwise (Keshavarzi Arshadi et al.,
> 2020). which focus on high-throughput virtual screening of compound
> libraries against a specific target, BenevolentAI primarily leverages
> advanced Deep Learning (DL) and Machine Learning (ML) techniques to
> achieve a deeper, mechanistic understanding of disease biology and to
> identify novel therapeutic targets.
>
> **Core Capabilities**
>
> BenevolentAI achieves its goals by analyzing diverse and comprehensive
> data sources, including (Sellwood et al., 2018):

1- Scientific Literature

2- Clinical Trial Data

3- Genetic Information

> By synthesizing insights from this massive and varied body of
> knowledge, the platform is able to spot connections and hypothesize
> new therapeutic approaches.
>
> **Context of AI-Driven Drug Discovery**
>
> BenevolentAI operates within the broader context of AI transforming
> drug discovery, where de novo design---creating new molecules from
> scratch---is accelerated by generative models (such as Recurrent
> Neural Networks (RNNs), autoencoders, Generative Adversarial Networks
> (GANs), and Reinforcement Learning based systems (RL) ). These systems
> are used to simultaneously optimize molecular properties like
> bioactivity and toxicity, expanding the chemical space and designing
> compounds with pre-defined characteristics.
>
> Complementary tools further advance the field, including:

- DiffDock (Corso et al., 2022) : Utilizes diffusion models for
 protein--ligand docking.

- MoleculeGen (Wu et al., 2018): An advanced molecule generation tool.

- ESM-2 (Tang et al., 2024); (Tong et al., 2021) : Advances protein
 structure prediction.

> The demonstrated success of AI-driven platforms like BenevolentAI in
> identifying novel compounds for challenging diseases, notably Ebola
> and COVID-19 (Wallach et al., 2024). underscores the transformative
> potential of its approach in accelerating the overall drug discovery
> process.
>
> **4.1.3.3. Numerate: A Model for AI-Pharma Collaboration in Medicinal
> Chemistry**
>
> Numerate is an exemplary AI company demonstrating the essential
> synergy between artificial intelligence researchers and pharmaceutical
> giants. Its collaboration with the pharmaceutical company Merck
> (Numerate, Inc. 2022). serves as a prime illustration of how merging
> expertise can drive innovation in drug development.
>
> Collaboration Focus and Impact
>
> The core objective of the Numerate-Merck partnership was the joint
> development of AI-based approaches specifically tailored for medicinal
> chemistry (Numerate, Inc. 2022). Numerate's proprietary technology,
> which leverages advanced algorithms and cloud computing, was deployed
> to accelerate the design of novel drug leads.
>
> Numerate\'s Role in Accelerating Drug Discovery
>
> The use of Numerate\'s powerful machine-learning models and algorithms
> offers several critical advantages to the drug discovery process:
>
> **Prediction of Efficacy**: Numerate\'s algorithms build predictive
> models for drug candidate efficacy and other molecular properties,
> with accuracies comparable to traditional lab testing.
>
> **Accelerated Development:** By delivering rapid and accurate
> predictions, Numerate helps pharma companies make quicker,
> better-informed decisions on which drug candidates to pursue,
> significantly shortening development timelines.
>
> Efficiency in Clinical Trials: AI algorithms are instrumental in
> analyzing trial data, identifying trends, and predicting potential
> adverse effects, thereby boosting the accuracy and efficiency of
> clinical trials.
>
> **Enhanced Accessibility and Affordability:** The analytical power of
> AI, as demonstrated by Numerate, can be used to analyze large
> population datasets to predict drug effectiveness for specific patient
> groups, moving healthcare toward tailored treatments.
>
> The increasing number of new companies entering this domain, mirroring
> Numerate\'s success (P360. 2022)., suggests that the impact of these
> AI-pharma collaborations will be significant in the near term.
> Ultimately, Numerate's model of working together with pharma
> facilitates the identification of new drug targets and the enhancement
> of existing treatments, directly benefiting patients.
>
> **4.2. CHALLENGES AND LIMITATIONS**
>
> **4.2.1. The "Black-Box" Problem: The Difficulty Of Interpreting AI
> Model Decisions**
>
> The "Black-Box" Problem: The Difficulty of Interpreting AI Model
> Decisions
>
> The core concern with current Artificial Intelligence (AI) in medicine
> centers on Deep Learning (DL) systems. This technology is founded on
> the Artificial Neural Network (ANN), a concept inspired by the
> intricate structure of the human brain. The fundamental active unit in
> the human brain is the neuron, with tens of billions interconnected to
> form a \"neural network.\" DL systems seek to emulate this biological
> \"neural network\" (Castelvecchi, D. (2016). to achieve a similar
> learning strategy.
>
> Medical AI systems possess three key features that define their
> utility and challenge:
>
> 1\. **Self-Learning Capacity**
>
> Unlike traditional, rule-based computational programs, DL systems can
> process vast amounts of data and develop the ability for
> self-learning. This algorithmic capability allows the systems to
> generate a desired output based on the input data without being
> explicitly programmed with specific rules (Miotto et al.,
> 2016); (McKinney et al., 2020).
>
> 2\. **High Predictive Accuracy**
>
> To achieve self-learning, these systems require extensive data, which
> is divided into training and testing sets. The training data \"fits\"
> the model, and the testing data validates its performance. After
> training, medical AI systems demonstrate exceptionally high accuracy
> in testing, sometimes even surpassing human experts in diagnosing
> specific conditions. For example, the Deep Patient system accurately
> predicted \"hidden\" diseases in over 700,000 electronic health
> records using DL (Miotto et al., 2016). Its high accuracy in
> predicting psychiatric disorders, like schizophrenia, was particularly
> notable, as these conditions are notoriously difficult to predict. In
> another instance, the AI system developed by Google\'s DeepMind
> outperformed six human radiologists in predicting breast cancer from
> new mammograms after analyzing X-ray images from nearly 29,000 female
> patients (McKinney et al., 2020).
>
> 3\. **Unexplainable Diagnoses and Suggestions**
>
> The third feature is the root of the \"black-box\" problem: the
> diagnoses and treatment suggestions from medical AI systems are
> fundamentally unexplainable. Because the ANNs mimic the
> still-mysterious workings of the human brain\'s neural network, these
> systems are \"black boxes\" to patients, doctors, and even their own
> designers.
>
> The term \"black box\" signifies a lack of understanding of the
> system\'s internal working mechanism. For instance, a medical AI
> system might accurately predict a tumor\'s response to a drug based on
> allelic patterns across thousands of genes, or forecast lung cancer
> prognosis by analyzing microscopic images, yet it cannot identify why
> those specific patterns or image features were significant.
>
> Regarding the Deep Patient system, researchers confirmed its accurate
> predictions for various diseases, including psychiatric disorders, but
> were puzzled by how it achieved such accurate conclusions and
> predictions. As Watson explicitly states, the main concern is a \"lack
> of understanding among patients and doctors about how predictions are
> made,\" especially with top-performing deep neural networks used in
> image recognition. While these models may reliably distinguish between
> malignant and benign tumors, they \"offer no explanation for their
> judgments\" (Watson et al., 2019).
>
> It remains a significant hurdle before medical AI systems become
> transparent enough for a physician to easily identify incorrect
> results or for an individual to reasonably contest a system\'s
> decision. Consequently, the potential harm arising from these opaque
> systems must be seriously considered.
>
> 4.2.2.**The Imperative For Experimental Validation Of Artificial
> Intelligence Predictions In Research**
>
> The application of Artificial Intelligence (AI), particularly in
> complex fields like drug discovery, offers tremendous predictive
> power. However, it is crucial to establish and reiterate a fundamental
> constraint: current AI-based approaches are not a replacement for
> traditional experimental methods (Grebner et al., 2021); (Schraagen &
> van Diggelen, 2021). While these systems are incredibly adept at
> pattern recognition and prediction, they do not possess the capacity
> to autonomously confirm or interpret the physical reality of their
> findings.
>
> **AI as a Hypothesis Generator**
>
> An AI system\'s core function is to act as a sophisticated hypothesis
> generator. Based on the massive datasets it processes, AI can only
> furnish a set of predictions concerning chemical properties,
> biological interactions, or disease pathways. This means the output
> from the algorithms is purely theoretical until proven otherwise.
> Consequently, the results delivered by the AI models must then be
> rigorously validated and interpreted by human researchers (Gilpin et
> al., 2019). The human element remains indispensable for contextualizing
> the findings, ensuring their biological plausibility, and designing
> the necessary experiments to move from a predicted outcome to a
> confirmed fact.
>
> **The Synergy of Prediction and Experience**
>
> Far from being a competitive alternative, the ideal role of AI is to
> foster a powerful integration with traditional experimental methods
> (Paul et al., 2021). This synergy leverages the strengths of both
> components. On one side, you have the unparalleled predictive power of
> AI---its ability to rapidly sift through vast chemical libraries and
> identify promising candidates that would take human researchers
> decades to evaluate. On the other side, you have the essential
> expertise and experience of human researchers (Jarrahi, M. H.
> (2018)---the deep, nuanced understanding of biochemistry, medicine,
> and laboratory techniques required to actually test, refine, and bring
> a compound to fruition.
>
> By strategically combining these elements, the scientific community
> can optimize the drug discovery process (Wang et al., 2019). AI
> dramatically reduces the initial search space, allowing human teams to
> focus their finite resources on the most promising avenues. This
> collaboration does not diminish the role of the researcher; rather, it
> elevates it, freeing human intellect to concentrate on complex
> problem-solving and critical validation, thereby accelerating the
> development of new medications (Wang et al., 2019). The ultimate
> success of an AI prediction is not its accuracy on a test set, but its
> confirmation under a microscope.
>
> 4.2.3. **High-Quality Data Scarcity And Its Impact On Model
> Performance In Drug Design**
>
> The central focus of this analysis is the influence of data quality
> and scarcity on AI-driven drug design, specifically addressing the key
> hurdles in data representation and prediction---areas where Artificial
> Intelligence (AI) holds considerable potential.
>
> **Obstacles in Defining AI-Ready Tasks**
>
> ​Many foundational drug discovery activities are difficult to translate
> into effective machine learning problems. The primary challenge lies
> in the lack of standardized knowledge representations and a deficit of
> AI-ready benchmark datasets.
>
> **​Non-Uniform Molecular Representations**: Drug molecules themselves
> can be encoded in diverse formats, such as linear SMILES strings,
> numerical descriptors like Extended Connectivity Fingerprints (ECFP),
> and intricate molecular graphs. Similarly, proteins can be modeled
> using a simple 1D amino acid sequence, a more complex sequence
> representation, or their complete 3D-structure. This inherent
> diversity in representation complicates the development of universal
> models.
>
> **Issues with Labels**: Further compounding this is the problem of low
> resource labels and significant disparity among labels, which makes
> the formulation of meaningful, generalizable learning tasks
> exceedingly difficult for AI systems.
>
> **Data Imperfections That Impact Performance**
>
> ​The performance and reliability of AI models are directly compromised
> by common flaws in the underlying data, including problems with data
> collection, the prevalence of small sample sizes, and the existence of
> noisy labels. These factors collectively depress model accuracy and
> dependability.
>
> **Recent Solutions and Progress**
>
> ​Despite these significant data-centric challenges, the past few years
> have demonstrated substantial advancements in applying deep-learning
> to drug discovery. This progress is greatly facilitated by the
> emergence of new resources designed to help overcome data scarcity and
> standardization issues:
>
> ​The development of open-source tools (Huang et al., 2020).
>
> ​The creation of AI-ready benchmark datasets (Huang et al., 2021)​.
>
> New deep learning platforms (Zhu et al., 2022). Specifically engineered
> for drug design applications.
>
> 4.3. **Ethical and Regulatory Considerations**
>
> 4.3.1**. Data Privacy And Algorithmic Bias: Core Ethical Challenges In
> AI**
>
> The application of Artificial Intelligence (AI) in the pharmaceutical
> sector necessitates a critical examination of its ethical implications
> (Naik et al., 2022); (Karimian et al., 2022) The discussion focuses on
> two paramount challenges: the potential for algorithmic bias and the
> vital necessity of maintaining data privacy and security.
>
> **The Risk of Algorithmic Bias and Inequity**
>
> A central ethical concern revolves around the potential for bias in AI
> algorithms. AI systems are increasingly being used to make decisions
> with direct bearing on public health and individual
> welfare---including choices regarding which drugs to develop, the
> execution of clinical trials, and the methods for marketing and
> distributing medications.
>
> If the training data is unrepresentative or reflects historical
> biases, the resulting algorithms can entrench and amplify those
> inequities. This risks causing unequal access to medical treatment and
> potentially the unfair treatment of specific demographic groups. Such
> outcomes fundamentally contradict the principles of equality and
> justice in healthcare.
>
> **Data Privacy, Security, and Compliance**
>
> Since AI systems rely heavily on large amounts of data to function,
> their integration into the pharmaceutical industry raises serious
> concerns about data privacy and security.
>
> There is a considerable risk that the sensitive, personal health
> information used by these models could be compromised through
> unauthorized access or misuse. A breach of this nature would have
> severe consequences for affected individuals and could significantly
> damage the reputation of the involved pharmaceutical companies.
> Consequently, the collection and use of sensitive medical data must be
> conducted in a manner that strictly respects individual privacy and
> adheres to all relevant regulations.
>
> **Wider Societal Concerns**
>
> Beyond data ethics and bias, the widespread adoption of AI also brings
> up socioeconomic issues, particularly the prospect of job losses due
> to automation in the pharmaceutical sector. It is essential to
> proactively assess the impact on the workforce and ensure support is
> available for those who might be displaced by these technological
> changes.
>
> 4.3.2. **Regulatory Frameworks: How Agencies Like The FDA Are Adapting
> To AI-Driven Submissions**
>
> The integration of Artificial Intelligence (AI) into pharmacy
> practice, despite its transformative potential, introduces a complex
> set of ethical and regulatory challenges. A key focus is on how
> regulatory bodies are evolving to govern these new technologies.
>
> **The Need for Regulatory Adaptation**
>
> The rapid evolution of AI in the pharmaceutical industry presents
> significant ethical and legal challenges, including issues like
> algorithmic bias, a lack of transparency in decision-making, ongoing
> data privacy concerns, and unclear liability frameworks (Shaki, F., et
> al. 2024). Currently, regulatory agencies are in the process of
> adapting to effectively oversee AI applications in pharma (Shaki, F.,
> et al. 2024). There is a recognized need for standardized guidelines
> that can successfully balance the need to ensure patient safety with
> the desire to avoid stifling innovation (Shaki, F., et al. 2024).
>
> **Regulatory Role in Clinical Trials and Safety**
>
> Patient safety and the integrity of clinical trials constitute a
> significant ethical and regulatory challenge. Regulatory bodies, such
> as the Food and Drug Administration (FDA), are vital in enforcing
> guidelines to protect trial participants (Boudi, A. L., et al. 2024).
> The integrity of these trials relies heavily on securing informed
> consent from participants, who must fully comprehend the risks
> involved. While the FDA works to protect individual rights, issues
> such as the exploitation of vulnerable populations remain a prevalent
> concern (Boudi, A. L., et al. 2024).
>
> **The Wider Ethical and Legal Landscape**
>
> Surveys among pharmacy professionals, particularly in the Middle East
> and North Africa (MENA) region, underscore the breadth of these
> concerns (Hasan, H. E., et al. 2024). Critical issues identified
> include:

- Lack of Legal Regulation (67.0%)

- Potential Job Displacement (62.9%)

- Patient Data Privacy (58.9%)

- Cybersecurity Threats (58.9%)

> These findings emphasize that realizing the full benefits of AI
> requires a commitment to responsible AI in medicine, anchored by
> transparent frameworks, multidisciplinary collaboration, and an
> unwavering focus on patient welfare (Boudi, A. L., et al. 2024).
> Ultimately, achieving public trust requires regulatory bodies to
> successfully manage the balance between AI's potential and robust
> ethical governance (Shaki, F., et al. 2024).
>
> 4.4**. FUTURE TRENDS**
>
> 4.4.1. **Emerging Technologies: Quantum Computing In Drug Design**
>
> The core challenge confronting pharmaceutical science is the
> time-intensive and exorbitant nature of drug development, with costs
> frequently exceeding one billion dollars (Berdigaliyev, N., & Aljofan,
> M. 2020). Historical precedents, such as the 35-year effort to cure
> Malaria (Magazine, S. 2022)., underscore the urgent need to accelerate
> the entire pipeline, which encompasses target identification, hit
> screening, lead optimization, pre-clinical testing, and clinical
> trials (Wang et al., 2023). While current AI deployment is already
> advantageous in speeding up the process, it faces limitations,
> including data quality issues, the complexity of biological systems,
> and the scarcity of high-quality data for rare diseases
> (Blanco-Gonzalez et al., 2023).
>
> **Quantum Computing as a Solution to Drug Discovery Hurdles**
>
> Quantum Computing (QC) offers a potential, paradigm-shifting solution
> by leveraging its superiority over classical supercomputers
> (Blanco-Gonzalez et al., 2023).
>
> Quantum computers are designed to tackle problems that are intractable
> for even the most powerful classical machines. The milestone of
> quantum supremacy was achieved in 2019 by Google\'s \'Sycamore\'
> system, which featured 53 programmable superconducting qubits  (Arute
> et al., 2019); (Zinner et al., 2021).
>
> The evolution of QC is highly promising for drug discovery and
> development (Mahesh & Shijo, 2023) as quantum technologies stand to
> revolutionize fields like machine learning, financial modeling, and
> especially chemistry and medicine (Sotelo, R. 2023).
>
> **Unique Advantages Of Quantum Computing**
>
> **QC excels in two key areas relevant to drug design:**
>
> Molecular Simulation and Prediction: Quantum computers are inherently
> superior at molecular simulations (Parenti & Rastelli, 2012); (McArdle
> et al., 2020). By predicting drug behavior and properties with greater
> precision, they significantly enhance the in-depth understanding of
> drug action (Parenti & Rastelli, 2012). This ability to accurately
> model quantum effects provides more precise predictions for drug
> design.
>
> **Accelerated Data Processing**: QC can accelerate machine learning
> algorithms  (Li et al., 2021). It achieves this by rapidly processing
> extensive data volumes, managing complex computations, and generating
> more precise predictions than traditional methods and classical AI (Li
> et al., 2021); (Chauhan et al., 2022).
>
> Quantum generative models, for example, can comprehensively cover
> complex distributions due to their intrinsic probabilistic nature
> (Biswas et al., 2020).
>
> **The Research Motivation and Structure**
>
> ![](media/image3.jpg){width="2.28125in" height="4.28125in"}The primary
> motivation driving this area of research is the imperative to expedite
> drug development, reduce costs, and fundamentally redefine the
> approach to creating new drugs, moving away from conventional methods
> (McArdle et al., 2020).

This research aims to delve into quantum computers\' medical
capabilities, analyzing drug behavior under diverse conditions using
specialized algorithms. The structure of this paper will cover:

- Previous work (Section II).

- A fundamental overview of core quantum technology (Section III).

- The integration of quantum technology at various stages of the
 simulation process (Section IV).

- A dedicated discussion of Quantum chemistry (Section V).

- The complete pipeline of the quantum-enhanced drug development process
 (Section VI).

- The potential use of QC for final stage trial and testing (Section
 VII).

- A necessary exploration of the technological and ethical challenges
 posed by quantum computers (Section VIII).

- Future prospects and new applications (Section IX)

- the conclusion (Section X).

**4.4.2. Personalized Medicine: Designing Drugs for Individual
Patients**

The digitization of medical records is paving the way for data-driven
methodologies to revolutionize several healthcare areas, including
clinical trials, health policy, drug discovery, and especially precision
medicine.

**AI and Data-Driven Drug Design**

Over the past decade, novel analytical and computational advances have
radically transformed drug discovery (Davenport & Kalakota, 2019); (Yu et
al., 2018); ( (Pandey et al., 2022); (Sierra-Sosa et al., 2019); (Powles &
Hodson, 2017). There is now intense interest in applying Artificial
Intelligence (AI) methods to improve various stages of the drug
discovery pipeline (Chen et al., 2018). The goal is to move towards
personalized treatment by utilizing AI in:

- De novo molecular design and optimization

- Structure-based drug design

- Pre-clinical and clinical development

The Foundation for Personalized Treatments

The integration of extensive biomedical datasets with sophisticated
analytical tools, particularly deep learning models, is the core
mechanism enabling this shift toward individualized medicine (Vamathevan
et al., 2019). These datasets include:

- Genomic profiles

- Imaging data

- Chemical and drug databases

By coordinating these tools, researchers can more effectively discover
and develop drugs and clinical applications tailored to individual
patient characteristics, making the vision of personalized medicine a
reality.

4.4.3. **The "AI-Scientist" Collaboration and the Rise of Automated
"Self-Driving" Labs**

The future success of AI in drug discovery hinges on fostering a
collaborative environment to generate high-quality data and advance
model representation. This collaboration must move beyond simple
prediction to embrace robust methods that enhance human thinking and
ultimately change the culture of research.

**Developing Foundational Datasets and Collaborative Models**

A key requirement is the creation of high-quality, annotated labeled
datasets and the learning of their representations, which necessitates
collaborative efforts from multiple disciplines. Following the
precedent set by ImageNet in computer vision, we urgently need to
develop the \"ImageNet\" for molecules and more benchmark resources like
MoleculeNet  (Wu et al., 2018).

We must develop robust methods where the human mind can teach the model
to optimize so that the AI generates insights that allow humans to think
in new directions. This co-optimization aims to bring better prospects
into clinics, enhance target validation, increase patient recruitment,
and improve clinical trial design (as depicted in Fig. 4).

**Shifting Focus to Causal Discovery**

Current AI mainly focuses on the manifestations of diseases, rather than
their actual causes. A crucial advancement will be understanding the
causal pathway of diseases---how genetic predisposition manifests---to
enable manipulation and potentially reverse the course of the disease.
This is a promising area for causal machine learning and causal
inference (Peters et al., 2011).which can also be applied to treatment
decisions and tracking patient health evolution.

**Cultivating a Collaborative Research Culture**

The full potential of data science in healthcare requires cultivating a
\"culture\" where stakeholders are willing to use computational models
and utilize their results. As the African proverb says, \"if you want to
go fast go alone, and if you want to go far go together.\"

This requires:

- Increased collaboration between industry, academia, and other
 stakeholders.

- Training professionals to understand both medicine and computer
 science.

Furthermore, organizing more workshops on AI for drug discovery or
computational biology at major AI conferences like NeuralIPS and
International Conference on Machine Learning (ICML) is necessary, along
with the long-term vision of developing new degree programs for AI in
drug discovery. This collaborative, transparent approach is exemplified
by initiatives like the 2019 partnership between AstraZeneca and Dialog
for DREAM Challenges, which focused on model repeatability and
methodological transparency on significant biomedical problems using
large, shared datasets (e.g., 11,576 experiments on cancer cell lines).

![](media/image4.jpg){width="6.041666666666667in"
height="2.488561898512686in"}Fig. 4. Learning from various data sources
can aid drug design, clinical decision support, and public health
policy. The collaborative intelligence resulting from the merger of
"mind and machine" is expected to improve decision-making in healthcare.

**Sources**

1. 11 Companies Using Pharma AI to Stimulate Growth in the
 Industry. Available
 online:https://www.p360.com/data360/11-companies-using-pharma-ai-to-stimulate-growth-in-the-industry-1/
 (accessed on 6 December 2022).

2. A. Blanco-Gonzalez, A. Cabezon, A. Seco-Gonzalez, D.
 Conde-Torres, P. Antelo-Riveiro, A. Pineiro, and R. Garcia-Fandino,
 "The role of ai in drug discovery: challenges, opportunities, and
 strategies," Pharmaceuti-cals, vol. 16, no. 6, p. 891, 2023.

3. Agarwal P, Searls DB. Literature mining in support of
 drug discovery. Brief Bioinform. 2008;9(6):479--92.

4. AI is a viable alternative to high throughput
 screening: a 318-target study. Sci Rep 2024. 14(1): 7526. 41.

5. Available online:
 https://www.fiercebiotech.com/biotech/numerate-forms-drug-discovery-collaboration-merck-to-utilize-numerate-s-silico-drug-design
 (accessed on 6 December 2022).

6. Bepler T, Berger B. Learning the protein language:
 evolution, structure, and function. Cell Syst. 2021;12(6):654--69.

7. Boudi AL, et al. Ethical challenges of artificial
 intelligence in medicine. Cureus. 2024;16(11):e74495.

8. Castelvecchi D. Can we open the black box of AI? Nature
 2016;538(7623):20--3. doi:10.1038/538020a.

9. Corso G et al. Diffdock: diffusion steps, twists, and
 turns for molecular docking. arXiv preprint arXiv:2210.01776, 2022

10. D. Sierra-Sosa, B. Garcia-Zapirain, C. Castillo, I.
 Oleagordia, R. Nuño-Solinis, M. Urtaran-Laresgoiti, A. Elmaghraby,
 Scalable healthcare assessment for diabetic patients using deep
 learning on multiple gpus, IEEE Trans. Ind. Inform. 15 (10) (2019)
 5682--5689.

11. Devi, R. V.; Sathya, S. S.; Coumar, M. S. Evolutionary
 Algorithms for de Novo Drug Design − A Survey. Appl. Soft Comput.
 2015, 27, 543−552.

12. F. Arute, K. Arya, R. Babbush, D. Bacon, J. C.
 Bardin, R. Barends, R. Biswas, S. Boixo, F. G. S. L. Brandao, D. A.
 Buell et al., "Quantum supremacy using a programmable
 superconducting processor," Nature, vol. 574, no. 7779, pp.
 505--510, Oct. 2019.

13. Ferruz N, Schmidt S, Höcker B. ProtGPT2 is a deep
 unsupervised language model for protein design. Nat Commun.
 2022;13(1):4348.

14. Gaul C, Cuesta-Lopez S. Machine learning for orbital
 energies of organic molecules upwards of 100 atoms. Phys Status
 Solidi (b). 2024;261(1): Article 2200553.

15. Gilpin, L. H.; Bau, D.; Yuan, B. Z.; Bajwa, A.; Specter,
 M.; Kagal, L. Explaining explanations: An overview of
 interpretability of machine learning. In Proceedings of the 2018
 IEEE 5th International Conference on Data Science and Advanced
 Analytics, DSAA Turin, Itali, 1--3 October 2018; Institute of
 Electrical and Electronics Engineers Inc.: Piscataway, NJ, USA,
 2019; pp. 80--89.

16. Grebner, C.; Matter, H.; Kofink, D.; Wenzel, J.;
 Schmidt, F.; Hessler, G. Application of Deep Neural Network Models
 in Drug Discovery Programs. ChemMedChem 2021, 16, 3772--3786.
 \[CrossRef\]

17. H. Chen, O. Engkvist, Y. Wang, M. Olivecrona, T.
 Blaschke, The rise of deep learning in drug discovery, Drug Discov.
 Today 23 (6) (2018) 1241--1250.

18. Hasan HE, et al. Ethical considerations and concerns in
 the implementation of AI in pharmacy practice: a cross-sectional
 study. BMC Med Ethics. 2024;25(1):55.

19. J. Jumper, R. Evans, A. Pritzel, T. Green, M.
 Figurnov, O. Ronneberger, K. Tunyasuvunakool, R. Bates, A. Žídek, A.
 Potapenko, et al., Highly accurate protein structure prediction with
 alphafold, Nature 596 (7873) (2021) 583--589.

20. J. Li, R. O. Topaloglu, and S. Ghosh, "Quantum
 generative models for small molecule drug discovery," IEEE
 Transactions on Quantum Engineering, vol. 2, pp. 1--8, 2021.

21. J. Moult, K. Fidelis, A. Kryshtafovych, T. Schwede, A.
 Tramontano, Critical assessment of methods of protein structure
 prediction (casp)---round x, Proteins, Struct. Funct. Bioinform.
 82 (2014) 1--6.

22. J. Peters, D. Janzing, B. Scholkopf, Causal inference
 on discrete data using additive noise models, IEEE Trans. Pattern
 Anal. Mach. Intell. 33 (12) (2011) 2436--2450.

23. J. Powles, H. Hodson, Google deepmind and healthcare
 in an age of algorithms, Health Technol. 7 (4) (2017) 351--367.

24. J. Vamathevan, D. Clark, P. Czodrowski, I. Dunham, E.
 Ferran, G. Lee, B. Li, A. Madabhushi, P. Shah, M. Spitzer, et al.,
 Applications of machine learning in drug discovery and development,
 Nat. Rev. Drug Discov. 18 (6) (2019) 463--477.

25. Jarrahi, M. H. Artificial intelligence and the future of
 work: Human-AI symbiosis in organizational decision making. Bus.
 Horiz.2018, 61, 577--586. \[CrossRef\]

26. Jumper J, et al. Highly accurate protein structure
 prediction with AlphaFold. Nat Rev Drug Discov.
 2021;596(7873):583--9.

27. K. Huang, T. Fu, L. M. Glass, M. Zitnik, C. Xiao, J.
 Sun, Deeppurpose: a deep learning library for drug--target
 interaction prediction, Bioinformatics 36 (22--23) (2020)
 5545--5547.

28. K. Huang, T. Fu, W. Gao, Y. Zhao, Y. Roohani, J.
 Leskovec, C. W. Coley, C. Xiao, J. Sun, M. Zitnik, Therapeutics data
 commons: machine learning datasets and tasks for therapeutics, arXiv
 e-prints, 2021.

29. K.-H. Yu, A. L. Beam, I. S. Kohane, Artificial
 intelligence in healthcare, Nat. Biomed. Eng. 2 (10) (2018)
 719--731.

30. Kadurin, A.; Aliper, A.; Kazennov, A.; Mamoshina, P.;
 Vanhaelen, Q.; Khrabrov, K.; Zhavoronkov, A. The Cornucopia of
 Meaningful Leads: Applying Deep Adversarial Autoencoders for New
 Molecule Development in Oncology. Oncotarget 2017, 8 (7),
 10883−10890.

31. Kadurin, A.; Nikolenko, S.; Khrabrov, K.; Aliper, A.;
 Zhavoronkov, A. druGAN: An Advanced Generative Adversarial
 Autoencoder Model for de Novo Generation of New Molecules with
 Desired Molecular Properties in Silico. Mol. Pharmaceutics 2017, 14
 (9), 3098−3104.

32. Karimian, G.; Petelos, E.; Evers, S. M. A. A. The ethical
 issues of the application of artificial intelligence in healthcare:
 A systematic scoping review. AI Ethics 2022, 2, 539--551.
 \[CrossRef\]

33. Keshavarzi Arshadi A, et al. Artificial intelligence
 for COVID-19 drug discovery and vaccine development. Front Artif
 Intell. 2020;3:65.

34. Khan T, et al. Synthesis, characterization,
 computational studies and antimicrobial activity evaluation of mixed
 ligand--metal complexes of selected thiosemicarbazones.
 ChemistrySelect. 2024;9(10): e202400202.

35. Kosonocky CW, et al. Mining patents with large
 language models elucidates the chemical function landscape. Digital
 Discovery. 2024;3(6):1150--9.

36. Kuznetsov, M.; Polykovskiy, D. MolGrow: A Graph
 Normalizing Flow for Hierarchical Molecular Generation. AAAI 2021,
 35 (9), 8226−8234.

37. Lin Z, et al. Evolutionary-scale prediction of
 atomic-level protein structure with a language model. Science.
 2023;379(6637):1123--30.

38. M. AlQuraishi, Alphafold2@ casp14: "it feels like
 one's child has left home", 2020.

39. M. D. Parenti and G. Rastelli, "Advances and
 applications of binding affinity prediction methods in drug
 discovery," Biotechnology advances, vol. 30, no. 1, pp. 244--250,

40. M. Pandey, M. Fernandez, F. Gentile, O. Isayev, A.
 Tropsha, A. C. Stern, A. Cherkasov, The transformational role of gpu
 computing and deep learning in drug discovery, Nat. Mach. Intell.
 4 (3) (2022) 211--221.

41. M. Zinner, F. Dahlhausen, P. Boehme, J. Ehlers, L.
 Bieske, and L. Fehring, "Quantum computing's potential for drug
 discovery: Early stage industry dynamics," Drug Discovery Today,
 vol. 26, no. 7, pp. 1680--1688, 2021. \[Online\]. Available:
 [[https://www.sciencedirect.com/]{.underline}](https://www.sciencedirect.com/)
 science/article/pii/S1359644621002750

42. McKinney SM, Sieniek M, Godbole V, et al. International
 evaluation of an AI system for breast cancer screening. Nature
 2020;577(7788):89--94. doi:10.1038/s41586-019-1799-6.

43. Miotto R, Li L, Dudley JT. Deep learning to predict
 patient future dis-eases from the electronic health records. In:
 Proceedings of 38th Euro-pean Conference on Information Retrieval
 Research, Padua; Italy. ECIR; 2016.doi:10.1007/978-3-319-30671-1_66.

44. N. Berdigaliyev and M. Aljofan, "\"an overview of drug
 discovery and development\"," vol. 12, no. 10, 2020, pp. 939--947.

45. Naik, N.; Hameed, B. M. Z.; Shetty, D. K.; Swain, D.;
 Shah, M.; Paul, R.; Aggarwal, K.; Brahim, S.; Patil, V.; Smriti, K.;
 et al. Legaland Ethical Consideration in Artificial Intelligence in
 Healthcare: Who Takes Responsibility? Front. Surg. 2022, 9, 266.
 \[CrossRef\]\[PubMed\]

46. Naumov, P. S., Kholodov, V. P., Oseev, A. E.,
 Osetrova, T. A., Artemov, A. D., et al. (2023). Chemistry42: An
 AI-Driven Platform for Molecular Design and Optimization. Journal of
 Chemical Information and Modeling, 63(4), 1279--1290.

47. Nussinov, R.; Zhang, M.; Liu, Y.; Jang, H. AlphaFold,
 Artificial Intelligence (AI), and Allostery. J. Phys. Chem. B 2022,
 126, 6372--6383. \[CrossRef\] \[PubMed\].

48. P.-H. Wang, J.-H. Chen, Y.-Y. Yang, C. Lee, and Y. J.
 Tseng, "Recent advances in quantum computing for drug discovery and
 development," IEEE Nanotechnology Magazine, vol. 17, no. 2, pp.
 26--30, 2023.

50. Polykovskiy, D.; Zhebrak, A.; Vetrov, D.; Ivanenkov,
 Y.; Aladinskiy, V.; Mamoshina, P.; Bozdaganyan, M.; Aliper, A.;
 Zhavoronkov, A.; Kadurin, A. Entangled Conditional Adversarial
 Autoencoder for de Novo Drug Discovery. Mol. Pharmaceutics 2018, 15
 (10), 4398−4405.

51. Pun, F. W.; Liu, B. H. M.; Long, X.; Leung, H. W.;
 Leung, G. H. D.; Mewborne, Q. T.; Gao, J.; Shneyderman, A.;
 Ozerov, I. V.; Wang, J.; Ren, F.; Aliper, A.; Bischof, E.;
 Izumchenko, E.; Guan, X.; Zhang, K.; Lu, B.; Rothstein, J. D.;
 Cudkowicz, M. E.; Zhavoronkov, A. Identification of Therapeutic
 Targets for Amyotrophic Lateral Sclerosis Using PandaOmics - An
 AI-Enabled Biological Target Discovery Platform. Front. Aging
 Neurosci. 2022, 14, 914017.

52. Pun, F. W.; Ozerov, I. V.; Zhavoronkov, A. AI-Powered
 Therapeutic Target Discovery. Trends Pharmacol. Sci. 2023, 44 (9),
 561−572.

53. Putin, E.; Asadulaev, A.; Ivanenkov, Y.; Aladinskiy,
 V.; Sanchez- Lengeling, B.; Aspuru-Guzik, A.; Zhavoronkov, A.
 Reinforced Adversarial Neural Computer for de Novo Molecular
 Design. J. Chem. Inf. Model. 2018, 58 (6), 1194−1204.

54. R. Biswas, A. Basu, A. Nandy, A. Deb, K. Haque, and D.
 Chanda, "Drug discovery and drug identification using ai," pp.
 49--51, 2020.

55. R. Sotelo, "Quantum in consumer technology," IEEE
 Consumer Elec-tronics Magazine, pp. 1--3, 2023.

56. Ren, F.; Ding, X.; Zheng, M.; Korzinkin, M.; Cai, X.;
 Zhu, W.; Mantsyzov, A.; Aliper, A.; Aladinskiy, V.; Cao, Z.; Kong,
 S.; Long, X.; Man Liu, B. H.; Liu, Y.; Naumov, V.; Shneyderman, A.;
 Ozerov, I. V.; Wang, J.; Pun, F. W.; Polykovskiy, D. A.; Sun, C.;
 Levitt, M.; Aspuru- Guzik, A.; Zhavoronkov, A. AlphaFold Accelerates
 Artificial Intelligence Powered Drug Discovery: Efficient Discovery
 of aNovel CDK20 Small Molecule Inhibitor. Chem. Sci. 2023, 14
 (6),1443−1452.

57. S. Magazine, "Why did it take 35 years to get a malaria
 vaccine?" Smithsonian.com, Jun 2022. \[Online\]. Available:
 [[https://www.smithsonianmag.com/science-nature/why-did-it-take-]{.underline}](https://www.smithsonianmag.com/science-nature/why-did-it-take-)
 35-years-to-get-a-malaria-vaccine-180980151/

58. S. McArdle, S. Endo, A. Aspuru-Guzik, S. C. Benjamin,
 and X. Yuan, "Quantum computational chemistry," Rev. Mod. Phys.,
 vol. 92, p. 015003, Mar 2020. \[Online\]. Available:
 [[https://link.aps.org/doi/10.1103/]{.underline}](https://link.aps.org/doi/10.1103/)
 RevModPhys.92.015003

59. Schneider, G. Automating Drug Discovery. Nat. Rev. Drug
 Discovery 2018, 17 (2), 97−113.

60. Schraagen, J. M.; van Diggelen, J. A Brief History of
 the Relationship Between Expertise and Artificial Intelligence. In
 Expertise at Work; Palgrave Macmillan: Cham, Switzerland, 2021; pp.
 149--175.

61. Segler, M. H. S.; Kogej, T.; Tyrchan, C.; Waller, M. P.
 Generating Focused Molecule Libraries for Drug Discovery with
 Recurrent Neural Networks. ACS Cent Sci. 2018, 4 (1), 120−131.

62. Sellwood MA, et al. Artificial intelligence in drug
 discovery. Future Med Chem. 2018;10(17):2025--8.

63. Shaki F, et al. Artificial intelligence in
 pharmaceuticals: exploring applications and legal challenges. Pharm
 Biomed Res. 2024;10(1):1--10.

64. T. Davenport, R. Kalakota, The potential for
 artificial intelligence in healthcare, Future Healthc. J.
 6 (2) (2019) 94.

65. Tang X, et al. A survey of generative AI for de novo
 drug design: new frontiers in molecule and protein generation. Brief
 Bioinform. 2024;25(4):bbae338.

66. Tong X, et al. Generative models for de novo drug
 design. J Med Chem. 2021;64(19):14011--27.

67. Urban, A.; Sidorenko, D.; Zagirova, D.; Kozlova, E.;
 Kalashnikov, A.; Pushkov, S.; Naumov, V.; Sarkisova, V.;
 Leung, G. H. D.; Leung, H. W.; Pun, F. W.; Ozerov, I. V.; Aliper,
 A.; Ren, F.; Zhavoronkov, A. Precious1GPT: Multimodal
 Transformer-Based Transfer Learning for Aging Clock Development and
 Feature Importance Analysis for Aging and Age-Related Disease Target
 Discovery. Aging 2023, 15 (11), 4649−4666.

68. V. Chauhan, S. Negi, D. Jain, P. Singh, A. K. Sagar,
 and A. K. Sharma, "Quantum computers: A review on how quantum
 computing can boom ai," in 2022 2nd International Conference on
 Advance Computing and Innovative Technologies in Engineering
 (ICACITE), 2022, pp. 559--563.

69. V. Mahesh and S. Shijo, "Accelerating drug discovery
 with quantum computing," Evolution and Applications of Quantum
 Computing, pp. 175--181, 2023.

70. Wallach I, Dzamba M, Heifets A. AtomNet: a deep
 convolutional neural network for bioactivity prediction in
 structure-based drug discovery. arXiv preprint, 2015, Art no.
 arXiv:1510.02855.

71. Wang, L.; Ding, J.; Pan, L.; Cao, D.; Jiang, H.;
 Ding, X. Artificial intelligence facilitates drug design in the big
 data era. Chemom. Intell. Lab. Syst. 2019, 194, 103850. \[CrossRef\]

72. Wang, Q.; Feng, Y.; Huang, J.; Wang, T.; Cheng, G. A
 Novel Framework for the Identification of Drug Target Proteins:
 Combining Stacked Auto-Encoders with a Biased Support Vector
 Machine. PLoS One 2017, 12 (4), No. e0176486.

73. Watson DS, Krutzinna J, Bruce IN, et al. Clinical
 applications of machine learning algorithms: beyond the black box.
 BMJ 2019;364:l886. doi:10.1136/bmj.l886.

74. West, M. D.; Labat, I.; Sternberg, H.; Larocca, D.;
 Nasonkin, I.; Chapman, K. B.; Singh, R.; Makarev, E.; Aliper, A.;
 Kazennov, A.; Alekseenko, A.; Shuvalov, N.; Cheskidova, E.;
 Alekseev, A.; Artemov, A.; Putin, E.; Mamoshina, P.; Pryanichnikov,
 N.; Larocca, J.; Copeland, K.; Izumchenko, E.; Korzinkin, M.;
 Zhavoronkov, A. Use of Deep Neural Network Ensembles to Identify
 Embryonic-Fetal Transition Markers: Repression of COX7A1 in
 Embryonic and Cancer Cells. Oncotarget 2018, 9 (8), 7796−7811.

75. Wu R, et al. High-resolution de novo structure
 prediction from primary sequence. BioRxiv. 2022.
 [[https://doi.org/10.1101/2022.07.21]{.underline}](https://doi.org/10.1101/2022.07.21).

76. Wu Z, et al. MoleculeNet: a benchmark for molecular
 machine learning. Chem Sci. 2018;9(2):513--30.

77. Z. Wu, B. Ramsundar, E. N. Feinberg, J. Gomes, C.
 Geniesse, A. S. Pappu, K. Leswing, V. Pande, Moleculenet: a benchmark
 for molecular machine learning, Chem. Sci. 9 (2) (2018) 513--530.

78. Z. Zhu, C. Shi, Z. Zhang, S. Liu, M. Xu, X. Yuan, Y.
 Zhang, J. Chen, H. Cai, J. Lu, et al., Torchdrug: a powerful and
 flexible machine learning platform for drug discovery, preprint,
 arXiv:2202.08320, 2022.

79. Zhang S, et al. Applications of transformer-based language models in
 bioinformatics: a survey. Bioinform Adv. 2023;3(1):001.

80. Zhavoronkov, A. From Paper to Industrial-scale
 Platform : a 3-YearBehind the Paper Journey from GENTRL to
 Chemistry42. Bioengeering, Springer Nature.(accessed2022-09-21)

81. Zhavoronkov, A.; Ivanenkov, Y. A.; Aliper, A.;
 Veselov, M. S.; Aladinskiy, V. A.; Aladinskaya, A. V.; Terentiev, V.
 A.; Polykovskiy, D. A.; Kuznetsov, M. D.; Asadulaev, A.; Volkov, Y.;
 Zholus, A.; Shayakhmetov, R. R.; Zhebrak, A.; Minaeva, L. I.;
 Zagribelnyy, B. A.; Lee, L. H.; Soll, R.; Madge, D.; Xing, L.; Guo,
 T.; Aspuru-Guzik, A. Deep Learning Enables Rapid Identification of
 Potent DDR1 Kinase Inhibitors. Nat. Biotechnol. 2019, 37 (9),
 1038−1040.

82. Zhu, W.; Liu, X.; Li, Q.; Gao, F.; Liu, T.; Chen, X.;
 Zhang, M.; Aliper, A.; Ren, F.; Ding, X.; Zhavoronkov, A. Discovery
 of Novel and Selective SIK2 Inhibitors by the Application of
 AlphaFold Structures and Generative Models. Bioorg. Med. Chem. 2023,
 91, 117414.

