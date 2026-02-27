# **Chapter Three:** AI for Drug Candidate Design and Screening

## 3.1. AI-Accelerated Virtual Screening

### 3.1.1. Molecular Representation: Inputting Molecules Into AI Models (SMILES Strings, Molecular Graphs, Fingerprints)

Advances in cheminformatics and artificial intelligence (AI) have
introduced several approaches to molecular representation. Traditional
methods rely on rule-based feature extraction, such as molecular
descriptors that quantify physical or chemical properties, and molecular
fingerprints that encode substructural information as binary strings or
numerical values. The most common representation is the Simplified
Molecular Input Line Entry System (SMILES), which provides a compact and
efficient way to encode chemical structures as strings (Weininger, 1988;
Wigh et al., 2022). Despite its simplicity, SMILES has limitations in
capturing the complexity of molecular interactions. As drug discovery
tasks become more sophisticated, traditional string-based
representations often fail to fully reflect the relationships between
molecular structure and key drug-related characteristics such as
biological activity and physicochemical properties (Li et al., 2024).
While traditional methods are interpretable, they often struggle to
navigate the vast chemical space in search of compounds with desired
biological properties. Therefore, molecular representation should not
only encode the chemical structure, but also enable efficient
exploration of chemical space. In recent years, AI-driven molecular
representation methods have applied deep learning techniques to learn
high-dimensional embeddings directly from large datasets. Models such as
graph neural networks (GNNs), variational auto-encoders (VAEs), and
transformers enable these approaches to move beyond predefined rules,
capturing both local and global molecular features (Irwin et al., 2020;
Kim et al., 2016; Mendez et al., 2019). These modern representations
better describe structural and functional relationships, providing
powerful tools for molecular generation, scaffold hopping, lead compound
optimization, and other tasks in drug discovery (Li et al., 2024; Tong
et al., 2021).

#### Molecular fingerprinting

Molecular fingerprinting is a computational technique that transforms
chemical structures into compact numerical representations, such as bit
vectors or feature arrays, to capture key structural and physicochemical
properties. These fingerprints facilitate rapid comparison, similarity
searches, and machine learning tasks, making them invaluable in drug
discovery and materials science. Common types include circular
fingerprints like Extended Connectivity Fingerprints (ECFP) for
substructure patterns, path-based fingerprints for bond sequences, and
3D fingerprints for molecular shapes (Li et al., 2024). Unlike natural
language processing (NLP), which processes human language, molecular
fingerprinting encodes chemical "grammar," such as functional groups and
bonds, rather than linguistic semantics. While natural language
processing (NLP) models like transformers can analyze molecules via
SMILES strings, traditional fingerprinting relies on cheminformatics
algorithms for applications like virtual screening and toxicity
prediction. Tools such as the Open-Source Cheminformatics Toolkit
(RDKit) and the Chemical Descriptor Calculation Platform (ChemDes) (Dong
et al., 2015) are widely used to compute fingerprints efficiently,
bridging the gap between chemistry and Artificial Intelligence (AI).
However, challenges remain in optimizing fingerprint methods for diverse
molecular datasets and improving their predictive power in biological
contexts. For instance, ECFPs have proven effective in
structure-activity modeling and similarity searching but require further
refinement to enhance their utility in identifying active compounds in
large-scale screenings.

### 3.1.2. Predictive Screening (QSAR/QSPR): Using ML/DL to Predict Compound Activity and Properties Before Synthesis

AI-powered virtual screening and other in silico approaches have
revolutionized the identification of potential lead compounds for drug
discovery. These methods utilize computational techniques to rapidly
evaluate vast chemical libraries, significantly accelerating the process
and reducing costs compared with traditional high-throughput screening
(Paul et al., 2021). Machine learning (ML) algorithms are essential for
these methods. For instance, they can be used to create quantitative
structure-activity relationship (QSAR) models, that predict the
biological activity of compounds based on their chemical structures.
These models can then be used to screen large chemical libraries and
prioritize compounds with the highest probability of binding to the
target of interest. These AI-driven approaches have the potential to
significantly accelerate the identification of promising lead compounds
and ultimately improve the success rate of drug development**.(Ref.)**

