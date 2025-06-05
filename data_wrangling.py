import pandas as pd
import json

# Load the dataset
df = pd.read_csv('dataset.csv')

df['product_price'] = df['product_price'].replace({'₹': ''}, regex=True).astype(float)

df['side_effects_type'] = df['side_effects'].apply(lambda x: [{'side_effect': effect} for effect in x.split(',')])ùùupdated_side_effects = [{'side_effect': [item['side_effect'] for item in row]} for row in df['side_effects_type']]

# Replace the 'side_effects_type' column with the updated values
df['side_effects_type'] = updated_side_effects

# Function to replace dictionary values with list values
def replace_with_list(row):
    return row['side_effects_type']['side_effect']

# Apply the function to the DataFrame column
df['side_effects_type'] = df.apply(replace_with_list, axis=1)


# Converting the lists to EJSON format
df['side_effects_type'] = df['side_effects_type'].apply(lambda x: json.dumps(x))

# Extracting text within parentheses and creating a new column
df['salt_composition_dose'] = df['salt_composition'].str.extract(r'\((.*?)\)')

# Removing the extracted content from the 'salt_composition' column
df['salt_composition'] = df['salt_composition'].str.replace(r'\(.*?\)', '').str.strip()

# Function to process each row in the column
def transform_row(row):
    # Split the row based on '+'
    elements = [elem.strip() for elem in row.split('+')]
    return {"composition": elements}

# Apply the transformation to each row in the column
df['salt_composition'] = df['salt_composition'].apply(transform_row)


def modify_salt_composition(row):
    composition = row['salt_composition']['composition']
    dose = row['salt_composition_dose']
    row['salt_composition'] = {'composition': composition, 'dose': dose}
    return row

# Apply the function to the DataFrame
df = df.apply(modify_salt_composition, axis=1)

df['salt_composition'] = df['salt_composition'].apply(lambda x: json.dumps(x)) 

def process_interaction(interaction_string):
    interaction_data = json.loads(interaction_string)

    interactions = []
    min_length = min(len(interaction_data['drug']), len(interaction_data['brand']), len(interaction_data['effect']))

    for i in range(min_length):
        interaction = {
            'drug': interaction_data['drug'][i],
            'brand': interaction_data['brand'][i],
            'effect': interaction_data['effect'][i]
        }
        interactions.append(interaction)

    if len(interaction_data['drug']) != len(interaction_data['brand']) or len(interaction_data['drug']) != len(interaction_data['effect']):
        diff1 = len(interaction_data['drug']) - min_length
        diff2 = len(interaction_data['brand']) - min_length
        diff3 = len(interaction_data['effect']) - min_length

        for i in range(abs(diff1)):
            interactions.append({
                'drug': interaction_data['drug'][min_length + i] if diff1 > 0 else 'nan',
                'brand': interaction_data['brand'][min_length + i] if diff2 > 0 else 'nan',
                'effect': interaction_data['effect'][min_length + i] if diff3 > 0 else 'nan'
            })

    return {"interactions": interactions}

# Function to transform 'brand' column into an array
def transform_brand(brand):
    # If brand contains commas, split by commas and return a list
    if ',' in brand:
        brand_list = [b.strip() for b in brand.split(',')]
        return brand_list
    else:
        return [brand]  # Return single value as a list

# Function to process 'drug_interactions' column
def process_drug_interactions(interactions):
    # Convert string representation to a dictionary
    interactions_dict = json.loads(interactions)

    # Transform 'brand' within 'interactions' into an array
    for interaction in interactions_dict['interactions']:
        interaction['brand'] = transform_brand(interaction['brand'])

    # Convert back to Extended JSON (EJSON) format
    return json.dumps(interactions_dict)

# Apply the transformation to the 'drug_interactions' column
df['drug_interactions'] = df['drug_interactions'].apply(process_drug_interactions)

