#%%
import pandas as pd

#%%
def abrir_archivos():
    """
    Esta funcion abre los archivos ventas.csv, clientes.csv y productos_corregidos.csv."""
    df_ventas = pd.read_csv("data/ventas.csv", index_col=0)
    df_clientes = pd.read_csv("data/clientes.csv", index_col=0)
    df_productos = pd.read_csv("data/productos_corregido.csv", sep=";", index_col=0)
    
    return df_ventas, df_clientes, df_productos     
# %%
