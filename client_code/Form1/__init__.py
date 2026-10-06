from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

  @handle("button_1", "click")
  def button_1_click(self, **event_args):
    numero1 = float(self.text_box_1.text)
    numero2 = float(self.text_box_2.text)

    suma = numero1 + numero2

    self.label_4.text = f"La suma de {numero1} y {numero2} es {suma}."

