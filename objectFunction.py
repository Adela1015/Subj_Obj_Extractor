def extractObject(input_sentence):
    """
    Extracts the object from a Japanese sentence based on the specified markers.
    
    Args:
        input_sentence (str): A Japanese sentence.
    
    Returns:
        str: The extracted object.
    """
    # Initialize variables to store the indices of "が" and "を"
    ga_index = -1
    wo_index = -1

    # Iterate through each character in the input sentence
    for i in range(len(input_sentence)):
        # Check if the character is "が"
        if input_sentence[i] == "が":
            ga_index = i
        # Check if the character is "を"
        elif input_sentence[i] == "を":
            wo_index = i
        elif input_sentence[i] == "に":
            wo_index = i
    
    # Check if both markers are found
    if ga_index != -1 and wo_index != -1 and ga_index < wo_index:
        # Extract the object between "が" and "を"
        extracted_object = input_sentence[ga_index + 1:wo_index]
        return extracted_object
    else:
        return None  # "が" or "を" not found or in incorrect order, return None

# Example usage
input_sentence = input("Sentence：")
extracted_object = extractObject(input_sentence)

if extracted_object is not None:
    print("Object：", extracted_object)
else:
    print("Nah")
