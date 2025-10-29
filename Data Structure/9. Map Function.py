items = [
  ("Product1", 10),
  ("Product2", 9 ),  
  ("Product3", 12),
]

#  LETS SAY WE WANT TO REMOVE THE FIRST ITEM OF EACH TOUPLE IN THE LIST (THE PRODUCT NAME) AND WE ONLY WANT A LIST WITH THE PRICES

prices =[]
for item in items:
    prices.append(item[1])


print(prices)   # but insted of this function we can use the built-in map function

prices = list(map(lambda item: item[1], items))


