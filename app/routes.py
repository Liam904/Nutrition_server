import requests
from flask import Flask, request, jsonify, Blueprint
from .models import Meal, db, Goal


routes = Blueprint("routes", __name__)
NUTRITIONIX_API_URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"
NUTRITIONIX_APP_ID = "e475c6ce"
NUTRITIONIX_APP_KEY = "122305c7af14862e9c798ce5380630df"


@routes.route("/add_meal", methods=["POST"])
def add_meal():
    data = request.json
    food_items = data.get("food_items")
    meal_type = data.get("meal_type")

    quantity = data.get("quantity", 1) 

    try:
        quantity = float(quantity)
    except ValueError:
        return jsonify({"error": "Invalid quantity value"}), 400

 
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_APP_KEY,
        "Content-Type": "application/json",
    }

    body = {"query": food_items}

    response = requests.post(NUTRITIONIX_API_URL, headers=headers, json=body)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch nutrition data"}), 500

    nutrition_data = response.json()

    total_calories = sum(item["nf_calories"] for item in nutrition_data["foods"])
    total_protein = sum(item["nf_protein"] for item in nutrition_data["foods"])
    total_fat = sum(item["nf_total_fat"] for item in nutrition_data["foods"])
    total_carbohydrates = sum(
        item["nf_total_carbohydrate"] for item in nutrition_data["foods"]
    )
    total_fiber = sum(item["nf_dietary_fiber"] for item in nutrition_data["foods"])
    total_sugar = sum(item["nf_sugars"] for item in nutrition_data["foods"])

    total_calories *= quantity
    total_protein *= quantity
    total_fat *= quantity
    total_carbohydrates *= quantity
    total_fiber *= quantity
    total_sugar *= quantity

    new_meal = Meal(
        user_id=1,
        food_items=food_items,
        meal_type=meal_type,
        quantity=quantity,
        total_calories=total_calories,
        total_protein=total_protein,
        total_fat=total_fat,
        total_carbohydrates=total_carbohydrates,
        total_fiber=total_fiber,
        total_sugar=total_sugar,
        notes=data.get("notes", ""),
    )

    db.session.add(new_meal)
    db.session.commit()

    return jsonify({"message": "Meal added successfully"}), 201




@routes.route("/nutrition_info", methods=["GET"])
def get_all_nf_info():
    meal = Meal.query.all()

    protein = []
    fats = []
    carbs = []
    calories = []
    for meals in meal:
        i = meals.total_protein
        j = meals.total_fat
        k = meals.total_carbohydrates
        m = meals.total_calories
        protein.insert(0, i)
        fats.insert(0, j)
        carbs.insert(0, k)
        calories.insert(0, m)

    return jsonify(
        {
            "protein": sum(protein),
            "fats": sum(fats),
            "carbs": sum(carbs),
            "calories": sum(calories),
        }
    )


@routes.route("/add_goals", methods=["POST"])
def set_goals():
    body = request.get_json()
    calories_goal = body.get("calories_goal")
    protein_goal = body.get("protein_goal")
    fat_goal = body.get("fat_goal")
    carbohydrates_goal = body.get("carbohydrates_goal")
    fiber_goal = body.get("fiber_goal")

    weight_goal = body.get("weight_goal")
    exercise_goal = body.get("exercise_goal")

    new_goal = Goal(
        user_id=1,
        calories_goal=calories_goal,
        protein_goal=protein_goal,
        fat_goal=fat_goal,
        carbohydrates_goal=carbohydrates_goal,
        fiber_goal=fiber_goal,
        weight_goal=weight_goal,
        exercise_goal=exercise_goal,
    )

    db.session.add(new_goal)
    db.session.commit()

    return jsonify({"Message": "Goals added successfulyy"}), 201


@routes.route("/all_goals", methods=["GET"])
def get_all_goals():
    goals = Goal.query.all()
    all_goals = []

    for goal in goals:
        goals_obj = {
            "id": goal.id,
            "calories": goal.calories_goal,
            "protein": goal.protein_goal,
            "fats": goal.fat_goal,
            "carbohydrates": goal.carbohydrates_goal,
            "fiber": goal.fiber_goal,
            "weight": goal.weight_goal,
            "exercise": goal.exercise_goal,
        }
        all_goals.append(goals_obj)

    return jsonify(all_goals)
