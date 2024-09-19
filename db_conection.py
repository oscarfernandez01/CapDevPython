from modulos.module_functions import db_conect
from modulos.module_functions import validated_dbconnect

validated_dbconnect(
                    in_db_data=db_conect(
                                ip_host='127.0.0.1',
                                user_name='root',
                                pwd_data='1234',
                                db_name='prueba_db'))


