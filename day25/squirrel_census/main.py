# Create a CSV file named squirrel_count that just has a small table. 
# The columns are fur color and count.
# There are only three fur colors: grey, red, and black
# The data for that can be found in the squirrel census data under the 'Primary Fur Color' column.
# Take the data, make a new DataFrame, and convert it into a csv file.


import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get the data from the column 'Primary Fur Color' and convert it to a list
fur_color_list = data["Primary Fur Color"].to_list()

# Count up how many times each fur count is in the list and store it in their own variables
gray_fur = fur_color_list.count("Gray")
red_fur = fur_color_list.count("Cinnamon")
black_fur = fur_color_list.count("Black")

# Create a dictionary of the data
squirrel_data_dict = {
    "color": ["Gray", "Red", "Black"],
    "count": [gray_fur, red_fur, black_fur]
}

# Convert the dictionary to a DataFrame
squirrel_DataFrame = pandas.DataFrame(squirrel_data_dict)

# Convert the DataFrame to a CSV file

squirrel_DataFrame.to_csv("squirrel_count.csv")
