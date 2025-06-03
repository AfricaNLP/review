---
title: "Machine Translation"
date: 2025-06-03
type: "topic"
layout: "single"
draft: false
---

# Machine Translation

<details>
<summary><strong>Improving Multilingual Math Reasoning for African Languages</strong> by Odunayo Ogundepo, Akintunde Oladipo, Kelechi Ogueji, Esther Adenuga, David Ifeoluwa Adelani, Jimmy Lin</summary>

- **Published**: May 26, 2025 at 11:35 AM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2505.19848v1)  
- **arXiv ID**: 2505.19848v1  
- **Summary**: Researchers working on low-resource languages face persistent challenges due to limited data availability and restricted access to computational resources. Although most large language models (LLMs) are predominantly trained in high-resource languages, adapting them to low-resource contexts, particularly African languages, requires specialized techniques. Several strategies have emerged for adapting models to low-resource languages in todays LLM landscape, defined by multi-stage pre-training and post-training paradigms. However, the most effective approaches remain uncertain. This work systematically investigates which adaptation strategies yield the best performance when extending existing LLMs to African languages. We conduct extensive experiments and ablation studies to evaluate different combinations of data types (translated versus synthetically generated), training stages (pre-training versus post-training), and other model adaptation configurations. Our experiments focuses on mathematical reasoning tasks, using the Llama 3.1 model family as our base model.

</details>

<details>
<summary><strong>Building a Functional Machine Translation Corpus for Kpelle</strong> by Kweku Andoh Yamoah, Jackson Weako, Emmanuel J. Dorley</summary>

- **Published**: May 24, 2025 at 11:39 PM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2505.18905v1)  
- **arXiv ID**: 2505.18905v1  
- **Summary**: In this paper, we introduce the first publicly available English-Kpelle dataset for machine translation, comprising over 2000 sentence pairs drawn from everyday communication, religious texts, and educational materials. By fine-tuning Meta's No Language Left Behind(NLLB) model on two versions of the dataset, we achieved BLEU scores of up to 30 in the Kpelle-to-English direction, demonstrating the benefits of data augmentation. Our findings align with NLLB-200 benchmarks on other African languages, underscoring Kpelle's potential for competitive performance despite its low-resource status. Beyond machine translation, this dataset enables broader NLP tasks, including speech recognition and language modelling. We conclude with a roadmap for future dataset expansion, emphasizing orthographic consistency, community-driven validation, and interdisciplinary collaboration to advance inclusive language technology development for Kpelle and other low-resourced Mande languages.

</details>

<details>
<summary><strong>In-Domain African Languages Translation Using LLMs and Multi-armed
  Bandits</strong> by Pratik Rakesh Singh, Kritarth Prasad, Mohammadi Zaki, Pankaj Wasnik</summary>

- **Published**: May 21, 2025 at 03:33 AM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2505.15069v1)  
- **arXiv ID**: 2505.15069v1  
- **Summary**: Neural Machine Translation (NMT) systems face significant challenges when working with low-resource languages, particularly in domain adaptation tasks. These difficulties arise due to limited training data and suboptimal model generalization, As a result, selecting an optimal model for translation is crucial for achieving strong performance on in-domain data, particularly in scenarios where fine-tuning is not feasible or practical. In this paper, we investigate strategies for selecting the most suitable NMT model for a given domain using bandit-based algorithms, including Upper Confidence Bound, Linear UCB, Neural Linear Bandit, and Thompson Sampling. Our method effectively addresses the resource constraints by facilitating optimal model selection with high confidence. We evaluate the approach across three African languages and domains, demonstrating its robustness and effectiveness in both scenarios where target data is available and where it is absent.

</details>

<details>
<summary><strong>Development of a WAZOBIA-Named Entity Recognition System</strong> by S. E Emedem, I. E Onyenwe, E. G Onyedinma</summary>

