def cake_recipe():
    name = "Simple Vanilla Cake"

    ingredients = [
        "2 cups flour",
        "1 cup sugar",
        "2 eggs",
        "1 cup milk",
        "1/2 cup butter",
        "1 tsp baking powder",
        "1 tsp vanilla extract"
    ]

    steps = [
        "Preheat oven to 180°C",
        "Mix dry ingredients in a bowl",
        "Add eggs, milk, butter, and vanilla",
        "Mix until smooth",
        "Pour batter into a cake tin",
        "Bake for 30 minutes"
    ]

    print(name)
    print("\nIngredients:")
    for item in ingredients:
        print("-", item)

    print("\nSteps:")
    for step in steps:
        print("-", step)


cake_recipe()