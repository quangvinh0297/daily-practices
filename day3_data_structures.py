# --- Part 1: Todo List Manager ---
todo_list = ["Learn Python", "Practice Git"]
print("=== TODO LIST ===")
for i, task in enumerate(todo_list, 1):
    print(f"{i}. {task}")

# --- Part 2: Shopping List Dictionary ---
shopping = {"fruits": ["apple", "banana"], "drinks": ["coffee"]}
print("\n=== SHOPPING LIST ===")
for category, items in shopping.items():
    print(f"{category.upper()}: {', '.join(items)}")
