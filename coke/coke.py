def main():
  accepted_coins = [25, 10, 5]
  amount_due = 50

  while amount_due > 0:
    print('Amount Due:', amount_due)
    inserted_coin = int(input('Insert Coin: '))

    if inserted_coin in accepted_coins:
      amount_due -= inserted_coin

  print('Change Owed:', abs(amount_due))

main()