def convert_to_words(num):
    # Function to convert a numeric value to words

    if num == 0:
        return "zero"

    # Define lists for the numbers written out
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    words = ""

    # Convert tens place for numbers 10-19
    if num >= 10 and num <= 19:
        words += teens[num - 10] + " "
        num = 0
    # Convert tens place for numbers 20 and above
    elif num >= 20:
        words += tens[num // 10] + " "
        num %= 10

    # Convert ones place for numbers 1-9
    if num >= 1 and num <= 9:
        words += ones[num] + " "

    return words.strip()

def replace_numbers_with_text(input_string):
    # Function to replace numeric values in a string with their word equivalents

    words_split = input_string.split()  # Split the input string into a list of words
    result_words = []

    for word in words_split:
        if word.isdigit():  # Check if the word is a numeric value
            numeric_value = int(word)
            converted_result = convert_to_words(numeric_value)  # Convert the numeric value to words
            result_words.append(converted_result)
        else:
            result_words.append(word)

    result_string = ' '.join(result_words)  # Join the words back into a string
    return result_string

# Get input from the user
input_string = input("Enter a string: ")

# Replace numbers with text
output_string = replace_numbers_with_text(input_string)

# Print the output string
print("Output string:", output_string)
