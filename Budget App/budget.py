class Category:

  def __init__(self, name):
    self.name = name
    self.funds = 0
    self.ledger = []

  def check_funds(self, amount):
    return False if amount > self.funds else True

  def get_balance(self):
    return self.funds

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})
    self.funds += amount

  def withdraw(self, amount, description=''):
    if self.check_funds(amount) == True:
      self.ledger.append({'amount': amount * -1, 'description': description})
      self.funds -= amount
      return True
    else:
      return False

  def transfer(self, amount, category):
    if self.check_funds(amount) == True:
      self.ledger.append({'amount': amount * -1, 'description': f'Transfer to {category.name}'})
      self.funds -= amount
      category.deposit(amount, f'Transfer from {self.name}')
      return True
    else:
      return False

  def __str__(self):
    title = self.name.center(30, '*') + '\n'
    content = ''
    total = f'Total: {self.funds:.2f}'

    for item in self.ledger:
      description = f"{item['description']:<23}"
      amount = f"{item['amount']:>7.2f}"
      content += f'{description[:23]}{amount[:7]}\n'

    return title + content + total

def create_spend_chart(categories):

  names_list = []
  withd_list = []

  for category in categories:
    names_list.append(category.name)

    withdraw_total = 0

    for item in category.ledger:
      amount = item['amount']
      if amount < 0: withdraw_total += amount
    withd_list.append(withdraw_total)

  total_spent = round(sum(withd_list))
  percentages = []

  for value in withd_list:
    per = value * 100 / total_spent
    per = round(per//10)*10
    percentages.append(per)

  chart = 'Percentage spent by category\n'

  for i in range(100, -1, -10):
    chart += f'{i:>3}|'
    for percent in percentages:
      if percent >= i:
        chart += ' o '
      else:
        chart += '   '
    chart += ' \n'

  chart += '    ' + ('-' * ((len(names_list)) * 3 + 1)) + '\n'

  height = len(max(names_list, key=len))
  padded = [word.ljust(height) for word in names_list]

  for i in range(height):
    new_line = '     '
    for j in range(len(names_list)):
      new_line += padded[j][i] + '  '
    chart += new_line + '\n'

  return chart.rstrip('\n')