AI-driven techniques are revolutionizing drug development by optimizing
critical properties, such as solubility, stability, and bioavailability.
Machine learning (ML) algorithms can be utilized to create quantitative
structure-properties relationship(QSPR) and analyze vast datasets of
chemical structures and their associated properties to predict crucial
parameters with high accuracy. For example, in QSPR predictions,
approximately 1000-5000 data points were used for water solubility
predictions, whereas deep learning (DL) models can be used to predict
drug stability under various conditions. For the protein function
prediction task, researchers can leverage two open databases---the
UniProt Consortium and the Protein Data Bank (PDB)---to gather protein
sequence data from various species. This data can then be used to train
prediction models through processes like batch downloading, data
cleaning, and pre-processing. These predictive models enable researchers
to rapidly identify and optimize drug candidates with improved
physicochemical properties, thereby increasing their chances of
successful clinical translation. Furthermore, deep learning (DL)
algorithms, such as generative adversarial networks (GANs), can be used
to generate novel chemical structures with desired properties, thereby
expanding the chemical space explored in the drug design process.
**(Ref.)**

### 3.1.3. AI-Enhanced Molecular Docking: Improving the Accuracy and Speed of Docking Simulations

Molecular docking is a crucial step to generate potential candidates for
lead compounds in drug discovery (Vamathevan et al., 2019). Docking is
composed of several steps, for example, binding pocket identification,
drug conformations sampling, scoring, and ranking. Generally, the
binding pocket is provided by users in re-docking, cross-docking and
virtual-screening tasks, with the pocket being identified by the
co-crystal structure of the target protein and associated ligands in the
experiments. However, with the development of protein structure
prediction methods, for example, AlphaFold (Jumper et al., 2021) and
ColabFold (Mirdita et al., 2022), a fast increasing number of protein
structures are generated without information on ligands. Therefore, it
is of high demand to perform reliable ligand docking based on protein
structures only and without known binding pockets.

Traditionally, the blind docking is regarded as a task of docking around
the entire protein, and many traditional docking programs are available
for such tasks, for example, Auto dock Vina (Trott & Olson, 2010), and
Glide (Friesner et al., 2004). It is of great value to improve the
docking speed and accuracy, given that normally a large space should be
sampled in limited searching steps. To deal with such a problem, a
number of optimized sampling methods were developed, for instance, Quick
Vina-W, which was developed based on Quick Vina 2. Quick Vina 2
optimized the local search frequency by searching only potentially
important spatial points. These spatial points are identified by
checking gradients of the scoring function against a thread history
before local optimization. Quick Vina-W is a program designed for blind
docking, and the potentially significant points are identified by
examination of the history of the present and other threads.**(Ref.)**

Besides the improvement on the sampling method, another strategy to
increase speed and accuracy is to decrease the searching space through
an identification of the potential ligand-protein binding pockets.
Methods based on both traditional geometrical or machine learning
strategies have been developed to recognize the protein pocket. The
traditional methods have a relatively long history, and have observed
the development of various strategies. For example, in Fun FOLD and
COFACTOR, the binding pocket is located by calculations on the
similarity between the target and the templates of known pockets.
Methods such as F pocket on the other hand, are based on an examination
of the shape and spatial geometry of the target protein. In another
strategy one performs the binding pocket search using designed probes
and identifies the pocket by calculating the interaction energy between
the probes and protein. **(Ref.)**

In addition to the traditional methods, the strategies based on machine
learning began to show high performance for the binding site prediction
over the last few years. Among them, P2Rank (Krivák & Hoksza, 2018) is a
widely used method based on the random forest algorithm, while COACH is
trained by the support vector. In these methods based on deep learning,
Three-Dimensional Convolutional Neural Network (3D-CNN) are often used,
as in DeepSite (Jiménez et al., 2017), DeepSurf, and PUResNet.