- **Published**: May 10, 2025 at 10:59 PM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2505.07884v1)  
- **arXiv ID**: 2505.07884v1  
- **Summary**: Named Entity Recognition NER is very crucial for various natural language processing applications, including information extraction, machine translation, and sentiment analysis. Despite the ever-increasing interest in African languages within computational linguistics, existing NER systems focus mainly on English, European, and a few other global languages, leaving a significant gap for under-resourced languages. This research presents the development of a WAZOBIA-NER system tailored for the three most prominent Nigerian languages: Hausa, Yoruba, and Igbo. This research begins with a comprehensive compilation of annotated datasets for each language, addressing data scarcity and linguistic diversity challenges. Exploring the state-of-the-art machine learning technique, Conditional Random Fields (CRF) and deep learning models such as Bidirectional Long Short-Term Memory (BiLSTM), Bidirectional Encoder Representation from Transformers (Bert) and fine-tune with a Recurrent Neural Network (RNN), the study evaluates the effectiveness of these approaches in recognizing three entities: persons, organizations, and locations. The system utilizes optical character recognition (OCR) technology to convert textual images into machine-readable text, thereby enabling the Wazobia system to accept both input text and textual images for extraction purposes. The system achieved a performance of 0.9511 in precision, 0.9400 in recall, 0.9564 in F1-score, and 0.9301 in accuracy. The model's evaluation was conducted across three languages, with precision, recall, F1-score, and accuracy as key assessment metrics. The Wazobia-NER system demonstrates that it is feasible to build robust NER tools for under-resourced African languages using current NLP frameworks and transfer learning.

</details>

<details>
<summary><strong>Bemba Speech Translation: Exploring a Low-Resource African Language</strong> by Muhammad Hazim Al Farouq, Aman Kassahun Wassie, Yasmin Moslem</summary>

- **Published**: May 05, 2025 at 09:51 AM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2505.02518v3)  
- **arXiv ID**: 2505.02518v3  
- **Summary**: This paper describes our system submission to the International Conference on Spoken Language Translation (IWSLT 2025), low-resource languages track, namely for Bemba-to-English speech translation. We built cascaded speech translation systems based on Whisper and NLLB-200, and employed data augmentation techniques, such as back-translation. We investigate the effect of using synthetic data and discuss our experimental setup.

</details>

<details>
<summary><strong>Low-Resource Neural Machine Translation Using Recurrent Neural Networks
  and Transfer Learning: A Case Study on English-to-Igbo</strong> by Ocheme Anthony Ekle, Biswarup Das</summary>

- **Published**: April 24, 2025 at 05:02 AM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2504.17252v1)  
- **arXiv ID**: 2504.17252v1  
- **Summary**: In this study, we develop Neural Machine Translation (NMT) and Transformer-based transfer learning models for English-to-Igbo translation - a low-resource African language spoken by over 40 million people across Nigeria and West Africa. Our models are trained on a curated and benchmarked dataset compiled from Bible corpora, local news, Wikipedia articles, and Common Crawl, all verified by native language experts. We leverage Recurrent Neural Network (RNN) architectures, including Long Short-Term Memory (LSTM) and Gated Recurrent Units (GRU), enhanced with attention mechanisms to improve translation accuracy. To further enhance performance, we apply transfer learning using MarianNMT pre-trained models within the SimpleTransformers framework. Our RNN-based system achieves competitive results, closely matching existing English-Igbo benchmarks. With transfer learning, we observe a performance gain of +4.83 BLEU points, reaching an estimated translation accuracy of 70%. These findings highlight the effectiveness of combining RNNs with transfer learning to address the performance gap in low-resource language translation tasks.

</details>

<details>
<summary><strong>Statistical Validation in Cultural Adaptations of Cognitive Tests: A
  Multi- Regional Systematic Review</strong> by Miit Daga, Priyasha Mohanty, Ram Krishna, Swarna Priya RM</summary>

- **Published**: April 18, 2025 at 06:25 AM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2504.13495v1)  
- **arXiv ID**: 2504.13495v1  
- **Summary**: This systematic review discusses the methodological approaches and statistical confirmations of cross-cultural adaptations of cognitive evaluation tools used with different populations. The review considers six seminal studies on the methodology of cultural adaptation in Europe, Asia, Africa, and South America. The results indicate that proper adaptations need holistic models with demographic changes, and education explained as much as 26.76% of the variance in MoCA-H scores. Cultural-linguistic factors explained 6.89% of the variance in European adaptations of MoCA-H; however, another study on adapted MMSE and BCSB among Brazilian Indigenous populations reported excellent diagnostic performance, with a sensitivity of 94.4% and specificity of 99.2%. There was 78.5% inter-rater agreement on the evaluation of cultural adaptation using the Manchester Translation Evaluation Checklist. A paramount message of the paper is that community feedback is necessary for culturally appropriate preparation, standardized translation protocols also must be included, along with robust statistical validation methodologies for developing cognitive assessment instruments. This review supplies evidence-based frameworks for the further adaptation of cognitive assessments in increasingly diverse global health settings.

