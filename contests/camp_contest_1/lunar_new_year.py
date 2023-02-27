n_foods, n_customers = map(int, input().split())

foods = list(map(int, input().split()))
prices = list(map(int, input().split()))

cheapest_prices = [(p, i) for i, p in enumerate(prices)]
cheapest_prices.sort()
cheapest_food_idx = 0

ans = []
for _ in range(n_customers):
    current_price = 0

    ordered_food_idx, order_quantity = map(int, input().split())
    ordered_food_idx -= 1

    available_quantity = foods[ordered_food_idx]

    if available_quantity >= order_quantity:
        current_price += prices[ordered_food_idx] * order_quantity
        foods[ordered_food_idx] -= order_quantity
    
    else:
        current_price += prices[ordered_food_idx] * available_quantity
        foods[ordered_food_idx] = 0

    orders_left = max(0, order_quantity - available_quantity)

    while orders_left > 0:
        # find cheapest   
        cheapest_food = None
        while cheapest_food_idx < len(cheapest_prices) and cheapest_food == None:            
            cheapest_price, cheapest_food = cheapest_prices[cheapest_food_idx]
            if foods[cheapest_food] == 0:
                cheapest_food = None                        
                cheapest_food_idx += 1
            else:
                break
        
        if cheapest_food == None:
            current_price = 0
            break
        
        else:            
            cheapest_available_quantity = foods[cheapest_food]   
            if cheapest_available_quantity >= orders_left:         
                current_price += cheapest_price * orders_left
            else:
                current_price += cheapest_price * cheapest_available_quantity
            
            foods[cheapest_food] = max(0, cheapest_available_quantity - orders_left)
            orders_left -= cheapest_available_quantity
    
    ans.append(current_price)


print("\n".join(map(str, ans)))