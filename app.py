from flask import Flask, render_template, request, redirect, url_for
import deal_json as dj

app = Flask(__name__, static_folder="./static")
task_json = dj.load_json("task.json")
hideout_json = dj.load_json("hideout.json")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/en/", methods=["GET", "POST"])
def index_en():
    return render_template("index_en.html")


@app.route("/task/", methods=["GET", "POST"])
def task_setting():
    if request.method == "GET":
        return render_template(
            "task_setting.html",
            prapor_tasks=task_json.get_dealer_task_name("prapor"),
            therapist_tasks=task_json.get_dealer_task_name("Therapist"),
            skier_tasks=task_json.get_dealer_task_name("Skier"),
            peacekeeper_tasks=task_json.get_dealer_task_name("Peacekeeper"),
            mechanic_tasks=task_json.get_dealer_task_name("Mechanic"),
            ragman_tasks=task_json.get_dealer_task_name("Ragman"),
            jaeger_tasks=task_json.get_dealer_task_name("Jaeger"),
        )


@app.route("/en/task/", methods=["GET", "POST"])
def task_setting_en():
    if request.method == "GET":
        return render_template(
            "task_setting_en.html",
            prapor_tasks=task_json.get_dealer_task_name("prapor"),
            therapist_tasks=task_json.get_dealer_task_name("Therapist"),
            skier_tasks=task_json.get_dealer_task_name("Skier"),
            peacekeeper_tasks=task_json.get_dealer_task_name("Peacekeeper"),
            mechanic_tasks=task_json.get_dealer_task_name("Mechanic"),
            ragman_tasks=task_json.get_dealer_task_name("Ragman"),
            jaeger_tasks=task_json.get_dealer_task_name("Jaeger"),
        )


@app.route("/task/item/", methods=["GET", "POST"])
def task_item():
    if request.method == "GET":
        return render_template("task_setting.html")
    else:
        tasks_no_symbol = []
        tasks = request.form.getlist("task")
        for task in tasks:
            tasks_no_symbol.append(task.replace("_", " "))
        remain_tasks = task_json.get_sa_tasks(tasks_no_symbol)
        tasks_item = task_json.get_task_item_sum(remain_tasks)
        return render_template("task_item.html", tasks_item=tasks_item)


@app.route("/en/task/item/", methods=["GET", "POST"])
def task_item_en():
    if request.method == "GET":
        return render_template("task_setting_en.html")
    else:
        tasks_no_symbol = []
        tasks = request.form.getlist("task")
        for task in tasks:
            tasks_no_symbol.append(task.replace("_", " "))
        remain_tasks = task_json.get_sa_tasks(tasks_no_symbol)
        tasks_item = task_json.get_task_item_sum(remain_tasks)
        return render_template("task_item_en.html", tasks_item=tasks_item)


@app.route("/hideout/", methods=["GET", "POST"])
def hideout_setting():
    if request.method == "GET":
        return render_template(
            "hideout_setting.html",
            Bitcoin_Farm_tasks=hideout_json.get_dealer_task_name(
                "Bitcoin Farm"
            ),
            Booze_Generator_tasks=hideout_json.get_dealer_task_name(
                "Booze Generator"
            ),
            Intelligence_Center_tasks=hideout_json.get_dealer_task_name(
                "Intelligence Center"
            ),
            Lavatory_tasks=hideout_json.get_dealer_task_name("Lavatory"),
            Medstation_tasks=hideout_json.get_dealer_task_name("Medstation"),
            Nutrition_Unit_tasks=hideout_json.get_dealer_task_name(
                "Nutrition Unit"
            ),
            Scav_case_tasks=hideout_json.get_dealer_task_name("Scav case"),
            Water_collector_tasks=hideout_json.get_dealer_task_name(
                "Water collector"
            ),
            Workbench_tasks=hideout_json.get_dealer_task_name("Workbench"),
            Air_Filtering_Unit_tasks=hideout_json.get_dealer_task_name(
                "Air Filtering Unit"
            ),
            Generator_tasks=hideout_json.get_dealer_task_name("Generator"),
            Heating_tasks=hideout_json.get_dealer_task_name("Heating"),
            Illumination_tasks=hideout_json.get_dealer_task_name(
                "Illumination"
            ),
            Library_tasks=hideout_json.get_dealer_task_name("Library"),
            Rest_Space_tasks=hideout_json.get_dealer_task_name("Rest Space"),
            Security_tasks=hideout_json.get_dealer_task_name("Security"),
            Shooting_range_tasks=hideout_json.get_dealer_task_name(
                "Shooting range"
            ),
            Solar_power_tasks=hideout_json.get_dealer_task_name("Solar power"),
            Stash_tasks=hideout_json.get_dealer_task_name("Stash"),
            Vents_tasks=hideout_json.get_dealer_task_name("Vents"),
            Defective_wall_tasks=hideout_json.get_dealer_task_name(
                "Defective wall"
            ),
            Gym_tasks=hideout_json.get_dealer_task_name("Gym"),
        )


