def solve(ingredients, scale):
    return [[round(ingredient[0] * scale, 2), ingredient[1]] for ingredient in ingredients]