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
chemical "grammar," such as functional groups and bonds, rather than
linguistic semantics. While natural language processing (NLP) models
like transformers can analyze molecules via SMILES strings, traditional
fingerprinting relies on cheminformatics algorithms for applications
like virtual screening and toxicity prediction. Tools such as
Open-Source Cheminformatics Toolkit (RDKit) and
Chemical Descriptor Calculation Platform (ChemDes) (Dong et al., 2015)
are widely used to compute fingerprints efficiently, bridging the gap
between chemistry and AI. However, challenges
remain in optimizing fingerprint methods for diverse molecular datasets
and improving their predictive power in biological contexts. For
instance, ECFPs have proven effective in structure-activity modeling and
similarity searching but require further refinement to enhance their
utility in identifying active compounds in large-scale screenings.

#### 3.1.2 Predictive screening (QSAR/QSPR): using ML/DL to predict compound activity and properties before synthesis

AI-powered virtual screening and other in silico approaches have revolutionized the identification of potential lead compounds for drug discovery. These methods utilize computational techniques to rapidly evaluate vast chemical libraries, significantly accelerating the process and reducing costs compared with traditional high-throughput screening (Paul et al., 2021). Machine learning (ML) algorithms are essential for these methods. For instance, they can be used to create quantitative structure-activity relationship (QSAR) models, that predict the biological activity of compounds based on their chemical structures. These models can then be used to screen large chemical libraries and prioritize compounds with the highest probability of binding to the target of interest. These AI-driven approaches have the potential to significantly accelerate the identification of promising lead compounds and ultimately improve the success rate of drug development.

AI-driven techniques are revolutionizing drug development by optimizing critical properties, such as solubility, stability, and bioavailability. Machine learning (ML) algorithms can analyze vast datasets of chemical structures and their associated properties to predict crucial parameters with high accuracy. For example, in QSAR predictions, approximately 1000-5000 data points were used for water solubility predictions, whereas deep learning (DL) models can be used to predict drug stability under various conditions. For the protein function prediction task, researchers can leverage two open databases—the UniProt Consortium and the Protein Data Bank (PDB)—to gather protein sequence data from various species. This data can then be used to train prediction models through processes like batch downloading, data cleaning, and pre-processing. These predictive models enable researchers to rapidly identify and optimize drug candidates with improved physicochemical properties, thereby increasing their chances of successful clinical translation. Furthermore, deep learning (DL) algorithms, such as generative adversarial networks (GANs), can be used to generate novel chemical structures with desired properties, thereby expanding the chemical space explored in the drug design process.

#### 3.1.3 AI-enhanced molecular docking: improving the accuracy and speed of docking simulations

Molecular docking is a crucial step to generate potential candidates for lead compounds in drug discovery (Vamathevan et al., 2019). Docking is composed of several steps, for example, binding pocket identification, drug conformations sampling, scoring, and ranking. Generally, the binding pocket is provided by users in re-docking, cross-docking and virtual-screening tasks, with the pocket being identified by the co-crystal structure of the target protein and associated ligands in the experiments. However, with the development of protein structure prediction methods, for example, AlphaFold (Jumper et al., 2021) and ColabFold (Mirdita et al., 2022), a fast increasing number of protein structures are generated without information on ligands. Therefore, it is of high demand to perform reliable ligand docking based on protein structures only and without known binding pockets.

Traditionally, the blind docking is regarded as a task of docking around the entire protein, and many traditional docking programs are available for such tasks, for example, Autodock Vina (Trott & Olson, 2010), and Glide (Friesner et al., 2004). It is of great value to improve the docking speed and accuracy, given that normally a large space should be sampled in limited searching steps. To deal with such a problem, a number of optimized sampling methods were developed, for instance, QuickVina-W, which was developed based on QuickVina 2. QuickVina 2 optimized the local search frequency by searching only potentially important spatial points. These spatial points are identified by checking gradients of the scoring function against a thread history before local optimization. QuickVina-W is a program designed for blind docking, and the potentially significant points are identified by examination of the history of the present and other threads.

Besides the improvement on the sampling method, another strategy to increase speed and accuracy is to decrease the searching space through an identification of the potential ligand-protein binding pockets. Methods based on both traditional geometrical or machine learning strategies have been developed to recognize the protein pocket. The traditional methods have a relatively long history, and have observed the development of various strategies. For example, in FunFOLD and COFACTOR, the binding pocket is located by calculations on the similarity between the target and the templates of known pockets. Methods such as Fpocket on the other hand, are based on an examination of the shape and spatial geometry of the target protein. In another strategy one performs the binding pocket search using designed probes and identifies the pocket by calculating the interaction energy between the probes and protein.

