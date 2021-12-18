

# 
# Introduction
# 
This is a simple GFS GraphQL integration example.
The GFSGQL class in gfsgql.py forms a fairly complete GraphQL client into GFS.


# 
# Sample code
# 
from gfsgql import GFSGQL

gfs_host = "localhost"
gfs_port = "5000"
gfs_username = None
gfs_password = None

gqlClient = GFSGQL(
    gfs_host = gfs_host,
    gfs_port = gfs_port,
    gfs_username = gfs_username,
    gfs_password = gfs_password,
)

gqlClient.gqlexec(
    """
        mutation updateIp($id:String!, $name:String, $address:String, ) {
            updateIp(id:$id, name:$name, address:$address, ) {
                instance {
                    id, name, address,
                },
                ok
            }
        }
    """,
    {
        "id": "5202",
        "name": "myname",
        "address": "myaddress"
    }
)


# 
# How to use
# 

# Set up virtualenv and install
> pipenv shell
> pip install -r ./requirements.txt

# Run
> python example.py 
DEBUG:GFSGQL:Running GQL query: 
DEBUG:GFSGQL:
            mutation updateIp($id:String!, $name:String, $address:String, ) {
                updateIp(id:$id, name:$name, address:$address, ) {
                    instance {
                        id, name, address,
                    },
                    ok
                }
            }
        
DEBUG:GFSGQL:with variables: 
DEBUG:GFSGQL:{'id': '5202', 'name': 'myname', 'address': 'myaddress'}
DEBUG:urllib3.connectionpool:Starting new HTTP connection (1): localhost:5000
DEBUG:urllib3.connectionpool:http://localhost:5000 "POST /gfs1/graphql HTTP/1.1" 200 168
DEBUG:GFSGQL:GQL query result
DEBUG:GFSGQL:{'data': {'updateIp': {'instance': {'id': '5202', 'name': 'myname', 'address': 'myaddress'}, 'ok': True}}}
