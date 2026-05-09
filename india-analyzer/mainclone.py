import pandas as pd
import matplotlib.pyplot as plt
import zipfile

# creating dataset and setting it to display max columns
with zipfile.ZipFile("dataset.zip", "r") as z:
    with z.open("india-news-headlines.csv") as f:
        df = pd.read_csv(f)

"""
cleaning done
"""

# Taking user input
fact1 = input("Enter your 'base topic' to analyze: ").strip().lower()
fact2 = input("Enter your topic to 'analyze against': ").strip().lower()

# counting the occurrences of the word fact1 across the dataset
fact1_mask = df.headline_text.str.contains(fact1, case=True,
                                     na=None, regex=False)
""" 9299 headlines found """

# counting the occurrences of the word fact2 across the dataset
fact2_mask = df.headline_text.str.contains(fact2, case=True,
                                           na=None, regex=False)
""" 1008 headlines found """


# keeping track of years when fact1 was mentioned
""" using boolean indexing """
fact1_mask = df['headline_text'].str.contains(fact1, case=False, na=False)
fact1_df = df[fact1_mask]
fact1_df = fact1_df.copy() # gives a new dataframe
fact1_df['year'] = fact1_df.publish_date.astype(str).str[:4]
fact1_by_year = fact1_df['year'].value_counts().sort_index()

# keeping track of years when fact2 was mentioned
"""
using boolean indexing
"""
fact2_mask = df['headline_text'].str.contains(fact2, case=False, na=False)
fact2_df = df[fact2_mask]
fact2_df = fact2_df.copy() # gives a new dataframe
fact2_df['year'] = fact2_df['publish_date'].astype(str).str[:4]
fact2_by_year = fact2_df['year'].value_counts().sort_index()

# combine both the dataframes
df_combined = pd.concat([fact1_df, fact2_df], ignore_index=True)

# combined years
years = fact1_by_year.index.union(fact2_by_year.index)


# matplotlib plotting
fig, ax = plt.subplots(figsize=(13.66, 7.68))
manager = plt.get_current_fig_manager()
manager.full_screen_toggle() # manager sets res to fullscreen

# adding title and subtitle
ax.set_title("Headline frequency analysis across Indian news (2001–2023)",
             fontsize=9, color='black', pad=25)
fig.suptitle("Education v/s Employment", fontsize=14, fontweight='bold')

# axis creation and labelling
ax.plot(ed_by_year.index, ed_by_year.values,
        label="Education", marker='o', color='blue')
ax.set_ylabel("Education", color='blue')
ax.tick_params(axis='y', labelcolor='blue')

# adding secondary axis to plot employment
ax2 = ax.twinx()
ax2.plot(emp_df_year.index, emp_df_year.values,
         label="Employment", marker='o', color='red')
ax2.set_ylabel('Employment', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.yaxis.set_major_locator(plt.MultipleLocator(10))
# ax.plot(emp_df_year.index, emp_df_year.values, label="Employment", marker='o') # Previous employment plotting

# Legend
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc="upper right")

# adding grid
ax.grid(True, linestyle='-', which='major')
ax.tick_params(axis='both')

ax.yaxis.set_major_locator(plt.MultipleLocator(100)) # y grid lines every 100 px
ax.xaxis.set_major_locator(plt.MultipleLocator(1)) # x grid lines year

# adding peak annotations
# education peak
peak_ed_year = ed_by_year.idxmax()
peak_ed_val = ed_by_year.max()
ax.annotate(f"Peak = {peak_ed_val}",
            xy=(peak_ed_year, peak_ed_val),
            xytext=(-100, 0),
            textcoords="offset points",
            ha='center',
            color='blue',
            arrowprops=dict(arrowstyle="->", color='blue'))

# employment peak
peak_emp_year = emp_df_year.idxmax()
peak_emp_value = emp_df_year.max()
ax2.annotate(f"Peak = {peak_emp_value}",
             xy=(peak_emp_year, peak_emp_value),
             xytext=(150, 0),
             textcoords="offset points",
             ha='center',
             color='red',
             arrowprops=dict(arrowstyle="->", color='red'))
ax.set_ylim(bottom=0)

plt.show()