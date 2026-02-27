Abdullah muhammed fayyad

Article review section 3

**3. Al for Drug Candidate Design and Screening**

**• [3.1. Al-Accelerated Virtual Screening]{.underline}**

**• 3.1.1. Molecular Representation: Inputting molecules into Al models
(SMILES strings, molecular graphs, fingerprints**

Advances in cheminformatics and artificial intelligence (Al) have
introduced several approaches to molecular representation. Traditional
methods rely on rule-based feature extraction, such as molecular
descriptors that quantify physical or chemical properties, and molecular
fingerprints that encode substructural information as binary strings or
numerical values. The most common representation is the Simplified
Molecular Input Line Entry System (SMILES), which provides a compact and
efficient way to encode chemical structures as strings (Wigh,D.S 2022;
Weininger,D 1988). Despite its simplicity, SMILES has limitations in
capturing the complexity of molecular interactions. As drug discovery
tasks become more sophisticated, traditional string-based
representations often fail to fully reflect the relationships between
molecular structure and key drug-related characteristics such as
biological activity and physicochemical properties (Li,Y. 2024). While
traditional methods are interpretable, they often struggle to navigate
the vast chemical space in search of compounds with desired biological
properties. Therefore, molecular representation should not only encode
the chemical structure, but also enable efficient exploration of
chemical space. In recent years, Al-driven molecular representation
methods have applied deep learning techniques to learn high-dimensional
embeddings directly from large datasets. Models such as graph neural
networks (GNNs), variational auto-encoders (VAEs), and transformers
enable these approaches to move beyond predefined rules, capturing both
local and global molecular features (Kim,S. 2016; Mendez,D. 2019;
Irwin,J.J. 2020; Liu,T.Q. 2007). These modern representations better
describe structural and functional relationships, providing powerful
tools for molecular generation, scaffold hopping, lead compound
optimization, and other tasks in drug discovery (Tong,X.C 2021; Wang,S.
2019; Grisoni,F. 2018; Kuz\'min,V. 2021; Li,Z. 2024).

**Molecular fingerprinting:-**Molecular fingerprinting is a
computational technique that transforms chemical structures into compact
numerical representations, such as bit vectors or feature arrays, to
capture key structural and physicochemical properties. These
fingerprints facilitate rapid comparison, similarity searches, and
machine learning tasks, making them invaluable in drug discovery and
materials science. Common types include circular fingerprints like
Extended Connectivity Fingerprints (ECFP) for substructure patterns,
path-based fingerprints for bond sequences, and 3D fingerprints for
molecular shapes (Li Z et al., 2024). Unlike natural language processing
(NLP), which processes human language, molecular fingerprinting encodes
chemical \"grammar,\" such as functional groups and bonds, rather than
linguistic semantics. While natural language processing (NLP) models
like transformers can analyze molecules via SMILES strings, traditional
fingerprinting relies on cheminformatics algorithms for applications
like virtual screening and toxicity prediction. Tools such as
Open-Source Cheminformatics Toolkit (RDKit) (Landrum,G. 2013), and
Chemical Descriptor Calculation Platform (ChemDes)(Dong,J. et al., 2015)
are widely used to compute fingerprints efficiently,bridging the gap
between chemistry and Al (Dong J et al., 2015). However, challenges
remain in optimizing fingerprint methods for diverse molecular datasets
and improving their predictive power in biological contexts. For
instance, ECFPs have proven effective in structure-activity modeling and
similarity searching but require further refinement to enhance their
utility in identifying active compounds in large-scale screenings (Ucak
UV, 2023).

**• 3.1.2. Predictive Screening (QSAR/QSPR): Using ML/DL to predict
compound activity and properties before synthesis**

AI-powered virtual screening and in silico approaches have
revolutionized the identification of potential lead compounds for drug
discovery. These methods utilize computational techniques to rapidly
evaluate vast chemical libraries, significantly accelerating the process
and reducing costs compared with traditional high-throughput screening
(Naithani U, 2024; Paul D et al., 2021). Machine learning (ML)
algorithms are essential for these methods. For instance, they can be
used to create quantitative structure--activity relationship (QSAR)
models, that predict the biological activity of compounds based on their
chemical structures (Ching T et al., 2018). These models can then be
used to screen large chemical libraries and prioritize compounds with
the highest probability of binding to the target of interest (Niazi SK,
2023). These AI-driven approaches have the potential to significantly
accelerate the identification of promising lead compounds and ultimately
improve the success rate of drug development (Abou Hajal A,
2024).AI-driven techniques are revolutionizing drug development by
optimizing critical properties, such as solubility, stability, and
bioavailability (Vidhya KS et al., 2023). Machine learning (ML)
algorithms can analyze vast datasets of chemical structures and their
associated properties to predict crucial parameters with high accuracy
(Singh S et al., 2023). For example, In QSAR predictions, approximately
1000--5000 data points were used for water solubility predictions (Piir
G et al., 2018), whereas deep learning (DL) models can be used to
predict drug stability under various conditions (An F et al., 2022). For
the protein function prediction task, researchers can leverage two open
databases---the UniProt Consortium (Consortium, 2024) and the Protein
Data Bank (PDB)---to gather protein sequence data from various species
(Berman HM, 2025). This data can then be used to train prediction models
through processes like batch downloading, data cleaning, and
pre-processing (Chen J-Y et al., 2025). These predictive models enable
researchers to rapidly identify and optimize drug candidates with
improved physicochemical properties, thereby increasing their chances of
successful clinical translation (Vora LK et al., 2023). Furthermore,
deep learning (DL) algorithms, such as generative adversarial networks
(GANs), can be used to generate novel chemical structures with desired
properties, thereby expanding the chemical space explored in the drug
design process (Sousa T et al., 2021).

**• 3.1.3. AI-Enhanced Molecular Docking: Improving the accuracy and
speed of docking simulations.**

Molecular docking is a crucial step to generate potential candidates for
lead compounds in drug discovery.(Vamathevan,J 2019; Saikia,S 2018)
Docking is composed of several steps, for example, binding pocket
identification, drug conformations sampling, scoring, and ranking.
Generally, the binding pocket is provided by users in re-docking,
cross-docking and virtual-screening tasks, with the pocket being
identified by the co-crystal structure of the target protein and
associated ligands in the experiments. However, with the development of
protein structure prediction methods, for example, AlphaFold(Jumper,J.
2021) ColabFold,(Mirdita,M. 2022)and RosettaFold,(Baek,M. 2021) a fast
increasing number of protein structures are generated without
information on ligands. Therefore, it is of high demand to perform
reliable ligand docking based on protein structures only and without
known binding pockets. Traditionally, the blind docking is regarded as a
task of docking around the entire protein, and many traditional docking
programs are available for such tasks, for example, Autodock Vina,
(Trott,O.2010) and Glide.(Friesner,R.A. 2004) It is of great value to
improve the docking speed and accuracy, given that normally a large
space should be sampled in limited searching steps. To deal with such a
problem, a number of optimized sampling methods were developed, for
instance, QuickVina-W,(Hassan,N.M.2017)which was developed based on
QuickVina 2. (Alhossary,A 2015; Handoko,S.D.2012) QuickVina 2 optimized
the local search frequency by searching only potentially important
spatial points. These spatial points are identified by checking
gradients of the scoring function against a thread history before local
optimization. QuickVina-W is a program designed for blind docking, and
the potentially significant points are identified by examination of the
history of the present and other threads. Besides the improvement on the
sampling method, another strategy to increase speed and accuracy is to
decrease the searching space through an identification of the potential
ligand-protein binding pockets. Methods based on both traditional
geometrical or machine learning strategies have been developed to
recognize the protein pocket. (Macari,G 2019; Zhao,J 2020) The
traditional methods have a relatively long history, and have observed
the development of various strategies. For example, in FunFOLD(Roche,D.B
2013) and COFACTOR(Roy,A 2012), the binding pocket is located by
calculations on the similarity between the target and the templets of
known pockets. Methods such as Fpocket(Le Guilloux, 2009) on the other
hand, are based on an examination of the shape and spatial geometry of
the target protein. In another strategy one performs the binding pocket
search using designed probes and identifies the pocket by calculating
the interaction energy between the probes and protein. (Tsujikawa,H
2016) In addition to the traditional methods, the strategies based on
machine learning began to show high performance for the binding site
prediction over the last few years. Among them, P2Rank(Krivák,R. 2018)
is a widely used method based on the random forest algorithm, while
COACH(Yang,J. 2013) is trained by the support vector. In these methods
based on deep learning, Three-Dimensional Convolutional Neural Network
(3D-CNN) are often used, as in DeepSite,(Jiménez,J. 2017) DeepSurf
(Mylonas,S.K. 2021)and PUResNet.(Kandel,J. 2021) Besides binding site
prediction, many studies focused on combining the site recognizing, pose
sampling and scoring in one shot to improve the performance of blind
docking. EquiBind(Stärk,H. 2022) is a popular method among them, which
applies an SE(Li,Z. 2024)-equivariant geometric deep learning strategy
and successfully decreases the runtime of docking to \< 1 s per system.
In addition, TANKBind,(Lu,W. 2022) another deep learning-based method
using trigonometry-aware neural networks, replaces the expensive
sampling by evaluation of the protein-ligand interaction energy
landscapes of different blocks of protein, which further improves the
performance in docking tasks. Recently, another state-of-the-art
approach, DiffDock(Corso,G. 2022)was reported which is based on deep
learning and treats the docking as a generative task. DiffDock used
diffusion generative model to generate conformations and applied a
confidence model to estimate the poses. This method enjoys a significant
improvement in the docking accuracy, representing a powerful
intermediate approach between traditional sampling and one-shot
prediction. The score function, which is commonly used to estimate the
confidence of ligand binding poses, is another important factor
affecting the accuracy of blind docking. There are four main categories
of scoring functions, namely, physics-based, knowledge-based, empirical,
and machine-learning based scoring functions. Many efforts have been
paid to improve the performance of score functions, for instance,
SMINA,(Koes,D.R. 2013) GNINA,(McNutt,A.T.2021;Francoeur,P.G. 2020)
RF-Score,(Ballester,P.J. 2010) and IGN.(Jiang,2021) Most of these
methods are based on linear regression or machine learning, and present
a reasonable performance in estimating the interactions between the
proteins and ligands. However, most of the machine-learning based
strategies are not introduced directly into the molecular docking
procedure in the form of the scoring function, but are used to rescore
the poses of ligands generated by the traditional sampling methods.
Because a high computational cost is required when the network is used
to guide the sampling, implementing a rescoring process after the
sampling is a common strategy to improve the accuracy of the latter, as
in GNINA. In the present work, to improve the speed and accuracy of
blind docking, researchers developed a method, Deep Site and Docking
Pose (DSDP), to combine the advantages of both machine learning and
traditional sampling strategies. It predicts the binding site on the
protein and provides the potential location of ligands to decrease the
searching space for the following binding pose sampling. A similar
strategy was used in EquiBind,(Stärk,H. 2022) DiffDock(Corso,G.2022) and
Uni-Dock(Yu,Y.2023). In these protocols, the binding site identification
and ligand conformation sampling are treated separately, and only the
predicted site center is used in the sampling step by ignoring the shape
of the binding pocket.

**• [3.2. De Novo Drug Design]{.underline}**

**o 3.2.1. Definition: Using algorithms to design entirely new molecules
from scratch.**

De novo molecular design aims to create new chemical entities with
desired properties and/or activities. These properties may be easily
quantifiable, such as molecular weight, or somewhat more abstract, as is
the case of toxicity. This is an inherently difficult task owing to the
immense search space of around 10\^33- 10\^80 feasible molecules from
which only a small fraction typically have the desired traits(Polishchuk
et al., 2013).\' As such, de novo molecular design was, for many years,
and mostly remains a process of almost exclusive trial and error, with
human expert knowledge and intuition about chemistry playing a major
role(Schneider, 2018)Meanwhile, the high costs associated with
developing new molecules, reaching \$2.8 billion dollars for a single
compound, have also led to the implementation of computational tools
capable of assisting the process. These have proven valuable and have
found wide usage in practical applications(Schneider, 2018 ،DiMasi et
al., 2016), A forthright approach consists in enumerating all possible
molecules that conform to valency rules and do not include chemically
unstable functional groups. A notable example is the Chemical Space
project, where this technique was employed to generate 166 billion
molecules(Ruddigkeit et al., 2012 ،Walters, 2019). \*S Another
technique, reaction-based de novo design, uses a set of known chemical
reactions to combine various readily available building blocks into new
molecules.This process can be guided by a similarity criterion to a
known molecule of interest, giving rise to a large number of new similar
molecules while ensuring their synthetic plausibility(Walters, 2019
،Hartenfeller et al., 2012) .Evolutionary Algorithms (EAs) have also
been successfully applied to de novo molecular design. As a recent
example, AutoGrow4\'(Spiegel & Durrant, 2020) uses an EA to create new
predicted ligands. At each iteration, new molecules are created using a
mutation operator, that performs an in silico chemical reaction, or a
crossover operator that merges two compounds into a new one by randomly
combining their decorating moieties. Grammatical Evolution on string
representations and evolving molecular graphs provide alternative
approaches that enable EAs to generate novel compounds targeting desired
properties(Jensen, 2019، Yoshikawa et al., 2018)).\' Although useful,
these methods still leave room for improve-ment. For instance,
enumeration often leads to molecules that are too difficult to
synthesize, and reaction-based design is fundamentally restricted in its
ability to explore the chemical space, both important aspects of
molecular design. EAs, while computationally efficient and capable of
performing on par with other recent approaches , rely on expertly
encoded operations, possibly limiting the search space and not
leveraging the large amounts of data currently available.
(Gómez-Bombarellietal., 2019) generated molecules. Notwithstanding
previous efforts on reviewing this field, we feel that a more rigorous
approach to this subject, containing a more systematic coverage of the
methods, can be important for researchers working on these topics. To
that end, here we aim to provide a comprehensive review of deep learning
(DL) methods for the targeted generation of novel compounds. As such,
after an introduction to molecular representations, we present the most
common deep generative models and the underlying neural network
architectures. Researchers , then, focus on the different optimization
approaches that allow to focus the search on molecules with desired
properties or activities, closing with a review of the main practical
applications(Gómez-Bombarelli et al., 2019).

**o 3.2.2. The Challenges: Navigating the immense size of chemical
space**

Creating new de novo molecules is an inherently difficult task owing to
the immense search space of around 10\^33- 10\^80 feasible molecules
from which only a small fraction typically have the desired
traits(Polishchuk et al., 2013).\' As such, de novo molecular design was
always challenging Despite all this progress and investment, only a few
AI-based drugs are actually in human clinics (Strickland, 2019).
Moreover, the cost of developing a drug is still increasing and there is
less adoption of Al tools for clinics at the moment. The pharmaceutical
industries are one of the riskiest industry in the world, due to high
failure rates and a long timeline. Many traditional drug design
scientists still think that all Al-enabled drug development is
incremental and hype(Mit technology review top 10 breakthrough
technologies in 2020)The de novo design, drug response analysis,
molecule optimization, and screening all are stages but most of the drug
candidates fail in the clinical trials, making all of the developments
incremental. Researchers have a very complex biological space, complex
chemical space, and complex clinical space, and optimizing all of them
at once is a big challenge(D.E. Clark, 2006)

**o 3.2.3. The Role of Deep Learning: Introducing generative Al as a
solution**

Generative-Al tools such as ChatGPT hold significant potential in
healthcare education and clinical practice. In pharmacy, they could
enhance efficiency by assisting with prescription reviews, drug
interaction checks, and adverse reaction monitoring, ultimately
improving patient care. However, their application in pharmacy education
remains under-explored, with limited research on implementation
challenges, underscoring the need for further investigation (Mortlock R,
2024). Beyond assisting in clinical tasks, generative Al can also
synthesize large datasets to train predictive models, expanding its
utility in medical research. Among these Al techniques, GANs stand out
as a powerful DL framework composed of two competing neural networks---a
generator that creates synthetic data and a discriminator that evaluates
its authenticity. Through iterative adversarial training, the generator
refines its outputs to produce highly realistic data, enabling
applications in medical imaging, super-resolution, and data augmentation
(Elahi M et al., 2023). For example, Super-Resolution GAN has
demonstrated success in enhancing low-resolution images, proving
valuable in medical diagnostics and video surveillance (Lan L et al.,
2020). Moving forward, realizing the full potential of Large Language
Model (LLM) driven biotechnology will require establishing rigorous
performance benchmarks, enhancing model transparency, and fostering
deeper collaboration between computational and life science communities.
This technological convergence promises to fundamentally reshape
research methodologies and industrial processes across the biological
sciences (Li W et al., 2025) .

**• 3.2.4. Key Models and Tools: Variational Auto-encuders (VAEe),
Generative Adversarial Networks (GANs), and Transformers**

Recently, generative deep learning DL has emerged as a promising
development for de novo molecular design, where deep neural networks are
employed as generative models. This specific application has attracted
considerable attention, with several novel architectures being proposed,
that are briefly reviewed next, being also illustrated in

**[Recurrent Neural Networks(RNNs)]{.underline}.** assume a sequential
structure in the data, one where a sample is composed of a set of steps.
This assumption is implemented by processing an input consecutively and
introducing a connection carrying the output from previous steps into
the current step. However, as the number of steps increases, RNNs can
suffer from vanishing or exploding gradients during back propagation,
impairing the training process and making the learning of long-term
dependencies extremely difficult. In practice, this is handled by using
specialized units such as gated recurrent units (GRUs)(Cho,K.et al.,
2014) or Long Short-Term Memory (LSTM)(Hochreiter & Schmidhuber, 1997)
which introduce gates, learnable parameters controlling the flow of
information through the steps.(Goodfellow, Bengio, & Courville, 2016
,Chollet, 2018)

**[Generative Adversarial Networks(GANs)]{.underline}.** define a pair
of networks, a generator, and a discriminator, trained competition with
each other. The generator is intended to transform random noise into
real looking data and is trained to maximize the synthetic samples
classified as real by the discriminator. Meanwhile, the discriminator is
trained to better discern between generated and real data. The training
framework resembles a competition, with both networks constantly
improving and adapting to each other.

[**Auto-encoders (AEs)**]{.underline} are neural networks trained to
copy their input into the output with restrictions imposed as to not
simply learn the identity function. They are usually thought of as two
separate parts, an encoder that transforms the input into a more compact
latent state, and a decoder that reconstructs the input from this
representation. Both are trained together to minimize the information
lost from reconstructing (Goodfellow, Bengio, & Courville, 2016
,Chollet, 2018)

**[Variational Auto-encoders (VAEs)]{.underline}** are a special type of
AE, which assume that the data was sampled from an arbitrary statistical
distribution. The encoder transforms its input into the parameters of a
multidimensional statistical distribution, that is, a set of means and
standard deviations. A sampling then occurs, where a point is drawn from
the encoded distribution and fed into the decoder that reconstructs it
into the original input. The objective function used for training
consists of a term penalizing reconstruction errors and a term
restricting the parameters encoded to be close to a normal distribution.
This stochastic process acts to regularize the network while
constraining the encoded parameters close to those of a normal
distribution helps in forming a useful latent space(Chollet, 2018
,Kingma & Welling, 2014).

**[Adversarial Auto-encoders (AAEs)]{.underline}** are an alternative to
VAEs that employ adversarial training for structuring the latent space.
In particular, the encoder transforms its input into a single point in
the latent space. A discriminator network then attempts to discern
between samples of a prior statistical distribution and encoded points.
As such, the encoder can also be viewed as a generator engaged in a
competition with the discriminator, ultimately balancing between the
reconstruction and adversarial error(Makhzani et al., 2016) Generating
Molecules.There have been several approaches to applying generative deep
learning DL to molecular generation, mainly differing on the chosen
molecular representation. As such, usually more than one method surfaced
for generating each of the main representations discussed in section.
Borrowing from the natural language processing field, molecules can be
generated as sequences, such as SMILES, by using RNNs. Specifically,
when using RNNs as a generative model, each token in the string is
encoded as a one-hot vector and the network is trained to predict the
next character in the sequence. The generation of new data is achieved
by running the network auto-regressively, that is, using its output as
the input for the next time-step. This process is usually seeded with a
special start token and the generation of a molecule ends when a special
stop token is sampled. These two tokens are also respectively prefixed
and appended to each molecule during training, illustrates the
generative proce Several research groups have employed this method with
a stacked RNN, usually with Long Short-Term Memory (LSTM) cells, leading
to good rates of validity, novelty, and diversity(Segler et al., 2018
&van Deursen et al., 2020 &Olivecrona et al., 2017 &Gupta et al., 2018).
More complex archi-tectures such as Variational Auto-encoders (VAEs) and
Generative Adversarial Networks (GANs) have also been employed to
generate molecules as strings; however, these also employ a RNN for the
sequence generation process, either as the decoder or the
generator.(Gómez-Bombarelli et al., 2018 &Guimaraes et al., 2018 &Lim,
2018) Despite some limitations of sequence-based approaches, such as the
need to learn a complex syntax and the mismatch between the edit
distance of two SMILES and the underlying molecular similarity, these
methods have produced impressive results

**• 3.2.5. The Impact: Drastically accelerating the design of novel and
optimised molecules**

Al-based methods are being adopted in the health care industry where
low-cost, intelligent, and flexible methods are affecting areas such as
drug design, support for clinical decision making, diagnosis,
prevention, and making clinical recommendations (H,Kempt 2017). Al
applications were previously thought to be inferior to experimental
high-throughput screening, combinatorial chemistry, and other technical
drivers. It was difficult to create new chemical entities using computer
programs, with desired features from the ground up, potentially even
better than a human expert (G.Schneider, 2021). The long and costly
process of drug design can be accelerated by employing data science
methods for target identification, De novo molecular design, drug
repurposing, retrosynthesis and prediction of reactivity and
bio-activity, FDA approval, and post-market analysis. Al has been
implemented by some pharmaceutical organizations, with revenue from
Al-based solutions in the pharmaceutical sector estimated to reach US
\$2.199 billion by 2022 (Paul et al., 2021). Deep neural networks (DNNs)
can be used to boost prediction power when inferring the properties of
small molecules (Chen et al., 2018), and one-shot learning (L.Fei-Fei,
Fergus, & Perona, 2006) can be used if a large amount of experimental
data is not available. Understanding technical and human errors,
labeling constraints, and biological variability associated with the
underlying data is crucial to create useful predictive models. It is
difficult to represent the experimental data in numerical or
computer-assisted form. Al is now being utilized to create
representations of trials that allow for data categorization and,
ultimately, the development of predictive models (G.Schneider &
P.Schneider, 2017). Great things happen in minds and are never done
alone, Al is delivering only a platform to execute the plans.
Researchers need to develop novel hypotheses for drug discovery by
employing the knowledge from different domain experts. After that,
researchers can design a data analysis algorithm, and then researchers
can learn from the data to modulate the hypothesis or modify the
algorithms. In short, both mind and machine need to work in synergy.
Researchers hope that the use of machine learning, especially deep
learning, will increase in the future and help us understand complex
biological systems, generate particles with the desired properties, and
lead to semi-automated smart healthcare systems. Researchers also expect
that Al would be a valuable tool in understanding human biology, a
catalyst in combating human diseases and will accelerate drug design. In
terms of drug discovery, quality, and safety are more important than
speed and cost, devising an Al system that can meet this multi-objective
optimization in a multi-dimensional complex space is a huge challenge,
which needs collaborative efforts from multiple disciplines in academia
and industry.(S.Kanza, 2021)

**[• 3.3. Al In
ADMET\[Absorption,Distribution,Metabolism,Excretion,Toxicity\]profiling]{.underline}**

**3.3.1 Predicting Pharmacokinetics and Pharmacodynamics**

The key concepts of pharmacology include pharmacokinetics and
pharmacodynamics.While pharmacodynamics focuses on how a drug works in
the body and how it affects other systems in the body, pharmacokinetics
deals with the study of drug absorption, distribution, metabolism, and
elimination (ADME) (Zhavoronkov, 2020). The application of Al techniques
in pharmacokinetics and pharmacodynamics has created new opportunities
to improve drug development and personalized treatments. It can analyze
complex datasets, identify trends and make predictions that could
improve patient outcomes, improve drug delivery and minimize side
effects (van Laar, 2020; Noorbakhsh-Sabet, 2019).machine learning (ML)
and deep learning (DL) techniques are widely used to predict
pharmacokinetic parameters. Numerous ML techniques-including Bayesian
model, random forest (RF), support vector machine (SVM), artificial
neural network (ANN), and decision tree-have been used to predict the
ADME of drugs. To predict various pharmacokinetic parameters such as
drug absorption, bioavailability, clearance, volume of distribution, and
half-life, DL algorithms such as Convolutional Neural Net- works (CNN),
Long Short-Term Memory (LSTM), and recurrent neural network (RNN) are
often used. A computational method called quantitative
structure-activity relationship (QSAR) uses the chemical structure of a
molecule to predict its biological activity (Bhattamisra, 2023;
Westreich, 2010; Daoui, 2019). With improved training data, a 47th
version of admetSAR 2.0 is now available. This program also includes a
module called ADMETopt, which is used to optimize lead activity based on
expected ADMET attributes (Yang et al., 2019). Al techniques facilitate
the modelling of drug-receptor interactions and the prediction of drug
efficacy and toxicity in the field of pharmacodynamics. The use of Al in
pharmacokinetics and pharmacodynamics can significantly accelerate the
drug discovery process and improve precision medicine (Noorbakhsh-Sabet,
2019; Kim, 2020). Obrezanova et al. used conventional ML techniques and
multitask convolutional neural networks to calculate time-dependent
pharmacokinetic profiles and nine in vivo pharmacokinetic parameters in
rats (oral and intravenous administration) based on in vitro measured
ADME properties and molecular chemical structures of 3000 different
compounds (Obrezanova, 2023). Ye et al. used transfer learning and
multitasked learning to pre-train the model on over 30 million
bioactivity data The model was then used to estimate four human
pharmacokinetic parameters: oral bioavailability, plasma protein
binding. Volume of Distribution (Va), and half-life, for 1104
FDA-approved small-molecule drugs. Compared to other traditional ML
techniques, their DL model showed the highest performance (although not
always by a significant margin) and generalization ability, achieving a
mean absolute error or Mean Absolute Error MAE = 0.31 for oral
bioavailability and MAE = 0.17 for volume of distribution (Va) (Ye,Z.
2018). Interestingly, Lou et al. created a model that predicts the
bioavailability of monoclonal antibody (mAbs) administered through
subcutaneous preparation in humans. A dataset of 45 clinical mAbs-with
sequence and structure-based features including isoelectric point, total
charge, aggregation propensity, solubility score, surface hydrophobicity
spots, positive charge, and negative charge (with a threshold of 70%
bioavailability)-were used to build a classification model. The study
used a range of traditional Scikit-Learn ML techniques such as Adaptive
Boost, Multilayer Perceptron,random forest (RF), and support vector
machine (SVM). Among them, the tree approach showed the highest
accuracy, reaching 78% (Lou,H. 2021). Two areas that benefit greatly
from the implementation of Al algorithms are drug de-sign and
optimization. De novo design, virtual screening, and structure-based
drug design are just a few examples of these algorithms. The application
of Al to drug development and optimization has a transformative impact
on the discipline, enabling the rapid discovery of new therapeutic
candidates and the more targeted and effective exploration of chemical
space. Using ML, DL, and computer modelling methods, Al models can
provide accurate predictions about the properties, interactions, and
behaviours of potential drug candidates

**3.3.2.Using multi-task learning to create comprehensive safety
profiles.**

The stringent safety requirements associated with drug development make
it challenging to introduce new drugs to the market. Clinical trials
often fail due to unexpected toxicity and post-marketing safety issues,
resulting in unnecessary morbidity and mortality. Clinical trials test
the safety and effectiveness of a drug before it is approved while
pharmacovigilance continually verifies a drug\'s safety information
during its usage in patients (Tannenbaum, 2017). The establishment of
pre-market drug safety has been shown to benefit significantly from the
use of Al-based approaches, particularly in the area of toxicity
assessment (Raies, 2016). The vast reach of Al helps to predict the side
effects, therapeutic targets, and in vivo safety of chemicals before
manufacturing. Usually, after designing of the small molecule, the
assays are employed to predict off-target toxicity, genotoxicity, organ
toxicity, cytotoxicity, and mitochondrial toxicity (Hasselgren, 2018).
The analysis of new types of data, including gene expression and cell
imaging data, combined with knowledge of chemical structure, can now be
used to predict the effects of in vivo toxicity (Vo,A.H.2020). Various
in silico calculation methods have proven useful in calculating the
toxicity of drug candidates. These methods, which include target-based
predictions and QSARs, evaluate multiple pharmacological properties to
predict toxicity. Various drug safety effects-such as skin/ eye
irritation, tissue-specific toxicity, and 50% lethal drug dose (LDso)
values-were modelled using QSAR techniques (Patlewicz, 2016). In
particular, the QSAR model allows for examining the relationship between
multiple predictors (e.g., molecular features) and responses (e.g.,
biological activities such as binding affinity) (Zakariya Yahya Algamal,
2015). Early QSAR approaches assessed the chemical properties of drug
candidates using multivariate linear regression (Luco,J.M. 1997). Due to
their excellent prediction accuracy, robustness, and readability of
ensemble techniques such as random forest (RF) and support vector
machines (SVMs), they are currently the most popular options
(Ma,J.2015). Compared to Naive Bayes, k-Nearest Neighbour (k-NN) and RF
algorithms, SVM showed better performance in predicting activity values
in the latest QSAR modelling of histone deacetylase (HDAC) inhibitors
(Shi,J. 2018). In addition, with the help of such QSARs, it is possible
to predict activity based on objectives such as toxicity. Recently,
Minerali et al. created and compared ML algorithms to predict
drug-induced liver injury (DILI) using the company\'s Assay Central
software. To do this, they used data previously collected by research
teams at Pfizer and AstraZeneca, as well as data from the FDA. The best
Bayesian model based on the DILI problem category from the DILI Rank
database produced results with an receiver operating characteristic
curve (ROC) of 81%, a sensitivity of 74%, a specificity of 76%, and an
accuracy of 75% (Minerali, 2020). Williams et al. used ML to predict
DILI with the pharmaceutical company, AstraZeneca. They were able to
quantify the risk of an association being classified as low, medium, or
high with an accuracy of 63%. The model provided an accuracy of 86%, a
sensitivity of 87%, a specificity of 85%, a positive predictive value of
92%, and a negative predictive value of 78% for binary (yes/no) DILI
prediction (Williams, 2019). In addition to developing in silico models
for eye irritation/ eye corosion (EI/EC) using ML techniques and
molecular fingerprints, Verma et al. combined quantitative
structure-toxicity relationship (STR) models by ANN to produce 88%
sensitivity and 82% specificity for EI; and 96% sensitivity and 91%
specificity for eye corrosion (EC). Manually gathering data for training
from X-Mol (http://www.x-mol.com) and ChemIDplus yielded 95% accuracy
for El and 96% for EC (Verma, 2015). Using data on the transcriptional
and molecular profiles of over a thousand drugs---35% of which have
known cardiotoxicities-Mamoshina et al. employed ML to predict various
drug-induced cardiotoxicities. The dataset was selected from a wide
range of open-source knowledge and data sources (including DrugBank),
with the best predictor achieving an average of 79% for safe vs. risky
drug area under the curve (AUC) and 66% for an unknown set of drugs. AUC
(80%) indicated specific cardiotoxicity for specific drug classes and
AUC (76%) indicated heart failures with potential for anti-neoplastic
drugs across all investigated drug categories (Mamoshina, 2020). Webel
et al. achieved greater than 70% cytotoxicity prediction accuracy using
a DL strategy developed from an internal dataset of more than 34,000
compounds with less than 5% cytotoxic chemicals. When applying this
technique to new compounds, care must be taken to carefully consider the
scope of the model. However, one of the advantages of this method is the
use of cytotoxicity maps that provide the visual meaning of the
substructures of different chemicals (Webel, H.E.2020). Hunta et al.
developed three ML methods based on SVM,k nearest neighbour (kNNs), and
neural networks to predict drug-drug interactions (DDIs) in
non-communicable diseases (NCDs). Using data from DrugBank, they
combined the functions of transport proteins and enzymes and compared
the results of different methods using five-fold cross-validation. This
allowed them to determine which two NN layers performed best and predict
NCDs based on pharmacokinetic mechanisms with an accuracy of 83%
(F-measure 85.23% andAUC 90%) (Hunta,S. 2018).

**References:-**

- Abou Hajal A, Al Meslamani AZ. Insights into artificial intelligence
  utilisation in drug discovery. J Med Econ. 2024;27(1):304--8.

- -Ahmad, W., Simon, E., Chithrananda, S., Grand, G. & Ramsundar, B.
  ChemBERTa-2: Towards Chemical Foundation Models. arXiv:2209.01712.

- -Alhossary, A.; Handoko, S. D.; Mu, Y.; Kwoh, C. K. Fast, Accurate,
  and Reliable Molecular Docking with QuickVina 2. Bioinformatics 2015,
  31 (13), 2214--2216.

- An F, et al. Machine learning model for prediction of drug solubility
  in supercritical solvent: modeling and experimental validation. JMol
  Liq. 2022;363:119901.

- Baek, M.; DiMaio, F.; Anishchenko, I.; Dauparas, J.; Ovchinnikov, S.;
  Lee, G. R.; Wang, J.; Cong, Q.; Kinch, L. N.; Dustin Schaeffer, R.;
  Millán, C.; Park, H.; Adams, C.;Glassman, C. R.; DeGiovanni, A.;
  Pereira, J. H.; Rodrigues, A. V.; Van Dijk, A. A.;Ebrecht, A. C.;
  Opperman, D. J.; Sagmeister, T.; Buhlheller, C.; Pavkov-Keller, T.;
  Rathinaswamy, M. K.; Dalwadi, U.; Yip, C. K.; Burke, J. E.;
  Christopher Garcia, K.; Grishin, N. V.; Adams, P. D.; Read, R. J.;
  Baker, D. Accurate Prediction of Protein\...

- Ballester, P. J.; Mitchell, J. B. O. A Machine Learning Approach to
  Predicting Protein-Ligand Binding Affinity with Applications to
  Molecular Docking. Bioinformatics 2010, 26 (9), 1169--1175.

- Berman HM, Burley SK. Protein Data Bank (PDB): Fifty-three years young
  and having a transformative impact on science and society. QRev
  Biophys. 2025;58:e9.

- Bhattamisra, S.K.; Banerjee, P.; Gupta, P.; Mayuren, J.; Patra, S.;
  Candasamy, M. Artificial Intelligence in Pharmaceutical and\
  Healthcare Research. Big Data Cogn. Comput. 2023, 7, 10. \[CrossRef\]

- Chen J-Y, et al. Evaluating the advancements in protein language
  models for encoding strategies in protein function prediction: a
  comprehensive review. Front Bioeng Biotechnol. 2025;13:506508.

- Ching T, et al. Opportunities and obstacles for deep learning in
  biology and medicine. J R Soc Interface. 2018;15(141):20170387.

- Cho, K.; Van Merrienboer, B.; Bahdanau, D.; Bengio, Y. On the
  properties of neural machine translation: Encoder-decoder approaches.
  ar Xiv (Computation and Language), October 7, 2014, 1409.1259, ver. 2.

- Chollet, F. Deep learning with Python; Manning Publications Co: NY2018

- Consortium TU UniProt: the universal protein knowledgebase in 2025.
  Nucleic Acids Res. 2024;53(D1):D609--17.

- Corso, G.; Stärk, H.; Jing, B.; Barzilay, R.; Jaakkola, T. DiffDock:
  Diffusion Steps, Twists, and Turns for Molecular Docking. 2022,
  arXiv:2210.01776v1.

- D. Paul, G. Sanap, S. Shenoy, D. Kalyane, K. Kalia, R.K. Tekade,
  Artificial intelligence in drug discovery and development, Drug
  Discov. Today 26 (1) (2021)

- D.E. Clark, What has computer-aided molecular design ever done for
  drug discovery?, Expert Opin. Drug Discov. 1 (2) (2006) 103-110.

- Daoui, O.; Elkhattabi, S.; Chtita, S.; Elkhalabi, R.; Zgou, H.;
  Benjelloun, A.T. QSAR, molecular docking and ADMET properties in
  silico studies of novel 4, 5, 6, 7-tetrahydrobenzo (D\]-thiazol-2-Yl
  derivatives derived from dimedone as potent anti-tumor agents through
  inhibition of C-Met receptor tyrosine kinase. Heliyon 2021, 7, e07463.
  \[CrossRef\] \[PubMed\] 

- DiMasi, J. A.; Grabowski, H. G.; Hansen, R. W. Innovation in the
  pharmaceutical industry: New estimates of R&D costs. Journal of Health
  Economics 2016, 47, 20-33.

- Dong J, et al. ChemDes: an integrated web-based platform for molecular
  descriptor and fingerprint computation. J Cheminform. 2015;7:60.

- E. Strickland, How ibm Watson overpromised and underdelivered on ai
  health care-ieee spectrum, IEEE Spectrum: Technology, Engineering, and
  Science News (2019). Accessed from 

- Elahi M, et al. A comprehensive literature review of the applications
  of Al techniques through the lifecycle of industrial equipment. Discov
  Artif Intell. 2023;3(1):43.

- Francoeur, P. G.; Masuda, T.; Sunseri, J.; Jia, A.; Iovanisci, R. B.;
  Snyder, I.; Koes, D. R. Three-Dimensional Convolutional Neural
  Networks and a Crossdocked Data Set for Structure-Based Drug
  Design. J. Chem. Inf. Model. 2020, 60 (9), 4200--4215.

- Friesner, R. A.; Banks, J. L.; Murphy, R. B.; Halgren, T. A.;
  Klicic, J. J.; Mainz, D. T.; Repasky, M. P.; Knoll, E. H.; Shelley,
  M.; Perry, J. K.; Shaw, Francis, P.; Shenkin, P. S. Glide: A New
  Approach for Rapid, Accurate Docking and Scoring. 1. Method and
  Assessment of Docking Accuracy. J. Med. Chem. 2004, 47 (7),
  1739--1749.

- G. Schneider, An insight into artificial intelligence in drug
  discovery: an interview with professor gisbert Schneider, Expert Opin.
  Drug Discov. 16(9) (2021) 933--935.

- G. Schneider, P. Schneider, Macromolecular target prediction by
  self-organizing feature maps, Expert Opin. Drug Discov. 12 (3) (2017)
  271-277.

- Gomez-Bombarelli, R.; Wei, J. N.; Duvenaud, D.; Hernández- Tyrchan,
  C.; Rey- mond, J.-L.; Chen, H.; Engkvist, O. Randomized Lobato, J. M.;
  Sanchez- Lengeling, B.; Sheberla, D.; Aguilera- SMILES strings improve
  the quality of molecular generative models. J. Iparraguirre, J.;
  Hirzel, T. D.; Adams, R. P.; Aspuru-Guzik, A.Cheminf. 2019, 11, 71.
  Automatic Chemical Design Using a Data-Driven Continuous
  Representation of molecule

- Gomez-Bombarelli, R.; Wei, J. N.; Duvenaud, D.; Hernández- Lobato, J.
  M.; Sanchez- Lengeling, B.; Sheberla, D.; Aguilera- Iparraguirre, J.;
  Hirzel, T. D.; Adams, R. P.; Aspuru-Guzik, A. Automatic Chemical
  Design Using a Data-Driven Continuous Rep-resentation of Molecules.
  ACS Cent. Sci. 2018, 4, 268-276.

- Goodfellow, L; Bengio, Y.; Courville, A. Deep Learning; MIT press2016

- Grisoni, F., Merk, D., Byrne, R. & Schneider, G. Scaffold-Hopping from
  Synthetic Drugs byHolistic Molecular Representation. Sci. Rep. 8,
  16469 (2018).

- Guimaraes, G. L.; Sanchez-Lengeling, B.; Outeiral, C.; Farias, P. L.
  C.; Aspuru- Guzik, A. Objective-Reinforced Generative Adversarial
  Networks (ORGAN) for Sequence Generation Models. arXiv (Machine
  learning). February 7. 2018, 1705.10843, ver.

- Gupta, A.; Müller, A. T.; Huisman, B. J.; Fuchs, J. A.; Schneider, P.;
  Schneider, G. Generative Recurrent Networks for De Novo Drug Design.
  Mol. Inf. 2018, 37, 1700111.

- H. Chen, O. Engkvist, Y. Wang, M. Olivecrona, T. Blaschke, The rise of
  deep learning in drug discovery, Drug Discov. Today 23(6) (2018)
  1241--1250 

- H. Kempt, S.K. Nagel, Responsibility, second opinions and
  peer-disagreement: ethical and epistemological challenges of using ai
  in clinical diagnostic contexts, J. Med. Ethics 48 (4) (2022) 222-229.
  121 R. Qureshi, M. Irfan, T.M. Gondal et al.Heliyon 9 (2023) e17575

- Handoko, S. D.; Ouyang, X.; Su, C. T. T.; Kwoh, C. K.; Ong, Y. S.
  QuickVina: Accelerating AutoDock Vina Using Gradient-Based Heuristics
  for Global Optimization. IEEE/ACM Trans. Comput. Biol. Bioinforma.
  2012, 9 (5), 1266--1272.

- Hartenfeller, M.; Zettl, H.; Walter, M.; Rupp, M.; Reisen, F.;
  Proschak, E.; Weggen, S.; Stark, H.; Schneider, G. DOGS: reaction-ark,
  H.; Schneider, c: DO driven de novo design of bioactive com- pounds.
  PLoS Comput. Biol. 2012, 8, No. e1002380.

- Hassan, N. M.; Alhossary, A. A.; Mu, Y.; Kwoh, C. K. Protein-Ligand
  Blind Docking Using QuickVina-W with Inter-Process Spatio-Temporal
  Integration. Sci. Rep. 2017, 7 (1),1--13.

- Hasselgren, C.; Myatt, G.J. Computational Toxicology and Drug
  Discovery. Methods Mol. Biol. 2018, 1800, 233-244. \[CrossRef\]

- Hochreiter, S.; Schmidhuber, J. Long short-term memory. Neural
  computation 1997, 9, 1735-1780. discovery. Mol. Inf. 2016, 35, 3-14.

- Hunta, S.; Yooyativong, T.; Aunsri, N. A novel integrated action
  crossing method for drug-drug interaction prediction in
  non-communicable diseases. Comput. Methods Programs Biomed. 2018, 163,
  183-193. \[CrossRef\]

- . inhibitors. J. Cheminform. 2020, 12, 42. \[CrossRef\] \[PubMed\]

- Irwin, J. J. et al. ZINC20-A Free Ultralarge-scale chemical database
  for ligand discovery. J.Chem. Inf. Model. 60, 6065-6073 (2020).

- Jensen, J. H. A graph-based genetic algorithm and generative
  model/Monte Carlo tree search for the exploration of chemical space.
  Chem. Sci. 2019, 10, 3567-3572.

- Jiang, D.; Hsieh, C. Y.; Wu, Z.; Kang, Y.; Wang, J.; Wang, E.; Liao,
  B.; Shen, C.; Xu, L.;Wu, J.; Cao, D.; Hou, T. InteractionGraphNet: A
  Novel and Efficient Deep Graph Representation Learning Framework for
  Accurate Protein-Ligand Interaction Predictions. J. Med. Chem. 2021,
  64 (24), 18209--18232.

- Jiménez, J.; Doerr, S.; Martínez-Rosell, G.; Rose, A. S.; De
  Fabritiis, G. DeepSite: Protein-Binding Site Predictor Using
  3D-Convolutional Neural Networks. Bioinformatics 2017, 33 (19),
  3036--3042.

- Jumper, J.; Evans, R.; Pritzel, A.; Green, T.; Figurnov, M.;
  Ronneberger, O.; Tunyasuvunakool, K.; Bates, R.; Žídek, A.; Potapenko,
  A.; Bridgland, A.; Meyer, C.; Kohl, S. A. A.; Ballard, A. J.; Cowie,
  A.; Romera-Paredes, B.; Nikolov, S.; Jain, R.; Adler, J.; Back, T.;
  Petersen, S.; Reiman, D.; Clancy, E.; Zielinski, M.; Steinegger, M.;
  Pacholska, M.; Berghammer, T.; Bodenstein, S.; Silver, D.; Vinyals,
  O.; Senior, A. W.; Kavukcuoglu, K.; Kohli, P.; Hassabis, D. Highly
  Accurate Protein Structure Pred\...

- Kandel, J.; Tayara, H.; Chong, K. T. PUResNet: Prediction of
  Protein-Ligand Binding Sites Using Deep Residual Neural Network. J.
  Cheminform. 2021, 13 (1), 1--14.

- Kim, S. et al. PubChem substance and compound databases. Nucleic Acids
  Res. 44, D1202-D1213 (2016)

- Kim, H.; Kim, E.; Lee, I.; Bae, B.; Park, M.; Nam, H. Artificial
  intelligence in drug discovery: A comprehensive review of data-driven
  and machine learning approaches. Biotechnol. Bioprocess Eng. 2020, 25,
  895-930. \[CrossRef\] \[PubMed\]

- Kingma, D. P.; Welling, M. Auto-encoding variational bayes. arXiv
  (Machine Learning), May 1, 2014, 1312.6114, ver. 10.

- Koes, D. R.; Baumgartner, M. P.; Camacho, C. J. Lessons Learned in
  Empirical Scoring with Smina from the CSAR 2011 Benchmarking
  Exercise. J. Chem. Inf. Model. 2013, 53(8), 1893--1904.

- Krivák, R.; Hoksza, D. P2Rank: Machine Learning Based Tool for Rapid
  and Accurate Prediction of Ligand Binding Sites from Protein
  Structure. J. Cheminform. 2018, 10 (1), 39.

- Kuz\'min, V. et al. Simplex representation of molecular structure as
  universal QSAR/QSPR tool. Struct. Chem. 32, 1365-1392 (2021).

- L. Fei-Fei, R. Fergus, P. Perona, One-shot learning of object
  categories, IEEE Trans. Pattern Anal. Mach. Intell. 28 (4) (2006)
  594-611.

-  Lan L, et al. Generative adversarial networks and its applications in
  biomedical informatics. Front Public Health. 2020;8:164.

- Landrum G. Rdkit documentation. Release. 2013;1 (1-79):4.

- Le Guilloux, V.; Schmidtke, P.; Tuffery, P. Fpocket: An Open Source
  Platform for Ligand Pocket Detection. BMC Bioinformatics 2009, 10 (1),
  168.

- Li, Y., Liu, B. Y., Deng, J. Y., Guo, Y. & Du, H. B. Image-based
  molecular representation learning for drug development: a survey.
  Brief. Bioinform. 25, bbae294 (2024).

- Li W, et al. Large language model for knowledge synthesis and
  Al-enhanced biomanufacturing. Trends Biotechnol. 2025. 

- Li Z, et al. Fingerprinting interactions between proteins and ligands
  for facilitating machine learning in drug discovery. Biomolecules.
  2024;14(1):72.

- Lim, J.; Ryu, S.; Kim, J. W.; Kim, W. Y. Molecular generativ model
  based on conditional variational autoencoder for de novo molecular
  design. J. Cheminf. 2018, 10, 31.

- Liu, T. Q., Lin, Y. M., Wen, X., Jorissen, R. N. & Gilson, M. K.
  BindingDB: a web-accessible database of experimentally determined
  protein-ligand binding affinities. Nucleic Acids Res.35, D198-D201
  (2007).

- Lou, H.; Hageman, M.J. Machine learning attempts for predicting human
  subcutaneous bioavailability of monoclonal antibodies.Pharm. Res.
  2021, 38, 451-460. \[CrossRef)

- Lu, W. TANKBind : Trigonometry-Aware Neural NetworKs for Drug-Protein
  Binding Structure Prediction ArXiv : Submit / 4332744 \[ Cs . LG \] 31
  May 2022. bioRxiv 2022.

- Luco, J.M.; Ferretti, F.H. QSAR Based on Multiple Linear Regression
  and PLS Methods for the Anti-HIV Activity of a Large Group\
  of HEPT Derivatives. J. Chem. Inf. Comput. Sci. 1997, 37, 392-401.
  \[CrossRef\] \[PubMed\]

- Ma, J.; Sheridan, R.P.; Liaw, A.; Dahl, G.E.; Svetnik, V. Deep Neural
  Nets as a Method for Quantitative Structure-Activity\
  Relationships. J. Chem. Inf. Model. 2015, 55, 263-274. \[CrossRef\]
  \[PubMed\]

- Macari, G.; Toti, D.; Polticelli, F. Computational Methods and Tools
  for Binding Site Recognition between Proteins and Small Molecules:
  From Classical Geometrical Approaches to Modern Machine Learning
  Strategies. J. Comput. Aided. Mol. Des. 2019, 33 (10), 887--903.

- Makhzani, A.; Shlens, J.; Jaitly, N.; Goodfellow, I.; Frey, B.
  Adversarial autoencoders. arXiv (Machine Learning), May 25, 2016,

- Mamoshina, P.; Bueno-Orovio, A.; Rodriguez, B. Dual transcriptomic and
  molecular machine learning predicts all major clinical forms of drug
  cardiotoxicity. Front. Pharmacol. 2020, 11, 639. \[CrossRef\]

- McNutt, A. T.; Francoeur, P.; Aggarwal, R.; Masuda, T.; Meli, R.;
  Ragoza, M.; Sunseri, J.; Koes, D. R. GNINA 1.0: Molecular Docking with
  Deep Learning. J. Cheminform. 2021,13 (1), 1--20.

- Mendez, D. et al. ChEMBL: towards direct deposition of bioassay data.
  Nucleic Acids Res. 47, D930-D940 (2019).

- Minerali, E.; Foil, D.H.; Zorn, K.M.; Lane, T.R.; Ekins, S. Comparing
  machine learning algorithms for predicting drug-induced liver injury
  (DILI). Mol. Pharm. 2020, 17, 2628-2637. \[CrossRef\] \[PubMed\]

- Mirdita, M.; Schütze, K.; Moriwaki, Y.; Heo, L.; Ovchinnikov, S.;
  Steinegger, M. ColabFold: Making Protein Folding Accessible to All.
  Nat. Methods 2022, 19 (6), 679--682.

- Mit technology review top 10 breakthrough technologies in 2020,
  https://www.technologyreview.com/10-breakthrough-technologies/2020/.

- Mortlock R, Lucas C. Generative artificial intelligence (Gen-Al) in
  pharmacy education: utilization and implications for academic
  integrity: a scoping review. Explor Res Clin Soc Pharm.
  2024;15:100481.

- Mylonas, S. K.; Axenopoulos, A.; Daras, P. DeepSurf: A Surface-Based
  Deep Learning Approach for the Prediction of Ligand Binding Sites on
  Proteins. Bioinformatics 2021, 37(12), 1681--1690.

- Naithani U, Guleria V. Integrative computational approaches for
  discovery and evaluation of lead compound for drug design. Front Drug
  Discov. 2024. https:// doi. org/ 10. 3389/ fddsv. 2024. 13624 56.

- Niazi SK, Mariam Z. Recent advances in machine-learning-based
  chemoinformatics: a comprehensive review. Int J Mol Sci.
  2023;24(14):11448.

- Noorbakhsh-Sabet, N.; Zand, R.; Zhang, Y.; Abedi, V. Artificial
  intelligence transforms the future of health care. Am. J. Med. 2019,

- Obrezanova, O. Artificial intelligence for compound pharmacokinetics
  prediction. Curr. Opin. Struct. Biol. 2023, 79, 102546. \[CrossRef\]

- Olivecrona, M.; Blaschke, T.; Engkvist, O.; Chen, H. Molecular de-novo
  design through deep reinforcement learning. J. Cheminf. 2017, 9, 48.

- Patlewicz, G.; Fitzpatrick, J.M. Current and Future Perspectives on
  the Development, Evaluation, and Application of in Silico Approaches
  for Predicting Toxicity. Chem. Res. Toxicol. 2016, 29, 438-451.
  \[CrossRef\] \[PubMed\]

- Paul D, et al. Artificial intelligence in drug discovery and
  development. Drug Discov Today. 2021;26(1):80--93.

- Piir G, et al. Best practices for QSAR model reporting: physical and
  chemical properties, ecotoxicity, environmental fate, human health,
  and toxicokinetics endpoints. Environ Health Perspect.
  2018;126(12):126001.

- Polishchuk, P. G.; Madzhidov, T. I.; Varnek, A. Estimation of the size
  of drug-like chemical space based on GDB-17 data. J. Comput.- Aided
  Mol. Des. 2013, 27, 675.

- Raies, A.B.; Bajic, V.B. In silico toxicology: Computational methods
  for the prediction of chemical toxicity. Wiley Interdiscip. Rev.
  Comput. Mol. Sci. 2016, 6, 147-172. \[CrossRef\]

- Roche, D. B.; Buenavista, M. T.; McGuffin, L. J. The FunFOLD2 Server
  for the Prediction of Protein--Ligand Interactions. Nucleic Acids Res.
  2013, 41 (W1), W303--W307.

- Roy, A.; Yang, J.; Zhang, Y. COFACTOR: An Accurate Comparative
  Algorithm for Structure-Based Protein Function Annotation. Nucleic
  Acids Res. 2012, 40 (W1), W471--W477.

- Ruddigkeit, L.; van Deursen, R.; Blum, L. C.; Reymond, J.-L.
  Enumeration of 166 Billion Organic Small Molecules in the Chemical
  Universe Database GDB-17. J. Chem. Inf. Model. 2012, 52, 2864-2875.

- S. Kanza, C.L. Bird, M. Niranjan, W. McNeill, J.G. Frey, The ai for
  scientific discovery network+, Patterns 2 (1) (2021) 100162.

- Saikia, S.; Bordoloi, M. Molecular Docking: Challenges, Advances and
  Its Use in Drug Discovery Perspective. Curr. Drug Targets 2018, 20
  (5), 501--521.

- Schneider, G. Automating drug discovery. Nat. Rev. Drug Discovery\
  2018, 17, 97-113.

- Segler, M. H.; Kogej, T.; Tyrchan, C.; Waller, M. P. Generating
  focused molecule libraries for drug discovery with recurrent neural
  networks. ACS Cent. Sci. 2018, 4, 120-.

- Shi, J.; Zhao, G.; Wei, Y. Computational QSAR model combined molecular
  descriptors and fingerprints to predict HDAC1 inhibitors. Med. Sci.
  2018, 34, 52-58. \[CrossRef\] \[PubMed\]

- Singh S, et al. Artificial intelligence and machine learning in
  pharmacological research: bridging the gap between data and drug
  discovery. Cureus. 2023;15(8):e44359.

- Sousa T, et al. Generative deep learning for targeted compound design.
  J Chem Inf Model. 2021;61(11):5343--61.

- Spiegel, J.; Durrant, J. AutoGrow4: An open-source genetic algorithm
  for de novo drug design and lead optimization. J. Cheminf. 2020, 12,
  25.

- Stärk, H.; Ganea, O.-E.; Pattanaik, L.; Barzilay, R.; Jaakkola, T.
  EquiBind: Geometric Deep Learning for Drug Binding Structure
  Prediction. 2022.

- Tannenbaum, C.; Day, D. Age and sex in drug development and testing
  for adults. Pharmacol. Res. 2017, 121, 83-93. \[CrossRef\]

- Tong, X. C. et al. Generative models for De novo drug design. J. Med.
  Chem. 64, 14011- 14027 (2021).

- Trott, O.; Olson, A. J. AutoDock Vina: Improving the Speed and
  Accuracy of Docking with a New Scoring Function, Efficient
  Optimization, and Multithreading. J. Comput. Chem. 2010, 31 (2),
  455--461.

- Tsujikawa, H.; Sato, K.; Wei, C.; Saad, G.; Sumikoshi, K.; Nakamura,
  S.; Terada, T.; Shimizu, K. Development of a Protein--Ligand-Binding
  Site Prediction Method Based on Interaction Energy and Sequence
  Conservation. J. Struct. Funct. Genomics 2016, 17 (2),39--49.

- Ucak UV, Ashyrmamatov I, Lee J. Reconstruction of lossless molecular
  representations from fingerprints. J Cheminform. 2023;15(1):26.

- Vamathevan, J.; Clark, D.; Czodrowski, P.; Dunham, I.; Ferran, E.;
  Lee, G.; Li, B.; Madabhushi, A.; Shah, P.; Spitzer, M.; Zhao, S.
  Applications of Machine Learning in Drug Discovery and Development.
  Nat. Rev. Drug Discov. 2019, 18 (6), 463--477.

- van Deursen, R.; Erti, P.; Tetko, I. V.; Godin, G. GEN: highly
  efficient SMILES explorer using autodidactic generative examination
  networks. \]. Cheminf. 2020, 12, 22..

- van Laar, S.A.; Gombert-Handoko, K.B.; Guchelaar, H.J.; Zwaveling, J.
  An electronic health record text mining tool to collect\
  real-world drug treatment outcomes: A validation study in patients
  with metastatic renal cell carcinoma. Clin. Pharmacol. Ther.\
  2020, 108, 644-652. \[CrossRef\]

- Verma, R.P.; Matthews, E.J. Estimation of the chemical-induced eve
  injury using a weight-of-evidence (WoE) battery of 21 artificial
  neural network (ANN) c-QSAR models (QSAR-21): Part I: Irritation
  potential. Regul. Toxicol. Pharmacol. 2015, 71, 318-330. \[CrossRef)

- Vidhya KS, et al. Artificial intelligence's impact on drug discovery
  and development from bench to bedside. Cureus. 2023;15(10):e47486.

- Vo, A.H.; Van Vleet, T.R.; Gupta, R.R.; Liguori, M.J.; Rao, M.S. An
  Overview of Machine Learning and Big Data for Drug Toxicity
  Evaluation. Chem. Res. Toxicol. 2020, 33, 20-37. \[CrossRef\]
  \[PubMed\]

- Vora LK, et al. Artificial intelligence in pharmaceutical technology
  and drug delivery design. Pharmaceutics. 2023;15(7):1916.

- Walters, W. P. Virtual Chemical Libraries: Miniperspective. J. Med.
  Chem. 2019, 62, 1116-1124.

- Wang, S., Guo, Y., Wang, Y., Sun, H., Huang, J. Proceedings of the
  10th ACM International Conference on Bioinformatics, Computational
  Biology and Health Informatics. Association for Computing Machinery:
  Niagara Falls, NY, USA, 2019). 429-436.

