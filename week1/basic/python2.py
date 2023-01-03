#if 문~!

# ==, !=
stock_name = "대신증권"
if stock_name == '키움증권':
    print('키움증권이 맞네요!')
elif stock_name != '카카오증권':
    print('카카오 증권이 맞네요!')
else:
    print('위에 if문 조건들이 다 안맞네요!')

print("위에 조건문 실행되고 밖으로 나와서 이게 실행됨!")

# < , <=
stock_price = 3000
if stock_price < 2000:
    print('2000보다 작네요')
elif stock_price <= 3000:
    print('3000보다 같거나 작네요')
# >, >=
stock_rate = 2.5
if stock_rate > 2.5:
    print("2.5보다 크네요")
elif stock_rate >= 2.5:
    print('2.5보다 크거나 같네요')
