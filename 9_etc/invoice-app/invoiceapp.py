import toga

class InvoiceApp(toga.App):
    def startup(self):
        # Create the main window
        main_box = toga.Box()
        main_box.style.flex_direction = 'column'
        
        add_contractor_button = toga.Button('Add Contractor', on_press=self.open_add_contractor_window)
        main_box.add(add_contractor_button)

        self.main_window = toga.MainWindow(title='Invoice App', size=(400, 200))
        self.main_window.content = main_box
        self.main_window.show()

    def open_add_contractor_window(self, widget):
        # Create the add contractor window
        add_contractor_box = toga.Box()
        add_contractor_box.style.flex_direction = 'column'

        contractor_input = toga.TextInput(placeholder='Enter Contractor Name')
        add_contractor_box.add(contractor_input)

        add_button = toga.Button('Add', on_press=self.add_contractor)
        add_contractor_box.add(add_button)

        add_contractor_window = toga.Window(title='Add Contractor', size=(300, 150))
        add_contractor_window.content = add_contractor_box
        add_contractor_window.show()

    def add_contractor(self, widget):
        contractor_name = widget.parent.children[0].value
        # Save the contractor to a CSV file or perform any other desired action
        print(f'Added contractor: {contractor_name}')

def main():
    app = InvoiceApp('com.example.invoiceapp', 'Invoice App')
    app.main_loop()

if __name__ == '__main__':
    main()