In addition to the traditional methods, the strategies based on machine learning began to show high performance for the binding site prediction over the last few years. Among them, P2Rank (Krivák & Hoksza, 2018) is a widely used method based on the random forest algorithm, while COACH is trained by the support vector. In these methods based on deep learning, Three-Dimensional Convolutional Neural Network (3D-CNN) are often used, as in DeepSite (Jiménez et al., 2017), DeepSurf, and PUResNet.

Besides binding site prediction, many studies focused on combining the site recognizing, pose sampling and scoring in one shot to improve the performance of blind docking. EquiBind is a popular method among them, which applies an SE(3)-equivariant geometric deep learning strategy and successfully decreases the runtime of docking to less than 1 second per system. In addition, TANKBind, another deep learning-based method using trigonometry-aware neural networks, replaces the expensive sampling by evaluation of the protein-ligand interaction energy landscapes of different blocks of protein, which further improves the performance in docking tasks.

Recently, another state-of-the-art approach, DiffDock (Corso et al., 2022), was reported which is based on deep learning and treats the docking as a generative task. DiffDock used diffusion generative model to generate conformations and applied a confidence model to estimate the poses. This method enjoys a significant improvement in the docking accuracy, representing a powerful intermediate approach between traditional sampling and one-shot prediction.

The score function, which is commonly used to estimate the confidence of ligand binding poses, is another important factor affecting the accuracy of blind docking. There are four main categories of scoring functions, namely, physics-based, knowledge-based, empirical, and machine-learning based scoring functions. Many efforts have been paid to improve the performance of score functions, for instance, SMINA, GNINA (Francoeur et al., 2020), RF-Score, and IGN. Most of these methods are based on linear regression or machine learning, and present a reasonable performance in estimating the interactions between the proteins and ligands. However, most of the machine-learning based strategies are not introduced directly into the molecular docking procedure in the form of the scoring function, but are used to rescore the poses of ligands generated by the traditional sampling methods. Because a high computational cost is required when the network is used to guide the sampling, implementing a rescoring process after the sampling is a common strategy to improve the accuracy of the latter, as in GNINA.

In the present work, to improve the speed and accuracy of blind docking, researchers developed a method, Deep Site and Docking Pose (DSDP), to combine the advantages of both machine learning and traditional sampling strategies. It predicts the binding site on the protein and provides the potential location of ligands to decrease the searching space for the following binding pose sampling. A similar strategy was used in EquiBind, DiffDock (Corso et al., 2022), and Uni-Dock. In these protocols, the binding site identification and ligand conformation sampling are treated separately, and only the predicted site center is used in the sampling step by ignoring the shape of the binding pocket.

### 3.2 De Novo Drug Design

#### 3.2.1 Definition: using algorithms to design entirely new molecules from scratch

De novo molecular design aims to create new chemical entities with desired properties and/or activities. These properties may be easily quantifiable, such as molecular weight, or somewhat more abstract, as is the case of toxicity. This is an inherently difficult task owing to the immense search space of around 10^33 to 10^80 feasible molecules from which only a small fraction typically have the desired traits (Polishchuk et al., 2013). As such, de novo molecular design was, for many years, and mostly remains a process of almost exclusive trial and error, with human expert knowledge and intuition about chemistry playing a major role (Schneider, 2018). Meanwhile, the high costs associated with developing new molecules, reaching $2.8 billion dollars for a single compound, have also led to the implementation of computational tools capable of assisting the process. These have proven valuable and have found wide usage in practical applications (Schneider, 2018).

A forthright approach consists in enumerating all possible molecules that conform to valency rules and do not include chemically unstable functional groups. A notable example is the Chemical Space project, where this technique was employed to generate 166 billion molecules. Another technique, reaction-based de novo design, uses a set of known chemical reactions to combine various readily available building blocks into new molecules. This process can be guided by a similarity criterion to a known molecule of interest, giving rise to a large number of new similar molecules while ensuring their synthetic plausibility.

Evolutionary Algorithms (EAs) have also been successfully applied to de novo molecular design. As a recent example, AutoGrow4 uses an EA to create new predicted ligands. At each iteration, new molecules are created using a mutation operator, that performs an in silico chemical reaction, or a crossover operator that merges two compounds into a new one by randomly combining their decorating moieties. Grammatical Evolution on string representations and evolving molecular graphs provide alternative approaches that enable EAs to generate novel compounds targeting desired properties.

