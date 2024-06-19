import pymysql

db_host = 'instance-cym.c3c8246s0kxx.us-east-1.rds.amazonaws.com' 
db_user = 'ingrid'
db_password = 'AWS-CYM21'
db_database = 'db_cym'
db_table = 'users'

def connectionSQL():
    try:
        connection_sql = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_database
        )
        print("Successful connection database")
        return connection_sql
    except Exception as err: 
        print("Error conectando a la base de datos")
        print(err)
        return None
        
def add_user(id, name, lastname, birthday):
    instruction_sql = "INSERT INTO" + " " + db_table + " (id, name, lastname, birthday) VALUES ("+id+", '"+name+"', '"+lastname+"', '"+birthday+"') "
    print(instruction_sql)
    connection_sql = connectionSQL()
    try:
        if connection_sql != None:
            cursor = connection_sql.cursor()
            cursor.execute(instruction_sql)
            connection_sql.commit()
            print("Usuario agregado")
            return True
        else:
            print("Error conectando a la BD")
            return False
    except Exception as err:
        print("Error creando el usuario")
        print(err)
        return False