- Webel, H.E.; Kimber, T.B.; Radetzki, S.; Neuenschwander, M.; Nazaré,
  M.; Volkamer, A. Revealing cytotoxic substructures in molecules using
  deep learning. J. Comput.-Aided Mol. Des. 2020, 34, 731-746.
  \[CrossRef\]

- Weininger, D. SMILES, a chemical language and information system. 1.
  Introduction to methodology and encoding rules. J. Chem. Inf. Comput.
  Sci. 28, 31-36 (1988).

- Westreich, D.; Lessler, J.; Funk, M.J. Propensity score estimation:
  Neural networks, support vector machines, decision trees\
  (CART), and meta-classifiers as alternatives to logistic
  regression. J. Clin. Epidemiol. 2010, 63, 826-833. \[CrossRef\]

- Wigh, D. S., Goodman, J. M. & Lapkin, A. A. A review of molecular
  representation in the age of machine learning. Wiley Interdiscip.
  Rev.-Comput. Mol. Sci. 12, 25010-25024 (2022).

- Williams, D.P.; Lazic, S.E.; Foster, A.J.; Semenova, E.; Morgan, P.
  Predicting drug-induced liver injury with Bayesian machine learning.
  Chem. Res. Toxicol. 2019, 33, 239-248. \[CrossRef\] \[PubMed\]

