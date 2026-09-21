import json
from pathlib import Path
# Original learning tasks. Links are free reference material, not copied course content.
modules=[
('Mathematical foundations','https://d2l.ai/chapter_preliminaries/index.html',[
('Diagnostic and tensor shapes','Explain a neuron, Bayes rule, a matrix product and your thesis aloud; score each 0–3.','Create tensors; distinguish reshape, transpose and broadcasting.',0),
('Linear algebra for representations','Compute dot products and projections; explain rank, eigenvectors and SVD geometrically.','Check matrix multiplication shapes and compare a low-rank reconstruction.',0),
('Calculus and computation graphs','Derive a scalar chain rule, a gradient and the gradient of a squared-error linear predictor.','Compare an analytic gradient with autograd and finite differences.',1),
('Probability and statistical evidence','Work through conditional probability, expectation, likelihood and sampling uncertainty.','Simulate class imbalance; calculate precision, recall and a bootstrap interval.',2)]),
('Core machine learning','https://www.statlearning.com/',[
('Linear and logistic regression','Derive squared-error and logistic gradients; explain regularization and decision thresholds.','Fit a tiny regression model with an explicit training loop.',1),
('Generalization and evaluation','Distinguish bias/variance, leakage, class imbalance and calibration; construct a safe split.','Implement a confusion matrix and test threshold changes.',4),
('SVM and tree ensembles','Explain maximum margin, slack and kernel intuition; contrast bagging with boosting.','Plot a toy boundary; explain why scaling affects distance-based methods.',5),
('PCA, clustering and naive Bayes','Work a PCA projection and one k-means update; explain EM responsibilities and independence assumptions.','Compare projected data with the original covariance matrix.',0)]),
('Neural network mechanics','https://d2l.ai/chapter_multilayer-perceptrons/index.html',[
('MLP forward and backward passes','Trace a two-layer network; derive one weight gradient and state every tensor dimension.','Build a tiny MLP; compare manual and automatic gradients.',1),
('Optimization and initialization','Compare SGD, momentum and AdamW; explain learning-rate schedules and variance-preserving initialization.','Record gradient norms under two initialization scales.',9),
('Normalization and regularization','Compute normalization axes; compare BatchNorm and LayerNorm at train and evaluation time.','Inspect running statistics and dropout behavior in train()/eval().',5),
('CNN mechanics and receptive fields','Derive convolution output sizes, parameters and receptive fields; distinguish correlation and convolution.','Implement a tiny convolution using loops and compare with Conv2d.',6)]),
('Sequence models and representations','https://d2l.ai/chapter_recurrent-modern/index.html',[
('Word representations and tokenization','Compare one-hot, TF-IDF, CBOW, skip-gram, negative sampling and subword representations.','Prepare CBOW context-target pairs and inspect Indic tokenizer outputs.',10),
('RNN, LSTM and GRU internals','Trace recurrent state and gates; explain how gradient paths differ without claiming vanishing gradients disappear.','Trace a two-step recurrent cell and detach hidden state deliberately.',9),
('Sequence-to-sequence and attention','Explain teacher forcing, encoder-decoder state transfer, alignment and exposure bias.','Implement a small attention-weighted context vector.',12),
('Transformer from input to logits','Draw embeddings, attention, residuals, normalization and FFN; distinguish all masks.','Implement scaled dot-product attention with a causal mask.',11)]),
('NLP and language modelling','https://web.stanford.edu/class/cs224n/',[
('Language-model objectives','Compare autoregressive, masked and denoising objectives using GPT, BERT and T5/mBART.','Build labels and ignored positions for a toy training batch.',4),
('Position and context','Explain sinusoidal positions, RoPE and relative positions; distinguish sequence length from embedding width.','Apply a two-dimensional rotation and check dot-product behavior.',13),
('Decoding and sequence evaluation','Trace greedy and beam decoding; distinguish temperature, top-k and top-p; compute CER/WER.','Implement edit-distance dynamic programming and a tiny beam search.',18),
('Transfer, multilinguality and correction','Explain tokenization costs, fine-tuning, language tags and over-correction in your own systems.','Compare token counts and correction errors across two scripts.',10)]),
('Vision foundations and architectures','https://szeliski.org/Book/',[
('Image processing and local features','Trace filtering, edges and morphology; explain SIFT stages and the source of invariances.','Apply filters to a toy image and inspect boundary handling.',8),
('Geometry and estimation','Compare translation, rigid, similarity, affine and projective transforms; state degrees of freedom and RANSAC assumptions.','Transform points in homogeneous coordinates and check preserved properties.',0),
('ResNet, detection and segmentation','Trace residual stages and pooling; compare two-stage detection, YOLO, U-Net and instance segmentation.','Record shapes at each ResNet stage for two input resolutions.',7),
('ViT and self-supervised vision','Trace patch embedding and position; compare ViT, Swin, contrastive learning and masked reconstruction.','Extract patches and count tokens for multiple aspect ratios.',14)]),
('Modern language-model systems','https://huggingface.co/learn/llm-course/chapter1/1',[
('Decoder internals and efficient attention','Trace normalization, RoPE, FFN and residual paths; compare MHA/MQA/GQA and exact attention implementations.','Calculate attention and KV-cache sizes from an explicit config.',22),
('Adaptation and quantization','Explain LoRA rank, QLoRA purpose and frozen versus trainable parameters; separate numerical precision from model size.','Implement a low-rank weight update and count trainable parameters.',17),
('Training and post-training','Compare pretraining, SFT, preference learning and reasoning-oriented training; identify assumptions in reported evaluations.','Inspect prompt/response loss masks and make a leakage checklist.',4),
('Retrieval and reliable generation','Trace retrieval, reranking and context construction; evaluate retrieval separately from generation.','Build a tiny local lexical retriever and inspect its failures.',20)]),
('Vision-language internals','https://huggingface.co/docs/transformers/en/model_doc/qwen2_vl',[
('CLIP and cross-modal alignment','Explain contrastive targets, normalization and similarity; distinguish retrieval alignment from text generation.','Construct a small image-text similarity matrix and both loss directions.',12),
('Projectors, resamplers and fusion','Compare a projected visual-token sequence, query-based resampling and cross-attention; inspect a selected checkpoint.','Trace visual width to language width and count connector parameters.',5),
('Variable resolution and spatial positions','For a pinned model version, trace resize policy, patch grid, merging, positions, batching and visual-token count.','Log processor output shapes for three aspect ratios; distinguish padding stages.',15),
('Document and video inputs','Compare page crops, layout, temporal sampling and token budgets; track information lost before generation.','Measure character height after resizing and record token budget per image.',16)]),
('Generative modelling and evaluation','https://d2l.ai/chapter_generative-adversarial-networks/index.html',[
('VAE and GAN mechanisms','Explain latent variables, reconstruction/KL trade-offs and adversarial objectives; identify what is optimized.','Calculate a toy Gaussian KL term and inspect reconstruction error.',4),
('Diffusion fundamentals','Trace forward corruption and reverse prediction; distinguish training loss from sampling procedure.','Corrupt a tiny tensor at several noise levels using a fixed seed.',23),
('Statistical and robustness evaluation','Separate paired comparisons, confidence intervals, subgroup errors and distribution shift.','Bootstrap paired per-example differences; inspect domain-specific failures.',23),
('Controlled architecture experiment','Choose one preprocessing or token-budget hypothesis; state its control, confound and falsification condition.','Run a small matched-budget comparison and save an experiment table.',15)]),
('Agents and workflows','https://huggingface.co/learn/agents-course/unit0/introduction',[
('Explicit tool-use loop','Distinguish a fixed workflow from model-directed control; trace messages, tools, state and stopping conditions.','Implement a deterministic mock model-tool-observation loop without paid APIs.',21),
('Tools, state and failure handling','Define schemas, validation, timeouts, retries and permissions; distinguish memory from conversation history.','Inject a malformed tool result and test bounded recovery.',21),
('Frameworks after mechanisms','Map one current framework to the loop you implemented; inspect its official docs and pin its version.','Recreate the same small workflow in one framework; compare traces.',20),
('Evaluate an agentic research idea','Compare a fixed correction workflow with an adaptive one; measure correctness, cost and failure cascades.','Use saved/mock outputs first; log tool success and task success separately.',21)]),
('Research depth and architecture defence','https://www.jmlr.org/',[
('Defend your first contribution','Explain the problem, novelty, strongest baseline, ablations, limitations and your personal role.','Reproduce one reported metric from a small saved example.',18),
('Defend complementary views','Explain when a second view adds information, when it conflicts and how to test dependence on translation quality.','Create controlled corruptions and compare single-view versus dual-view behavior.',23),
('Find and challenge a research gap','Separate established facts, observations and hypotheses; search primary literature before claiming novelty.','Specify a minimal falsifying experiment with a matched-compute baseline.',16),
('Build a reproducibility record','Document splits, normalization, seeds, model revisions, prompt templates and evaluation choices.','Write a small evaluation entry point and a configuration record.',18)]),
('Teaching and application readiness','https://d2l.ai/',[
('Teach backpropagation','Deliver a 10-minute undergraduate explanation using one scalar example before matrix notation.','Create a tiny gradient demonstration with assertions.',1),
('Teach attention or convolution','Deliver a second teaching demo; anticipate misconceptions and include one worked example.','Build a two-query attention or convolution visualization from small arrays.',11),
('Research talk and future programme','Prepare short and full versions; state two feasible future projects and the first experiment for each.','Prepare one clean figure/table from your research pipeline.',23),
('Role-specific application package','Refine CV, research and teaching statements; map your skills to one real advertisement.','Check that links, repository instructions and examples are reproducible.',5)]),
('Mock interviews and repair','https://web.stanford.edu/class/cs224n/',[
('Technical mock and diagnostic repair','Answer a mixed set aloud; score correctness, reasoning, clarity and recovery from uncertainty.','Reimplement the concept you could not explain.',11),
('Research defence mock','Answer challenges about novelty, data validity, baselines, failure modes and practical value.','Verify the key numerical claim and a failure case.',18),
('Architecture reconstruction challenge','Draw one selected model cold from raw input to prediction, then inspect code to locate errors.','Use hooks or intermediate outputs to verify the disputed shapes.',15),
('Targeted foundation repair','Choose the lowest-confidence foundational concept from your error log; solve a new example.','Write a unit check that fails under your earlier misconception.',1)]),
('Consolidation and long-term practice','https://docs.pytorch.org/tutorials/beginner/basics/intro.html',[
('Mixed recall without notes','Explain connections across representations, optimization, attention and evaluation; revisit unresolved gaps.','Rebuild a short training loop without copying a tutorial.',5),
('Full interview rehearsal','Combine introduction, teaching, technical questions and research vision; record timing and errors.','Prepare a runnable miniature demo relevant to your claimed expertise.',12),
('Research synthesis and next experiment','Select one supported research question; define baseline, budget, outcome and stopping condition.','Create the smallest reproducible experiment scaffold.',23),
('January review and continuation','Review evidence of mastery, remaining weaknesses and your realistic workload after joining a role.','Clean notebooks and create a monthly maintenance checklist.',0)])]
core=[
('Asymptotic analysis and recurrences','Derive merge-sort complexity; distinguish worst-case, expected and amortized bounds.','Implement and count operations for two input sizes.'),
('Sorting, searching and hashing','Trace quicksort and binary search invariants; compare collision strategies.','Write binary search and test empty/boundary cases.'),
('Lists, stacks, queues and trees','Trace pointer changes and traversals; explain BST invariants and heap operations.','Implement traversal and test a malformed edge case.'),
('Heaps and amortized analysis','Explain O(n) build-heap and amortized dynamic-array growth.','Compare repeated insertion with bottom-up heap construction.'),
('BFS, DFS and topological order','Trace queue/stack state; distinguish directed and undirected cycle detection.','Implement BFS distances and topological sorting.'),
('Shortest paths and minimum spanning trees','State Dijkstra assumptions; compare Bellman-Ford, Prim and Kruskal.','Construct a negative-edge counterexample to naive Dijkstra.'),
('Dynamic programming','Derive state, recurrence, initialization and reconstruction for LCS/edit distance.','Implement edit distance with a table and recover an alignment.'),
('Greedy proofs and complexity classes','Explain exchange arguments, P/NP and reduction direction using a concrete example.','Contrast a greedy rule with an exhaustive solution on tiny inputs.'),
('Relational model and algebra','Map ER entities and keys; trace selection, projection, join and division.','Express a query in relational algebra and SQL.'),
('SQL and joins','Explain nulls, grouping, outer joins and correlated subqueries.','Run queries on a tiny database with missing values.'),
('Functional dependencies and normal forms','Compute closure; distinguish 3NF/BCNF, losslessness and dependency preservation.','Work a decomposition and show a spurious-tuple counterexample.'),
('Indexes and query execution','Explain B+ trees, selectivity and clustered indexes; trace a join strategy.','Inspect a simple query plan before and after an index.'),
('Transactions and concurrency','Trace conflict serializability, locking, isolation levels and deadlocks.','Draw a precedence graph for two schedules.'),
('Recovery and DBMS consolidation','Explain write-ahead logging and checkpoints; solve mixed normalization/transaction questions.','Trace a crash and identify undo/redo needs under stated assumptions.'),
('Network layers and link protocols','Trace encapsulation; explain framing, CRC and medium access.','Work one small XOR-based CRC example.'),
('IP addressing and subnetting','Calculate masks, network boundaries and host ranges; explain CIDR and routing prefixes.','Solve subnet examples and verify binary representations.'),
('Routing, ARP, DHCP and NAT','Trace a packet between subnets; compare distance-vector and link-state routing.','Draw a packet path including address changes.'),
('TCP, UDP and congestion','Explain handshake, reliability, flow control and congestion control separately.','Trace sequence/acknowledgment numbers through a lost segment.'),
('DNS, HTTP and TLS overview','Explain what happens after entering a URL and where caching occurs.','Inspect a local HTTP request and response; identify headers.'),
('Processes, threads and memory','Explain scheduling, virtual memory, paging and deadlock conditions.','Trace a page-table lookup with a small address example.'),
('Core-CS teaching demo','Teach Dijkstra or normalization with an example, assumptions and a check question.','Prepare an executable example and its edge case.'),
('Mixed core-CS problems','Solve a timed mixture; explain wrong options and update your error log.','Reproduce two mistakes with minimal examples.'),
('DSA repair','Revisit the weakest graph or DP topic; explain correctness before writing code.','Solve a new instance without a solution template.'),
('DBMS repair','Revisit the weakest normalization, SQL or concurrency topic.','Test your reasoning on an unfamiliar schema/schedule.'),
('CN and OS repair','Revisit the weakest packet-flow, subnetting or memory topic.','Work a numerical example and explain each intermediate result.'),
('Written-test rehearsal','Attempt a timed mixed core-CS set using free official past questions where available.','Classify each miss as concept, calculation or time-management.'),
('Teach outside your speciality','Explain an undergraduate core concept clearly and answer follow-up questions.','Build one five-line example that exposes a misconception.'),
('Core-CS final retrieval','Solve representative questions across DSA, DBMS, CN and essential OS.','Create a concise list of remaining fragile concepts.')]
resources={'DSA':'https://jeffe.cs.illinois.edu/teaching/algorithms/','DBMS':'https://www.db-book.com/','CN':'https://gaia.cs.umass.edu/kurose_ross/online_lectures.htm','OS':'https://pages.cs.wisc.edu/~remzi/OSTEP/'}
lessons=[]
for i,(name,url,topics) in enumerate(modules):
 for title,goal,code,hand in topics:lessons.append(dict(title=title,group=name,goal=goal,code=code,url=url,hand=hand))
 for j in range(2):
  k=i*2+j;t,g,c=core[k];subject='DSA' if k<8 else 'DBMS' if k<14 else 'CN' if k<19 else 'OS' if k==19 else 'DSA'
  lessons.append(dict(title=t,group='Core CS',goal=g,code=c,url=resources[subject],hand=[0,1,2,5,18,23][i%6]))