Although useful, these methods still leave room for improvement. For instance, enumeration often leads to molecules that are too difficult to synthesize, and reaction-based design is fundamentally restricted in its ability to explore the chemical space, both important aspects of molecular design. EAs, while computationally efficient and capable of performing on par with other recent approaches, rely on expertly encoded operations, possibly limiting the search space and not leveraging the large amounts of data currently available. Notwithstanding previous efforts on reviewing this field, a more rigorous approach to this subject, containing a more systematic coverage of the methods, can be important for researchers working on these topics. To that end, here we aim to provide a comprehensive review of deep learning (DL) methods for the targeted generation of novel compounds. As such, after an introduction to molecular representations, we present the most common deep generative models and the underlying neural network architectures. Researchers then focus on the different optimization approaches that allow to focus the search on molecules with desired properties or activities, closing with a review of the main practical applications (Gómez-Bombarelli et al., 2018).

#### 3.2.2 Challenges: navigating the immense size of chemical space

Creating new de novo molecules is an inherently difficult task owing to the immense search space of around 10^33 to 10^80 feasible molecules from which only a small fraction typically have the desired traits (Polishchuk et al., 2013). As such, de novo molecular design was always challenging. Despite all this progress and investment, only a few AI-based drugs are actually in human clinics. Moreover, the cost of developing a drug is still increasing and there is less adoption of AI tools for clinics at the moment. The pharmaceutical industries are one of the riskiest industry in the world, due to high failure rates and a long timeline.

Many traditional drug design scientists still think that all AI-enabled drug development is incremental and hype. The de novo design, drug response analysis, molecule optimization, and screening all are stages but most of the drug candidates fail in the clinical trials, making all of the developments incremental. Researchers have a very complex biological space, complex chemical space, and complex clinical space, and optimizing all of them at once is a big challenge.

#### 3.2.3 The role of deep learning: introducing generative AI as a solution

Generative AI tools such as ChatGPT hold significant potential in healthcare education and clinical practice. In pharmacy, they could enhance efficiency by assisting with prescription reviews, drug interaction checks, and adverse reaction monitoring, ultimately improving patient care. However, their application in pharmacy education remains under-explored, with limited research on implementation challenges, underscoring the need for further investigation.

Beyond assisting in clinical tasks, generative AI can also synthesize large datasets to train predictive models, expanding its utility in medical research. Among these AI techniques, GANs stand out as a powerful DL framework composed of two competing neural networks—a generator that creates synthetic data and a discriminator that evaluates its authenticity. Through iterative adversarial training, the generator refines its outputs to produce highly realistic data, enabling applications in medical imaging, super-resolution, and data augmentation. For example, Super-Resolution GAN has demonstrated success in enhancing low-resolution images, proving valuable in medical diagnostics and video surveillance.

Moving forward, realizing the full potential of Large Language Model (LLM) driven biotechnology will require establishing rigorous performance benchmarks, enhancing model transparency, and fostering deeper collaboration between computational and life science communities. This technological convergence promises to fundamentally reshape research methodologies and industrial processes across the biological sciences.

#### 3.2.4 Key models and tools: Variational Auto-encoders (VAEs), Generative Adversarial Networks (GANs), and Transformers

Recently, generative deep learning (DL) has emerged as a promising development for de novo molecular design, where deep neural networks are employed as generative models. This specific application has attracted considerable attention, with several novel architectures being proposed, that are briefly reviewed next.

**Recurrent Neural Networks (RNNs)** assume a sequential structure in the data, one where a sample is composed of a set of steps. This assumption is implemented by processing an input consecutively and introducing a connection carrying the output from previous steps into the current step. However, as the number of steps increases, RNNs can suffer from vanishing or exploding gradients during back propagation, impairing the training process and making the learning of long-term dependencies extremely difficult. In practice, this is handled by using specialized units such as gated recurrent units (GRUs) or Long Short-Term Memory (LSTM) (Hochreiter & Schmidhuber, 1997) which introduce gates, learnable parameters controlling the flow of information through the steps.

**Generative Adversarial Networks (GANs)** define a pair of networks, a generator, and a discriminator, trained in competition with each other. The generator is intended to transform random noise into real looking data and is trained to maximize the synthetic samples classified as real by the discriminator. Meanwhile, the discriminator is trained to better discern between generated and real data. The training framework resembles a competition, with both networks constantly improving and adapting to each other.

