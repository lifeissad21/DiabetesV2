import pandas as pd
import os

def merge_umi_files_parquet(
    output_file="umi_merged.parquet", 
    suffix="_umi.csv.gz"
):
    umis = []
    print(f"Scanning for {suffix} files in current directory...")
    for fn in sorted(os.listdir("data/GSE137766")):
        if fn.endswith(suffix):
            print(f"Loading: {fn}")
            df = pd.read_csv(os.path.join("data/GSE137766", fn), compression="gzip", index_col=0)
            # Prefix columns to keep unique (file-based)
            df.columns = [f"{fn[:-7]}_{c}" for c in df.columns]
            umis.append(df)
            print(f"Loaded {fn}: {df.shape}")

    if not umis:
        print(f"No {suffix} files found! Exiting.")
        return

    print("Merging all UMI dataframes on gene index...")
    umi_merged = pd.concat(umis, axis=1)
    print("Final UMI matrix:", umi_merged.shape)
    umi_merged.to_parquet(output_file, compression="gzip")
    print(f"Saved merged UMI matrix as {output_file}")

# To run:
merge_umi_files_parquet()