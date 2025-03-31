# Audio-Data-Quality-Audit
A project to audit and analyze data using Python, SQL and Power BI

# 🎵 Audio Data Quality Audit

This project aims to perform a comprehensive data quality audit for an audio dataset using Python, SQL, and Power BI. The goal is to ensure clean and consistent data by detecting missing values, duplicates, and misclassified genres.

## 🛠️ Step 1: Metadata Generation using Python

- Extracted audio metadata using `extract_metadata.py`.
- Generated a `metadata.csv` file containing:
  - **TrackName** → Name of the audio file.
  - **Genre** → Genre derived from the folder structure.
  - **FilePath** → Full file path for the track.
- This step helped in structuring the data for further analysis.

### 📂 File Overview
- **data/metadata.csv** → Contains metadata of all tracks.
- **src/extract_metadata.py** → Python script used to create the CSV.

## 🚀 Next Steps
- Perform Data Quality Checks using SQL.
- Visualize insights using Power BI.

Stay tuned for updates!

## 📊 Project Progress

### ✅ Step 1: Data Overview

- Conducted an initial analysis to understand the structure and quality of the dataset.
- Verified file path consistency using SQL to ensure proper alignment of genre, filename, and file path.
- Checked for any missing or inconsistent data.
- All file paths were validated and confirmed to be correct.

**Next Step:** Proceeding to data cleaning and transformation to prepare the dataset for further analysis.

