import csv


def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
results = []


with open('tweets.csv','r') as csv_file:
  csv_reader = csv.reader(csv_file)

  for line in csv_reader:
    p = line[1]
    results.append(str(p))
  
final_arr = Remove(results)


with open('tweets_final.csv', 'a',newline='') as tf:  
    writter = csv.writer(tf)
    writter.writerow(final_arr)

print(len(results))
print(len(final_arr))


