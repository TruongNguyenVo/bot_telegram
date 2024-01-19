import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)



# File path of the CSV file
file_path = "questions_n5_vocabulary.csv"  # Replace with the actual file path

df = pd.read_csv(file_path)


# Display the contents of the DataFrame
print(df['Question'])
# import pandas as pd
# import csv
# # Create a DataFrame with quoted values containing comma
# data = {'Field1': ['Value1', 'Value2'],
#         'Field2': ['Value, with comma', 'Another value'],
#         'Field3': ['Value3', 'Value, with comma']}
# df = pd.DataFrame(data)

# # Save the DataFrame to a CSV file with quotes
# df.to_csv('test.csv', index=False, quoting=csv.QUOTE_ALL)