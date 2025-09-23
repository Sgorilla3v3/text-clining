좋습니다 🙆
GitHub 리포지토리의 `README.md`에 그대로 **복사·붙여넣기** 할 수 있는 고도화된 한국어 버전을 만들어드렸습니다.

---

```markdown
# 키워드 분석 프로젝트
[![CI](https://github.com/<USER>/<REPO>/actions/workflows/ci.yml/badge.svg)](https://github.com/<USER>/<REPO>/actions)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)

> 텍스트 데이터셋을 실행(run) 단위로 관리하고, 키워드·토픽·엔터티를 분석해 HTML 대시보드로 출력하는 파이프라인
```
---

## 📌 목차
- [0) TL;DR](#0-tldr)
- [1) 주요 기능](#1-주요-기능)
- [2) 폴더 구조](#2-폴더-구조)
- [3) 빠른 실행 방법](#3-빠른-실행-방법)
- [4) 설정파일](#4-설정파일)
- [5) 파이프라인 단계](#5-파이프라인-단계--현재-vs-미구현)
- [6) 출력물](#6-출력물)
- [7) 요구 사항](#7-요구-사항)
- [8) 로드맵](#8-로드맵)
- [9) 라이선스](#9-라이선스)

---

## 0) TL;DR
- 🗂️ **유연한 데이터셋 관리**: `data/raw/{dataset_id}/`에 snapshot 저장 (기본값: `latest`)
- 📂 **실행(run) 단위 출력**: 실행 시마다 `*/{run_id}`에 결과 저장 (`{dataset_id}_{YYYYMMDDHHMMSS}`)
- ⚙️ **현재 상태**: 파이프라인은 end-to-end 실행 가능. 일부 단계는 **placeholder 로직**으로 구현 → 추후 업그레이드 예정

---

## 1) 주요 기능
- ✅ Dataset / 버전 관리 (`latest` 또는 `--dataset_id` 지정 가능)
- ✅ 8단계 파이프라인 (로드 → 토큰화 → 키워드 → 공동출현 → 토픽 → NER → 분류 → 대시보드)
- ✅ 실행(run) 단위별 재현 가능한 출력
- ⏳ 업그레이드 예정: 한국어 형태소 분석기, TF-IDF, LDA/BERTopic, spaCy NER, ML 분류기, Plotly 대시보드

---

## 2) 폴더 구조

```markdown
.github/workflows/ci.yml
.gitignore
LICENSE
README.md
configs/config.yaml
data/raw/.gitkeep
data/raw/filtered\_blog2.json
dicts/layer\_rules.yml
dicts/persona\_rules.yml
dicts/program\_list.csv
dicts/stopwords.txt
dicts/synonyms.csv
requirements.txt
src/08\_dashboard.py
src/utils/io.py
src/utils/log.py
src/utils/text.py
```


---

## 3) 빠른 실행 방법
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 최신 dataset으로 실행
python run_pipeline.py

# 특정 dataset snapshot 지정
python run_pipeline.py --dataset_id 2025-09-23_1000
````

---

## 4) 설정파일 (configs/config.yaml)

```
configs/config.yaml
- dataset.mode: `None`
- dataset.id: `None`
- dataset.raw_root: `None` (glob: `None`)
- run.run_id: `None` (자동: `{dataset_id}_{YYYYMMDDHHMMSS}`)
- outputs_root: `None`
- interim_root: `None`, processed_root: `None`
```

---

## 5) 파이프라인 단계 — 현재 vs 미구현

| 단계 파일                 | 상태 / 설명             |
| --------------------- | ------------------- |
| `src/08_dashboard.py` | 정적 HTML 대시보드 (stub) |

### 🚧 계획은 되었으나 미구현된 파일

* src/02\_tokenize\_korean.py
* src/03\_keywords\_tfidf\_true.py
* src/05\_topics\_lda.py
* src/05\_topics\_bertopic.py
* src/06\_ner\_spacy\_ko.py
* src/07\_classify\_ml.py
* src/08\_dashboard\_plotly.py
* notebooks/EDA.ipynb

---

## 6) 출력물

* `data/interim/{run_id}/cleaned.csv`, `tokens.csv`
* `data/processed/{run_id}/keywords_top.csv`, `ngrams_edges.csv`, `topics.json`, `entities.csv`, `layer_tags.csv`
* `outputs/runs/{run_id}/dashboard/dash.html`
* `outputs/latest_run.json`

---

## 7) 요구 사항 (요약)

* pandas, numpy, PyYAML, tqdm, scikit-learn, networkx, matplotlib, plotly

---

## 8) 로드맵

* 🔤 토큰화 → `kiwipiepy` / `OKT` 적용 (품사 필터링, 복합명사 처리)
* 🗝️ 키워드 → TF-IDF (scikit-learn)
* 📑 토픽 → LDA + coherence / BERTopic (다국어 지원)
* 🧩 NER → spaCy Ko/KoELECTRA 기반
* 🏷️ 분류기 → ML 기반 정교화
* 📊 대시보드 → Plotly 인터랙티브 시각화

---

## 9) 라이선스

MIT (상세 내용은 `LICENSE` 파일 참고)

```




