def cheesecake_recipe():
    name = "Classic Cheesecake"

    ingredients = [
        "200g cream cheese",
        "1/2 cup sugar",
        "2 eggs",
        "1 cup crushed biscuits",
        "1/2 cup melted butter",
        "1 tsp vanilla extract"
    ]

    steps = [
        "Preheat oven to 170°C",
        "Mix crushed biscuits with melted butter",
        "Press mixture into cake tin",
        "Beat cream cheese, sugar, eggs, and vanilla",
        "Pour mixture over base",
        "Bake for 40 minutes"
    ]

    print(name)
    print("\nIngredients:")
    for item in ingredients:
        print("-", item)

    print("\nSteps:")
    for step in steps:
        print("-", step)


cheesecake_recipe()