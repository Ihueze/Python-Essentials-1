# number of frinds
friends = 5

# slice per person
slice_per_person = 8

# slice per pizza
slice_per_pizza = 8

# price per pizza
price_per_pizza = 10

# Total sices needed
total_slices_needed = friends * slice_per_person

# Number of pizzas needed
pizzas_needed = total_slices_needed / slice_per_pizza

# Total cost
total_cost = pizzas_needed * price_per_pizza
print("friends:", friends, "\n"
      "slice per person:", slice_per_person, "\n"
      "slice per pizza:", slice_per_pizza, "\n"
      "price per pizza:", price_per_pizza, "\n"
      "total slices needed:", total_slices_needed, "\n"
      "pizzas needed:", pizzas_needed, "\n"
      "total cost:", total_cost)
