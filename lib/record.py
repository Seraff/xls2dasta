from datetime import datetime

class Record():
  SEXES = [{'excel': ['M', 'Muž'], 'dasta': 'M'},
           {'excel': ['Ž', 'F', 'Žena'], 'dasta': 'F'}]

  @staticmethod
  def parse_date(date):
    if type(date) != datetime:
      return datetime.fromisoformat(date)

    return date


  @staticmethod
  def is_value_empty(val):
    if type(val) == str and val.strip() == '':
      return True

    return val == None or val == False


  def __init__(self, xls_dict):
    self.errors = []

    self.xls_dict = xls_dict
    self.fields = ("personal_number",
                   "first_name",
                   "last_name",
                   "birth_date",
                   "sex",
                   "invoice_number",
                   "test_date",
                   "exam_date",
                   "result_date",
                   "pango",
                   "variant")

    self.personal_number = xls_dict['Rodné číslo']
    self.first_name = xls_dict['Jméno']
    self.last_name = xls_dict['Příjmení']
    self.birth_date = Record.parse_date(xls_dict['Datum narození'])
    self.sex = xls_dict['Pohlaví']

    # convert sex to dasta format value
    for sex in Record.SEXES:
      if self.sex in sex['excel']:
        self.sex = sex['dasta']

    self.invoice_number = xls_dict['Číslo žádanky']

    self.test_date = Record.parse_date(xls_dict['Datum odběru'])
    self.exam_date = Record.parse_date(xls_dict['Datum vyšetření'])
    self.result_date = Record.parse_date(xls_dict['Datum výsledku'])

    self.pango = xls_dict['Pango linie']
    self.variant = xls_dict['Varianta dle číselníku']
    self.note = xls_dict['Accession number (GISAID)']

    # removing space symbols around all the values
    for fld in self.fields:
      val = getattr(self, fld)

      if type(val) == str:
        setattr(self, fld, val.strip())

  def __str__(self):
    data = [f'{k}: "{v}"' for k, v in self.xls_dict.items()]
    return f'[{ ", ".join(data) }]'


  def validate(self):
    for fld in self.fields:
      val = getattr(self, fld)

      if Record.is_value_empty(val):
        self.errors.append(f'the field {fld} is empty')

    if self.sex not in ('Muž', 'Žena'):
      self.errors.append(f'the field "sex" can only have values M or Ž')


  def is_valid(self):
    return len(self.errors) == 0


  def print_errors(self):
    if self.is_valid():
      return False

    errors = ', '.join(self.errors)
    errors += '.'

    print(f"The record {str(self)} has problems: {errors}")

  






