import pandas
from fpdf import FPDF

df = pandas.read_csv('articles.csv')


class PrintPDF:
    def __init__(self,stock_id):
        self.stock_id = stock_id
    def print(self):
        pdf = FPDF(orientation = 'P', unit = "mm",format = "A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"{self.stock_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"{df.loc[df['id'] == self.stock_id, 'name'].squeeze()}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"{df.loc[df['id'] == self.stock_id, 'price'].squeeze()}", ln=1)

        df.loc[df['id'] == self.stock_id, 'in stock'] = '-1'
        df.to_csv('articles.csv',index=False)

        pdf.output("receipt.pdf")
        print(df)


stock_id=int(input('Enter the ID '))
print_instance = PrintPDF(stock_id)
print_instance.print()