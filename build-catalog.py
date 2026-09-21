import json
from pathlib import Path

# Stable identifiers preserve reading progress if the schedule is revised.
rows = '''bengio|Neural language model|A Neural Probabilistic Language Model|2003|NLP|https://www.jmlr.org/papers/v3/bengio03a.html|Learn word vectors jointly with a conditional language model.
word2vec1|Word2Vec: CBOW & Skip-gram|Efficient Estimation of Word Representations in Vector Space|2013|NLP|1301.3781|Compare context-to-word and word-to-context prediction.
lenet|LeNet-5|Gradient-Based Learning Applied to Document Recognition|1998|CV|https://doi.org/10.1109/5.726791|Trace local connectivity, weight sharing and subsampling.
word2vec2|Word2Vec: negative sampling|Distributed Representations of Words and Phrases and their Compositionality|2013|NLP|1310.4546|Derive negative sampling and explain frequent-word subsampling.
glove|GloVe|GloVe: Global Vectors for Word Representation|2014|NLP|https://aclanthology.org/D14-1162/|Compare weighted co-occurrence fitting with predictive embeddings.
alexnet|AlexNet|ImageNet Classification with Deep Convolutional Neural Networks|2012|CV|https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks|Connect architecture, ReLU, augmentation and GPU training.
lstm|LSTM|Long Short-Term Memory|1997|NLP|https://doi.org/10.1162/neco.1997.9.8.1735|Follow the cell-state gradient and explain the original gates.
gru|GRU / RNN encoder-decoder|Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation|2014|NLP|1406.1078|Compare gated recurrence and sequence representations with LSTM.
vgg|VGG|Very Deep Convolutional Networks for Large-Scale Image Recognition|2014|CV|1409.1556|Calculate the receptive field of stacked small convolutions.
seq2seq|Seq2Seq|Sequence to Sequence Learning with Neural Networks|2014|NLP|1409.3215|Explain teacher forcing, decoding and the fixed-vector bottleneck.
bahdanau|Bahdanau attention|Neural Machine Translation by Jointly Learning to Align and Translate|2014|NLP|1409.0473|Derive soft alignment and additive attention.
inception|GoogLeNet / Inception|Going Deeper with Convolutions|2014|CV|1409.4842|Explain parallel convolution branches and 1x1 bottlenecks.
luong|Luong attention|Effective Approaches to Attention-based Neural Machine Translation|2015|NLP|1508.04025|Compare attention scoring functions and local versus global attention.
backprop|Backpropagation|Learning representations by back-propagating errors|1986|Foundations|https://doi.org/10.1038/323533a0|Derive gradients through two layers using the chain rule.
resnet|ResNet|Deep Residual Learning for Image Recognition|2015|CV|1512.03385|Distinguish the degradation problem from overfitting.
dropout|Dropout|Dropout: A Simple Way to Prevent Neural Networks from Overfitting|2014|Foundations|https://jmlr.org/papers/v15/srivastava14a.html|Explain stochastic masking and inference-time scaling.
batchnorm|Batch normalization|Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift|2015|Foundations|1502.03167|Track normalized axes, learned affine terms and running statistics.
layernorm|Layer normalization|Layer Normalization|2016|Foundations|1607.06450|Compare normalization axes and dependence on batch size.
bpe|BPE for translation|Neural Machine Translation of Rare Words with Subword Units|2015|NLP|1508.07909|Construct BPE merges and discuss rare-word representation.
transformer|The Transformer|Attention Is All You Need|2017|NLP|1706.03762|Trace Q, K, V shapes, masks, positions and computational cost.
elmo|ELMo|Deep Contextualized Word Representations|2018|NLP|1802.05365|Explain contextual embeddings and bidirectional language models.
gpt1|GPT-1|Improving Language Understanding by Generative Pre-Training|2018|NLP|https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf|Separate generative pretraining from supervised adaptation.
bert|BERT|BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding|2018|NLP|1810.04805|Explain masked language modelling and downstream adaptation.
roberta|RoBERTa|RoBERTa: A Robustly Optimized BERT Pretraining Approach|2019|NLP|1907.11692|Ask which apparent model gains come from the training recipe.
gpt2|GPT-2|Language Models are Unsupervised Multitask Learners|2019|NLP|https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf|Compare task conditioning with explicitly supervised fine-tuning.
xlnet|XLNet|XLNet: Generalized Autoregressive Pretraining for Language Understanding|2019|NLP|1906.08237|Explain permutation language modelling and two-stream attention.
electra|ELECTRA|ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators|2020|NLP|2003.10555|Compare replaced-token detection with masked-token prediction.
bart|BART|BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension|2019|NLP|1910.13461|Connect corruption functions with sequence reconstruction.
t5|T5|Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer|2019|NLP|1910.10683|Compare pretraining objectives under a common text-to-text setup.
flan|FLAN|Finetuned Language Models Are Zero-Shot Learners|2021|NLP|2109.01652|Explain instruction tuning and held-out task generalization.
rcnn|R-CNN|Rich feature hierarchies for accurate object detection and semantic segmentation|2013|CV|1311.2524|Explain proposals, region features and the cost of separate stages.
fastrcnn|Fast R-CNN|Fast R-CNN|2015|CV|1504.08083|Explain shared feature computation and RoI pooling.
fasterrcnn|Faster R-CNN|Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks|2015|CV|1506.01497|Trace region proposals, anchors, classification and box regression.
yolo|YOLO|You Only Look Once: Unified, Real-Time Object Detection|2015|CV|1506.02640|Compare single-stage prediction with proposal-based detection.
ssd|SSD|SSD: Single Shot MultiBox Detector|2015|CV|1512.02325|Explain multiscale feature maps and default boxes.
focal|Focal loss / RetinaNet|Focal Loss for Dense Object Detection|2017|CV|1708.02002|Derive how focal loss reduces the weight of easy examples.
fcn|Fully convolutional networks|Fully Convolutional Networks for Semantic Segmentation|2014|CV|1411.4038|Turn classification features into dense pixel predictions.
unet|U-Net|U-Net: Convolutional Networks for Biomedical Image Segmentation|2015|CV|1505.04597|Explain encoder-decoder skip connections and spatial detail.
maskrcnn|Mask R-CNN|Mask R-CNN|2017|CV|1703.06870|Compare semantic and instance segmentation; explain RoIAlign.
vit|Vision Transformer|An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale|2020|CV|2010.11929|Compare patch tokens and CNN inductive biases.
deit|DeiT|Training data-efficient image transformers & distillation through attention|2020|CV|2012.12877|Explain the distillation token and data-efficient training recipe.
swin|Swin Transformer|Swin Transformer: Hierarchical Vision Transformer using Shifted Windows|2021|CV|2103.14030|Explain shifted windows, hierarchy and attention complexity.
simclr|SimCLR|A Simple Framework for Contrastive Learning of Visual Representations|2020|CV|2002.05709|Derive the contrastive objective and question augmentation choices.
byol|BYOL|Bootstrap Your Own Latent: A New Approach to Self-Supervised Learning|2020|CV|2006.07733|Explain online and target networks; investigate representation collapse.
dino|DINO|Emerging Properties in Self-Supervised Vision Transformers|2021|CV|2104.14294|Explain self-distillation, centering and teacher updates.
mae|Masked autoencoders|Masked Autoencoders Are Scalable Vision Learners|2021|CV|2111.06377|Explain asymmetric encoding and high masking ratios.
dinov2|DINOv2|DINOv2: Learning Robust Visual Features without Supervision|2023|CV|2304.07193|Separate training objective, data curation and scaling effects.
convnext|ConvNeXt|A ConvNet for the 2020s|2022|CV|2201.03545|Ask which Transformer-era design choices benefit convolutional networks.
xlmr|XLM-R|Unsupervised Cross-lingual Representation Learning at Scale|2019|NLP|1911.02116|Explain cross-lingual transfer and multilingual capacity trade-offs.
mbart|mBART|Multilingual Denoising Pre-training for Neural Machine Translation|2020|NLP|2001.08210|Connect multilingual denoising to low-resource sequence generation.
byt5|ByT5|ByT5: Towards a Token-Free Future with Pre-trained Byte-to-Byte Models|2021|NLP|2105.13626|Compare byte and subword representations for noisy Indic text.
vae|Variational autoencoder|Auto-Encoding Variational Bayes|2013|CV|1312.6114|Derive the ELBO and explain the reparameterization trick.
gan|GAN|Generative Adversarial Nets|2014|CV|1406.2661|Explain the minimax game, training instability and mode collapse.
ddpm|DDPM|Denoising Diffusion Probabilistic Models|2020|CV|2006.11239|Explain forward noising and learned reverse denoising.
ldm|Latent diffusion|High-Resolution Image Synthesis with Latent Diffusion Models|2021|Multimodal|2112.10752|Explain latent-space generation and cross-attention conditioning.
nerf|NeRF|NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis|2020|CV|2003.08934|Connect continuous scene representations with volume rendering.
efficientnet|EfficientNet|EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks|2019|CV|1905.11946|Compare scaling depth, width and resolution together.
gpt3|GPT-3|Language Models are Few-Shot Learners|2020|NLP|2005.14165|Distinguish in-context learning from gradient-based adaptation.
scaling|Language-model scaling laws|Scaling Laws for Neural Language Models|2020|NLP|2001.08361|Read scaling curves and separate empirical laws from guarantees.
chinchilla|Chinchilla|Training Compute-Optimal Large Language Models|2022|NLP|2203.15556|Compare data and parameter allocation under fixed compute.
lora|LoRA|LoRA: Low-Rank Adaptation of Large Language Models|2021|NLP|2106.09685|Derive low-rank updates and distinguish training from inference costs.
instructgpt|InstructGPT|Training language models to follow instructions with human feedback|2022|NLP|2203.02155|Explain supervised tuning, preference data, reward models and RL.
dpo|DPO|Direct Preference Optimization: Your Language Model is Secretly a Reward Model|2023|NLP|2305.18290|Explain the preference objective and reference-model constraint.
rag|RAG|Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks|2020|NLP|2005.11401|Separate retriever and generator errors and parametric knowledge.
cot|Chain-of-thought prompting|Chain-of-Thought Prompting Elicits Reasoning in Large Language Models|2022|NLP|2201.11903|Distinguish improved answer accuracy from faithful reasoning traces.
lostmiddle|Lost in the Middle|Lost in the Middle: How Language Models Use Long Contexts|2023|NLP|2307.03172|Test whether context position affects evidence use.
rope|RoPE / RoFormer|RoFormer: Enhanced Transformer with Rotary Position Embedding|2021|NLP|2104.09864|Derive the relative-position effect of rotary embeddings.
alibi|ALiBi|Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation|2021|NLP|2108.12409|Compare attention-score biases with rotary position embeddings.
flashattention|FlashAttention|FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness|2022|Foundations|2205.14135|Explain tiling and memory movement without claiming linear attention FLOPs.
mqa|Multi-query attention|Fast Transformer Decoding: One Write-Head is All You Need|2019|NLP|1911.02150|Explain sharing keys and values and reducing KV-cache bandwidth.
gqa|Grouped-query attention|GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints|2023|NLP|2305.13245|Place grouped-query attention between MHA and MQA.
longformer|Longformer|Longformer: The Long-Document Transformer|2020|NLP|2004.05150|Compare sliding-window and global attention with dense attention.
switch|Switch Transformer|Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity|2021|NLP|2101.03961|Explain expert routing, active parameters and load balancing.
llama|LLaMA|LLaMA: Open and Efficient Foundation Language Models|2023|NLP|2302.13971|Inspect architectural and data choices in an open model family.
mamba|Mamba|Mamba: Linear-Time Sequence Modeling with Selective State Spaces|2023|NLP|2312.00752|Explain input-dependent state updates and compare recall with attention.
clip|CLIP|Learning Transferable Visual Models From Natural Language Supervision|2021|Multimodal|2103.00020|Derive image-text contrastive alignment and zero-shot classification.
blip2|BLIP-2|BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models|2023|Multimodal|2301.12597|Explain the Q-Former and bridging frozen vision and language models.
llava|LLaVA|Visual Instruction Tuning|2023|Multimodal|2304.08485|Separate visual projection, alignment and instruction tuning.
crnn|CRNN|An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition|2015|Document AI|1507.05717|Trace CNN features, recurrent sequence modelling and CTC decoding.
trocr|TrOCR|TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models|2021|Document AI|2109.10282|Compare autoregressive OCR with CTC and post-OCR correction.
layoutlm|LayoutLM|LayoutLM: Pre-training of Text and Layout for Document Image Understanding|2019|Document AI|1912.13318|Explain layout embeddings and document pretraining.
layoutlmv3|LayoutLMv3|LayoutLMv3: Pre-training for Document AI with Unified Text and Image Masking|2022|Document AI|2204.08387|Explain joint text-image masking and word-patch alignment.
donut|Donut|OCR-free Document Understanding Transformer|2021|Document AI|2111.15664|Compare OCR-free generation with OCR-dependent pipelines.
olmocr|olmOCR|olmOCR: Unlocking Trillions of Tokens in PDFs with Vision Language Models|2025|Document AI|2502.18443|Examine document conversion quality, reading order and evaluation coverage.
calibration|Neural-network calibration|On Calibration of Modern Neural Networks|2017|Evaluation|1706.04599|Distinguish confidence from correctness and explain temperature scaling.
checklist|CheckList|Beyond Accuracy: Behavioral Testing of NLP Models with CheckList|2020|Evaluation|2005.04118|Design minimum-functionality, invariance and directional tests.
pope|POPE / VLM hallucination|Evaluating Object Hallucination in Large Vision-Language Models|2023|Evaluation|2305.10355|Examine object-presence probes and the limits of hallucination metrics.
siglip|SigLIP|Sigmoid Loss for Language Image Pre-Training|2023|Multimodal|2303.15343|Compare pairwise sigmoid and batch-softmax alignment objectives.
sam|Segment Anything|Segment Anything|2023|CV|2304.02643|Explain promptable segmentation and the data engine.
sam2|SAM 2|SAM 2: Segment Anything in Images and Videos|2024|CV|2408.00714|Explain temporal memory and propagation in video segmentation.
r1|DeepSeek-R1|DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning|2025|NLP|2501.12948|Separate training-stage evidence, reward design and reasoning claims.
qwen3|Qwen3|Qwen3 Technical Report|2025|NLP|2505.09388|Compare dense and MoE systems and reasoning post-training.
dinov3|DINOv3|DINOv3|2025|CV|2508.10104|Explain dense-feature degradation and Gram anchoring.
qwen25vl|Qwen2.5-VL|Qwen2.5-VL Technical Report|2025|Multimodal|2502.13923|Trace dynamic resolution, visual tokens and document understanding.
qwen3vl|Qwen3-VL|Qwen3-VL Technical Report|2025|Multimodal|2511.21631|Compare multi-level visual features, positional encoding and evaluation.
dbn|Deep belief networks|A Fast Learning Algorithm for Deep Belief Nets|2006|Foundations|https://doi.org/10.1162/neco.2006.18.7.1527|Explain layerwise unsupervised pretraining and its historical motivation.
autoencoder2006|Deep autoencoders|Reducing the Dimensionality of Data with Neural Networks|2006|Foundations|https://doi.org/10.1126/science.1127647|Compare nonlinear compression, pretraining and PCA.'''
papers=[]
for row in rows.splitlines():
    id,short,title,year,track,url,goal=row.split('|')
    papers.append(dict(id=id,short=short,title=title,year=int(year),track=track,url=url if url.startswith('http') else 'https://arxiv.org/abs/'+url,goal=goal))
