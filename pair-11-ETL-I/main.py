#%%
import pandas as pd
from src import support as sp

# %%
dataframes = sp.abrir_archivos()

# %%
df_ventas = dataframes[0] 
df_clientes = dataframes[1]
df_productos = dataframes[2]