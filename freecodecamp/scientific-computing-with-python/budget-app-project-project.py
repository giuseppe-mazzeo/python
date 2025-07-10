class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total_withdraw = 0

    def __str__(self):
        title = self.category.center(30,'*')
        list_items = ''
        total = f'Total: {self.get_balance()}'
        lenght_category = len(self.ledger) - 1
        
        for i, dic in enumerate(self.ledger):
            new_line = '\n' if i < lenght_category else ''
            list_items += f"{dic['description'][:23]:23}{dic['amount']:7.2f}{new_line}"

        result = [title, list_items, total]
        
        return '\n'.join(result)

    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False

        self.ledger.append({'amount': -amount, 'description': description})
        self.total_withdraw += amount
        return True

    def get_balance(self):
        budget = 0
        for dic in self.ledger:
            budget += dic['amount']
        return budget

    def transfer(self, amount, category):
        description = f'Transfer to {category.category}'
        if not self.withdraw(amount, description):
            return False

        description =  f'Transfer from {self.category}'
        category.deposit(amount, description)
        return True

    def check_funds(self, amount):
        return self.get_balance() >= amount





def create_spend_chart(categories):
    spend_by_category = {}
    percentage_spend_by_category = {}

    for category in categories:
        spend_by_category[category.category] = round(category.total_withdraw)

    total_spend = sum(x for x in spend_by_category.values())
    
    for key, value in spend_by_category.items():
        percentage_spend_by_category[key] = round((value / total_spend) * 100)

    chart = [[x] for x in range(100, -10, -10)]
    chart.append([])

    for i, x in enumerate(range(100, -1,-10)):
        for key, value in percentage_spend_by_category.items():
            if value >= x:
                chart[i].append('o')
            else:
                chart[i].append(' ')

            if not key in chart[-1]:
                chart[-1].append(key)
    
    line = 'Percentage spent by category\n'
    for row in chart:
        if not str(row[0]).isdigit():
            max_lenght = max(len(str(category)) for category in row)
            padded = [category.ljust(max_lenght) for category in row]

            count = max_lenght
            width = (len(row)*3) + 1
            line += '    ' + '-'*(width) + '\n'
            for letter in zip(*padded):
                line += '     ' + '  '.join(letter) + '  '
                if count > 1:
                    line += '\n'
                count -= 1
            break

        for i, col in enumerate(row):
            if i == 0:
                line += f'{col:>3}|'
                continue
            
            line += f' {col} '

        line += ' \n'

    return line.rstrip('\n')


food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')

food.deposit(900, 'deposit')
entertainment.deposit(900, 'deposit')
business.deposit(900, 'deposit')

food.withdraw(78)
entertainment.withdraw(22)
business.withdraw(8)


cu = create_spend_chart([food, entertainment, business])


for i in cu.split('\n'):
    print(i, '-')

