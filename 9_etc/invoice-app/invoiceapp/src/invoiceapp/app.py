import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from datetime import datetime

class InvoiceApp(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)

        job_label = toga.Label('Job', style=Pack(padding=(0, 5)))
        self.job_input = toga.TextInput(style=Pack(flex=1))

        contractor_label = toga.Label('Contractor', style=Pack(padding=(0, 5)))
        self.contractor_input = toga.Selection(items=('Contractor 1', 'Contractor 2', 'Contractor 3'), style=Pack(flex=1))

        date_label = toga.Label('Date', style=Pack(padding=(0, 5)))
        self.date_input = toga.DateTimeInput(value=datetime.now(), style=Pack(flex=1))

        self.add_btn = toga.Button('Add Job', on_press=self.add_job, style=Pack(padding=(5, 5)))

        formbox = toga.Box(children=[
            job_label,
            self.job_input,
            contractor_label,
            self.contractor_input,
            date_label,
            self.date_input,
            self.add_btn
        ], style=Pack(direction=COLUMN, padding=5))

        self.main_window.content = formbox
        self.main_window.show()

    def add_job(self, widget):
        # Here, you should add the code to store the inputs in a csv file.
        pass

def main():
    return InvoiceApp('InvoiceApp', 'org.pybee.invoiceapp')

if __name__ == '__main__':
    main().main_loop()

