PLACEHOLDER = "[name]"

# Print names with a new line
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Replace name and remove new line
with open("./Input/Letters/starting_letters.txt") as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

