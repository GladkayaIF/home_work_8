with open('1.txt', encoding="utf8") as f:
    result = {}
    for food in f:
        counter = int(f.readline().strip())
        temp_data = []
        for item in range(counter):
            ingredient_name, quantity, measure = f.readline().split('|')
            temp_data.append(
                {'ingredient_name': ingredient_name.strip(), "quantity": int(quantity.strip()), "measure": measure.strip()}
            )
        result[food.strip()] = temp_data
        f.readline()
    cook_book = result


def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for i in dishes:
        for j in cook_book[i]:
            if j['ingredient_name'] in res.keys():
                res[j["ingredient_name"]]["quantity"] += j["quantity"]
            else:
                res[j["ingredient_name"]] = {}
                res[j["ingredient_name"]]["measure"] = j["measure"]
                res[j["ingredient_name"]]["quantity"] =j["quantity"]*person_count
    return res
print(get_shop_list_by_dishes(["Омлет", "Омлет"],2))



