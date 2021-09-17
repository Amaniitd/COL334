First run the server.py file
python server.py
it will run on localhost

Run client.py
python client.py
it will ask for server's ip address
Enter localhost
It will show error if it fails to connect to server

    it will ask your user name

    Username Format:
        Only alphanumeric characters are allowed
        Username "ALL" is not allowed

    It will show error if username is malformed or already taken

Format of sending messages to [Username]
@[Username] [message]
Format of sending messages to ALL (broadcasting)
@ALL [message]
It will show error if message fails to deliver.
