import fitz  # PyMuPDF
import pandas as pd
import re
from datetime import datetime

# Načti PDF jako text
with fitz.open("data_MSUL/PaK/2023/.pdf") as doc:
    text = "\n".join(page.get_text() for page in doc)

# Najdi řádky s datem, počtem a cenou
lines = re.findall(r"(\\d{2}\\.\\d{2}\\.\\d{4}).*?(\\d+)\\s+([\\d\\s]+,\\d{2})\\s*Kč", text)

# Zpracuj do seznamu
data = []
for date_str, count, price_str in lines:
    date = datetime.strptime(date_str, "%d.%m.%Y")
    count = int(count)
    price = int(float(price_str.replace(" ", "").replace(",", ".")))
    data.append((date, count, price))

df = pd.DataFrame(data, columns=["Datum", "Pocet", "Cena"])

# Doplnění celého roku 2023
full_dates = pd.date_range("2023-01-01", "2023-12-31")
full_df = pd.DataFrame({"Datum": full_dates})
merged = full_df.merge(df, on="Datum", how="left").fillna(0)
merged[["Pocet", "Cena"]] = merged[["Pocet", "Cena"]].astype(int)

# Výpis ve formátu vhodném pro Excel (kopírování jako tabulka)
for _, row in merged.iterrows():
    print(f"{row['Pocet']}\\t{row['Cena']}")