**Auto-encoders (AEs)** are neural networks trained to copy their input into the output with restrictions imposed as to not simply learn the identity function. They are usually thought of as two separate parts, an encoder that transforms the input into a more compact latent state, and a decoder that reconstructs the input from this representation. Both are trained together to minimize the information lost from reconstructing.

**Variational Auto-encoders (VAEs)** are a special type of AE, which assume that the data was sampled from an arbitrary statistical distribution. The encoder transforms its input into the parameters of a multidimensional statistical distribution, that is, a set of means and standard deviations. A sampling then occurs, where a point is drawn from the encoded distribution and fed into the decoder that reconstructs it into the original input. The objective function used for training consists of a term penalizing reconstruction errors and a term restricting the parameters encoded to be close to a normal distribution. This stochastic process acts to regularize the network while constraining the encoded parameters close to those of a normal distribution helps in forming a useful latent space (Kingma & Welling, 2014).

**Adversarial Auto-encoders (AAEs)** are an alternative to VAEs that employ adversarial training for structuring the latent space. In particular, the encoder transforms its input into a single point in the latent space. A discriminator network then attempts to discern between samples of a prior statistical distribution and encoded points. As such, the encoder can also be viewed as a generator engaged in a competition with the discriminator, ultimately balancing between the reconstruction and adversarial error.

**Generating Molecules:** There have been several approaches to applying generative deep learning (DL) to molecular generation, mainly differing on the chosen molecular representation. As such, usually more than one method surfaced for generating each of the main representations discussed in section. Borrowing from the natural language processing field, molecules can be generated as sequences, such as SMILES, by using RNNs. Specifically, when using RNNs as a generative model, each token in the string is encoded as a one-hot vector and the network is trained to predict the next character in the sequence. The generation of new data is achieved by running the network auto-regressively, that is, using its output as the input for the next time-step. This process is usually seeded with a special start token and the generation of a molecule ends when a special stop token is sampled. These two tokens are also respectively prefixed and appended to each molecule during training.

Several research groups have employed this method with a stacked RNN, usually with Long Short-Term Memory (LSTM) cells, leading to good rates of validity, novelty, and diversity (Segler et al., 2018; van Deursen et al., 2020; Olivecrona et al., 2017; Gupta et al., 2018). More complex architectures such as Variational Auto-encoders (VAEs) and Generative Adversarial Networks (GANs) have also been employed to generate molecules as strings; however, these also employ a RNN for the sequence generation process, either as the decoder or the generator (Gómez-Bombarelli et al., 2018; Guimaraes et al., 2018; Lim et al., 2018). Despite some limitations of sequence-based approaches, such as the need to learn a complex syntax and the mismatch between the edit distance of two SMILES and the underlying molecular similarity, these methods have produced impressive results.

#### 3.2.5 Impact: drastically accelerating the design of novel and optimized molecules

AI-based methods are being adopted in the health care industry where low-cost, intelligent, and flexible methods are affecting areas such as drug design, support for clinical decision making, diagnosis, prevention, and making clinical recommendations (Kempt & Nagel, 2022). AI applications were previously thought to be inferior to experimental high-throughput screening, combinatorial chemistry, and other technical drivers. It was difficult to create new chemical entities using computer programs, with desired features from the ground up, potentially even better than a human expert (Schneider, 2021).

The long and costly process of drug design can be accelerated by employing data science methods for target identification, de novo molecular design, drug repurposing, retrosynthesis and prediction of reactivity and bio-activity, FDA approval, and post-market analysis. AI has been implemented by some pharmaceutical organizations, with revenue from AI-based solutions in the pharmaceutical sector estimated to reach US $2.199 billion by 2022 (Paul et al., 2021). Deep neural networks (DNNs) can be used to boost prediction power when inferring the properties of small molecules, and one-shot learning can be used if a large amount of experimental data is not available.

Understanding technical and human errors, labeling constraints, and biological variability associated with the underlying data is crucial to create useful predictive models. It is difficult to represent the experimental data in numerical or computer-assisted form. AI is now being utilized to create representations of trials that allow for data categorization and, ultimately, the development of predictive models. Great things happen in minds and are never done alone, AI is delivering only a platform to execute the plans. Researchers need to develop novel hypotheses for drug discovery by employing the knowledge from different domain experts. After that, researchers can design a data analysis algorithm, and then researchers can learn from the data to modulate the hypothesis or modify the algorithms. In short, both mind and machine need to work in synergy.

