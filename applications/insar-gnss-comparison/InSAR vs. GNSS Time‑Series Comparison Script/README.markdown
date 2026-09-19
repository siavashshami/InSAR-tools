# InSAR vs. GNSS Time-Series Comparison Script

## Overview

This Python script compares vertical displacement time series derived from **InSAR** and **GNSS** observations at the SJB1 station.

The workflow reads the two time series from CSV files, converts the observation dates to datetime format, estimates linear displacement trends, and calculates the corresponding displacement velocities.

## Input Data

* `A_SJB1.csv` — GNSS vertical displacement time series.
* `B_SJB1.csv` — InSAR vertical displacement time series.

The input files should contain observation dates and vertical displacement values in millimeters.

## Method

Linear trends are estimated using a least-squares first-order polynomial fit. The slope of each fitted trend is used to estimate the displacement velocity.

The resulting InSAR and GNSS time series and their linear trends are plotted together to facilitate comparison of deformation behavior and estimated velocities.

## Requirements

* Python 3
* NumPy
* Pandas
* Matplotlib

## Output

The script produces a comparative time-series plot containing:

* GNSS displacement
* InSAR displacement
* GNSS linear trend
* InSAR linear trend
* Estimated displacement velocities in mm/year

The figure can be used to visually assess the temporal consistency between InSAR and GNSS observations and to compare their estimated deformation rates.