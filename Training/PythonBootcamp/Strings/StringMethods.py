language = '$Python$$'
message = 'I love Python!'

# YOUR CODE STARTS HERE:
language1 = language.strip('$')  # remove all leading and trailing $ signs
language2 = language1.lower()  # lowercase version of language1 variable
message1 = message.upper()  # uppercase version of message variable
# replace Python with Java
message2 = message.replace('Python', 'Java')
