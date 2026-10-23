# Question 1

def main():

    P0 = float(input("What is the amount to finance? "))
    r = float(input("What is the annual interest rate? "))
    N = int(input("What is the loan terms in years? "))
    k = 12

    d = P0 / ((1 - (1 + r / k) ** (-N * k )) / (r / k))

    balance = P0
    total_payments = N * k

    print(f"{'Payment':<10}{'Amount':<15}{'Interest':<15}{'Principal':<15}{'Balance':<15}")

    for payment in range(1, total_payments + 1):
        interest = balance * (r / k)
        principal = d - interest
        balance -= principal

        print(f"{payment:<10}${d:<15.2f}${interest:<15.2f}${principal:<15,.2f}${balance:<15.2f}")

main()