Researchers hope that the use of machine learning, especially deep learning, will increase in the future and help us understand complex biological systems, generate particles with the desired properties, and lead to semi-automated smart healthcare systems. Researchers also expect that AI would be a valuable tool in understanding human biology, a catalyst in combating human diseases and will accelerate drug design. In terms of drug discovery, quality, and safety are more important than speed and cost, devising an AI system that can meet this multi-objective optimization in a multi-dimensional complex space is a huge challenge, which needs collaborative efforts from multiple disciplines in academia and industry.

### 3.3 AI in ADMET (Absorption, Distribution, Metabolism, Excretion, Toxicity) profiling

#### 3.3.1 Predicting pharmacokinetics and pharmacodynamics

The key concepts of pharmacology include pharmacokinetics and pharmacodynamics. While pharmacodynamics focuses on how a drug works in the body and how it affects other systems in the body, pharmacokinetics deals with the study of drug absorption, distribution, metabolism, and elimination (ADME) (Zhavoronkov et al., 2020). The application of AI techniques in pharmacokinetics and pharmacodynamics has created new opportunities to improve drug development and personalized treatments. It can analyze complex datasets, identify trends and make predictions that could improve patient outcomes, improve drug delivery and minimize side effects.

Machine learning (ML) and deep learning (DL) techniques are widely used to predict pharmacokinetic parameters. Numerous ML techniques—including Bayesian model, random forest (RF), support vector machine (SVM), artificial neural network (ANN), and decision tree—have been used to predict the ADME of drugs. To predict various pharmacokinetic parameters such as drug absorption, bioavailability, clearance, volume of distribution, and half-life, DL algorithms such as Convolutional Neural Networks (CNN), Long Short-Term Memory (LSTM), and recurrent neural network (RNN) are often used. A computational method called quantitative structure-activity relationship (QSAR) uses the chemical structure of a molecule to predict its biological activity.

With improved training data, a 47th version of admetSAR 2.0 is now available. This program also includes a module called ADMETopt, which is used to optimize lead activity based on expected ADMET attributes (Yang et al., 2019). AI techniques facilitate the modelling of drug-receptor interactions and the prediction of drug efficacy and toxicity in the field of pharmacodynamics. The use of AI in pharmacokinetics and pharmacodynamics can significantly accelerate the drug discovery process and improve precision medicine.

Obrezanova et al. used conventional ML techniques and multitask convolutional neural networks to calculate time-dependent pharmacokinetic profiles and nine in vivo pharmacokinetic parameters in rats (oral and intravenous administration) based on in vitro measured ADME properties and molecular chemical structures of 3000 different compounds. Ye et al. used transfer learning and multitasked learning to pre-train the model on over 30 million bioactivity data. The model was then used to estimate four human pharmacokinetic parameters: oral bioavailability, plasma protein binding, Volume of Distribution (Vd), and half-life, for 1104 FDA-approved small-molecule drugs. Compared to other traditional ML techniques, their DL model showed the highest performance (although not always by a significant margin) and generalization ability, achieving a mean absolute error (MAE) = 0.31 for oral bioavailability and MAE = 0.17 for volume of distribution (Vd).

Interestingly, Lou et al. created a model that predicts the bioavailability of monoclonal antibody (mAbs) administered through subcutaneous preparation in humans. A dataset of 45 clinical mAbs—with sequence and structure-based features including isoelectric point, total charge, aggregation propensity, solubility score, surface hydrophobicity spots, positive charge, and negative charge (with a threshold of 70% bioavailability)—were used to build a classification model. The study used a range of traditional Scikit-Learn ML techniques such as Adaptive Boost, Multilayer Perceptron, random forest (RF), and support vector machine (SVM). Among them, the tree approach showed the highest accuracy, reaching 78%.

Two areas that benefit greatly from the implementation of AI algorithms are drug design and optimization. De novo design, virtual screening, and structure-based drug design are just a few examples of these algorithms. The application of AI to drug development and optimization has a transformative impact on the discipline, enabling the rapid discovery of new therapeutic candidates and the more targeted and effective exploration of chemical space. Using ML, DL, and computer modelling methods, AI models can provide accurate predictions about the properties, interactions, and behaviours of potential drug candidates.

#### 3.3.2 Using multi-task learning to create comprehensive safety profiles

