from pathlib import Path
import pandas as pd
from collections import Counter
import argparse

CANONICAL = {
    'surprise': 'Surprise',
    'terkejut': 'Surprise',
    'trkejut': 'Surprise',
    'kaget': 'Surprise',
    'trekejut': 'Surprise',

    'joy': 'Joy',
    'happy': 'Joy',

    'trust': 'Trust',
    'faith': 'Trust',
    'loyalty': 'Trust',
    'percaya': 'Trust',

    'proud': 'Proud',
    'pride': 'Proud',
    'bangga': 'Proud',
    'love': 'Proud',

    'sadness': 'Sadness',
    'sad': 'Sadness',

    'anger': 'Anger',
    'angry': 'Anger',
    'marah': 'Anger',
    'marh': 'Anger',

    'fear': 'Fear',

    'neutral': 'Neutral'
}


def normalize_label(raw_label: str) -> str:
    if pd.isna(raw_label):
        return ''
    s = str(raw_label).strip()
    low = s.lower()
    return CANONICAL.get(low, s.title())


def normalize_video(v: str) -> str:
    if pd.isna(v):
        return ''
    s = str(v).strip()
    s = s.replace('\n', ' ').replace('\r', ' ')
    return s.strip()


def dedupe_and_report(df: pd.DataFrame):
    df = df.copy()
    # normalize labels and video keys
    df['emotion_clean'] = df['emotion'].apply(normalize_label)
    df['video_norm'] = df['video'].apply(normalize_video)
    df['video_key'] = df['video_norm'].str.lower().str.replace('\s+', ' ', regex=True).str.strip()

    groups = df.groupby('video_key')
    keep_rows = []
    conflict_rows = []
    report = []

    for key, g in groups:
        unique_labels = g['emotion_clean'].dropna().unique().tolist()
        counts = Counter(g['emotion_clean'].dropna().tolist())
        if len(unique_labels) <= 1:
            # safe to dedupe: keep first
            keep_rows.append(g.iloc[0].to_dict())
        else:
            # conflict - save for review
            for _, r in g.iterrows():
                conflict_rows.append(r.to_dict())
            report.append({'video_key': key, 'n_rows': len(g), 'labels': dict(counts)})

    df_keep = pd.DataFrame(keep_rows)
    df_conflicts = pd.DataFrame(conflict_rows)
    report_df = pd.DataFrame(report)
    return df_keep, df_conflicts, report_df


def resolve_conflicts_majority(df_conflicts: pd.DataFrame):
    # For each video_key choose majority label; if tie, choose first alphabetically
    resolved = []
    if df_conflicts.empty:
        return pd.DataFrame()
    for key, g in df_conflicts.groupby('video_key'):
        counts = Counter(g['emotion_clean'].dropna().tolist())
        if not counts:
            chosen = ''
        else:
            max_count = max(counts.values())
            candidates = [lab for lab, c in counts.items() if c == max_count]
            chosen = sorted(candidates)[0]
        # pick first row from group but force emotion_clean to chosen
        row = g.iloc[0].to_dict()
        row['emotion_clean'] = chosen
        resolved.append(row)
    return pd.DataFrame(resolved)


def run_pipeline(raw_path: Path, out_clean: Path, out_conflicts: Path, strategy: str = 'none'):
    raw = pd.read_csv(raw_path)
    keep, conflicts, report = dedupe_and_report(raw)

    # always write conflicts for review
    conflicts.to_csv(out_conflicts, index=False)

    # By default do NOT include conflicting groups in the final file.
    # If a resolution strategy is explicitly requested, resolve and include them.
    if strategy == 'majority':
        resolved = resolve_conflicts_majority(conflicts)
        final = pd.concat([keep, resolved], ignore_index=True)
    else:
        final = keep.copy()

    cols = list(raw.columns) + ['emotion_clean']
    cols = [c for c in cols if c in final.columns]
    final = final[cols]
    final.to_csv(out_clean, index=False)
    return len(raw), len(final), len(conflicts)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Clean datatrain.csv and dedupe videos')
    parser.add_argument('--input', type=str, default='data/datatrain.csv')
    parser.add_argument('--out', type=str, default='data/datatrain_clean.csv')
    parser.add_argument('--conflicts', type=str, default='data/duplicate_conflicts.csv')
    parser.add_argument('--strategy', type=str, default='none', help='conflict resolution strategy: "none" (exclude conflicts), "majority" (resolve by majority)')
    args = parser.parse_args()

    raw_path = Path(args.input)
    out_clean = Path(args.out)
    out_conflicts = Path(args.conflicts)

    raw_n, final_n, conflict_n = run_pipeline(raw_path, out_clean, out_conflicts, args.strategy)
    print(f'Raw rows: {raw_n}, Final rows: {final_n}, Conflict rows: {conflict_n}')
