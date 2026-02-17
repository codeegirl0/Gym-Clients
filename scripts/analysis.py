import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('./data/clients_with_coaches.csv')

##### UNIVARIATE ANALYSIS #####
# Count clients per city
data = df['City'].value_counts()
names = data.index
values = data.values

# Set the Seaborn color palette
colors = sns.color_palette('pastel')[0:len(names)]

# Create the Pie Chart
plt.pie(values, labels=names, autopct='%1.1f%%', startangle=90, colors=colors, pctdistance=0.85)

# Draw a Circle in the middle
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Ensure that pie is drawn as a circle.
plt.axis('equal')  
plt.title('Distribution of Client City')
plt.text(0, 0, f'Total\n{sum(data)} Clients', ha='center', va='center', fontsize=14, fontweight='bold')
plt.savefig('./images/clients_by_city_chart.png', dpi=300, bbox_inches='tight')
plt.close()



##### BIVARIATE ANALYSIS ######

# ---- Quantitative  VS Quantitative Variable ---
# Create a regression plot
sns.regplot(data=df, x='Distance_km', y='Sessions_Month', 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Correlation: Distance vs Sessions per Month')
plt.xlabel('Distance from Gym (km)')
plt.ylabel('Monthly Sessions')
plt.savefig('./images/distance_vs_sessions_chart.png', dpi=300, bbox_inches='tight')
plt.close()


# ---- Quantitative VS Qualitative Variable ---
# Create the bar plot
sns.barplot(data=df, x='Level', y='Sessions_Month', hue='Level' , palette='viridis', legend=False , errorbar=None)

# Add labels and title
plt.title('Average Monthly Sessions by Client Level', fontsize=15)
plt.xlabel('Client Level', fontsize=12)
plt.ylabel('Average Sessions per Month', fontsize=12)

# Save chart
plt.savefig('./images/level_vs_sessions.png', bbox_inches='tight')
plt.close()



#------Qualitative VS Qualitative Variable -----#
# Reshape data for stacking
stacked_data = df.groupby(['Level', 'Gender']).size().unstack()

# Plot using Pandas 
stacked_data.plot(kind='bar', stacked=True, figsize=(10, 6), color=['#e74c3c' , '#3498db'])

# Format and add labels
plt.title('Client Levels Stacked by Gender', fontsize=15)
plt.xlabel('Level')
plt.ylabel('Number of Clients')
plt.legend(title='Gender')
plt.xticks(rotation=0) 

# Save chart
plt.savefig('./images/level_by_gender_chart.png', bbox_inches='tight')
plt.close()



##### MULTIVARIATE ANALYSIS #####

# Create Line Plot
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Sessions_Month', y='Satisfaction', hue='Level', marker='o')

# Format and add labels
plt.title('Impact of Sessions on Satisfaction by Client Level', fontsize=15)
plt.xlabel('Sessions per Month')
plt.ylabel('Satisfaction')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Client Level', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save chart
plt.savefig('./images/sessions_impact_curve.png')
plt.close()