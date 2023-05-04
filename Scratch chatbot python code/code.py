#!python 3
#Python X Scratch
#A paring with Python and Scratch
import scratchattach as scratch3
print('IMPORTED')

session = scratch3.login("USERNAME", "PASSWORD")
conn = session.connect_cloud("PROJECT_ID")

client = scratch3.CloudRequests(conn)

@client.event
def on_request(request):
    print("Received request", request.name, request.requester, request.arguments, request.timestamp, request.id)

@client.event
def on_unknown_request(request):
    print("Received unknown request", request.name, request.requester, request.arguments, request.timestamp, request.id)

@client.event
def on_error(request, e):
    print("Request: ", request.name, request.requester, request.arguments, request.timestamp, request.id)
    print("Error that occured: ", e)

@client.event
def on_disabled_request(request):
    print("Received disabled request", request.name, request.requester, request.arguments, request.timestamp, request.id)


@client.request
def ping(): 
    print("Ping request received")
    return "pong" 

@client.request
def GET(): 
    return_data = []
    print("Get request received")

    with open('queue.txt', 'r') as f:
        output = f.read()
        
    return_data.append(output)
    return return_data
    print("Sent!")

@client.request
def add_to_txt(argument1):
    with open('queue.txt', 'a') as f:
        f.write('\n')
        f.write(argument1)
        print('added ' + argument1 + ' to queue')
        return 'added!'

@client.request
def question_limit(argument1, argument2):
    with open('limit.txt', 'w') as f:
        f.write(argument2)
        print(argument1 + ' has ' + argument2 + ' questions left')
    return 'added'

@client.request
def delete_user():
    with open('queue.txt', 'r') as f:
        lines = f.readlines()

    with open('queue.txt', 'w') as f:
        f.writelines(lines[1:])

    return 'deleted user'

@client.request
def get_limit():
    with open('limit.txt', 'r') as f:
        line = f.readlines()

    return line


@client.request
def bot(argument1, argument2):

    with open('log.txt', 'a') as f:
        f.write('\n')
        f.write(argument1)
        f.write('\n')
        f.write('said:')
        f.write('\n')
        f.write(argument2)
        f.write('\n')
    
    return ('added to log')

    
@client.event
def on_ready():
    print("Request handler is running")

client.run(thread=True)
client.get_timestamp()
client.get_requester()
