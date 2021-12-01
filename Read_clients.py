client_file = open("clients.txt", 'r')

clientNo = 1

for client in client_file:
    print(clientNo, ", ", client.rstrip('\n'), sep='')
    clientNo += 1