lessons.extend([dict(title='Flexible repair and catch-up',group='Buffer',goal='Use this slot for unfinished priority work; do not add a new model family.',code='Verify an unresolved implementation question.',url='https://d2l.ai/',hand=11),dict(title='Readiness review and next-month plan',group='Review',goal='Review mastery evidence; choose next month’s weak concepts and research investigation.',code='Archive a runnable example and export a complete backup.',url='https://d2l.ai/',hand=15)])
assert len(lessons)==86
fast=['Linear algebra and tensor shapes','Probability, Bayes and uncertainty','Regression, regularization and metrics','Trees, ensembles, clustering and PCA','Backpropagation and optimization','CNNs and receptive fields','RNN/LSTM and sequence models','Word2Vec, CBOW and subword tokenization','Attention, masking and tensor shapes','Transformers and positional representations','BERT, GPT and encoder-decoder objectives','Decoding and CER/WER','Image processing, SIFT and geometry','Detection, segmentation and ViT','LLMs: adaptation, cache and retrieval','VLMs: input processing, fusion and tokens','Agents: tools, state and evaluation','DSA: complexity, sorting and trees','DSA: graphs, greedy and DP','DBMS: algebra, SQL and normalization','DBMS: transactions and indexes','CN: packet flow, subnetting and TCP','OS: processes, memory and deadlocks','Research pitch, teaching and experimental design']
questions=[
('ML','Why does L2 regularization change the solution?','Explain the objective and gradient; connect penalty strength to model flexibility. Distinguish regularization from a guarantee of improved test performance.'),
('ML','When is accuracy misleading?','Discuss class prevalence, error costs, precision/recall and thresholds. Give a numerical imbalanced-data example.'),
('Mathematics','What is a gradient, and why do tensor dimensions matter?','Explain a local direction of greatest increase, the chain rule and the shape of a derivative. Work one scalar-to-vector example.'),
('DL','Derive one weight gradient in a two-layer network.','Write forward equations, identify the upstream derivative, apply the chain rule and verify dimensions.'),
('DL','Why use residual connections?','Explain the identity path and additive gradient term. Discuss optimization without claiming all gradient problems disappear.'),
('DL','How do BatchNorm and LayerNorm differ?','Specify normalized axes, learned affine terms, train/eval behavior and why batch statistics matter.'),
('NLP','How do CBOW and skip-gram differ?','Identify input/target direction, shared embedding tables and the training objective; explain negative sampling separately.'),
('NLP','What does the attention scaling factor do?','Discuss dot-product variance under assumptions, softmax saturation and the role of head dimension. Do a small calculation.'),
('NLP','Which mask is needed during training and generation?','Separate causal, padding and loss masks; trace visible positions and ignored targets.'),
('NLP','Compare BERT, GPT and T5 objectives.','Explain context visibility, targets and encoder/decoder roles; connect those choices to a task.'),
('CV','Must ResNet receive a 224×224 image?','Distinguish a preprocessing recipe from architectural constraints. Inspect convolutional layers, pooling and classifier dimensions in the selected implementation.'),
('CV','What makes SIFT approximately scale invariant?','Trace scale-space extrema, localization, orientation and descriptor construction; explain limits of the invariance.'),
('VLM','Trace an image through a selected VLM.','Name the exact checkpoint/config; trace resize/crop, patch grid, vision encoder, connector, position handling and language-model input.'),
('VLM','Are patch size, token width and token count the same?','Define each quantity; calculate one grid; explain where merging or resampling changes sequence length.'),
('VLM','Does avoiding image padding mean no padding anywhere?','Distinguish image processing, packed vision sequences, language batching and masks. Verify the specific code path.'),
('LLM','How do LoRA and KV caching solve different problems?','LoRA changes adaptation parameterization; KV caching reuses inference states. Explain costs and limitations separately.'),
('Agents','How is an agent different from a fixed workflow?','Discuss who controls the sequence of operations; trace state, tool calls, observations and stopping conditions.'),
('Agents','How would you evaluate an agent beyond answer accuracy?','Include task success, tool errors, cost, latency, retries and unsafe actions; compare with a fixed pipeline.'),
('DSA','Why does Dijkstra need nonnegative edge weights?','Explain the finalized-distance invariant and provide a counterexample with a negative edge.'),
('DSA','Derive edit distance and its complexity.','Define prefixes, substitution/deletion/insertion transitions, boundaries, O(mn) time and memory trade-offs.'),
('DBMS','Does BCNF decomposition always preserve dependencies?','Distinguish lossless join from dependency preservation; work an explicit dependency set.'),
('DBMS','How do you test conflict serializability?','Build a precedence graph from conflicting operations of different transactions; test for a cycle.'),
('CN','Distinguish TCP flow control and congestion control.','Explain receiver capacity versus network load, advertised window and congestion window.'),
('Research','Why correct recognition output instead of improving the recognizer?','State the deployment constraints and complementary value; acknowledge cases where recognizer improvement is the stronger baseline.'),
('Research','How do you show that a second view adds useful information?','Compare matched single/dual-view baselines, corrupt or shuffle the second view, stratify disagreements and control compute.'),
('Research','How could your evaluation overstate improvements?','Discuss leakage, synthetic-to-real gaps, tuning on test data, normalization, baseline strength and uncertainty.'),
('Teaching','Teach attention to an undergraduate in ten minutes.','Start with a small weighted-retrieval example, add Q/K/V, calculate weights and finish with a diagnostic question.'),
('Research','What would you do in your first three months in this role?','Give a scoped problem, accessible data, baseline, falsifiable experiment, resource budget and deliverable.')]
Path('hub/content.json').write_text(json.dumps(dict(lessons=lessons,fast=fast,questions=[dict(area=a,q=q,guide=g)for a,q,g in questions]),ensure_ascii=False,indent=2))
print(len(lessons),'daily lessons',len(questions),'interview prompts')
