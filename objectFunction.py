def extractObject(inputLIST):
    """
    Extracts the object from a Japanese sentence based on the specified markers.
    
    Args:
        inputLIST (list): A list of words in the sentence.
    
    Returns:
        str: The extracted object.
    """
    # Find the index of the word "が" (before the object)
    ga_index = -1
    if "が" in inputLIST:
        ga_index = inputLIST.index("が")
    
    # Find the index of the word "を" (after the object)
    wo_index = -1
    if "を" in inputLIST:
        wo_index = inputLIST.index("を")
    
    if ga_index != -1 and wo_index != -1:  # Both markers found
        # Extract the object between "が" and "を"
        extracted_object = "".join(inputLIST[ga_index + 1 : wo_index])
        return extracted_object
    else:
        return None  # "が" or "を" not found, return None

# Example usage
input_sentence = input("Sentence:")
input_words = input_sentence.split(" ")
extracted_object = extractObject(input_words)

if extracted_object is not None:
    print("Object:", extracted_object)
else:
    print("Nah")
