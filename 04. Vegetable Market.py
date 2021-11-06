price_kg_vegetable = float(input())
price_kg_fruit = float(input())
kg_vegetable = int(input())
kg_fruit = int(input())

cost_vegetable = price_kg_vegetable*kg_vegetable
cost_fruit = price_kg_fruit*kg_fruit

total_leva = cost_fruit+cost_vegetable
total_euro = total_leva/1.94

print(f'{total_euro:.2f}')

