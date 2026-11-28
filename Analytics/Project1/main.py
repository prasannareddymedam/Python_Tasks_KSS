# =============================================================================
# PROJECT NAME : Railway_Guages  (Railway Gauge Analysis)
# -----------------------------------------------------------------------------
# DATASET      : railway_gauges.csv
# COLUMNS      : Year (e.g. "1964-65"), Broad Gauge, Metre Gauge,
#                Narrow Gauge, Total   (track length per gauge type)
# WHAT IT DOES : Solves all 5 scenarios (cleaning -> line -> bar -> pie ->
#                advanced analysis) and saves every graph in the "graphs" folder.
# HOW TO RUN   : python main.py   (keep this file and the CSV in the same folder)
# =============================================================================


# =============================================================================
# IMPORTS
# =============================================================================
import os                          # build file/folder paths and create the graphs folder
import pandas as pd                # load the CSV, clean data, filter, group, new columns
import numpy as np                 # np.diff() for year-on-year growth, array maths
import matplotlib.pyplot as plt    # draw and save all the graphs


# =============================================================================
# SETUP: paths and output folder
# =============================================================================
# Folder where this main.py lives -> works no matter where you run it from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "railway_gauges.csv")
GRAPHS_DIR = os.path.join(BASE_DIR, "graphs")

# Create the graphs folder if it does not exist (task note: save all graphs there)
os.makedirs(GRAPHS_DIR, exist_ok=True)


def save_graph(filename):
    """Save the current figure inside the graphs folder, then close it."""
    plt.tight_layout()                                           # stop labels getting cut off
    plt.savefig(os.path.join(GRAPHS_DIR, filename), dpi=150)     # write PNG to graphs/
    plt.close()                                                  # free memory, start fresh next time


# =============================================================================
# SCENARIO 1: Basic Data Loading & Cleaning
# =============================================================================
"""You are given a CSV file containing railway gauge data. 
�
�
Tasks: 
1. Load the dataset into a Pandas DataFrame. 
2. Display the first 5 rows and column names. 
3. Check for missing values and replace them with 0. 
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.
"""
print("=" * 70)
print("SCENARIO 1: Basic Data Loading & Cleaning")
print("=" * 70)

# 1. Load the dataset into a Pandas DataFrame
df = pd.read_csv(CSV_PATH)

# 2. Display the first 5 rows and the column names
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:", list(df.columns))

# 3. Check for missing values, then replace them with 0
print("\nMissing values per column (before filling):")
print(df.isnull().sum())
df = df.fillna(0)    # replaces every NaN with 0 (this file has none, but the step is required)

# 4. Convert all gauge columns to numeric types
#    errors="coerce" turns any bad text into NaN, which fillna(0) then makes 0
gauge_cols = ["Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]
for col in gauge_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

print("\nData types after conversion:")
print(df.dtypes)

# Helper column used by later scenarios:
# "Year" is text like "1964-65", so we take the first 4 characters (1964) as a number.
# This lets us plot, filter ("after 2000") and sort by year properly.
df["Start Year"] = df["Year"].str[:4].astype(int)


# =============================================================================
# SCENARIO 2: Simple Visualization (line graph of Total tracks)
# =============================================================================
"""You want a quick understanding of total railway track growth. 
�
�
Tasks: 
1. Extract Year and Total columns. 
2. Plot a line graph showing Total tracks over years. 
3. Add: 
○ Title 
○ X and Y labels 
4. Identify whether the trend is increasing or decreasing. 
"""
print("\n" + "=" * 70)
print("SCENARIO 2: Total railway track growth")
print("=" * 70)

# 1. Extract the Year and Total columns
year_total = df[["Year", "Total"]]

# 2 & 3. Line graph with title, x label and y label
plt.figure(figsize=(12, 6))
plt.plot(year_total["Year"], year_total["Total"], marker="o", color="tab:blue")
plt.title("Total Railway Track Length Over the Years")
plt.xlabel("Year")
plt.ylabel("Total Track Length (km)")
plt.xticks(rotation=90)       # 49 year labels are long, so rotate them
plt.grid(alpha=0.3)
save_graph("scenario2_total_line.png")

# 4. Identify whether the trend is increasing or decreasing
#    Compare the first value with the last value, and find the lowest point (the dip)
first_total = df["Total"].iloc[0]
last_total = df["Total"].iloc[-1]
lowest_row = df.loc[df["Total"].idxmin()]
highest_row = df.loc[df["Total"].idxmax()]
trend = "INCREASING" if last_total > first_total else "DECREASING"
print(f"Total went from {first_total} ({df['Year'].iloc[0]}) to "
      f"{last_total} ({df['Year'].iloc[-1]}): overall trend is {trend} "
      f"({last_total - first_total:+d} km)")
print(f"Lowest point : {lowest_row['Total']} in {lowest_row['Year']}")
print(f"Highest point: {highest_row['Total']} in {highest_row['Year']}")
print("Interpretation: the total grew in the 1960s-70s, stayed almost flat and then "
      "fell during the 1990s to its lowest point in 2000-01 (old lines closed or "
      "were converted), and rose again afterwards to a new peak. Overall: INCREASING.")


# =============================================================================
# SCENARIO 3: Filtering + Grouped Bar Chart (years after 2000)
# =============================================================================
"""You are asked to analyze modern railway expansion. 
�
�
Tasks: 
1. Filter the dataset for years after 2000. 
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
3. Plot a grouped bar chart comparing all three gauges. 
4. Add legend and proper labels. 
5. Identify which gauge dominates in recent years.
"""
print("\n" + "=" * 70)
print("SCENARIO 3: Modern railway expansion (after 2000)")
print("=" * 70)

# 1. Filter the dataset for years after 2000 (start year 2001-02 onwards)
modern = df[df["Start Year"] > 2000]

# 2. Select the three gauge types
three_gauges = ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]
modern_gauges = modern.set_index("Year")[three_gauges]
print(modern_gauges)

