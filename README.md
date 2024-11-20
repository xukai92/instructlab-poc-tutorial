# InstructLab POC Tutorial

## 1. SDG preparation

### 1.1 Get your document ready

Collect the knowledge documents in PDF format that you want to teach your model.
- For example, we use the [`bnpp-fin-statement.pdf`](./bnpp-fin-statement.pdf) in a previous POC.
- Optionally, you can use the [`preprocess.py`](./preprocess.py) script to preprocess your document using [docling](https://github.com/DS4SD/docling).

### 1.2 Prepare your `qna.yaml` file

You need to prepare a `qna.yaml` file to describe the types knowledge you want to teach your model.
- The [`qna.yaml`](./qna.yaml) provided in the repo is the one we used together with [`bnpp-fin-statement.pdf`](./bnpp-fin-statement.pdf).
- This [repository](https://github.com/abhi1092/qna_guideline) provides a good guide for beginners to work with `qna.yaml` files.

## 2. Train the model

You can use the InstructLab Service on IBM Cloud to train your model.

## 3. Evaluate the model in RAG system

### 3.1 Serve the trained model
---with your serving method

You need to deploy the trained model, either on the cloud or downloading it and serving it locally.

### 3.2 Use the trained model to answer questions and run evaluation
---with your favorite RAG system

You can follow [this notebook](https://github.com/rh-aiservices-bu/rhel-ai-poc/blob/b880c2e6937d7497b35362dcd7a87ea97c2a69ff/eval/llm_judge_eval.ipynb) where has a simple RAG with LLM judge evaluation.
- You don't have to use the RAG system in the notebook---you can use your own RAG system and continue the evaluation with from the section called "Grade responses using Judge Model".