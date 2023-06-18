from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import csv


class AddContractorPopup(Popup):
    def __init__(self, add_contractor_callback, **kwargs):
        super(AddContractorPopup, self).__init__(**kwargs)
        self.add_contractor_callback = add_contractor_callback

        layout = BoxLayout(orientation='vertical', spacing=10)

        contractor_input = TextInput(hint_text='Enter Contractor')
        layout.add_widget(contractor_input)

        add_button = Button(text='Add Contractor')
        add_button.bind(on_release=lambda instance: self.add_contractor(contractor_input.text))
        layout.add_widget(add_button)

        self.content = layout

    def add_contractor(self, contractor_name):
        self.add_contractor_callback(contractor_name)
        self.dismiss()


class WorkEntryApp(App):
    def build(self):
        contractors = []

        def add_work_entry(instance):
            add_contractor_popup = AddContractorPopup(add_contractor)
            add_contractor_popup.open()

        def add_contractor(contractor_name):
            contractors.append(contractor_name)
            with open('contractors.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([contractor_name])
            print(f"Contractor '{contractor_name}' added!")

        def generate_invoice(instance):
            # Add your logic to generate an invoice here
            print("Invoice generated!")

        # Create the layout
        layout = BoxLayout(orientation='vertical')

        # Create and add the add work entry button
        add_work_entry_button = Button(text='Add Work Entry')
        add_work_entry_button.bind(on_release=add_work_entry)
        layout.add_widget(add_work_entry_button)

        # Create and add the generate invoice button
        generate_invoice_button = Button(text='Generate Invoice')
        generate_invoice_button.bind(on_release=generate_invoice)
        layout.add_widget(generate_invoice_button)

        return layout


if __name__ == '__main__':
    WorkEntryApp().run()
