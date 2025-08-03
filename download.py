import os
import urllib.request
import tarfile

def download_and_extract_geo_raw(gse_id, out_dir="data"):
    """
    Download the GSE<id>_RAW.tar from GEO and extract its contents,
    which include the bc.csv.gz and umi.csv.gz count matrices.
    """
    # prepare directories
    os.makedirs(out_dir, exist_ok=True)
    prefix = gse_id[:7] + "nnn"  # e.g. "GSE1377" -> "GSE1377nnn"
    tar_name = f"{gse_id}_RAW.tar"
    tar_path = os.path.join(out_dir, tar_name)

    # construct FTP URL
    url = (
        f"ftp://ftp.ncbi.nlm.nih.gov/geo/series/"
        f"{prefix}/{gse_id}/suppl/{tar_name}"
    )
    print(f"Downloading {tar_name} …")
    urllib.request.urlretrieve(url, tar_path)
    print(f"Saved raw archive to {tar_path}")

    # extract
    extract_dir = os.path.join(out_dir, gse_id)
    print(f"Extracting to {extract_dir} …")
    with tarfile.open(tar_path, "r") as tar:
        tar.extractall(path=extract_dir)
    print("Done.")

    return extract_dir

if __name__ == "__main__":
    # Download & extract GSE137766
    extracted_folder = download_and_extract_geo_raw("GSE137766", out_dir="data")

    # List the extracted CSVs
    print("\nExtracted files:")
    for fn in sorted(os.listdir(extracted_folder)):
        if fn.endswith(".csv.gz"):
            print("  ", fn)