The stringent safety requirements associated with drug development make it challenging to introduce new drugs to the market. Clinical trials often fail due to unexpected toxicity and post-marketing safety issues, resulting in unnecessary morbidity and mortality. Clinical trials test the safety and effectiveness of a drug before it is approved while pharmacovigilance continually verifies a drug's safety information during its usage in patients.

The establishment of pre-market drug safety has been shown to benefit significantly from the use of AI-based approaches, particularly in the area of toxicity assessment. The vast reach of AI helps to predict the side effects, therapeutic targets, and in vivo safety of chemicals before manufacturing. Usually, after designing of the small molecule, the assays are employed to predict off-target toxicity, genotoxicity, organ toxicity, cytotoxicity, and mitochondrial toxicity. The analysis of new types of data, including gene expression and cell imaging data, combined with knowledge of chemical structure, can now be used to predict the effects of in vivo toxicity.

Various in silico calculation methods have proven useful in calculating the toxicity of drug candidates. These methods, which include target-based predictions and QSARs, evaluate multiple pharmacological properties to predict toxicity. Various drug safety effects—such as skin/eye irritation, tissue-specific toxicity, and 50% lethal drug dose (LD50) values—were modelled using QSAR techniques. In particular, the QSAR model allows for examining the relationship between multiple predictors (e.g., molecular features) and responses (e.g., biological activities such as binding affinity). Early QSAR approaches assessed the chemical properties of drug candidates using multivariate linear regression. Due to their excellent prediction accuracy, robustness, and readability of ensemble techniques such as random forest (RF) and support vector machines (SVMs), they are currently the most popular options. Compared to Naive Bayes, k-Nearest Neighbour (k-NN) and RF algorithms, SVM showed better performance in predicting activity values in the latest QSAR modelling of histone deacetylase (HDAC) inhibitors. In addition, with the help of such QSARs, it is possible to predict activity based on objectives such as toxicity.

Recently, Minerali et al. created and compared ML algorithms to predict drug-induced liver injury (DILI) using the company's Assay Central software. To do this, they used data previously collected by research teams at Pfizer and AstraZeneca, as well as data from the FDA. The best Bayesian model based on the DILI problem category from the DILI Rank database produced results with a receiver operating characteristic curve (ROC) of 81%, a sensitivity of 74%, a specificity of 76%, and an accuracy of 75%.

Williams et al. used ML to predict DILI with the pharmaceutical company, AstraZeneca. They were able to quantify the risk of an association being classified as low, medium, or high with an accuracy of 63%. The model provided an accuracy of 86%, a sensitivity of 87%, a specificity of 85%, a positive predictive value of 92%, and a negative predictive value of 78% for binary (yes/no) DILI prediction.

In addition to developing in silico models for eye irritation/eye corrosion (EI/EC) using ML techniques and molecular fingerprints, Verma & Matthews combined quantitative structure-toxicity relationship (STR) models by ANN to produce 88% sensitivity and 82% specificity for EI; and 96% sensitivity and 91% specificity for eye corrosion (EC). Manually gathering data for training from X-Mol and ChemIDplus yielded 95% accuracy for EI and 96% for EC.

Using data on the transcriptional and molecular profiles of over a thousand drugs—35% of which have known cardiotoxicities—Mamoshina et al. employed ML to predict various drug-induced cardiotoxicities. The dataset was selected from a wide range of open-source knowledge and data sources (including DrugBank), with the best predictor achieving an average of 79% for safe vs. risky drug area under the curve (AUC) and 66% for an unknown set of drugs. AUC (80%) indicated specific cardiotoxicity for specific drug classes and AUC (76%) indicated heart failures with potential for anti-neoplastic drugs across all investigated drug categories.

Webel et al. achieved greater than 70% cytotoxicity prediction accuracy using a DL strategy developed from an internal dataset of more than 34,000 compounds with less than 5% cytotoxic chemicals. When applying this technique to new compounds, care must be taken to carefully consider the scope of the model. However, one of the advantages of this method is the use of cytotoxicity maps that provide the visual meaning of the substructures of different chemicals.

Hunta et al. developed three ML methods based on SVM, k nearest neighbour (kNNs), and neural networks to predict drug-drug interactions (DDIs) in non-communicable diseases (NCDs). Using data from DrugBank, they combined the functions of transport proteins and enzymes and compared the results of different methods using five-fold cross-validation. This allowed them to determine which two NN layers performed best and predict NCDs based on pharmacokinetic mechanisms with an accuracy of 83% (F-measure 85.23% and AUC 90%).

## References

