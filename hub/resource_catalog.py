"""Curated alternatives, checked against instructor/publisher entry pages 2026-09-22.
Shared indexes intentionally have topic-specific section guidance. No scraped descriptions.
"""
def resource(title, url, use, kind='Reading', scope='Course index'):
    return dict(title=title, url=url, use=use, type=kind, scope=scope)

STAT='https://statquest.org/video_index.html'
D2L='https://d2l.ai/'
KAR='https://karpathy.ai/zero-to-hero.html'
MIT='https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/'
CMU='https://15445.courses.cs.cmu.edu/fall2024/'
KR='https://gaia.cs.umass.edu/kurose_ross/'
FSDL='https://fullstackdeeplearning.com/'

def augment(topics):
    for t in topics:
        for r in t['resources']:
            r['type']='Practice' if 'tutorial' in r['url'] else 'Reading'
            r['scope']='Paper' if 'arxiv.org' in r['url'] else 'Reference / index'
            if r['url'].startswith('https://d2l.ai/chapter_'): r['scope']='Direct chapter'
        id=t['id']; rs=t['resources']
        def add(title,url,use,kind='Reading',scope='Course index'):
            rs.append(resource(title,url,use,kind,scope))
        if t['subject']=='ML':
            focus={
                'linear-algebra':'Matrix algebra, tensors and matrix multiplication; track shapes by hand.',
                'probability':'Conditional probability, Bayes theorem, expectation and distributions.',
                'regression':'Linear regression, logistic regression and maximum likelihood.',
                'generalization':'Bias and variance, cross-validation and regularization.',
                'svm':'Support Vector Machines: main idea, polynomial kernel and RBF kernel.',
                'ensembles':'Decision trees, random forests, gradient boosting and XGBoost.',
                'pca-clustering':'PCA step by step, k-means and hierarchical clustering.'}[id]
            add('StatQuest · visual explanations',STAT,focus,'Video','Video index')
            if id=='linear-algebra':
                add('3Blue1Brown · Essence of Linear Algebra','https://www.3blue1brown.com/?topic=linear-algebra','Start with span, linear transformations and matrix multiplication.','Video','Video series index')
                add('D2L · mathematical foundations',D2L,'Preliminaries → linear algebra exercises; compare dot products, matrix products and broadcasting.','Practice','Textbook / exercise index')
            else:
                add('scikit-learn · runnable examples','https://scikit-learn.org/stable/auto_examples/index.html',{'probability':'Probability calibration: inspect reliability curves and predicted probabilities.','regression':'Linear Models: compare linear and logistic regression examples.','generalization':'Model Selection: learning curves and cross-validation examples.','svm':'Support Vector Machines: compare kernels and decision boundaries.','ensembles':'Ensemble Methods: compare forests and boosting on one dataset.','pca-clustering':'Decomposition and Clustering: PCA projection and cluster comparison examples.'}[id],'Practice','Example index')
                if id in ['svm','ensembles','pca-clustering']:
                    add('Introduction to Statistical Learning','https://www.statlearning.com/',{'svm':'Support Vector Machines chapter and Python lab: margins, kernels and support vectors.','ensembles':'Tree-Based Methods chapter and Python lab: bagging, random forests and boosting.','pca-clustering':'Unsupervised Learning chapter and Python lab: PCA and clustering.'}[id],'Reading','Free textbook / lab index')
                else: add('Google · Machine Learning Crash Course','https://developers.google.com/machine-learning/crash-course',{'probability':'Classification: interpret predicted probabilities and thresholds.','regression':'Linear Regression and Logistic Regression modules; work the embedded exercises.','generalization':'Overfitting and Generalization: training/validation splits and model capacity.'}[id],'Practice','Course / exercise index')
        elif t['subject']=='DL':
            focus={'backprop':'Build micrograd: scalar computational graphs and reverse-mode autodiff.','optimization':'Backpropagation and gradient descent; pause to calculate one update.','regularization':'Neural networks: training versus evaluation, loss and learning curves.','convolution':'Convolutional Neural Networks: filters, stride and pooling.','residual':'CNN lecture: architecture progression and residual networks.','sequence':'Recurrent Neural Networks and Long Short-Term Memory.','training-loop':'Introduction to PyTorch: tensors, gradients, model, loss and optimizer.'}[id]
            url=KAR if id in ['backprop','regularization'] else FSDL+'course/2022/' if id=='residual' else STAT
            add('Karpathy · Zero to Hero' if url==KAR else 'FSDL · CNN lecture archive' if id=='residual' else 'StatQuest · neural networks',url,focus,'Video','Video course index')
            reading={
                'backprop':('CS231n · backpropagation','https://cs231n.github.io/optimization-2/','Trace the computational circuits and chain-rule examples.'),
                'optimization':('CS231n · learning and evaluation','https://cs231n.github.io/neural-networks-3/','Momentum, adaptive updates, gradient checks and learning-rate diagnostics.'),
                'regularization':('CS231n · data and loss','https://cs231n.github.io/neural-networks-2/','Weight initialization, batch normalization, dropout and regularization.'),
                'convolution':('CS231n · convolutional networks','https://cs231n.github.io/convolutional-networks/','Calculate output sizes and parameter counts before checking the examples.'),
                'residual':('D2L · ResNet and ResNeXt','https://d2l.ai/chapter_convolutional-modern/resnet.html','Trace identity and projection shortcuts and inspect their tensor shapes.'),
                'sequence':('D2L · recurrent neural networks','https://d2l.ai/chapter_recurrent-neural-networks/index.html','Hidden state, language modelling and backpropagation through time.'),
                'training-loop':('CS231n · learning diagnostics','https://cs231n.github.io/neural-networks-3/','Gradient checks, small-batch overfitting and loss-curve diagnosis.')}
            title,url,use=reading[id];add(title,url,use,'Reading','Chapter / notes')
            if id=='sequence':add('PyTorch · sequence models','https://docs.pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html','Run the LSTM example and annotate sequence, batch and feature axes.','Practice','Direct tutorial')
            elif id in ['convolution','residual']:add('Torchvision · model implementations','https://docs.pytorch.org/vision/stable/models.html','Open a CNN/ResNet model and its source; inspect blocks and weight-specific preprocessing.','Code','Model index')
            else:add('CS231n · assignments','https://cs231n.github.io/','Select backprop, fully connected networks, normalization or dropout exercises. Do a small component, not the whole course.','Practice','Assignment index')
        elif t['subject']=='NLP':
            focus={'embeddings':'makemore: inspect embedding lookup and how gradients update a row.','tokenization':'Build the GPT tokenizer: byte-level encoding, merges and special tokens.','attention':'Build GPT: trace query/key/value shapes, masking and weighted sums.','positions':'Build GPT: first understand learned positions; contrast with the RoPE and ALiBi papers below.','objectives':'Build GPT: trace next-token targets and autoregressive cross-entropy.','decoding':'Build GPT: inspect the generation loop and categorical sampling.','adaptation':'RLHF explanation: preference feedback; compare with parameter-efficient fine-tuning.'}[id]
            add('StatQuest · RLHF' if id=='adaptation' else 'Karpathy · Zero to Hero',STAT if id=='adaptation' else KAR,focus,'Video','Video index')
            url='https://d2l.ai/chapter_natural-language-processing-pretraining/index.html' if id in ['embeddings','objectives','adaptation'] else 'https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html'
            add('D2L · NLP pretraining' if 'pretraining' in url else 'D2L · attention and transformers',url,{'embeddings':'Word2Vec, negative sampling, GloVe and subword embeddings.','tokenization':'Transformer input representations: connect token IDs to embeddings; use Karpathy for tokenizer mechanics.','attention':'Work the attention scoring and multi-head attention code.','positions':'Self-attention and positional encoding: calculate a sinusoidal example.','objectives':'Compare Word2Vec and BERT training objectives.','decoding':'Transformer encoder-decoder example: contrast training with autoregressive prediction.','adaptation':'Fine-tune BERT for sequence classification; contrast with LoRA.'}[id],'Reading','Chapter index')
            if id=='adaptation':add('Hugging Face · PEFT','https://huggingface.co/docs/peft/index','Choose LoRA; inspect adapter parameters and freezing of the base model.','Code','Documentation index')
            elif id=='decoding':add('Transformers · generation strategies','https://huggingface.co/docs/transformers/en/generation_strategies','Compare greedy, beam and sampling configurations on the same prompt.','Practice','Direct guide')
            else:add('Stanford CS336 · language modelling from scratch','https://cs336.stanford.edu/spring2025/',{'embeddings':'Lecture 1 and Assignment 1: embeddings inside the language model.','tokenization':'Lecture 1 and Assignment 1: implement a tokenizer and examine segmentation.','attention':'Architecture lecture and Assignment 1: implement a transformer block.','positions':'Architecture lecture: rotary position embeddings; follow the associated implementation assignment.','objectives':'Architecture and data lectures: inspect next-token training and dataset construction.'}[id],'Practice','Lecture / assignment index')
        elif t['subject']=='CV':
            classical=id in ['image-processing','fourier','sift','geometry']
            focus={'image-processing':'Image Processing I: linear shift-invariant systems and convolution.','fourier':'Image Processing II: Fourier transform, convolution theorem and frequency filtering.','sift':'SIFT Detector and SIFT Descriptor sections: scale-space, orientation and histograms.','geometry':'Image Stitching: computing a homography and RANSAC; Image Formation for camera models.','detection':'FSDL 2021 Computer Vision lecture: object detection and recognition tasks.','segmentation':'Image Segmentation: clustering and graph-based methods; use the textbook for modern neural segmentation.','vit-ssl':'Foundation Models: CLIP and representation learning; connect to the ViT and SSL exercises.'}[id]
            video='https://fpcv.cs.columbia.edu/' if classical or id=='segmentation' else FSDL+('course/2022/lecture-7-foundation-models/' if id=='vit-ssl' else 'course/2022/')
            add('Nayar · First Principles of Computer Vision' if 'columbia' in video else 'FSDL · vision foundations',video,focus,'Video','Lecture page' if id=='vit-ssl' else 'Video index')
            if classical:
                add('OpenCV · Python tutorials','https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html',{'image-processing':'Image Processing: smoothing, filtering and thresholding tutorials.','fourier':'Image Processing → Fourier Transform: inspect magnitude and filtered reconstructions.','sift':'Feature Detection and Description → SIFT and Feature Matching.','geometry':'Camera Calibration and 3D Reconstruction; Feature Matching + Homography.'}[id],'Practice','Tutorial index')
                add('Nayar · written monographs','https://fpcv.cs.columbia.edu/Monographs',{'image-processing':'Image Processing I: kernels and convolution derivations.','fourier':'Image Processing II: Fourier analysis and filtering derivations.','sift':'SIFT Detector: scale-space construction and extrema.','geometry':'Image Formation, Image Stitching and Camera Calibration: coordinate transformations and geometry.'}[id],'Reading','Monograph index')
            else:
                add('Torchvision · vision model implementations','https://docs.pytorch.org/vision/stable/models.html',{'detection':'Object Detection: inspect Faster R-CNN and RetinaNet inputs, outputs and preprocessing.','segmentation':'Semantic and instance segmentation: inspect output masks and class dimensions.','vit-ssl':'VisionTransformer: inspect patch projection and positional interpolation in the source.'}[id],'Code','Model index')
                add('D2L · vision models',D2L,{'detection':'Computer Vision → bounding boxes, anchors, multiscale detection and SSD.','segmentation':'Computer Vision → semantic segmentation, transposed convolution and fully convolutional networks.','vit-ssl':'Attention Mechanisms and Transformers → Vision Transformer; then compare with CS231n SSL assignments.'}[id],'Reading','Textbook index')
        elif t['subject']=='DSA':
            lesson={'complexity':'lecture-1-algorithms-and-computation','arrays-hashing':'lecture-4-hashing','stacks-queues':'lecture-2-data-structures-and-dynamic-arrays','sorting-search':None,'trees-heaps':'lecture-6-binary-trees-part-1','graphs':'lecture-9-breadth-first-search','dp-greedy':'lecture-15-dynamic-programming-part-1-srtbot-fib-dags-bowling'}[id]
            focus={'complexity':'Lecture 1: specify the problem, algorithm and cost model.','arrays-hashing':'Lecture 4: hashing assumptions, collisions and expected lookup cost.','stacks-queues':'Lecture 2: sequence interfaces and representation costs; use linked structures to reason about stacks and queues.','sorting-search':'Lectures 3 and 5: sorting and linear sorting; compare assumptions and invariants.','trees-heaps':'Lecture 6: binary trees; continue with Lecture 8 for heaps.','graphs':'Lecture 9: BFS; follow with DFS and shortest-path lectures for weighted graphs.','dp-greedy':'Lecture 15: DP state, recurrence, topological order and reconstruction; use Erickson for greedy proofs.'}[id]
            add('MIT 6.006 · selected lecture',MIT+('resources/'+lesson+'/' if lesson else 'video_galleries/lecture-videos/'),focus,'Video','Direct lesson' if lesson else 'Video index')
            add('MIT 6.006 · lecture notes',MIT+'pages/lecture-notes/',focus+' Read the corresponding notes after attempting the derivation.','Reading','Notes index')
            add('MIT 6.006 · practice problems',MIT+'pages/practice-problems/','Select the problem set matching '+t['section'].lower()+'. Attempt first, then inspect solutions.','Practice','Problem index')
        elif t['subject']=='DBMS':
            lecture={'relational':('01-relationalmodel','01 Relational Model & Algebra'),'sql':('02-modernsql','02 Modern SQL'),'indexes':('08-indexes1','08 Indexes & Filters I'),'query-planning':('15-optimization','15 Query Planning & Optimization'),'transactions':('16-concurrencycontrol','16 Concurrency Control Theory'),'recovery':('21-recovery','21 Database Crash Recovery')}
            if id=='normalization':
                add('NPTEL · Database Design, IIT Madras','https://nptel.ac.in/courses/106106093','Find functional dependencies, normalization and decomposition in the lecture list.','Video','Video course index')
                add('NPTEL · DBMS, IIT Kharagpur','https://nptel.ac.in/courses/106105175','Alternative instructor course: focus on relational design, functional dependencies and normal forms.','Video','Video course index')
                add('Database System Concepts · companion material','https://www.db-book.com/','Choose relational database design exercises/solutions from the student companion material; compute closures before checking.','Practice','Book companion index')
            else:
                slug,label=lecture[id]
                add('CMU 15-445 · lecture videos',CMU+'schedule.html','Fall 2024 lecture '+label+'. Use the Video link on that row.','Video','Video / syllabus index')
                add('CMU · '+label,CMU+'notes/'+slug+'.pdf','Read the lecture handout; work one example using your own tiny tables or transaction history.','Reading','Direct PDF notes')
                add('Berkeley CS186 · exam practice','https://cs186berkeley.net/resources/','Choose database exam questions on '+t['title'].lower()+'. Use solutions only after an independent attempt.','Practice','Exam archive')
        elif t['subject']=='CN':
            chapter={'layers':1,'application':2,'transport':3,'congestion':3,'subnetting':4,'routing':5,'link-security':6}[id]
            # Replace the old general video index instead of counting two equivalent indexes.
            rs[0]=resource('Kurose–Ross · chapter '+str(chapter)+' videos',KR+'videos/'+str(chapter)+'/',{'layers':'Introduction: delay, throughput, layers and encapsulation.','application':'Application layer: HTTP and DNS.','transport':'Transport: reliable transfer, UDP and TCP.','congestion':'Transport: congestion control, TCP window behaviour and fairness.','subnetting':'Network data plane: IP addresses, subnetting and longest-prefix matching.','routing':'Network control plane: routing algorithms, OSPF and BGP.','link-security':'Link layer: Ethernet, ARP and switching. Use the security slides separately for TLS.'}[id],'Video','Chapter video index')
            add('Kurose–Ross · Wireshark labs',KR+'wireshark.php',{'layers':'Introductory lab: annotate encapsulation and packet timings.','application':'HTTP and DNS labs: inspect requests, replies and caching.','transport':'TCP lab: sequence numbers, ACKs and retransmissions.','congestion':'TCP lab: inspect RTT and throughput; distinguish receiver and congestion limits.','subnetting':'IP lab: connect observed header fields to subnet calculations.','routing':'IP and ICMP labs: inspect TTL and traceroute; pair with routing theory.','link-security':'Ethernet/ARP and TLS labs: distinguish local delivery from encrypted transport.'}[id],'Practice','Lab index')
            add('Kurose–Ross · chapter slides',KR+'ppt.php','Choose chapter '+str(chapter)+(' and chapter 8 for security' if id=='link-security' else '')+'. Reconstruct one diagram before consulting the slide.','Reading','Slide index')
            if id=='subnetting':add('Python · ipaddress','https://docs.python.org/3/library/ipaddress.html','Check network/broadcast boundaries, subnet subdivision and /31 hosts against your hand calculation.','Code','Direct API reference')
            else:add('Kurose–Ross · knowledge checks',KR+'knowledgechecks/','Choose chapter '+str(chapter)+' questions for closed-book practice.'+(' Security chapter questions are not supplied here; use your topic drills for that part.' if id=='link-security' else ''),'Practice','Question index')
        else:
            data={
             'vlm-inputs':[
              ('FSDL · Foundation Models',FSDL+'course/2022/lecture-7-foundation-models/','CLIP and multimodal foundations; this 2022 lecture does not explain Qwen-specific processing.','Video','Lecture page'),
              ('Torchvision · preprocessing and model code','https://docs.pytorch.org/vision/stable/models.html','Compare CNN/ViT weight transforms with the Qwen processor. Separate model constraints from preprocessing defaults.','Code','Model index'),
              ('D2L · attention and transformers','https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html','Vision Transformer chapter: patch counts, embedding width and positional encodings.','Reading','Chapter index')],
             'rag':[
              ('FSDL · Augmented Language Models',FSDL+'llm-bootcamp/spring-2023/augmented-language-models/','Retrieval and tools: trace what information reaches the generator.','Video','Lecture page'),
              ('FSDL · askFSDL walkthrough',FSDL+'llm-bootcamp/spring-2023/askfsdl-walkthrough/','Inspect the retrieval application design; treat 2023 APIs as historical examples.','Practice','Project walkthrough'),
              ('Stanford CS336 · evaluation and data','https://cs336.stanford.edu/spring2025/','Use evaluation/data lectures to design contamination checks and generation evaluation; add retrieval recall separately.','Reading','Lecture / assignment index')],
             'agents':[
              ('FSDL · Harrison Chase on agents',FSDL+'llm-bootcamp/spring-2023/chase-agents/','Historical 2023 introduction: tools and agent execution. Compare with current course APIs.','Video','Lecture page'),
              ('FSDL · augmented language models',FSDL+'llm-bootcamp/spring-2023/augmented-language-models/','Contrast fixed retrieval workflows with tool-using model loops.','Video','Lecture page'),
              ('FSDL · askFSDL walkthrough',FSDL+'llm-bootcamp/spring-2023/askfsdl-walkthrough/','Study a bounded retrieval application before adding autonomous planning.','Practice','Project walkthrough')],
             'llm-systems':[
              ('Stanford CS336 · systems lectures','https://cs336.stanford.edu/spring2025/','Use the public videos: architecture, GPUs, kernels and inference. Follow the associated assignments.','Video','Lecture / video index'),
              ('Transformers · cache strategies','https://huggingface.co/docs/transformers/en/kv_cache','Compare dynamic, static, offloaded and quantized caches; estimate memory before running.','Code','Direct guide'),
              ('FSDL · Foundation Models',FSDL+'course/2022/lecture-7-foundation-models/','Architectural context for large models; use CS336 for newer systems details.','Video','Lecture page')],
             'generative':[
              ('FSDL · Foundation Models',FSDL+'course/2022/lecture-7-foundation-models/','Stable Diffusion and generative model context; connect to the DDPM equations.','Video','Lecture page'),
              ('Hugging Face · Diffusers','https://huggingface.co/docs/diffusers/index','Inspect a scheduler and pipeline; distinguish training noise prediction from sampling.','Code','Documentation index'),
              ('CS231n · diffusion assignments','https://cs231n.github.io/','Select the diffusion-model assignment; first implement a small forward-noising calculation.','Practice','Assignment index')],
             'ocr-research':[
              ('FSDL · Paragraph Recognition',FSDL+'spring2021/lab-7/','Trace detection/recognition and paragraph-level evaluation in the lab video.','Video','Lab / video page'),
              ('Transformers · TrOCR','https://huggingface.co/docs/transformers/en/model_doc/trocr','Run a baseline and inspect image processor and decoder outputs; pretrained coverage is not a guarantee for Indic scripts.','Code','Direct model guide'),
              ('PyTorch · sequence modelling','https://docs.pytorch.org/tutorials/beginner/nlp/sequence_models_tutorial.html','Build a small sequence baseline to contrast with transformer recognition/correction.','Practice','Direct tutorial')],
             'research-defence':[
              ('FSDL · Research Directions',FSDL+'spring2021/lecture-12/','Observe how problems, limitations and research opportunities are framed; examples are from 2021.','Video','Lecture page'),
              ('FSDL · experiment management',FSDL+'course/2022/','Lab 4: experiment management. Record hypotheses, metrics, seeds and decisions.','Practice','Lab index'),
              ('CS231n · taking a project to publication','https://cs231n.github.io/choose-project/','Use the project advice to sharpen your question, baselines, experimental evidence and contribution narrative.','Reading','Direct article')]
            }
            for row in data[id]:add(*row)
        assert len({r['url'] for r in rs})==len(rs),(id,'duplicate URL')
        assert len(rs)>=5,(id,len(rs))
        assert any(r['type']=='Video' for r in rs),id
    return topics
