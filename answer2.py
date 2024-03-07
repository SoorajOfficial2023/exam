import json

with open('data.json', 'r') as file:
    data = json.load(file)
    items = data['items']
    new_list = []
    for item in items:
        arr = {
                "name" : item.get('name'),
                "categories" :item.get('categories'),
                "image" : item.get('image'),
                "base_price" : item.get('base_price'),
                "availability_status":item.get('availability_status')
                }
        new_list.append(arr)
        # print(f"{new_list}")     


    user_input = input('Enter keyword: ')
     
    for sort in arr:
        name = arr.get('name')
        if user_input  == name:
            print(True)
    else:
        print(False)
