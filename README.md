# audio-data-quality-audit
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
