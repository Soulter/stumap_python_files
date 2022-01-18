wfsy = float(input("万份收益："))
deposit = int(input("存入金额（整数）:"))
days = 29
total_money = 0
print(wfsy)
while days>0:
    print("shares :"+str(deposit/10000*wfsy*days))
    total_money = total_money+ deposit + deposit/10000*wfsy*days
    print(total_money)
    days = days - 1
print(total_money)
