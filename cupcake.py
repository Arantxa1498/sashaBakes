def cupcake_recipe():
    name = "Classic Vanilla Cupcakes"

    ingredients = [
        "1 cup all-purpose flour",
        "1/2 cup sugar",
        "1/2 cup butter (softened)",
        "2 eggs",
        "1 tsp vanilla extract",
        "1 tsp baking powder",
        "1/4 cup milk"
    ]

    steps = [
        "Preheat oven to 180°C",
        "Mix butter and sugar until creamy",
        "Add eggs and vanilla extract and mix well",
        "Add flour and baking powder",
        "Pour in milk and mix until smooth batter forms",
        "Fill cupcake liners halfway with batter",
        "Bake for 18-20 minutes"
    ]

    print(name)
    print("\nIngredients:")
    for item in ingredients:
        print("-", item)

    print("\nSteps:")
    for step in steps:
        print("-", step)


cupcake_recipe()