"""
4)
Реализовать функцию bank, которая приннимает следующие аргументы: сумма депозита, кол-во лет, и процент.
Результатом выполнения должна быть сумма по истечению депозита
"""


def bank(deposit_amount, number_of_years, percent):
    ''' it is bank def '''
    for year in range(1, number_of_years):
        deposit_amount = (deposit_amount*percent/100)+deposit_amount
    return deposit_amount
