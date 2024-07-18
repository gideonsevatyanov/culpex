import re

# Define the regex pattern
regex_pattern = re.compile(r"\D(\d{4})\D")

# Search for matching numbers in a string
matching_numbers = re.findall(regex_pattern, some_string)
print(matching_numbers)
