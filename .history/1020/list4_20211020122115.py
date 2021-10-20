n=input("整数を入力してください")
sum = 0;
lists = []
for num in range(int(n) + 1):
    sum = sum + num
    lists.append(num)

print(f"1~{n}までの合計:{sum}" )
print(f"平均：{sum / int(n)}")


