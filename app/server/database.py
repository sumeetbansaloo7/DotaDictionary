from pymongo import MongoClient

conn = None


def get_client():
    if(conn == None):
        client = MongoClient(
            'mongodb+srv://<username>:<password>@<cluster>/myFirstDatabase?retryWrites=true&w=majority')
        print(client.server_info())
        return client
    else:
        print(conn.server_info())
        return conn
