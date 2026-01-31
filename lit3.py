
f=open("C:\\Users\\Admin\\Desktop\\pyhton class\\lit3.txt","a")

# 1. Ask the user for a list of names separated by commas
user_input = input("Enter a list of names (separated by commas): ")

# 2. Convert the string into a list and remove extra spaces
# .split(",") breaks the string at every comma
# .strip() removes whitespace around each name
names_list = [name.strip() for name in user_input.split(",")]

# 3. Count the total number of names entered (including duplicates)
total_count = len(names_list)

# 4. Remove duplicates by converting the list to a 'set'
# Sets automatically delete duplicate values
unique_names = set(names_list)

# 5. Sort the names alphabetically
# sorted() returns a new, organized list
final_list = sorted(unique_names)

# 6. Display the results
print(names_list, file=f)
print("\n--- Results ---")
print(f"Total names entered: {total_count}", file=f)
print(f"Sorted list (no duplicates): {final_list}", file=f)