a = {
    "김밥" : 3000, 
    "라면" : 4000, 
    "아메리카노" : 3000, 
    "구운 계란" : 1000, 
    "빵" : 1000,
    "카페라떼" : 3500
}

print(a.keys())
print(a.values())
print(a.items())
menu_list = list(a.keys())
print(menu_list, type(menu_list))