original='word2vec1 word2vec2 alexnet glove vgg resnet lstm seq2seq gru bahdanau luong transformer dropout batchnorm layernorm elmo bert roberta bpe bart t5 fasterrcnn yolo detr fcn unet maskrcnn vit deit swin simclr byol dino xlmr mbart byt5 vae gan ddpm gpt3 scaling chinchilla lora instructgpt dpo rag cot lostmiddle clip blip2 llava mae ldm sam crnn trocr layoutlmv3 rope flashattention mamba calibration checklist pope dinov2 siglip sam2 r1 qwen3 dinov3 qwen25vl qwen3vl olmocr'.split()
claude='backprop lstm bengio dbn autoencoder2006 dropout word2vec1 glove seq2seq bahdanau transformer elmo gpt1 bert gpt2 xlnet roberta bart t5 electra gpt3 longformer switch rag scaling flan lora cot instructgpt chinchilla llama dpo mamba rope alibi flashattention gqa bpe lenet alexnet vgg inception batchnorm resnet rcnn fastrcnn fasterrcnn yolo ssd unet maskrcnn vae gan ddpm vit detr swin simclr mae dinov2 clip ldm sam llava focal efficientnet convnext nerf crnn trocr layoutlm donut'.split()
# DETR bridges detection and attention in the recent-systems week.
papers.insert(95,dict(id='detr',short='DETR',title='End-to-End Object Detection with Transformers',year=2020,track='CV',url='https://arxiv.org/abs/2005.12872',goal='Explain set prediction, object queries and bipartite matching.'))
# Move DETR beside ViT; move DeiT to the architectural comparison week.
order=[p['id'] for p in papers]
order.remove('detr'); order.insert(order.index('vit')+1,'detr')
order.remove('deit'); order.insert(order.index('qwen25vl'),'deit')
lookup={p['id']:p for p in papers};papers=[lookup[i] for i in order]
assert len(papers)==98 and len(set(order))==98
assert set(order)==set(original+claude+['mqa'])
light={'gpt2','xlnet','rcnn','fastrcnn','ssd','alibi','dbn','autoencoder2006','inception','vgg','roberta','deit','convnext','efficientnet','llama','qwen3','qwen25vl','qwen3vl','olmocr','dinov3'}
for i,p in enumerate(papers):
    p.update(week=i//3+1,slot=i%3,depth='Compare' if p['id'] in light else 'Deep read',origin='Both plans' if p['id'] in original and p['id'] in claude else 'Added separately' if p['id']=='mqa' else 'Original plan' if p['id'] in original else 'Claude plan')
themes=['Words & pixels','Learning representations','Memory & depth','Sequences & alignment','Attention & residual learning','Training neural networks','Tokens & Transformers','The pretraining era','Alternative language objectives','Text-to-text & instructions','The R-CNN family','Single-stage detection','Dense prediction','Transformers for vision','Self-supervised vision','Reconstruction & modern backbones','Multilingual & byte-level NLP','Generative foundations','Generation, geometry & scaling','Scaling language models','Adaptation & alignment','Retrieval & reasoning','Positions & efficient attention','Efficient decoding & long context','Sparse & alternative architectures','Vision meets language','Reading documents','Document understanding','Reliability & evaluation','Visual foundation models','Recent language & vision','Modern systems & comparisons','Historical perspective & synthesis']
Path('lib/papers.json').write_text(json.dumps(papers,ensure_ascii=False,indent=2))
Path('lib/themes.json').write_text(json.dumps(themes,indent=2))
print('Catalog:',len(papers),'papers;',len(themes),'weeks')
for w in range(1,34):print(w,', '.join(p['short'] for p in papers if p['week']==w))