Besides binding site prediction, many studies focused on combining site
recognition, pose sampling, and scoring in one shot to improve the
performance of blind docking. EquiBind is a popular method among them,
which applies a Special Euclidean group in 3 dimensions
(SE(3))-equivariant geometric deep learning strategy and successfully
decreases the runtime of docking to less than 1 second per system. In
addition, Trigonometry-Aware Neural networks (TANKBind), another deep
learning-based method, replaces the expensive sampling by evaluation of
the protein-ligand interaction energy landscapes of different blocks of
the protein, which further improves the performance in docking tasks.
**(Ref.)**

Recently, another state-of-the-art approach, DiffDock (Corso et al.,
2022), was reported which is based on deep learning and treats the
docking as a generative task. DiffDock used diffusion generative model
to generate conformations and applied a confidence model to estimate the
poses. This method enjoys a significant improvement in the docking
accuracy, representing a powerful intermediate approach between
traditional sampling and one-shot prediction. **(Ref.)**

The score function, which is commonly used to estimate the confidence of
ligand binding poses, is another important factor affecting the accuracy
of blind docking. There are four main categories of scoring functions,
namely, physics-based, knowledge-based, empirical, and machine-learning
based scoring functions. Many efforts have been paid to improve the
performance of score functions, for instance, SMINA, GNINA (Francoeur et
al., 2020), Random Forest Score (RF-Score), and Interaction Graph
Network (IGN). Most of these methods are based on linear regression or
machine learning, and present a reasonable performance in estimating the
interactions between the proteins and ligands. However, most of the
machine-learning based strategies are not introduced directly into the
molecular docking procedure in the form of the scoring function, but are
used to rescore the poses of ligands generated by the traditional
sampling methods. Because a high computational cost is required when the
network is used to guide the sampling, implementing a rescoring process
after the sampling is a common strategy to improve the accuracy of the
latter, as in GNINA. **(Ref.)**

In the present work, to improve the speed and accuracy of blind docking,
researchers developed a method, Deep Site and Docking Pose (DSDP), to
combine the advantages of both machine learning and traditional sampling
strategies. It predicts the binding site on the protein and provides the
potential location of ligands to decrease the searching space for the
following binding pose sampling. A similar strategy was used in
EquiBind, DiffDock (Corso et al., 2022), and Uni-Dock. In these
protocols, the binding site identification and ligand conformation
sampling are treated separately, and only the predicted site center is
used in the sampling step by ignoring the shape of the binding pocket.

## 3.2. De Novo Drug Design

### 3.2.1. Definition: Using Algorithms to Design Entirely New Molecules From Scratch

De novo molecular design aims to create new chemical entities with
desired properties and/or activities. These properties may be easily
quantifiable, such as molecular weight, or somewhat more abstract, as is
the case of toxicity. This is an inherently difficult task owing to the
immense search space of around 10\^33 to 10\^80 feasible molecules from
which only a small fraction typically have the desired traits
(Polishchuk et al., 2013). As such, de novo molecular design was, for
many years, and mostly remains a process of almost exclusive trial and
error, with human expert knowledge and intuition about chemistry playing
a major role (Schneider, 2018). Meanwhile, the high costs associated
with developing new molecules, reaching \$2.8 billion dollars for a
single compound, have also led to the implementation of computational
tools capable of assisting the process. These have proven valuable and
have found wide usage in practical applications (Schneider, 2018).

A forthright approach consists in enumerating all possible molecules
that conform to valency rules and do not include chemically unstable
functional groups. A notable example is the Chemical Space project,
where this technique was employed to generate 166 billion molecules.
Another technique, reaction-based de novo design, uses a set of known
chemical reactions to combine various readily available building blocks
into new molecules. This process can be guided by a similarity criterion
to a known molecule of interest, giving rise to a large number of new
similar molecules while ensuring their synthetic plausibility.
**(Ref.)**

