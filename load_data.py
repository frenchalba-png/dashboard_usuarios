import pandas as pd
import sqlite3

# Archivos de entrada
JSON_FILE = "personas_data.json"  
CSV_FILE = "personas_data.csv"    
DB_FILE = "empresa.db"
TABLE_NAME = "usuarios"

# Leer JSON
df = pd.read_json(JSON_FILE)

# Conexión a SQLite
conn = sqlite3.connect(DB_FILE)

# Guardar DataFrame en la tabla "usuarios"
df.to_sql(TABLE_NAME, conn, if_exists="replace", index=False)

print(f"Datos cargados en {DB_FILE} en la tabla {TABLE_NAME}. Total registros:", len(df))
conn.close()
