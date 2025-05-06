from PyPDF2 import PdfReader
import polars as pl
from typing import List
from datetime import date

def page_parser(page_str: str) -> List[str | int | float]:
    #NOTE: Tohle smaže jakej to je den v týdnu
    print(page_str)
    prepage = page_str.split(" ")[1:3]
    cash = float(prepage[1].replace(",", "."))
    dated, amount = (prepage[0][:10], int(prepage[0][10:]))
    date_pre = dated.split(".")
    dated = date(int(date_pre[2]), int(date_pre[1]), int(date_pre[0]))
    return [dated, amount, cash]

def rip_pdf():
    print("Beru soubor do2504.pdf")
    end_file = input("Zadejte název souboru s výstupem: ")
    reader = PdfReader("do2504.pdf")
    pages_text = [page.extract_text() for page in reader.pages]
    print(pages_text)

    test_data = []
    for page in pages_text:
        test_data += page.split('\n')[2:-1]

    test_data = test_data[:-1]
    print(test_data)
    test_header = ["Datum", "Celkový počet", "Tržba"]
    test_data = [page_parser(page) for page in test_data]
    'st 01.01.2025206 16865,00 Kč 20,60'
    print(test_data)
    #test_columns = [pl.Series(name=test_header[i])]
    #print(test_page)
    dates = pl.Series(test_header[0], [page[0] for page in test_data], dtype=pl.Date)
    amounts = pl.Series(test_header[1], [page[1] for page in test_data], dtype=pl.Int64)
    cash = pl.Series(test_header[2], [page[2] for page in test_data], dtype=pl.Float32)

    db = pl.DataFrame([dates, amounts, cash])

    cor_dates = pl.DataFrame(pl.date_range(test_data[0][0], test_data[-1][0], "1d", eager=True).alias("Datum"))

    db = db.join(cor_dates, how="full", on="Datum").drop("Datum").rename({"Datum_right":"Datum"}).select(test_header)
    print(cor_dates)
    print(db.head())

    db.write_csv(f"{end_file}.csv")



if __name__ == "__main__":
    rip_pdf()