Evolutionary Algorithms (EAs) have also been successfully applied to de
novo molecular design. As a recent example, AutoGrow4 uses an EA to
create new predicted ligands. At each iteration, new molecules are
created using a mutation operator, that performs an in silico chemical
reaction, or a crossover operator that merges two compounds into a new
one by randomly combining their decorating moieties. Grammatical
Evolution on string representations and evolving molecular graphs
provide alternative approaches that enable EAs to generate novel
compounds targeting desired properties. **(Ref.)**

Although useful, these methods still leave room for improvement. For
instance, enumeration often leads to molecules that are too difficult to
synthesize, and reaction-based design is fundamentally restricted in its
ability to explore the chemical space, both important aspects of
molecular design. EAs, while computationally efficient and capable of
performing on par with other recent approaches, rely on expertly encoded
operations, possibly limiting the search space and not leveraging the
large amounts of data currently available. Notwithstanding previous
efforts on reviewing this field, a more rigorous approach to this
subject, containing a more systematic coverage of the methods, can be
important for researchers working on these topics. To that end, here we
aim to provide a comprehensive review of deep learning (DL) methods for
the targeted generation of novel compounds. As such, after an
introduction to molecular representations, we present the most common
deep generative models and the underlying neural network architectures.
Researchers then focus on the different optimization approaches that
allow to focus the search on molecules with desired properties or
activities, closing with a review of the main practical applications
(Gómez-Bombarelli et al., 2018).

### 3.2.2. Challenges: Navigating the Immense Size of Chemical Space

Creating new de novo molecules is an inherently difficult task owing to
the immense search space of around 10\^33 to 10\^80 feasible molecules
from which only a small fraction typically have the desired traits
(Polishchuk et al., 2013). As such, de novo molecular design was always
challenging. Despite all this progress and investment, only a few
AI-based drugs are actually in human clinics. Moreover, the cost of
developing a drug is still increasing and there is less adoption of AI
tools for clinics at the moment. The pharmaceutical industries are one
of the riskiest industry in the world, due to high failure rates and a
long timeline. **(Ref.)**

Many traditional drug design scientists still think that all AI-enabled
drug development is incremental and hype. The de novo design, drug
response analysis, molecule optimization, and screening all are stages
but most of the drug candidates fail in the clinical trials, making all
of the developments incremental. Researchers have a very complex
biological space, complex chemical space, and complex clinical space,
and optimizing all of them at once is a big challenge. **(Ref.)**

### 3.2.3. The Role of Deep Learning: Introducing Generative AI as a Solution

Generative AI tools such as ChatGPT hold significant potential in
healthcare education and clinical practice. In pharmacy, they could
enhance efficiency by assisting with prescription reviews, drug
interaction checks, and adverse reaction monitoring, ultimately
improving patient care. However, their application in pharmacy education
remains under-explored, with limited research on implementation
challenges, underscoring the need for further investigation. **(Ref.)**

Beyond assisting in clinical tasks, generative AI can also synthesize
large datasets to train predictive models, expanding its utility in
medical research. Among these AI techniques, GANs stand out as a
powerful DL framework composed of two competing neural networks---a
generator that creates synthetic data and a discriminator that evaluates
its authenticity. Through iterative adversarial training, the generator
refines its outputs to produce highly realistic data, enabling
applications in medical imaging, super-resolution, and data
augmentation. For example, Super-Resolution GAN has demonstrated success
in enhancing low-resolution images, proving valuable in medical
diagnostics and video surveillance. **(Ref.)**

Moving forward, realizing the full potential of Large Language Model
(LLM) driven biotechnology will require establishing rigorous
performance benchmarks, enhancing model transparency, and fostering
deeper collaboration between computational and life science communities.
This technological convergence promises to fundamentally reshape
research methodologies and industrial processes across the biological
sciences. **(Ref.)**

