# Functions ---------------------
def db_conect(ip_host,user_name,pwd_data,db_name):
    db_connect = {

    'host':ip_host,
    'user':user_name,
    'password':pwd_data,
    'dbname':db_name
}
    return db_connect


# Functions ---------------------
def validated_dbconnect(in_db_data):
    if not in_db_data:
        print("Error")
    else:
        consulta = in_db_data
        consulta.execute()
        consulta.close()
