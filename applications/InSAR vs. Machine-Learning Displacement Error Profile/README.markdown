# InSAR vs. Machine-Learning Displacement Error Profile

This README describes the provided data file `EW-AA.csv` and the Python plotting script `code.py`. Together they produce a two-panel profile plot comparing the east–west (E-W) displacement rate estimated by InSAR with the RFR and SVR machine-learning models along profile AA′, as a component of Fig. 8 of the associated study. Background shading highlights whether each model agrees with InSAR within a ±3 threshold.

---

## Purpose and Context

The plot corresponds to the prediction-output panel of Fig. 8 for profile AA′, whose caption reads:

    Fig. 8. The maps depict the displacement rate for the InSAR (E-W) (a), RFR (E-W) model (b), and SVR (E-W) model (c) from 2020 to 2022, InSAR (E-W), RFR (E-W), and SVR (E-W) displacement rate for profile AA′ (d), InSAR (E-W), RFR (E-W), and SVR (E-W) displacement rate for profile BB′ (e), prediction output in profile AA′ (f), and in profile BB′ (g).

Profiles (d) and (e) show the raw displacement rates of the three methods. The present script produces the difference (error) profile for AA′: InSAR minus each model, with background colouring indicating whether the model is within tolerance.

---

## Data File: `EW-AA.csv`

The CSV stores a repeating three-column block for profile AA′. Each block contains distance along the profile and one difference column:

| Column | Content | Unit |
|--------|---------|------|
| 1 | Distance along profile AA′ | metres |
| 2 | `Diff RFR` = InSAR − RFR (E-W) | mm |
| 3 | Empty separator | — |
| 4 | Distance (repeated) | metres |
| 5 | `Diff SVR` = InSAR − SVR (E-W) | mm |
| 6 | Empty separator | — |
| 7 | Distance (repeated) | metres |
| 8 | Third difference column | mm |

Notes:

- The distance values run from 0 to about 9832, i.e. the profile is roughly 9.8 km long. Despite the `Dist km` column header used in the script, the numeric values are in metres.
- `Diff RFR` contains `None` values in the middle section of the profile, meaning no valid RFR output or no overlapping InSAR data there.
- The remaining difference values span roughly −35 to +48 mm, with isolated spikes near the structural markers.

---

## Plotting Script

### Libraries

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

The `mpatches` import is unused in the current script.

### Input

The CSV is read from a hard-coded local path:

    df = pd.read_csv(r"C:\Users\siavash\Documents\sentinel\EW-AA.csv")

This path must be updated before running on another machine.

### Style

    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams['savefig.dpi'] = 500

The output is intended for publication-quality figures.

### Figure Layout

    fig = plt.figure()
    gs = fig.add_gridspec(2, hspace=0)
    ax = gs.subplots(sharex=True, sharey=True)

Two vertically stacked panels share x and y axes with zero vertical spacing.

- Top panel: `InSAR − RFR (EW)`
- Bottom panel: `InSAR − SVR (EW)`

### Background Colouring

For each row index `i` and value in `Diff RFR` (top panel) and `Diff SVR` (bottom panel):

    if -3 <= value <= 3:
        ax[n].axvspan(i-0.5, i+0.5, facecolor='greenyellow', alpha=0.2)
    else:
        ax[n].axvspan(i-0.5, i+0.5, facecolor='red', alpha=0.2)

Interpretation:

- Greenish background = model agrees with InSAR within ±3 mm
- Red background = model deviates from InSAR by more than 3 mm
- `None` / `NaN` values are skipped

### Data Lines

    ax[0].plot(df.index, df["Diff RFR"], color='black', label='InSAR - RFR (EW)')
    ax[1].plot(df.index, df["Diff SVR"], color='black', label='InSAR - SVR (EW)')

### Axis Settings

    ax[0].set_ylim(-50, 50)
    ax[1].set_ylim(-50, 50)

    ax[0].axhline(y=0, color='gray', linestyle='--')
    ax[1].axhline(y=0, color='gray', linestyle='--')

The x tick labels are placed at five evenly spaced positions using the distance column:

    ax[0].set_xticks(df.index[::len(df.index)//5], labels=df['Dist km'][::len(df.index)//5])

Because the underlying values are metres, the tick labels are numerically correct but the column name implies kilometres. Renaming the column or dividing by 1000 is recommended.

### Structural Markers

Two vertical dashed lines are drawn at row indices 22 and 44 on both panels:

    ax[0].axvline(x=22, color='black', linestyle='--')
    ax[0].axvline(x=44, color='black', linestyle='--')
    ax[1].axvline(x=22, color='black', linestyle='--')
    ax[1].axvline(x=44, color='black', linestyle='--')

Each line is labelled with a boxed marker:

    ax[0].text(21, -45, ' i ',  ...)
    ax[0].text(43, -45, " i' ", ...)
    ax[1].text(21, -45, ' i ',  ...)
    ax[1].text(43, -45, " i' ", ...)

These markers indicate the positions of the main structural features (faults or reference markers) crossing the profile AA′.

### Typography and Legends

    plt.tick_params(axis="x", labelsize=25)
    ax[0].tick_params(axis='y', labelsize=25)
    ax[1].tick_params(axis='y', labelsize=25)

    ax[0].legend(loc=1, fontsize=25, shadow=True, fancybox=True)
    ax[1].legend(loc=4, fontsize=25, shadow=True, fancybox=True)

Axis labels for displacement and distance are commented out in the current script and must be re-enabled if a fully labelled figure is required.

---

## Interpretation

- Green bands mark segments of profile AA′ where RFR or SVR reproduces the InSAR E-W displacement rate within ±3 mm.
- Red bands mark segments where the model deviates by more than 3 mm, typically near the structural markers `i` and `i′` and at the profile ends.
- Direct comparison of the two panels shows which model (RFR or SVR) follows InSAR more closely along AA′ and where each model fails.
- The `None` values in `Diff RFR` appear as gaps in the top panel line and no shading, indicating missing model output in the middle of the profile.

---

## How to Run

1. Ensure Python with `pandas`, `numpy`, and `matplotlib` is installed.
2. Place `EW-AA.csv` at the path expected by the script, or edit the path in `pd.read_csv`.
3. Update the `Dist km` column reference if the CSV is renamed.
4. Run the script; a two-panel figure window opens.
5. Optionally call `plt.savefig(...)` to export the figure at 500 dpi.

The script reads one CSV, produces one two-panel profile figure, and does not write any output files by itself. It performs no geographic processing, no InSAR computation, and no model training; it only visualises precomputed difference values along profile AA′.