- Yang, H.; Lou, C.; Sun, L.; Li, J.; Cai, Y.; Wang, Z.; Li, W.; Liu,
  G.; Tang, Y. admetSAR 2.0: Web-service for prediction and optimization
  of chemical ADMET properties. Bioinformatics 2019, 35, 1067-1069.
  \[CrossRef\]

- Yang, J.; Roy, A.; Zhang, Y. Protein--Ligand Binding Site Recognition
  Using Complementary Binding-Specific Substructure Comparison and
  Sequence Profile Alignment. Bioinformatics 2013, 29 (20), 2588--2595.

- Ye, Z.; Yang, Y.; Li, X.; Cao, D.; Ouyang, D. An integrated transfer
  learning and multitask learning approach for pharmacokinetic parameter
  prediction. Mol. Pharm. 2018, 16, 533-541. \[CrossRef\] \[PubMed\]

- Yoshikawa, N.; Terayama, K.; Sumita, M.; Homma, T.; Oono, K.; latent
  space and molecular de novo generation diversity with Tsuda, K.
  Population-based De Novo Molecule Generation, Using heteroencoders.
  Biomolecules 2018, 8, 131. Grammatical Evolution. Chem. Lett. 2018,
  47, 1431-1434.

- Yu, Y.; Lu, S.; Gao, Z.; Zheng, H.; Ke, G. Do Deep Learning Models
  Really OutperformTraditional Approaches in Molecular Docking? 2023,
  arXiv:2302.07134.

- Zakariya Yahya Algamal, M.H.L. High-dimensional QSAR prediction of
  anticancer potency of imidazo(4,5-bJpyridine derivatives\
  using adjusted adaptive LASSO. J. Chemom. 2015, 29, 547-556.
  \[CrossRef\]

- Zhao, J.; Cao, Y.; Zhang, L. Exploring the Computational Methods for
  Protein-Ligand Binding Site Prediction. Comput. Struct. Biotechnol. J.
  2020, 18, 417--426.

- Zhavoronkov, A.; Vanhaelen, Q.; Oprea, T.I. Will artificial
  intelligence for drug discovery impact clinical pharmacology? Clin.\
  Pharmacol. Ther. 2020, 107, 780-785. \[CrossRef\] \[PubMed\]

- Zhou, G. et al. In International Conference on Learning
  Representations.
