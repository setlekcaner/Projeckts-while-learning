from collections import Counter
shoe_num = int(input("number of shoes: "))
shoe_sizes = [int(x) for x in input("shoe sizes: ").split(" ")[:shoe_num]]
# shoe number limit is absent
num_costumers = int(input("number of custemers: "))

dict = Counter(shoe_sizes)
total = 0
for i in range(num_costumers):
    costumer = [int(x) for x in input("custumer info: ").split(" ")]

    if costumer[0] in dict and int(dict[costumer[0]]) > 0:
        total += int(costumer[1])
        dict[costumer[0]] = int(dict[costumer[0]]) - 1

print(total)