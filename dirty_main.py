from package_data.salary import calculate_salary
from package_data.db.people import get_employees
from datetime import date

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(f'Текущая дата {date.today()}')
