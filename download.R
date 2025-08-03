# install if needed
if (!requireNamespace("GEOquery", quietly=TRUE)) {
  BiocManager::install("GEOquery")
}
library(GEOquery)

# 1) Download the RAW tarball into data/GSE137766
getGEOSuppFiles(
  "GSE137766",
  baseDir       = "data",
  makeDirectory = TRUE
)

# 2) Untar it
tar_file <- file.path("data","GSE137766","GSE137766_RAW.tar")
untar(tar_file, exdir = file.path("data","GSE137766"))

# Now you’ll have the *_bc.csv.gz and *_umi.csv.gz files in data/GSE137766/