- Corso, G., Stärk, H., Jing, B., Barzilay, R., & Jaakkola, T. (2022). DiffDock: Diffusion steps, twists, and turns for molecular docking (arXiv:2210.01776). arXiv. https://arxiv.org/abs/2210.01776

- Dong, J., Cao, D.S., Miao, H.Y., Liu, S., Deng, B.C., Yun, Y.H., Wang, N.N., Lu, A.P., Zeng, W.B., & Chen, A.F. (2015). ChemDes: an integrated web-based platform for molecular descriptor and fingerprint computation. Journal of Cheminformatics, 7(1), 60. https://doi.org/10.1186/s13321-015-0109-z

- Francoeur, P.G., Masuda, T., Sunseri, J., Jia, A., Iovanisci, R.B., Snyder, I., & Koes, D.R. (2020). Three-Dimensional Convolutional Neural Networks and a Cross-Docked Data Set for Structure-Based Drug Design. Journal of Chemical Information and Modeling, 60(9), 4200-4215. https://doi.org/10.1021/acs.jcim.0c00411

- Friesner, R.A., Banks, J.L., Murphy, R.B., Halgren, T.A., Klicic, J.J., Mainz, D.T., Repasky, M.P., Knoll, E.H., Shelley, M., Perry, J.K., Shaw, D.E., Francis, P., & Shenkin, P.S. (2004). Glide: A New Approach for Rapid, Accurate Docking and Scoring. 1. Method and Assessment of Docking Accuracy. Journal of Medicinal Chemistry, 47(7), 1739-1749. https://doi.org/10.1021/jm0306430

- Gómez-Bombarelli, R., Wei, J.N., Duvenaud, D., Hernández-Lobato, J.M., Sánchez-Lengeling, B., Sheberla, D., Aguilera-Iparraguirre, J., Hirzel, T.D., Adams, R.P., & Aspuru-Guzik, A. (2018). Automatic chemical design using a data-driven continuous representation of molecules. ACS Central Science, 4, 268-276.

- Hochreiter, S., & Schmidhuber, J. (1997). Long Short-Term Memory. Neural Computation, 9(8), 1735-1780. https://doi.org/10.1162/neco.1997.9.8.1735

- Irwin, J.J., Tang, K.G., Young, J., Dandarchuluun, C., Wong, B.R., Khurelbaatar, M., Moroz, Y.S., Mayfield, J., & Sayle, R.A. (2020). ZINC20—A Free Ultralarge-Scale Chemical Database for Ligand Discovery. Journal of Chemical Information and Modeling, 60(12), 6065-6073. https://doi.org/10.1021/acs.jcim.0c00675

- Jiménez, J., Doerr, S., Martínez-Rosell, G., Rose, A.S., & De Fabritiis, G. (2017). DeepSite: protein-binding site predictor using 3D-convolutional neural networks. Bioinformatics, 33(19), 3036-3042. https://doi.org/10.1093/bioinformatics/btx350

- Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., Tunyasuvunakool, K., Bates, R., Žídek, A., Potapenko, A., Bridgland, A., Meyer, C., Kohl, S.A.A., Ballard, A.J., Cowie, A., Romera-Paredes, B., Nikolov, S., Jain, R., Adler, J., …, Hassabis, D. (2021). Highly accurate protein structure prediction with AlphaFold. Nature, 596(7873), 583-589. https://doi.org/10.1038/s41586-021-03819-2

- Kim, S., Thiessen, P.A., Bolton, E.E., Chen, J., Fu, G., Gindulyte, A., Han, L., He, J., He, S., Shoemaker, B.A., Wang, J., Yu, B., Zhang, J., & Bryant, S.H. (2016). PubChem Substance and Compound databases. Nucleic Acids Research, 44(D1), D1202-D1213. https://doi.org/10.1093/nar/gkv951

- Kingma, D.P., & Welling, M. (2014). Auto-encoding variational Bayes (arXiv:1312.6114). arXiv. https://arxiv.org/abs/1312.6114

- Krivák, R., & Hoksza, D. (2018). P2Rank: machine learning based tool for rapid and accurate prediction of ligand binding sites from protein structure. Journal of Cheminformatics, 10(1), 39. https://doi.org/10.1186/s13321-018-0285-8

- Li, Y., Liu, B., Deng, J., Guo, Y., & Du, H. (2024). Image-based molecular representation learning for drug development: a survey. Briefings in Bioinformatics, 25(4), bbae294. https://doi.org/10.1093/bib/bbae294