@app.route("/en/hideout/", methods=["GET", "POST"])
def hideout_setting_en():
    if request.method == "GET":
        return render_template(
            "hideout_setting_en.html",
            Bitcoin_Farm_tasks=hideout_json.get_dealer_task_name(
                "Bitcoin Farm"
            ),
            Booze_Generator_tasks=hideout_json.get_dealer_task_name(
                "Booze Generator"
            ),
            Intelligence_Center_tasks=hideout_json.get_dealer_task_name(
                "Intelligence Center"
            ),
            Lavatory_tasks=hideout_json.get_dealer_task_name("Lavatory"),
            Medstation_tasks=hideout_json.get_dealer_task_name("Medstation"),
            Nutrition_Unit_tasks=hideout_json.get_dealer_task_name(
                "Nutrition Unit"
            ),
            Scav_case_tasks=hideout_json.get_dealer_task_name("Scav case"),
            Water_collector_tasks=hideout_json.get_dealer_task_name(
                "Water collector"
            ),
            Workbench_tasks=hideout_json.get_dealer_task_name("Workbench"),
            Air_Filtering_Unit_tasks=hideout_json.get_dealer_task_name(
                "Air Filtering Unit"
            ),
            Generator_tasks=hideout_json.get_dealer_task_name("Generator"),
            Heating_tasks=hideout_json.get_dealer_task_name("Heating"),
            Illumination_tasks=hideout_json.get_dealer_task_name(
                "Illumination"
            ),
            Library_tasks=hideout_json.get_dealer_task_name("Library"),
            Rest_Space_tasks=hideout_json.get_dealer_task_name("Rest Space"),
            Security_tasks=hideout_json.get_dealer_task_name("Security"),
            Shooting_range_tasks=hideout_json.get_dealer_task_name(
                "Shooting range"
            ),
            Solar_power_tasks=hideout_json.get_dealer_task_name("Solar power"),
            Stash_tasks=hideout_json.get_dealer_task_name("Stash"),
            Vents_tasks=hideout_json.get_dealer_task_name("Vents"),
            Defective_wall_tasks=hideout_json.get_dealer_task_name(
                "Defective wall"
            ),
            Gym_tasks=hideout_json.get_dealer_task_name("Gym"),
        )


@app.route("/hideout/item/", methods=["GET", "POST"])
def hideout_item():
    if request.method == "GET":
        return render_template("hideout_setting.html")
    else:
        tasks_no_symbol = []
        tasks = request.form.getlist("task")
        for task in tasks:
            tasks_no_symbol.append(task.replace("_", " "))
        remain_tasks = hideout_json.get_sa_hideout(tasks_no_symbol)
        tasks_item = hideout_json.get_hideout_task_item_sum(remain_tasks)
        return render_template("hideout_item.html", tasks_item=tasks_item)


@app.route("/en/hideout/item/", methods=["GET", "POST"])
def hideout_item_en():
    if request.method == "GET":
        return render_template("hideout_setting_en.html")
    else:
        tasks_no_symbol = []
        tasks = request.form.getlist("task")
        for task in tasks:
            tasks_no_symbol.append(task.replace("_", " "))
        remain_tasks = hideout_json.get_sa_hideout(tasks_no_symbol)
        tasks_item = hideout_json.get_hideout_task_item_sum(remain_tasks)
        return render_template("hideout_item_en.html", tasks_item=tasks_item)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