### 3.2.4. Key Models and Tools: Variational Auto-Encoders (VAEs), Generative Adversarial Networks (GANs), and Transformers

Recently, generative deep learning (DL) has emerged as a promising
development for de novo molecular design, where deep neural networks are
employed as generative models. This specific application has attracted
considerable attention, with several novel architectures being proposed,
that are briefly reviewed next.

**Recurrent Neural Networks (RNNs)** assume a sequential structure in
the data, one where a sample is composed of a set of steps. This
assumption is implemented by processing an input consecutively and
introducing a connection carrying the output from previous steps into
the current step. However, as the number of steps increases, RNNs can
suffer from vanishing or exploding gradients during back propagation,
impairing the training process and making the learning of long-term
dependencies extremely difficult. In practice, this is handled by using
specialized units such as gated recurrent units (GRUs) or Long
Short-Term Memory (LSTM) (Hochreiter & Schmidhuber, 1997) which
introduce gates, learnable parameters controlling the flow of
information through the steps.

**Generative Adversarial Networks (GANs)** define a pair of networks, a
generator, and a discriminator, trained in competition with each other.
The generator is intended to transform random noise into real looking
data and is trained to maximize the synthetic samples classified as real
by the discriminator. Meanwhile, the discriminator is trained to better
discern between generated and real data. The training framework
resembles competition, with both networks constantly improving and
adapting to each other. **(Ref.)**

**Auto-encoders (AEs)** are neural networks trained to copy their input
into the output with restrictions imposed as not to simply learn the
identity function. They are usually thought of as two separate parts, an
encoder that transforms the input into a more compact latent state, and
a decoder that reconstructs the input from this representation. Both are
trained together to minimize the information lost from reconstructing.
**(Ref.)**

**Variational Auto-encoders (VAEs)** are a special type of AE, which
assume that the data was sampled from an arbitrary statistical
distribution. The encoder transforms its input into the parameters of a
multidimensional statistical distribution, that is, a set of means and
standard deviations. A sampling then occurs, where a point is drawn from
the encoded distribution and fed into the decoder that reconstructs it
into the original input. The objective function used for training
consists of a term penalizing reconstruction errors and a term
restricting the parameters encoded to be close to a normal distribution.
This stochastic process acts to regularize the network while
constraining the encoded parameters close to those of a normal
distribution help in forming a useful latent space (Kingma & Welling,
2014).

**Adversarial Auto-encoders (AAEs)** are an alternative to VAEs that
employ adversarial training for structuring the latent space. In
particular, the encoder transforms its input into a single point in the
latent space. A discriminator network then attempts to discern between
samples of a prior statistical distribution and encoded points. As such,
the encoder can also be viewed as a generator engaged in a competition
with the discriminator, ultimately balancing between the reconstruction
and adversarial error. **(Ref.)**

**Generating Molecules:** There have been several approaches to applying
generative deep learning (DL) to molecular generation, mainly differing
on the chosen molecular representation. As such, usually more than one
method surfaced for generating each of the main representations
discussed in section. Borrowing from the natural language processing
field, molecules can be generated as sequences, such as SMILES, by using
RNNs. Specifically, when using RNNs as a generative model, each token in
the string is encoded as a one-hot vector and the network is trained to
predict the next character in the sequence. The generation of new data
is achieved by running the network auto-regressively, that is, using its
output as the input for the next time-step. This process is usually
seeded with a special start token, and the generation of a molecule ends
when a special stop token is sampled. These two tokens are also prefixed
and appended to each molecule during training. **(Ref.)**

Several research groups have employed this method with a stacked RNN,
usually with Long Short-Term Memory (LSTM) cells, leading to good rates
of validity, novelty, and diversity (Gupta et al., 2018; Olivecrona et
al., 2017; Segler et al., 2018; van Deursen et al., 2020). More complex
architectures such as Variational Auto-encoders (VAEs) and Generative
Adversarial Networks (GANs) have also been employed to generate
molecules as strings; however, these also employ a RNN for the sequence
generation process, either as the decoder or the generator
(Gómez-Bombarelli et al., 2018; Guimaraes et al., 2018; Lim et al.,
2018). Despite some limitations of sequence-based approaches, such as
the need to learn a complex syntax and the mismatch between the edit
distance of two SMILES and the underlying molecular similarity, these
methods have produced impressive results.

