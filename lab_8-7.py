def print_possessive_names(rows):
    for row in rows:
        first_name = row[0]
        last_name = row[1]

        # Determine whether to add 's or just an apostrophe based on the last character of the last name
        possessive_suffix = "'" if last_name[-1] == 's' else "'s"

        # Print the possessive name
        print(f"{first_name}'{possessive_suffix}")

# Example nested list rows from the "Nested Data" slide
nested_data = [
    ["Liam", "O'Hara"],
    ["Matt", "Corn"],
    ["Caleb", "Jones"],
    ["Boris", "Johnson"]
]

# Call the function with the provided nested list
print_possessive_names(nested_data)
