import pandas as pd

df_clients = pd.read_csv("./data/clients_data_cleaned.csv")

# Create Coach table
coaches = {
	'Level' : ['Beginner' , 'Intermediate' , 'Expert'],
	'Coach_Name' : [ 'Camellia' , 'Lora' , 'Charlie']
}

df_coaches = pd.DataFrame(coaches) 

# Join tables and save it 
df_joined = pd.merge(df_clients , df_coaches , on='Level' , how='left')
df_joined.to_csv('./data/clients_with_coaches.csv' , index=False)