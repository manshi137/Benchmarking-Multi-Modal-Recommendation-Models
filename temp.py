# import csv
# import torch
# import numpy as np
import random


import csv


inputcsv = 'data/baby/u_id_mapping.csv'

# List to store the data
data_array = []
# headers = ["userID",  "itemID",  "rating",  "timestamp",   "x_label"]
# data_array.append(headers)

# Reading data from the CSV file
with open(inputcsv, mode='r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        # row.append(random.randint(0, 1000)%3)
        data_array.append(row)

# Display the data
# for row in data_array:
#     print(row)


outputcsv = 'data/ml100k/u_id_mapping.csv'

# Writing data to the CSV file
with open(outputcsv, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    for i in range(945):
        writer.writerow(data_array[i])

print(f'Data has been written to {outputcsv}.')


# file_path = 'items.csv'
# file = open(file_path, encoding="utf8")

# data_reader = csv.reader(file)
# data = [row for row in data_reader]

# id2name = {}
# moviedesc = []
# movie_names = []


# for i in range(1, len(data)):
#     movie_names.append(data[i][5])
#     # print({i-1}, {data[i][5]})

# for i in range(len(movie_names)):
#     movie_names[i] = movie_names[i].strip()
#     movie_names[i] = movie_names[i][:-6]
#     movie_names[i] = movie_names[i].strip()

# for i in range(len(movie_names)):
#     id2name[i] = str(i)+"_"+movie_names[i]
# print(id2name)


# file_path = 'items.csv'


# # with open(file_path, 'r') as file:
# #     data_reader = csv.reader(file)
# #     data = [row for row in data_reader]


# file = open(file_path, encoding="utf8")

# data_reader = csv.reader(file)
# data = [row for row in data_reader]


# ind1 = [5, 29, 30, 31, 32]
# # movie title-5, summary-28, cast-29, director-30, rating-31, runtime-32

# moviedesc = []
# movie_names = []



# # MAKING ITEM ID MAPPINGS
# for i in range(1, len(data)):
#     movie_names.append(data[i][5])
#     # print({i-1}, {data[i][5]})

# for i in range(len(movie_names)):
#     movie_names[i] = movie_names[i].strip()
#     movie_names[i] = movie_names[i][:-6]
#     movie_names[i] = movie_names[i].strip()
#     # tmp = re.sub(r'[\\/:"*?<>|]', '', movie_names[i])
#     # movie_names[i] = tmp

# print(movie_names)

# itemid = []
# for i in range(len(movie_names)):
#     name = movie_names[i]
#     name = name.strip()
#     itemid.append([name, i])

# csv_file = 'i_id_mapping.csv'

# # Writing data into the CSV file
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file, delimiter='\t')
#     writer.writerows(itemid)

# ADDING X_LABEL COLUMN IN U.DATA -> ML100K.INTER


# Data to be added in the new column
# x_label = []
# for i in range(100000):
#     x_label.append(random.randint(0, 1000)%3)
 
# input_file = "u.csv"
# output_file = "ml100kinter.csv"

# # Data to be added in the new column
# # new_column_data = ['new_value1', 'new_value2', 'new_value3']  # Replace these with your desired values

# # Read the existing CSV file and add the new column
# with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
#     reader = csv.reader(infile, delimiter='\t')
#     writer = csv.writer(outfile, delimiter='\t')
    
#     # Iterate through the rows and add the new column
#     for row, new_value in zip(reader, x_label):
#         row.append(new_value)
#         writer.writerow(row)