# 3 & 4. Grouped bar chart: pandas draws 3 bars side by side for each year
ax = modern_gauges.plot(kind="bar", figsize=(13, 6), width=0.8)
ax.set_title("Gauge-wise Track Length After 2000")
ax.set_xlabel("Year")
ax.set_ylabel("Track Length (km)")
ax.legend(title="Gauge Type")           # legend
plt.xticks(rotation=45)
save_graph("scenario3_grouped_bar.png")

# 5. Which gauge dominates in recent years?
avg_recent = modern_gauges.mean()
print("\nAverage track length per gauge after 2000:")
print(avg_recent.round(1))
print(f"Dominant gauge in recent years: {avg_recent.idxmax()}")


# =============================================================================
# SCENARIO 4: Feature Engineering + Pie Chart
# =============================================================================
"""You want to analyze the contribution of each gauge type. 
�
�
Tasks: 
1. Calculate total sum of each gauge across all years. 
2. Create a new structure (Series/DataFrame) for totals. 
3. Plot a pie chart showing percentage contribution. 
4. Add percentage labels (autopct). 
5. Interpret which gauge contributes the most.
"""
print("\n" + "=" * 70)
print("SCENARIO 4: Contribution of each gauge")
print("=" * 70)

# 1 & 2. Sum of each gauge across all years, stored as a new Series
gauge_totals = df[three_gauges].sum()
print(gauge_totals)

# 3 & 4. Pie chart with percentage labels (autopct)
plt.figure(figsize=(7, 7))
plt.pie(gauge_totals, labels=gauge_totals.index, autopct="%1.1f%%",
        startangle=90, colors=["tab:blue", "tab:orange", "tab:green"])
plt.title("Percentage Contribution of Each Gauge (All Years)")
save_graph("scenario4_pie.png")

# 5. Interpret which gauge contributes the most
top_gauge = gauge_totals.idxmax()
share = gauge_totals.max() / gauge_totals.sum() * 100
print(f"\n{top_gauge} contributes the most ({share:.1f}% of the combined track length).")


# =============================================================================
# SCENARIO 5: Advanced Analysis + Multiple Graphs
# =============================================================================
"""You are asked to perform a complete analysis of railway trends. 
�
�
Tasks: 
1. Create new columns: 
○ % Broad Gauge 
○ % Metre Gauge 
○ % Narrow Gauge 
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks. 
3. Plot: 
○ Line graph for all gauges 
○ Stacked bar chart showing composition 
4. Highlight: 
○ Years with highest growth 
○ Decline in any gauge 
5. Provide a final conclusion: 
�
�
“Is the railway system shifting towards a single dominant gauge?”
"""
print("\n" + "=" * 70)
print("SCENARIO 5: Complete analysis of railway trends")
print("=" * 70)

