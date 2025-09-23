---

# 키워드 분석 프로젝트 — README (초안)

> 저장소 내용을 기반으로 자동 생성되었습니다. **구현 완료**된 부분과 **계획 단계**를 구분하여 표시합니다.

## 0) TL;DR

* **유연한 데이터셋 관리**: `data/raw/{dataset_id}/`에 dataset snapshot 저장 (기본값은 `latest`).
* **실행(run) 단위 출력**: 실행할 때마다 `*/{run_id}`에 결과 저장 (`{dataset_id}_{YYYYMMDDHHMMSS}`).
* **상태**: 파이프라인은 처음부터 끝까지 실행 가능. 다만 일부 단계는 **임시(placeholder) 로직**으로 구현되어 있으며 업그레이드 예정.

## 1) 주요 기능

* ✅ Dataset / 버전 관리 (`latest` 또는 `--dataset_id` 지정 가능)
* ✅ 8단계 파이프라인 (로드 → 토큰화 → 키워드 → 공동출현 → 토픽 → NER → 분류 → 대시보드)
* ✅ 실행(run) 단위별 재현 가능한 출력
* ⏳ 업그레이드 예정: 한국어 형태소 분석기, TF-IDF, LDA/BERTopic, spaCy NER, ML 기반 분류기, Plotly 대시보드

## 2) 폴더 구조 (zip 기준)

```
.github/workflows/ci.yml
.gitignore
LICENSE
README.md
configs/config.yaml
data/raw/.gitkeep
data/raw/filtered_blog2.json
dicts/layer_rules.yml
dicts/persona_rules.yml
dicts/program_list.csv
dicts/stopwords.txt
dicts/synonyms.csv
requirements.txt
src/08_dashboard.py
src/utils/io.py
src/utils/log.py
src/utils/text.py
```

## 3) 빠른 실행 방법

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 최신 dataset으로 실행
python run_pipeline.py

# 특정 dataset snapshot 지정
python run_pipeline.py --dataset_id 2025-09-23_1000
```

## 4) 설정파일 (configs/config.yaml)

```
- dataset.mode: `None`
- dataset.id: `None`
- dataset.raw_root: `None` (glob: `None`)
- run.run_id: `None` (자동: `{dataset_id}_{YYYYMMDDHHMMSS}`)
- outputs_root: `None`
- interim_root: `None`, processed_root: `None`
```

## 5) 파이프라인 단계 — 현재 vs 미구현

| 단계 파일                 | 상태 / 설명             |
| --------------------- | ------------------- |
| `src/08_dashboard.py` | 정적 HTML 대시보드 (stub) |

### 계획은 되었으나 미구현된 파일

* src/02\_tokenize\_korean.py
* src/03\_keywords\_tfidf\_true.py
* src/05\_topics\_lda.py
* src/05\_topics\_bertopic.py
* src/06\_ner\_spacy\_ko.py
* src/07\_classify\_ml.py
* src/08\_dashboard\_plotly.py
* notebooks/EDA.ipynb

## 6) 출력물

* `data/interim/{run_id}/cleaned.csv`, `tokens.csv`
* `data/processed/{run_id}/keywords_top.csv`, `ngrams_edges.csv`, `topics.json`, `entities.csv`, `layer_tags.csv`
* `outputs/runs/{run_id}/dashboard/dash.html`
* `outputs/latest_run.json`

## 7) 요구 사항 (요약)

* pandas, numpy, PyYAML, tqdm, scikit-learn, networkx, matplotlib, plotly

## 8) 로드맵

* 토큰화 → `kiwipiepy` / `OKT` 적용 (품사 필터링, 복합명사 처리)
* 키워드 → TF-IDF (scikit-learn)
* 토픽 → LDA + coherence / BERTopic (다국어 지원)
* NER → spaCy Ko/KoELECTRA 기반
* 분류기 → ML 기반 정교화
* 대시보드 → Plotly 인터랙티브 시각화

## 9) 라이선스

MIT (상세 내용은 `LICENSE` 파일 참고)

---

