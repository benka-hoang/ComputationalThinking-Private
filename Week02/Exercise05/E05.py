number_of_members = 0
amount_of_outgoing_traffic = 0

while True:
    try:
        command = input()
    except EOFError:
        break

    if not command:
        continue
    
    # Process command here
    if command[0] == '+':
        number_of_members += 1
    elif command[0] == '-':
        number_of_members -= 1
    else:
        amount_of_outgoing_traffic += (len(command) - command.find(':') - 1) * number_of_members


print(amount_of_outgoing_traffic)