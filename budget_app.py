class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def __str__(self):
        line_chars = (30 - len(self.category)) // 2
        ledger_list = []
        for _ in self.ledger:
            if 'amount' in _:
                _amount = '%.2f' % round(_['amount'], 2)
            amount = str(_amount) if len(str(_amount)) <= 7 else str(_amount[:7])
            description = _['description'] if len(_['description']) <= 23 else _['description'][0:23]
            spaces = 30 - (len(str(amount)) + (len(description) if len(description) <= 23 else 23))
            lista = [description, ' '*spaces, amount]
            pack = ''.join(lista)
            ledger_list.append(pack)
        first=  '*'*(line_chars) + self.category + '*'*(line_chars) + "\n"
        second = '\n'.join(ledger_list)
        third = '\nTotal: ' +  str('%.2f' % round(self.get_balance(), 2))   
        display = ''.join(first + second + third)
        return display

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
         
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': - amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for _ in self.ledger:
            if 'amount' in _:
                balance += _['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        budget = 0
        for _ in self.ledger:
            if 'amount' in _:
                budget += _['amount']
            else:
                pass
        if amount > budget:
            return False
        else:
            return True



def create_spend_chart(categories):
    total_spent = 0
    total_per_category = 0
    dict_categories_percent = {}
    for category in categories:
        for _ in category.ledger:
            if _['amount'] < 0:
                total_spent += abs(_['amount'])
                total_per_category += abs(_['amount'])
            else:
                pass
        dict_categories_percent[category.category] = total_per_category
        total_per_category = 0
    
    _percents = {category:round((amount / total_spent)*100) for category, amount in dict_categories_percent.items()}

    string_dict = {n:[f'{n}', '|'] for n in range(0,110,10)}

    for percent in _percents.values():
        if percent == 0:
            string_dict[0].append(' o ')
            for _ in range(10,110,10):
                string_dict[_].append('   ')
        elif int(str(percent)[-1]) >= 5:
            for _ in range(0, percent + 10, 10):
                string_dict[_].append(' o ')
            for _ in range((10 - int(str(percent)[-1]) + percent + 10), 110, 10):
                string_dict[_].append('   ')
        elif int(str(percent)[-1]) < 5:
            if int(str(percent)[-1]) != 0:
                for _ in range(0, percent, 10):
                    string_dict[_].append(' o ')
                for _ in range(int(str(percent)[0])*10 + 10, 110, 10):
                    string_dict[_].append('   ')
            else:
                for _ in range(0, percent + 10, 10):
                    string_dict[_].append(' o ')
                for _ in range(percent + 10, 110, 10):
                    string_dict[_].append('   ')

    string_dict[0][0] = '  0'
    for key, val in string_dict.items():
        if int(key) == 0:
            string_dict[key][0] = '  0'
        elif int(key) < 100:
            string_dict[key][0] = f' {val[0]}'
         
    _string1 = []
    for _ in reversed(string_dict.values()):
        _string1.append((''.join(_)))

    string1 = 'Percentage spent by category\n' + ' \n'.join(_string1) + '\n'

    bar = '    ' + ''.join([3*'-' for category in _percents.keys()]) + '-'  

    levels = max([len(_) for _ in _percents.keys()])
    catg_name = {_: ['    '] for _ in range(0,levels + 1)}
    for key in _percents.keys():
        level = 1
        if len(key) < levels:
            for _ in key:
                catg_name[level].append(f' {_} ')
                level += 1
            for _ in range(level, levels + 1):
                catg_name[_].append('   ')
        else:
            for _ in key:
                catg_name[level].append(f' {_} ')
                level += 1

    _string2 = []
    for _ in catg_name.values():
        _string2.append(''.join(_))

    string2 = ' \n'.join(_string2) 
    

    display = (string1 + bar + string2).strip(' \n') + '  '
    return display

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))