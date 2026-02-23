def tiramisu_recipe():
    name = "Simple Tiramisu"

    ingredients = [
        "250g mascarpone",
        "250g cream cheese",
        "350g whipping cream",
        "2 eggs",
        "1/2 cup sugar",
        "1 tsp vanilla extract",
        "1 cup coffee",
        "Ladyfinger biscuits",
        "Cocoa powder"
    ]

    steps = [
        "Separate egg whites and yolks",
        "Mix yolks with 2 tbsps sugar and cook it on a double boiler until it turns pale yellow",
        "Mix mascarpone, cream cheese and whipping cream with 1/2 cup sugar and add vanilla extract",
        "Mix the egg yolks and cream mixture together do not over mix",
        "Dip biscuits in coffee",
        "Layer biscuits and cream mixture",
        "Dust with cocoa powder",
        "Chill for 4 hours in the fridge"
    ]

    print(name)
    print("\nIngredients:")
    for item in ingredients:
        print("-", item)

    print("\nSteps:")
    for step in steps:
        print("-", step)


tiramisu_recipe()