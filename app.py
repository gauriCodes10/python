from flask import Flask, render_template, request
import random 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", files_list=[6], sides_default=6, dice_default=1)
     
    elif request.method == "POST":
        num_sides = int(request.form.get("num_sides"))
        num_dice = int(request.form.get("num_dice"))
        
        chosen_nums = []
        for x in range(0, num_dice):
            chosen_nums.append(random.randint(1, num_sides))
            
        files_list = []
        for item in chosen_nums:
            files_list.append(item)
            
        return render_template('index.html', files_list=files_list, sides_default=num_sides, dice_default=num_dice)        
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
    