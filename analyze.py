# Open the file in read mode 
text = open("responses.txt", "r") 
  
# Create an empty dictionary 
d = dict() 
  
# Loop through each line of the file 
for line in text:
    # Remove the leading spaces and newline character 
    line = line.strip() 
  
    # Convert the characters in line to  
    # lowercase to avoid case mismatch 
    line = line.lower() 
  
    # Split the line into words 
    words = line.split(" ") 
  
    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in d: 
            # Increment count of word by 1 
            d[word] = d[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            d[word] = 1
  
# Print the contents of dictionary
d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
d = {k:v for (k,v) in d.items() if len(k) > 3}
i = 0
for key in list(d.keys()): 
    if (i < 100):
        print(key, ":", d[key])
        i += 1