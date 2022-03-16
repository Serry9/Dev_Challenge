from tkinter import*
from tkinter import messagebox


		

aplicacion = Tk()
aplicacion.title("Ingreso de mercaderia")


"""miFrame = Frame(root, width="1200", height="600")
miFrame.pack()"""


miFrame = LabelFrame(aplicacion, text="Ingreso de mercaderia")
miFrame.config(bg="pink")
miFrame.grid(column=0, row=0, padx=10, pady=10)

miFrame2 = LabelFrame(aplicacion, text='Ingresos', width=250, height=100)
miFrame2.config(bg="green")
miFrame2.grid(column=0, row=1, padx=10, pady=10)

"""miarticulo=StringVar()
minombre=StringVar()
micolor=StringVar()"""




ingresaarticulo=Entry(miFrame, textvariable="miarticulo")
ingresaarticulo.grid(row="0", column="1", padx="10", pady="10" )

ingresanombre=Entry(miFrame,  textvariable="minombre")
ingresanombre.grid(row="1", column="1", padx="10", pady="10")

ingresacolor=Entry(miFrame, textvariable="micolor")
ingresacolor.grid(row="2", column="1", padx="10", pady="10")

articuloLabel= Label(miFrame,text="Articulo:")
articuloLabel.grid(row="0", column="0", sticky="e", padx="10", pady="10")

nombreLabel= Label(miFrame,text="Nombre:")
nombreLabel.grid(row="1", column="0", sticky="e", padx="10", pady="10")

colorLabel= Label(miFrame,text="Color:")
colorLabel.grid(row="2", column="0", sticky="e", padx="10", pady="10")


#---------------------------------botones---------------------------------------------------
botonAgregar=Button(miFrame, text="Cargar")
botonAgregar.grid(row="3", column="0", sticky="w", padx="5", pady="5"  )

botonEditar=Button(miFrame, text="Editar")
botonEditar.grid(row="3", column="1",  padx="5", pady="5"  )

botonEliminar=Button(miFrame, text="Eliminar")
botonEliminar.grid(row="3", column="2", sticky="e", padx="5", pady="5"  )
#--------------------------------------------------------------------------------------------------
import sqlite3


def crear_conexion(db_archivo):
    """ Crea conexión con la base de datos
        espeficiado por db_archivo
    :parametro db_archivo: nombre de archivo de DB
    :return: Objeto de conexión o None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_archivo)
        return conn
    except Exception as e:
        print(e)

    return conn
    
def query(conn, query, commit=False):
    """ ejecuta query de sql
    :parametro conn: Objeto de conexión
    :parametro query: query
    :return: Cursor o None
    """
    try:
        c = conn.cursor()
        c.execute(query)
        if commit == True:
            conn.commit()
        return c
    except Exception as e:
        print(e)

    return None
    
def inizializar_db():
    """ inicializa db
    :return: Objeto de conexión o None
    """
    db_senda = r"ventanaaplic.db"
    sql_create_articulo_table = """
        CREATE TABLE IF NOT EXISTS articulo (
            id integer NOT NULL,
            nombre varchar NOT NULL,
            color varchar NOT NULL,
            
            PRIMARY KEY (id)
        );
    """
    sql_create_nombre_table = """
        CREATE TABLE IF NOT EXISTS nombre (
            id integer NOT NULL,
            nombre varchar NOT NULL,
            color varchar NOT NULL,
            
            PRIMARY KEY (id)
        );
    """
    sql_create_color_table = """
        CREATE TABLE IF NOT EXISTS color (
            id integer NOT NULL,
            articulo_id   integer NOT NULL,
           nombre_id integer NOT NULL,
			
            PRIMARY KEY (id),
            FOREIGN KEY (articulo_id) REFERENCES articulo (id) ON DELETE CASCADE,
            FOREIGN KEY (nombre_id) REFERENCES nombre (id) ON DELETE CASCADE
        );
    """
    conn = crear_conexion(db_senda)
    if conn is not None:
        query(conn, sql_create_articulo_table)        
        query(conn, sql_create_nombre_table)
        query(conn, sql_create_color_table)
    else:
        print("Error! No se puede crear conexión de base de datos.")

    return conn
