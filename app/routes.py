from flask import Blueprint, request, redirect, render_template
from .store import add_task, get_tasks, complete_task, delete_task
from .ai import get_ai_suggestions
from .auth import authenticate_user

main = Blueprint("main", __name__)
suggestions_cache = []

@main.route("/", methods=["GET", "POST"])
def home():
    token = request.headers.get("Authorization", "Bearer mysecrettoken")
    if not authenticate_user(token):
        return "Unauthorized", 401

    if request.method == "POST":
        task = request.form.get("task")
        if task:
            add_task(task)

    tasks = get_tasks()
    return render_template("index.html", tasks=tasks, suggestions=suggestions_cache)

@main.route("/complete/<int:index>")
def complete(index):
    complete_task(index)
    return redirect("/")

@main.route("/delete/<int:index>")
def delete(index):
    delete_task(index)
    return redirect("/")

@main.route("/suggest", methods=["POST"])
def suggest():
    global suggestions_cache
    goal = request.form.get("goal")
    if goal:
        suggestions_cache = get_ai_suggestions(goal)
    return redirect("/")
