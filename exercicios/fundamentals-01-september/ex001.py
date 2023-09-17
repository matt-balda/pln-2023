string = input('Digite qualquer coisa: ')

counter = string.__len__()

counter_2 = 0

for i in string:
    counter_2 += 1

print("Com a função len(): "+ str(counter)) 
print("Com for in: "+ str(counter_2))