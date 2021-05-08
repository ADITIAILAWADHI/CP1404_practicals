def main():
    incomes = []
    total_months = int(input("How many months? "))

    for total_months in range(1, total_months + 1):
        income = float(input("Enter income for month {}: ".format(total_months)))
        incomes.append(income)

    display_income_report(incomes, total_months)


def display_income_report(incomes, month):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:9.2f}    Total: ${:9.2f}".format(month, income, total))


main()
