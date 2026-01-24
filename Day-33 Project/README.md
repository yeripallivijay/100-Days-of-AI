# Day 33 – Algerian Forest Fire Prediction (Part 1)

## Project Overview
Predicting whether a forest fire will occur based on weather data (Temperature, Humidity, Wind, Rain).

## Phase 1: Data Cleaning & EDA
- **Data Cleaning:**
  - Removed headers inserted in the middle of the dataset.
  - Converted object columns to float/int.
  - Cleaned whitespace from column names.
- **EDA:**
  - Heatmap shows strong correlation between **FWI (Fire Weather Index)** and Temperature.
  - Boxplots revealed outliers in **FFMC** and **ISI** columns.
- **Encoding:**
  - `Classes`: 'fire' -> 1, 'not fire' -> 0.