- Li, Z., Huang, R., Xia, M., Patterson, T.A., & Hong, H. (2024). Fingerprinting Interactions between Proteins and Ligands for Facilitating Machine Learning in Drug Discovery. Biomolecules, 14(1), 72. https://doi.org/10.3390/biom14010072

- Mendez, D., Gaulton, A., Bento, A.P., Chambers, J., De Veij, M., Félix, E., Magariños, M.P., Mosquera, J.F., Mutowo, P., Nowotka, M., Gordillo-Marañón, M., Hunter, F., Junco, L., Mugumbate, G., Rodriguez-Lopez, M., Atkinson, F., Bosc, N., Radoux, C.J., Segura-Cabrera, A., …, Leach, A.R. (2019). ChEMBL: towards direct deposition of bioassay data. Nucleic Acids Research, 47(D1), D930-D940. https://doi.org/10.1093/nar/gky1075

- Mirdita, M., Schütze, K., Moriwaki, Y., Heo, L., Ovchinnikov, S., & Steinegger, M. (2022). ColabFold: making protein folding accessible to all. Nature Methods, 19(6), 679-682. https://doi.org/10.1038/s41592-022-01488-1

- Olivecrona, M., Blaschke, T., Engkvist, O., & Chen, H. (2017). Molecular de-novo design through deep reinforcement learning. Journal of Cheminformatics, 9(1), 48. https://doi.org/10.1186/s13321-017-0235-x

- Paul, D., Sanap, G., Shenoy, S., Kalyane, D., Kalia, K., & Tekade, R.K. (2021). Artificial intelligence in drug discovery and development. Drug Discovery Today, 26(1), 80-93. https://doi.org/10.1016/j.drudis.2020.10.010

- Polishchuk, P.G., Madzhidov, T.I., & Varnek, A. (2013). Estimation of the size of drug-like chemical space based on GDB-17 data. Journal of Computer-Aided Molecular Design, 27(8), 675-679. https://doi.org/10.1007/s10822-013-9672-4

- Schneider, G. (2018). Automating drug discovery. Nature Reviews Drug Discovery, 17(2), 97-113. https://doi.org/10.1038/nrd.2017.232

- Segler, M.H.S., Kogej, T., Tyrchan, C., & Waller, M.P. (2018). Generating Focused Molecule Libraries for Drug Discovery with Recurrent Neural Networks. ACS Central Science, 4(1), 120-131. https://doi.org/10.1021/acscentsci.7b00512

- Tong, X., Liu, X., Tan, X., Li, X., Jiang, J., Xiong, Z., Xu, T., Jiang, H., Qiao, N., & Zheng, M. (2021). Generative Models for De Novo Drug Design. Journal of Medicinal Chemistry, 64(19), 14011-14027. https://doi.org/10.1021/acs.jmedchem.1c00927

- Trott, O., & Olson, A.J. (2010). AutoDock Vina: Improving the speed and accuracy of docking with a new scoring function, efficient optimization, and multithreading. Journal of Computational Chemistry, 31(2), 455-461. https://doi.org/10.1002/jcc.21334

- Vamathevan, J., Clark, D., Czodrowski, P., Dunham, I., Ferran, E., Lee, G., Li, B., Madabhushi, A., Shah, P., Spitzer, M., & Zhao, S. (2019). Applications of machine learning in drug discovery and development. Nature Reviews Drug Discovery, 18(6), 463-477.

- Weininger, D. (1988). SMILES, a chemical language and information system. 1. Introduction to methodology and encoding rules. Journal of Chemical Information and Computer Sciences, 28(1), 31-36. https://doi.org/10.1021/ci00057a005

- Wigh, D.S., Goodman, J.M., & Lapkin, A.A. (2022). A review of molecular representation in the age of machine learning. WIREs Computational Molecular Science, 12(5), e1603. https://doi.org/10.1002/wcms.1603

- Yang, H., Lou, C., Sun, L., Li, J., Cai, Y., Wang, Z., Li, W., Liu, G., & Tang, Y. (2019). admetSAR 2.0: web-service for prediction and optimization of chemical ADMET properties. Bioinformatics, 35(6), 1067-1069. https://doi.org/10.1093/bioinformatics/bty707

- Zhavoronkov, A., Vanhaelen, Q., & Oprea, T.I. (2020). Will artificial intelligence for drug discovery impact clinical pharmacology? Clinical Pharmacology & Therapeutics, 107, 780-785.
