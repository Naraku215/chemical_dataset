  ## 简介
  ChemData700K 是一个包含了九项化学核心任务，730K个高质量问答的大语言模型化学能力指令微调数据集.

  ChemData是大模型语料数据联盟成员单位上海人工智能实验室 AI for Science团队精心构建的大规模数据集，旨在为化学语言模型的微调提供支持，从而提高、释放其全部化学潜力。

## 数据集来源

为确保化学语言模型的有效性，获取多样化且高质量的数据集至关重要。因此，研究团队从大量的知名在线数据库中收集了海量化学数据，这其中包括了PubChem、ChEMBL、ChEBI、ZINC、USPTO、ORDerly、ChemXiv、LibreTexts Chemistry、Wikipedia和Wikidata等等。基于这一系列在线数据库，研究团队构建了ChemData数据集。

## 数据集构成

ChemData包含了7,000,000条用于指令微调（Instruction Tuning）的问答对。同时，ChemData覆盖了广泛的化学领域专业知识，主要面向三种化学任务类型：分子（Molecules）、反应（Reactions）以及其它特定领域（Domain-specific）任务。

● 分子（Molecules）
具体而言，分子相关的任务包括名称转换（Name Conversion）、文生分子（Caption2Mol）、分子生文（Mol2Caption）和分子属性预测（Molecular Property Prediction），这些任务旨在优化、提升语言模型对化学分子的理解能力。

● 反应（Reactions）
与反应相关的任务涵盖了逆合成（Retrosynthesis）、产物预测（Product Prediction）、产率预测（Yield Prediction）、温度预测（Temperature Prediction）和溶剂预测（Solvent Prediction），涵盖了化学反应的各个方面。

● 其它特定领域（Domain-specific）
此外，所有无法明确分类的其他数据都归类为特定领域任务，这些数据提升了化学语言模型对整个化学领域的理解。


## 引文
```
@misc{zhang2024chemllm,
      title={ChemLLM: A Chemical Large Language Model}, 
      author={Di Zhang and Wei Liu and Qian Tan and Jingdan Chen and Hang Yan and Yuliang Yan and Jiatong Li and Weiran Huang and Xiangyu Yue and Wanli Ouyang and Dongzhan Zhou and Shufei Zhang and Mao Su and Han-Sen Zhong and Yuqiang Li},
      year={2024},
      eprint={2402.06852},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
  ‌​‌‌​​​​‌​​​‌‌‌‌‌​​‌‌​‌​‌​​‌​​​‌‌​‌‌‌​‌‌‌​​‌‌‌‌​‌​​​‌​‌‌‌​​‌‌‌‌​‌​‌‌​​‌‌‌​​‌‌‌‌​‌​​‌‌‌​‌