</details>

<details>
<summary><strong>Lugha-Llama: Adapting Large Language Models for African Languages</strong> by Happy Buzaaba, Alexander Wettig, David Ifeoluwa Adelani, Christiane Fellbaum</summary>

- **Published**: April 09, 2025 at 02:25 AM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2504.06536v1)  
- **arXiv ID**: 2504.06536v1  
- **Summary**: Large language models (LLMs) have achieved impressive results in a wide range of natural language applications. However, they often struggle to recognize low-resource languages, in particular African languages, which are not well represented in large training corpora. In this paper, we consider how to adapt LLMs to low-resource African languages. We find that combining curated data from African languages with high-quality English educational texts results in a training mix that substantially improves the model's performance on these languages. On the challenging IrokoBench dataset, our models consistently achieve the best performance amongst similarly sized baselines, particularly on knowledge-intensive multiple-choice questions (AfriMMLU). Additionally, on the cross-lingual question answering benchmark AfriQA, our models outperform the base model by over 10%. To better understand the role of English data during training, we translate a subset of 200M tokens into Swahili language and perform an analysis which reveals that the content of these data is primarily responsible for the strong performance. We release our models and data to encourage future research on African languages.

</details>

<details>
<summary><strong>The Challenge of Achieving Attributability in Multilingual Table-to-Text
  Generation with Question-Answer Blueprints</strong> by Aden Haussmann</summary>

- **Published**: March 29, 2025 at 08:04 PM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2503.23204v1)  
- **arXiv ID**: 2503.23204v1  
- **Summary**: Multilingual Natural Language Generation (NLG) is challenging due to the lack of training data for low-resource languages. However, some low-resource languages have up to tens of millions of speakers globally, making it important to improve NLG tools for them. Table-to-Text NLG is an excellent measure of models' reasoning abilities but is very challenging in the multilingual setting. System outputs are often not attributable, or faithful, to the data in the source table. Intermediate planning techniques like Question-Answer (QA) blueprints have been shown to improve attributability on summarisation tasks. This work explores whether QA blueprints make multilingual Table-to-Text outputs more attributable to the input tables. This paper extends the challenging multilingual Table-to-Text dataset, TaTA, which includes African languages, with QA blueprints. Sequence-to-sequence language models are then finetuned on this dataset, with and without blueprints. Results show that QA blueprints improve performance for models finetuned and evaluated only on English examples, but do not demonstrate gains in the multilingual setting. This is due to inaccuracies in machine translating the blueprints from English into target languages when generating the training data, and models failing to rely closely on the blueprints they generate. An in-depth analysis is conducted on why this is challenging.

</details>

<details>
<summary><strong>Using Machine Learning to Detect Fraudulent SMSs in Chichewa</strong> by Amelia Taylor, Amoss Robert</summary>

- **Published**: February 24, 2025 at 08:17 AM UTC  
- **PDF**: [Download PDF](http://arxiv.org/pdf/2502.16947v1)  
- **arXiv ID**: 2502.16947v1  
- **Summary**: SMS enabled fraud is of great concern globally. Building classifiers based on machine learning for SMS fraud requires the use of suitable datasets for model training and validation. Most research has centred on the use of datasets of SMSs in English. This paper introduces a first dataset for SMS fraud detection in Chichewa, a major language in Africa, and reports on experiments with machine learning algorithms for classifying SMSs in Chichewa as fraud or non-fraud. We answer the broader research question of how feasible it is to develop machine learning classification models for Chichewa SMSs. To do that, we created three datasets. A small dataset of SMS in Chichewa was collected through primary research from a segment of the young population. We applied a label-preserving text transformations to increase its size. The enlarged dataset was translated into English using two approaches: human translation and machine translation. The Chichewa and the translated datasets were subjected to machine classification using random forest and logistic regression. Our findings indicate that both models achieved a promising accuracy of over 96% on the Chichewa dataset. There was a drop in performance when moving from the Chichewa to the translated dataset. This highlights the importance of data preprocessing, especially in multilingual or cross-lingual NLP tasks, and shows the challenges of relying on machine-translated text for training machine learning models. Our results underscore the importance of developing language specific models for SMS fraud detection to optimise accuracy and performance. Since most machine learning models require data preprocessing, it is essential to investigate the impact of the reliance on English-specific tools for data preprocessing.

</details>