### 3.2.5. Impact: Drastically Accelerating the Design of Novel and Optimized Molecules

AI-based methods are being adopted in the health care industry where
low-cost, intelligent, and flexible methods are affecting areas such as
drug design, support for clinical decision making, diagnosis,
prevention, and making clinical recommendations (Kempt & Nagel, 2022).
AI applications were previously thought to be inferior to experimental
high-throughput screening, combinatorial chemistry, and other technical
drivers. It was difficult to create new chemical entities using computer
programs, with desired features from the ground up, potentially even
better than a human expert (Schneider, 2021).

The long and costly process of drug design can be accelerated by
employing data science methods for target identification, de novo
molecular design, drug repurposing, retrosynthesis and prediction of
reactivity and bioactivity, FDA approval, and post-market analysis. AI
has been implemented by some pharmaceutical organizations, with revenue
from AI-based solutions in the pharmaceutical sector estimated to reach
US \$2.199 billion by 2022 (Paul et al., 2021). Deep neural networks
(DNNs) can be used to boost prediction power when inferring the
properties of small molecules, and one-shot learning can be used if a
large amount of experimental data is not available.

Understanding technical and human errors, labeling constraints, and
biological variability associated with the underlying data is crucial to
create useful predictive models. It is difficult to represent the
experimental data in numerical or computer-assisted form. AI is now
being utilized to create representations of trials that allow for data
categorization and, ultimately, the development of predictive models.
Great things happen in minds and are never done alone; AI is delivering
only a platform to execute the plans. Researchers need to develop novel
hypotheses for drug discovery by employing the knowledge from different
domain experts. After that, researchers can design a data analysis
algorithm, and then researchers can learn from the data to modulate the
hypothesis or modify the algorithms. In short, both mind and machine
need to work in synergy. **(Ref.)**

Researchers hope that the use of machine learning, especially deep
learning, will increase in the future and help us understand complex
biological systems, generate particles with the desired properties, and
lead to semi-automated smart healthcare systems. Researchers also expect
that AI would be a valuable tool in understanding human biology, a
catalyst in combating human diseases and will accelerate drug design. In
terms of drug discovery, quality, and safety are more important than
speed and cost, devising an AI system that can meet this multi-objective
optimization in a multi-dimensional complex space is a huge challenge,
which needs collaborative efforts from multiple disciplines in academia
and industry. **(Ref.)**

**3.3. AI in ADMET (Absorption, Distribution, Metabolism, Excretion,
Toxicity) profiling**

### 3.3.1. Predicting pharmacokinetics and pharmacodynamics

The key concepts of pharmacology include pharmacokinetics and
pharmacodynamics. While pharmacodynamics focuses on how a drug works in
the body and how it affects other systems in the body, pharmacokinetics
deals with the study of drug absorption, distribution, metabolism, and
elimination (ADME) (Zhavoronkov et al., 2020). The application of AI
techniques in pharmacokinetics and pharmacodynamics has created new
opportunities to improve drug development and personalized treatments.
It can analyze complex datasets, identify trends and make predictions
that could improve patient outcomes, improve drug delivery and minimize
side effects.

Machine learning (ML) and deep learning (DL) techniques are widely used
to predict pharmacokinetic parameters. Numerous ML
techniques---including Bayesian model, random forest (RF), support
vector machine (SVM), artificial neural network (ANN), and decision
tree---have been used to predict the ADME of drugs. To predict various
pharmacokinetic parameters such as drug absorption, bioavailability,
clearance, volume of distribution, and half-life, DL algorithms such as
Convolutional Neural Networks (CNN), Long Short-Term Memory (LSTM), and
recurrent neural network (RNN) are often used. A computational method
called quantitative structure-activity relationship (QSAR) uses the
chemical structure of a molecule to predict its biological activity.
**(Ref.)**

