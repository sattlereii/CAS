import re
from datetime import datetime, timedelta
from PyPDF2 import PdfReader

reader = PdfReader("cely rok.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()

pattern = re.compile(r"(po|út|st|čt|pá|so|ne)\s+(\d{2}\.\d{2}\.2023)(\d+)\s+([\d\s]*\d,\d{2})\s*Kč")

zaznamy = {}

for match in pattern.finditer(text):
    datum = match.group(2)
    trzba_raw = match.group(4).replace(" ", "").replace("\xa0", "")
    trzba_float = float(trzba_raw.replace(",", "."))
    zaznamy[datum] = trzba_float

start_date = datetime.strptime("01.07.2023", "%d.%m.%Y")
end_date = datetime.strptime("31.12.2023", "%d.%m.%Y")

current_date = start_date
vystup = []

while current_date <= end_date:
    datum_str = current_date.strftime("%d.%m.%Y")
    if datum_str in zaznamy:
        vystup.append(zaznamy[datum_str])
    else:
        vystup.append(0.0)
    current_date += timedelta(days=1)

# Výpis: čísla s čárkou místo tečky
for t in vystup:
    print(f"{t:,.2f}".replace(",", "X").replace(".", ",").replace("X", ""))
