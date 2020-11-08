# IEEE_Rookies_task_08_part_01
# name: Mahmoud_Ramadan
# task: get the first 10 links of google search.


from googlesearch import search

query = input('enter your search: ')
for i in search(query, tld="com", num=10, stop=10, pause=2):
    print(i)


input('press enter to exit...')