With improved training data, a 47th version of admetSAR 2.0 is now
available. This program also includes a module called ADMETopt, which is
used to optimize lead activity based on expected ADMET attributes (Yang
et al., 2019). AI techniques facilitate the modelling of drug-receptor
interactions and prediction of drug efficacy and toxicity in the field
of pharmacodynamics. The use of AI in pharmacokinetics and
pharmacodynamics can significantly accelerate the drug discovery process
and improve precision medicine. **(Ref.)**

Obrezanova and coworkers used conventional ML techniques and multitask
convolutional neural networks to calculate time-dependent
pharmacokinetic profiles and nine in vivo pharmacokinetic parameters in
rats (oral and intravenous administration) based on in vitro measured
ADME properties and molecular chemical structures of 3000 different
compounds. Ye and coworkers  used transfer learning and multitasked
learning to pre-train the model on over 30 million bioactivity data. The
model was then used to estimate four human pharmacokinetic parameters:
oral bioavailability, plasma protein binding, Volume of Distribution
(Vd), and half-life, for 1104 FDA-approved small-molecule drugs.
Compared to other traditional ML techniques, their DL model showed the
highest performance (although not always by a significant margin) and
generalization ability, achieving a mean absolute error (MAE) = 0.31 for
oral bioavailability and MAE = 0.17 for volume of distribution (Vd).
**(Ref.)**

Interestingly, Lou and coworkers  created a model that predicts the
bioavailability of monoclonal antibody (mAbs) administered through
subcutaneous preparation in humans. A dataset of 45 clinical mAbs---with
sequence and structure-based features including isoelectric point, total
charge, aggregation propensity, solubility score, surface hydrophobicity
spots, positive charge, and negative charge (with a threshold of 70%
bioavailability)---were used to build a classification model. The study
used a range of traditional Scikit-Learn ML techniques such as Adaptive
Boost, Multilayer Perceptron, random forest (RF), and support vector
machine (SVM). Among them, the tree approach showed the highest
accuracy, reaching 78%.**(Ref.)**

Two areas that benefit greatly from the implementation of AI algorithms
are drug design and optimization. De novo design, virtual screening, and
structure-based drug design are just a few examples of these algorithms.
The application of AI to drug development and optimization has a
transformative impact on the discipline, enabling the rapid discovery of
new therapeutic candidates and the more targeted and effective
exploration of chemical space. Using ML, DL, and computer modelling
methods, AI models can provide accurate predictions about the
properties, interactions, and behaviors of potential drug candidates.
**(Ref.)**

### 3.3.2. Using multi-task learning to create comprehensive safety profiles

The stringent safety requirements associated with drug development make
it challenging to introduce new drugs to the market. Clinical trials
often fail due to unexpected toxicity and post-marketing safety issues,
resulting in unnecessary morbidity and mortality. Clinical trials test
the safety and effectiveness of a drug before it is approved while
pharmacovigilance continually verifies a drug's safety information
during its usage in patients. **(Ref.)**

The establishment of pre-market drug safety has been shown to benefit
significantly from the use of AI-based approaches, particularly in the
area of toxicity assessment. The vast reach of AI helps to predict the
side effects, therapeutic targets, and in vivo safety of chemicals
before manufacturing. Usually, after designing of the small molecule,
the assays are employed to predict off-target toxicity, genotoxicity,
organ toxicity, cytotoxicity, and mitochondrial toxicity. The analysis
of new types of data, including gene expression and cell imaging data,
combined with knowledge of chemical structure, can now be used to
predict the effects of in vivo toxicity. **(Ref.)**

