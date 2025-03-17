secretMessage = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
    file.write(secretMessage)

with open('sent_message.txt', 'r+') as file: # r+ is used to indicate both reading and writing
    original_message = file.read()
    file.seek(0)

    unsent_message = 'This message has been unsent'

    file.truncate(len(unsent_message))

    file.write(unsent_message)

print("Original Message:", original_message)
print("Unsent Message:", unsent_message)    