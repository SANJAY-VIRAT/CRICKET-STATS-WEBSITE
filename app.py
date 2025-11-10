# app.py (Flask backend)
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Stats calculation route
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    role = data.get("role")
    stat_type = data.get("statType")
    result = {}

    if role == "BATSMEN":
        try:
            if stat_type in ["average", "both"]:
                innings = int(data.get("innings", 0))
                not_outs = int(data.get("notOuts", 0))
                runs_list_raw = data.get("runsList", "").strip()
                if not runs_list_raw:
                    return jsonify({"error": "Runs per innings not provided."})
                runs_list = list(map(int, runs_list_raw.split()))
                if len(runs_list) != innings:
                    return jsonify({"error": "Mismatch between innings and run entries."})
                if not_outs > innings:
                    return jsonify({"error": "Not outs can't exceed innings."})
                if innings == 0:
                    result["average"] = "NA (No innings played)"
                elif innings - not_outs == 0:
                    result["average"] = "NA (Never got out)"
                else:
                    result["average"] = round(sum(runs_list) / (innings - not_outs), 2)

            if stat_type in ["strikeRate", "both"]:
                total_runs = int(data.get("totalRuns", 0))
                balls_faced = int(data.get("ballsFaced", 0))
                result["strikeRate"] = (
                    "NA (No balls faced)" if balls_faced == 0 else round((total_runs / balls_faced) * 100, 2)
                )

            return jsonify(result)

        except ValueError:
            return jsonify({"error": "Please enter valid numeric values."})
        except Exception as e:
            return jsonify({"error": f"Unexpected error: {str(e)}"})

    elif role == "BOWLER":
        try:
            balls = int(data.get("balls", 0))
            runs_conceded = int(data.get("runsConceded", 0))
            wickets = int(data.get("wickets", 0))

            if balls < 0 or runs_conceded < 0 or wickets < 0:
                return jsonify({"error": "Negative values are not allowed."})

            if stat_type in ["average", "all"]:
                result["average"] = "NA" if wickets == 0 else round(runs_conceded / wickets, 2)

            if stat_type in ["strikeRate", "all"]:
                result["strikeRate"] = "NA" if wickets == 0 else round(balls / wickets, 2)

            if stat_type in ["economyRate", "all", "strikeRate", "average"]:
                overs = balls / 6
                result["economyRate"] = (
                    "NA (No overs bowled)" if overs == 0 else round(runs_conceded / overs, 2)
                )

            return jsonify(result)

        except ValueError:
            return jsonify({"error": "Please enter valid numeric values."})
        except Exception as e:
            return jsonify({"error": f"Unexpected error: {str(e)}"})

    return jsonify({"error": "Invalid role selected."})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)