Various in silico calculation methods have proven useful in calculating
the toxicity of drug candidates. These methods, which include
target-based predictions and QSARs, evaluate multiple pharmacological
properties to predict toxicity. Various drug safety effects---such as
skin/eye irritation, tissue-specific toxicity, and 50% lethal drug dose
(LD50) values---were modelled using QSAR techniques. In particular, the
QSAR model allows for examining the relationship between multiple
predictors (e.g., molecular features) and responses (e.g., biological
activities such as binding affinity). Early QSAR approaches assessed the
chemical properties of drug candidates using multivariate linear
regression. Due to their excellent prediction accuracy, robustness, and
readability of ensemble techniques such as random forest (RF) and
support vector machines (SVMs), they are currently the most popular
options. Compared to Naive Bayes, k-Nearest Neighbour (k-NN) and RF
algorithms, SVM showed better performance in predicting activity values
in the latest QSAR modelling of histone deacetylase (HDAC) inhibitors.
In addition, with the help of such QSARs, it is possible to predict
activity based on objectives such as toxicity. **(Ref.)**

Recently, Minerali and coworkers. created and compared ML algorithms to
predict drug-induced liver injury (DILI) using the company's Assay
Central software. To do this, they used data previously collected by
research teams at Pfizer and AstraZeneca, as well as data from the FDA.
The best Bayesian model based on the DILI problem category from the DILI
Rank database produced results with a receiver operating characteristic
curve (ROC) of 81%, a sensitivity of 74%, a specificity of 76%, and an
accuracy of 75%.**(Ref.)**

Williams and cowokers used ML to predict DILI with the pharmaceutical
company, AstraZeneca. They were able to quantify the risk of an
association being classified as low, medium, or high with an accuracy of
63%. The model provided an accuracy of 86%, a sensitivity of 87%, a
specificity of 85%, a positive predictive value of 92%, and a negative
predictive value of 78% for binary (yes/no) DILI prediction. **(Ref.)**

In addition to developing in silico models for eye irritation/eye
corrosion (EI/EC) using ML techniques and molecular fingerprints, Verma
& Matthews combined quantitative structure-toxicity relationship (STR)
models by ANN to produce 88% sensitivity and 82% specificity for EI; and
96% sensitivity and 91% specificity for eye corrosion (EC). Manually
gathering data for training from X-Mol and ChemIDplus yielded 95%
accuracy for EI and 96% for EC. **(Ref.)**

Using data on the transcriptional and molecular profiles of over a
thousand drugs---35% of which have known cardiotoxicities---Mamoshina
and coworkers employed ML to predict various drug-induced
cardiotoxicities. The dataset was selected from a wide range of
open-source knowledge and data sources (including DrugBank), with the
best predictor achieving an average of 79% for safe vs. risky drug area
under the curve (AUC) and 66% for an unknown set of drugs. AUC (80%)
indicated specific cardiotoxicity for specific drug classes and AUC
(76%) indicated heart failures with potential for anti-neoplastic drugs
across all investigated drug categories. **(Ref.)**

Webel and coworkers  achieved greater than 70% cytotoxicity prediction
accuracy using a DL strategy developed from an internal dataset of more
than 34,000 compounds with less than 5% cytotoxic chemicals. When
applying this technique to new compounds, care must be taken to
carefully consider the scope of the model. However, one of the
advantages of this method is the use of cytotoxicity maps that provide
the visual meaning of the substructures of different chemicals.
**(Ref.)**

Hunta and coworkers developed three Machine Learning (ML) methods based
on Support Vector Machine (SVM), k-Nearest Neighbors (k-NNs), and Neural
Networks (NNs) to predict Drug-Drug Interactions (DDIs) in
Non-Communicable Diseases (NCDs). Using data from DrugBank, they
combined the functions of transport proteins and enzymes and compared
the results of different methods using five-fold cross-validation. This
allowed them to determine which two Neural Network (NN) layers performed
best and predict NCDs based on pharmacokinetic mechanisms with an
accuracy of 83% (F-measure 85.23% and Area Under the Curve (AUC)
90%).**(Ref.)**
