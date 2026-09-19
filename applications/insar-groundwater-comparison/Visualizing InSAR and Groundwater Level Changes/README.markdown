# Visualizing InSAR and Groundwater Level Changes

## Overview

This Python script visualizes the relationship between **InSAR-derived LOS displacement** and **groundwater level changes** measured by a piezometer.

The script reads groundwater and InSAR time-series data from a CSV file and displays them in a combined time-series plot, allowing the temporal behavior of groundwater-level variations and surface deformation to be compared.

## Input Data

* `s23.csv` — Contains:

  * `Time1` and `as` — Ascending InSAR observations.
  * `Time2` and `des` — Descending InSAR observations.
  * `Time3` and `well` — Groundwater-level observations from a piezometer.

Dates are converted to datetime format for time-series visualization.

## Method

The script uses a **dual y-axis time-series visualization**:

* The left y-axis represents groundwater level changes in meters.
* The right y-axis represents InSAR LOS displacement in millimeters.
* Ascending and descending InSAR measurements are plotted separately to distinguish their viewing geometries.

This visualization provides a qualitative comparison of temporal variations between groundwater-level changes and satellite-observed surface displacement.

## Requirements

* Python 3
* Pandas
* NumPy
* Matplotlib
* SciPy

## Output

The script generates a publication-quality JPEG figure:

`Example Output.jpg`

The figure simultaneously displays piezometer measurements and ascending/descending InSAR displacement time series, providing a visual basis for investigating their temporal relationship.