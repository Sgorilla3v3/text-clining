## Pipeline at a Glance
- Dataset layout: `data/raw/{dataset_id}` → run-scoped outputs at `*/{run_id}`
- Orchestrator: `python run_pipeline.py --dataset_id 2025-09-23_1000` (or omit to use latest)

### Steps (현재 → 계획)
- 02 Tokenize: `src/02_tokenize.py` → (planned) `src/02_tokenize_korean.py`
- 03 Keywords: `src/03_keywords_tfidf.py` → (planned) `src/03_keywords_tfidf_true.py`
- 05 Topics: `src/05_topics.py` → (planned) `src/05_topics_lda.py` / `src/05_topics_bertopic.py`
- 06 NER: `src/06_ner.py` → (planned) `src/06_ner_spacy_ko.py`
- 07 Classify: `src/07_classify.py` → (planned) `src/07_classify_ml.py`
- 08 Dashboard: `src/08_dashboard.py` → (planned) `src/08_dashboard_plotly.py`

