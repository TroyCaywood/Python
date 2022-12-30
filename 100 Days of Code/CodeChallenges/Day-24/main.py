#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Open invited_names.txt file in read mode
with open("./Input/Names/invited_names.txt", mode="r") as invited_names:
    # Set names variable to invited_names.readlines() to read each line in the file and add to names list
    names = invited_names.readlines()
    # For name in names list
    for name in names:
        # Open starting letter in read mode
        with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
            # Read letter and store in read_letter variable
            read_letter = starting_letter.read()
            # Replace [name] section in starting_letter with current name from name list and strip return after name
            replace_name = read_letter.replace("[name]", name.rstrip("\r\n"))
            # Open new letter in append mode using name variable
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="a+") as output_letter:
                # Write replacement name variable to new letter
                output_letter.write(replace_name)
