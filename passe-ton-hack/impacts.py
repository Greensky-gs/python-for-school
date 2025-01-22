#Valeur d'entrée: variable input_s
#Sortie: résultat de print()

raw_array = input_s.split('[')[1].split(']')[0].split(", ")
impacts = [ int(x) for x in raw_array ]
k = int(input_s.split(':')[2])

cumulative_sum_frequency = {0: 1}
cumulative_sum = 0
count = 0
    
for impact in impacts:
    cumulative_sum += impact
        
    if (cumulative_sum - k) in cumulative_sum_frequency:
        count += cumulative_sum_frequency[cumulative_sum - k]
        
    if cumulative_sum in cumulative_sum_frequency:
        cumulative_sum_frequency[cumulative_sum] += 1
    else:
        cumulative_sum_frequency[cumulative_sum] = 1

print(count)
