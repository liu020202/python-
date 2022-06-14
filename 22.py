B = {
    "000 000":1000,
    "111 111":2000,
    "222 222":3000
}

group = int(input("輸入查詢組數:"))
for i in range(group):
    id = input("XXX XXX")
    if id in B:
        print(f"帳戶餘額:{B[id]}")
    else:
        print("帳號或密碼有誤")