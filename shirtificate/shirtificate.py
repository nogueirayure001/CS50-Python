from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font('times', 'B', 40)
        self.cell(0, 30, 'CS50 Shirtificate', align='C')
        self.ln(60)

    def place_shirt(self, background_path):
        self.image(background_path, w=self.epw)

    def write_over_shirt(self, text):
        self.set_font('helvetica', 'B', 26)
        self.set_text_color(255, 255, 255)
        self.set_y(135)
        self.set_x(50)
        self.multi_cell(110, None, text, align='C')


def main():
    name = input('Name: ')
    shirt_text = f'{name} took CS50'

    make_shirt(shirt_text)


def make_shirt(text):
    pdf = PDF()
    pdf.add_page()
    pdf.place_shirt('shirtificate.png')
    pdf.write_over_shirt(text)
    pdf.output('shirtificate.pdf')


if __name__ == '__main__':
    main()