# 1. New columns: percentage share of each gauge in that year's Total
#    (we use the sum of the three gauges as the base so shares always add to 100)
gauge_sum = df[three_gauges].sum(axis=1)
df["% Broad Gauge"] = df["Broad Gauge"] / gauge_sum * 100
df["% Metre Gauge"] = df["Metre Gauge"] / gauge_sum * 100
df["% Narrow Gauge"] = df["Narrow Gauge"] / gauge_sum * 100
print(df[["Year", "% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]].round(1).head())

# 2. Yearly growth of Total tracks using np.diff()
#    np.diff gives (value[i+1] - value[i]) so it is one element shorter than the data;
#    the first year has no previous year, so its growth is set to NaN.
total_array = df["Total"].to_numpy()
growth = np.diff(total_array)
df["Total Growth"] = np.concatenate(([np.nan], growth))

# 3a. Line graph for all gauges (plus Total)
plt.figure(figsize=(12, 6))
for col, color in zip(three_gauges, ["tab:blue", "tab:orange", "tab:green"]):
    plt.plot(df["Year"], df[col], marker="o", markersize=3, label=col, color=color)
plt.plot(df["Year"], df["Total"], linestyle="--", color="black", label="Total")
plt.title("Railway Track Length by Gauge Over the Years")
plt.xlabel("Year")
plt.ylabel("Track Length (km)")
plt.xticks(rotation=90)
plt.legend()
plt.grid(alpha=0.3)
save_graph("scenario5_all_gauges_line.png")

# 3b. Stacked bar chart showing the composition (percentage) of each year
pct_cols = ["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]
ax = df.set_index("Year")[pct_cols].plot(
    kind="bar", stacked=True, figsize=(13, 6), width=0.9,
    color=["tab:blue", "tab:orange", "tab:green"])
ax.set_title("Gauge Composition by Year (Stacked, % of Track)")
ax.set_xlabel("Year")
ax.set_ylabel("Share of Track (%)")
ax.legend(title="Gauge Type", loc="upper center", bbox_to_anchor=(0.5, -0.25), ncol=3)
plt.xticks(rotation=90)
save_graph("scenario5_stacked_bar.png")

# 4a. Highlight the years with the highest growth in Total tracks
top_growth = df.nlargest(3, "Total Growth")[["Year", "Total Growth"]]
print("\nTop 3 years with the highest growth in Total tracks (km):")
print(top_growth.to_string(index=False))

# Growth bar chart: green bars = growth, red = decline, gold = top-3 growth years
plt.figure(figsize=(12, 6))
bar_colors = ["tab:red" if g < 0 else "tab:green" for g in growth]
for i, year in enumerate(df["Year"].iloc[1:]):
    if year in top_growth["Year"].values:
        bar_colors[i] = "gold"
plt.bar(df["Year"].iloc[1:], growth, color=bar_colors, edgecolor="black", linewidth=0.3)
plt.axhline(0, color="black", linewidth=0.8)
plt.title("Yearly Growth in Total Track Length (Gold = Top 3 Growth Years, Red = Decline)")
plt.xlabel("Year")
plt.ylabel("Change vs previous year (km)")
plt.xticks(rotation=90)
save_graph("scenario5_total_growth.png")

# 4b. Highlight declines in any gauge: np.diff on each gauge column
print("\nOverall change from first to last year for each gauge:")
for col in three_gauges:
    change = df[col].iloc[-1] - df[col].iloc[0]
    print(f"  {col}: {df[col].iloc[0]} -> {df[col].iloc[-1]} ({change:+d} km)")

print("\nYear-on-year declines per gauge:")
for col in three_gauges:
    diffs = np.diff(df[col].to_numpy())
    decline_years = df["Year"].iloc[1:][diffs < 0]       # years where value fell
    print(f"  {col}: fell in {len(decline_years)} years; "
          f"biggest single-year fall = {diffs.min()} km "
          f"in {df['Year'].iloc[1:].iloc[diffs.argmin()]}")

# 5. Final conclusion: is the system shifting towards a single dominant gauge?
broad_first, broad_last = df["% Broad Gauge"].iloc[0], df["% Broad Gauge"].iloc[-1]
metre_first, metre_last = df["% Metre Gauge"].iloc[0], df["% Metre Gauge"].iloc[-1]
print("\n" + "-" * 70)
print("FINAL CONCLUSION")
print("-" * 70)
print(f"Broad Gauge share: {broad_first:.1f}% ({df['Year'].iloc[0]}) -> "
      f"{broad_last:.1f}% ({df['Year'].iloc[-1]})")
print(f"Metre Gauge share: {metre_first:.1f}% -> {metre_last:.1f}%")
if broad_last > broad_first and broad_last > 50:
    print("YES - the railway system is clearly shifting towards a single dominant "
          "gauge: Broad Gauge.")
    print("Broad Gauge grew while Metre and Narrow Gauge declined, which matches "
          "the gauge conversion programme (Project Unigauge).")
else:
    print("NO - no single gauge is taking over.")

print(f"\nAll graphs saved in: {GRAPHS_DIR}")
