import datetime
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class InvoiceApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title='Invoice App')

        # Create the date input widget
        date = toga.DatePicker()

        # Create the day view label
        self.day_view_label = toga.Label('No date selected')
        self.day_view_label.style.update(padding=20)

        # Create the add button
        self.add_button = toga.Button('Add', on_press=self.on_add_button_press)

        # Create the main box container
        main_box = toga.Box(style=Pack(direction=COLUMN))

        # Create the top row with the date input and add button
        top_row = toga.Box(style=Pack(direction=ROW, padding=10))
        top_row.add(self.date_input)
        top_row.add(self.add_button)

        # Create the bottom row with the day view
        bottom_row = toga.Box(style=Pack(direction=ROW, padding=10))
        bottom_row.add(self.day_view_label)

        # Add the rows to the main box
        main_box.add(top_row)
        main_box.add(bottom_row)

        # Set the main box as the content of the main window
        self.main_window.content = main_box

        # Show the main window
        self.main_window.show()

    def on_add_button_press(self, widget):
        date = self.date_input.value
        self.day_view_label.text = f'Selected date: {date}'

    def calculate_days_between(self, start_date, end_date):
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        return (end_date - start_date).days


def main():
    app = InvoiceApp('Invoice App', 'com.example.invoiceapp')
    return app


if __name__ == '__main__':
    main().main_loop()
