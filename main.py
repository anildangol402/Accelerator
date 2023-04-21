from add_to_snowflake import add_new_connectors_and_map
import snowflake.connector
#from meltano import get_connectors

####################################################################################################################
# Instructions:
# 1) Add new python file with the name of the integration service and add the function get_connectors() to that file
# 3) import the function like so: from file_name import get_connectors
# 4) Make sure you fill out your credentials below

# Set up connection parameters 
account = 'strivepartner.east-us-2.azure'
user = 'YOUR_USERNAME'
password = 'YOUR_PASSWORD'
database = 'ACCELERATOR'
schema = 'PUBLIC'
warehouse = 'adf_demo_wh'
role = 'sysadmin'

# Create connection object 
conn = snowflake.connector.connect(
    account=account,
    user=user,
    password=password,
    database=database,
    schema=schema,
    warehouse=warehouse,
    role=role
)

# 5) Fill out remaining code


connectors = [] #get_connectors() # replace [] with get_connectors()
intregrationid = #28 # replace integrationid with the intregationtoolid found in the snowflake table
add_new_connectors_and_map(connectors, intregrationid)