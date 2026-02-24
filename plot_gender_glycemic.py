import matplotlib.pyplot as plt
import numpy as np

# Data from the article
categories = ['Normal', 'Hyperglycemic', 'Severe']
male_pcts = [7.3, 80.7, 12.0]
female_pcts = [1.3, 60.0, 38.7]

x = np.arange(len(categories))  # the label locations
width = 0.35  # width of the bars

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Left panel: grouped bar chart ---
bars1 = ax1.bar(x - width/2, male_pcts, width, label='Male', color='steelblue')
bars2 = ax1.bar(x + width/2, female_pcts, width, label='Female', color='coral')

# Add some text for labels, title and custom x-axis tick labels
ax1.set_ylabel('Percentage (%)')
ax1.set_title('Glycemic Status by Gender', fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(categories)
ax1.legend()

# Add value labels on top of bars
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height}%',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9)
for bar in bars2:
    height = bar.get_height()
    ax1.annotate(f'{height}%',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=9)

# --- Right panel: gender balance pie chart ---
labels = ['Male', 'Female']
sizes = [50, 50]
colors = ['steelblue', 'coral']
explode = (0.05, 0.05)  # slightly explode both slices

ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.0f%%', startangle=90, shadow=True)
ax2.set_title('Gender Distribution', fontweight='bold')
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Overall figure title and layout
plt.suptitle('Figure 3: Gender-Based Blood Glucose Distribution', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
