import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas as pd

st.title("big Query connction")
# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = bigquery.Client(credentials=credentials)
query="SELECT * FROM streamlit-473312.MVP2.produto LIMIT 1000"
query_0= "INSERT INTO streamlit-473312.MVP2.produto (produto_id, nome, categoria, preco, estoque) VALUES (1, 'Notebook', 'Eletrônicos', 5500.00, 10), (2, 'Teclado Mecânico', 'Acessórios', 450.50, 25), (3, 'Mouse', 'Acessórios', 120.99, 50);"
# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.



#rows = run_query("SELECT * FROM streamlit-473312.MVP2.produto LIMIT 1000")
#res= client.query(query_0)
res= client.query(query)
rows = [dict(row) for row in res.result()]

df=pd.DataFrame(rows)
st.dataframe(df)





