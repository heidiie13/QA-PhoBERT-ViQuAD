# QA-PhoBERT-ViQuAD

- Step 1: Create and activate conda env

```sh
conda create -n qa_viquad python=3.10
conda activate qa_viquad
```

- Step 2: Install requirements

```sh
pip install -r requirements.txt
```
- Step 3: Create pipeline

```sh
python app/core_ai/qa.py
```

- Step 4: Run app (api)

```sh
uvicorn app.api.main:app --host 0.0.0.0 --port 8000
```
