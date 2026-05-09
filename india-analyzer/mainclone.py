import pandas as pd
import matplotlib.pyplot as plt
import zipfile

# creating dataset and setting it to display max columns
with zipfile.ZipFile("dataset.zip", "r") as z:
    with z.open("india-news-headlines.csv") as f:
        df = pd.read_csv(f)

# cleaning
"""
cleaning done
"""

# Taking user input
fact1 = input("Enter your 'base topic' to analyze: ").strip().lower()
fact2 = input("Enter your topic to 'analyze against': ").strip().lower()

# keeping track of years when fact1 was mentioned
""" using boolean indexing """
fact1_mask = df['headline_text'].str.contains(fact1, case=False, na=False)
fact1_df = df[fact1_mask]
fact1_df = fact1_df.copy()  # gives a new dataframe
fact1_df['year'] = fact1_df.publish_date.astype(str).str[:4]
fact1_by_year = fact1_df['year'].value_counts().sort_index()

# keeping track of years when fact2 was mentioned
""" using boolean indexing """
fact2_mask = df['headline_text'].str.contains(fact2, case=False, na=False)
fact2_df = df[fact2_mask]
fact2_df = fact2_df.copy()  # gives a new dataframe
fact2_df['year'] = fact2_df['publish_date'].astype(str).str[:4]
fact2_by_year = fact2_df['year'].value_counts().sort_index()

# combine both the dataframes
df_combined = pd.concat([fact1_df, fact2_df], ignore_index=True)

# combined years
years = fact1_by_year.index.union(fact2_by_year.index)

# matplotlib plotting
fig, ax = plt.subplots(figsize=(13.66, 7.68))
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()  # manager sets res to fullscreen

# adding title and subtitle
ax.set_title("Headline frequency analysis across Indian news (2001–2023)",
             fontsize=9, color='black', pad=25)
fig.suptitle(f"{fact1} v/s {fact2}", fontsize=14, fontweight='bold')

# axis creation and labelling — fact1 on left axis
ax.plot(fact1_by_year.index, fact1_by_year.values,  # FIXED: was fact2_by_year.values
        label=fact1, marker='o', color='blue')
ax.set_ylabel(fact1, color='blue')
ax.tick_params(axis='y', labelcolor='blue')
ax.yaxis.set_major_locator(plt.MultipleLocator(100))  # y grid lines every 100
ax.xaxis.set_major_locator(plt.MultipleLocator(1))    # x grid lines every year

# adding secondary axis — fact2 on right axis
ax2 = ax.twinx()
ax2.plot(fact2_by_year.index, fact2_by_year.values,
         label=fact2, marker='o', color='red')
ax2.set_ylabel(fact2, color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.yaxis.set_major_locator(plt.MultipleLocator(10))

# legend
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

# adding grid
ax.grid(True, linestyle='-', which='major')
ax.tick_params(axis='both')

# adding peak annotations
peak_fact1_year = fact1_by_year.idxmax()
peak_fact1_val = fact1_by_year.max()
ax.annotate(f"Peak = {peak_fact1_val}",
            xy=(peak_fact1_year, peak_fact1_val),
            xytext=(-60, 10),
            textcoords="offset points",
            ha='center',
            color='blue',
            arrowprops=dict(arrowstyle="->", color='blue'))

peak_fact2_year = fact2_by_year.idxmax()
peak_fact2_value = fact2_by_year.max()
ax2.annotate(f"Peak = {peak_fact2_value}",
             xy=(peak_fact2_year, peak_fact2_value),
             xytext=(60, 10),
             textcoords="offset points",
             ha='center',
             color='red',
             arrowprops=dict(arrowstyle="->", color='red'))

ax.set_ylim(bottom=0)

plt.show()