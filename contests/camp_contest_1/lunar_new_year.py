import heapq

n_foods, n_customers = map(int, input().split())

foods = list(map(int, input().split()))
prices = list(map(int, input().split()))

prices_heap = [(p, i) for i, p in enumerate(prices)]
heapq.heapify(prices_heap)

total_food = sum(foods)
ans = []
for _ in range(n_customers):
    food_idx, quantity = map(int, input().split())

    if total_food == 0 or total_food < quantity:
        ans.append(0)
        continue    
    
    elif quantity >= foods[food_idx - 1]: 
        cur_price = 0
        index = food_idx - 1
        if foods[index] != 0:
            quantity -= foods[index]
            total_food -= foods[index]
            cur_price += foods[index] * prices[index]
            foods[index] = 0

        while quantity > 0:
            price, index = heapq.heappop(prices_heap) 

            ava = foods[index]
        
            if ava > quantity:            
                foods[index] -= quantity
                total_food -= quantity
                cur_price += price * quantity                
                quantity = 0
                heapq.heappush(prices_heap, (price, index)) 

            else:
                cur_price += price * foods[index]
                quantity -= foods[index] 
                total_food -= foods[index] 
                foods[index] = 0        

        ans.append(cur_price)

    else:
        foods[food_idx - 1] -= quantity
        ans.append(quantity * prices[food_idx - 1])
    
        total_food -= quantity

print("\n".join(map(str, ans)))
