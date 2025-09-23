import sys, argparse
from pathlib import Path
from utils.config import load_cfg

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="configs/config.yaml")
    p.add_argument("--dataset_id", default=None, help="override dataset.id and set mode=id")
    return p.parse_args()

def get_cfg(args):
    return load_cfg(args.config, dataset_id_override=args.dataset_id)

from pathlib import Path
import pandas as pd
import json

def main():
    args = parse_args()
    cfg = get_cfg(args)
    R = cfg["_resolved"]

    cleaned = pd.read_csv(Path(R["paths"]["data_interim"]) / "cleaned.csv")
    keywords = pd.read_csv(Path(R["paths"]["data_processed"]) / "keywords_top.csv")
    edges = pd.read_csv(Path(R["paths"]["data_processed"]) / "ngrams_edges.csv")

    top_rows = "".join("<tr><td>{}</td><td>{}</td></tr>".format(t, f) for t, f in keywords.values.tolist()[:20])
    edge_rows = "".join("<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(s, d, w) for s, d, w in edges.values.tolist()[:20])

    html = '''
    <html><head><meta charset="utf-8"><title>Keyword Dashboard</title></head>
    <body style="font-family:Arial; padding:24px">
      <h1>Keyword Analysis Dashboard</h1>
      <p><b>dataset_id</b>: {dataset_id} &nbsp; <b>run_id</b>: {run_id}</p>
      <p>Documents: {doc_count}</p>
      <h2>Top Keywords</h2>
      <table border="1" cellpadding="6">
        <tr><th>token</th><th>freq</th></tr>
        {top_rows}
      </table>
      <h2>Co-occurrence Edges (Top 20)</h2>
      <table border="1" cellpadding="6">
        <tr><th>src</th><th>dst</th><th>weight</th></tr>
        {edge_rows}
      </table>
    </body></html>
    '''.format(dataset_id=R["dataset_id"], run_id=R["run_id"], doc_count=len(cleaned), top_rows=top_rows, edge_rows=edge_rows)

    out_dir = Path(R["paths"]["outputs"]) / "dashboard"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "dash.html"
    out.write_text(html, encoding="utf-8")
    print("Wrote dashboard → {}".format(out))

    # Write latest pointer
    latest = Path("outputs/latest_run.json")
    latest.parent.mkdir(parents=True, exist_ok=True)
    latest.write_text(json.dumps({{"dataset_id": R["dataset_id"], "run_id": R["run_id"]}}, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()