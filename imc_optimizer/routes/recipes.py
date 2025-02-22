from flask import Blueprint, request, jsonify
from models.food import FoodItem
import random

recipes_bp = Blueprint('recipes', __name__)

@recipes_bp.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    data = request.json
    diet_type = data['diet_type']
    calorie_target = data['calories']
    
    foods = FoodItem.query.filter_by(diet_type=diet_type).all()
    selected_foods = random.sample(foods, min(3, len(foods)))  # Seleccionar 3 al azar
    
    total_calories = sum(f.calories for f in selected_foods)
    
    return jsonify({
        "recipe": [f.name for f in selected_foods],
        "total_calories": total_calories
    })
