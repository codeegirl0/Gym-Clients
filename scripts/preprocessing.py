import pandas as pd


# Read DF
df = pd.read_csv("./data/clients_data.csv")

#_____ DUPLICATED ROWS_____

# Drop duplicated rows based on everything except ID column
df_cleaned = df.drop_duplicates(subset=df.columns.difference(['ID'])).reset_index(drop=True)

# Recount IDs
df_cleaned['ID'] = range(1 , len(df_cleaned) + 1)


#_____EPMTY CELLS ______________

# Check empty cells for each column
empty_cell = df_cleaned.isnull().sum()
print(empty_cell)

# Fill epmty cells (Level Gender Children) with average values
mean_children_value = round(df_cleaned['Children'].mean())
df_cleaned['Children'] = df_cleaned['Children'].fillna(mean_children_value).astype(int)

most_gender = df['Gender'].mode()[0]
df_cleaned['Gender'] = df_cleaned['Gender'].fillna(most_gender)

most_level = df['Level'].mode()[0]
df_cleaned['Level'] = df_cleaned['Level'].fillna(most_level)

# Save data to new CSV file
df_cleaned.to_csv('./data/clients_data_cleaned.csv' , index=False)



# ________SPELLING ERRORS / ABBREVIATION  ____________

# Correct spelling errors / abbreviations  in City column
corrections = {
	'BX' : 'Bordeaux',
	'PAR' : 'Paris', 
	'NTE' : 'Nantes',
	'TLS' : 'Toulouse',
	'OM' : 'Marseille',
	'LYS' : 'Lyon',
	'LIL' : 'Lille'
}
df_cleaned['City'] =df_cleaned['City'].replace(corrections)



# _______ ABNORMAL VALUES _________

# Correct abnormal values (Children and Sessions_Month)
normal_children_mean = df_cleaned[df_cleaned['Children'] <= 10]['Children'].mean().round().astype(int)
df_cleaned.loc[df_cleaned['Children'] > 10, 'Children'] = normal_children_mean


normal_session_mean = df_cleaned[df_cleaned['Sessions_Month'] <= 25]['Sessions_Month'].mean().round().astype(int)
df_cleaned.loc[df_cleaned['Sessions_Month'] > 25, 'Sessions_Month'] = normal_session_mean

# Save data to CSV file
df_cleaned.to_csv('./data/clients_data_cleaned.csv' , index=False)
