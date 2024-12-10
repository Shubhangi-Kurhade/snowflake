import snowflake.connector

class SnowflakeConnector:
    def __init__(self,account,user,password,warehouse,database,schema,role):
        self.account=account
        self.user=user
        self.password=password
        self.warehouse=warehouse
        self.database=database
        self.schema=schema
        self.role=role

    def connect(self):

        self.connection = snowflake.connector.connect(

            user=self.user,
            password=self.password,
            account=self.account,
            warehouse=self.warehouse,
            database=self.database,
            schema=self.schema
        )
        self.cursor=self.connection.cursor()

##execute query
    def execute_query(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def close_connection(self):
        self.cursor.close()
        self.connection.close()

account = "LPHIFGW-KY51552"
user = "SHUBHANGI"
password = "Shub@4308"
database="SNOWFLAKE_SAMPLE_DATA"
schema="TPCH_SF1"
role="ACCOUNTADMIN"
warehouse="COMPUTE"

sf_connector = SnowflakeConnector(
    account=account,
    user=user,
    password=password,
    warehouse=warehouse,
    database=database,
    schema=schema,
    role=role
) 
sf_connector.connect() 

query="select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.SUPPLIER LIMIT 10"

result=sf_connector.execute_query(query)
print(result)

sf_connector.close_connection()