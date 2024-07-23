def guess_original_number():
    # Step 1: Prompt the user to imagine a number (we'll use a placeholder here as we can't read the user's mind)
    print("Imagine a number in your mind.")
    
    # Step 2: Add 5 to the imagined number
    print("Add 5 to your imagined number.")
    
    # Step 3: Add 10 to the result
    print("Now add 10 to the result.")
    
    # Step 4: Multiply the result by 2
    print("Now multiply the result by 2.")
    
    # Step 5: Ask the user for the final result
    final_result = int(input("Enter the final result: "))
    
    # Step 6: Calculate the original number
    original_number = (final_result - 30) / 2
    
    # Step 7: Print the original number
    print(f"The  number  you imagined at first was: ,{original_number}")

    


# Call the function
guess_original_number()