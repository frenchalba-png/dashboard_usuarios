import pandas as pd
from sqlalchemy import create_engine

DB_FILE = "empresa.db"
TABLE = "usuarios"

engine = create_engine(f"sqlite:///{DB_FILE}")
df = pd.read_sql_table(TABLE, engine)

# 1) quitar "8-" al inicio
df['cedula'] = df['cedula'].astype(str).str.replace(r'^8-', '', regex=True)

# 2) quitar todos los '7'
df['cedula'] = df['cedula'].str.replace('7', '', regex=False)

# Guardar cambios de vuelta a SQL
df.to_sql(TABLE, engine, if_exists='replace', index=False)

print("Limpieza completa. Ejemplo:")
print(df[['nombre','apellido','cedula']].head())
