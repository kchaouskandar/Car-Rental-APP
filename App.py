from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
cars = {}

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = request.form['year']
        car_id = len(cars)
        cars[car_id] = [brand, model, year, "Available"]
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/rent', methods=['GET', 'POST'])
def rent():
    if request.method == 'POST':
        car_id = int(request.form['car_id'])
        if car_id in cars:
            car = cars[car_id]
            if car[3] == "Available":
                car[3] = "Rented"
                return redirect(url_for('index'))
            else:
                return render_template('rent.html', error="Car is already rented", cars=cars)
        else:
            return render_template('rent.html', error="Invalid Car ID", cars=cars)
    return render_template('rent.html', cars=cars)

@app.route('/return', methods=['GET', 'POST'])
def return_car():
    if request.method == 'POST':
        car_id = int(request.form['car_id'])
        if car_id in cars:
            cars[car_id][3] = "Available"
            return redirect(url_for('index'))
        else:
            return render_template('return.html', error="Invalid Car ID", cars=cars)
    return render_template('return.html', cars=cars)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        car_id = int(request.form['car_id'])
        if car_id in cars:
            del cars[car_id]
            return redirect(url_for('index'))
        else:
            return render_template('delete.html', error="Invalid Car ID", cars=cars)
    return render_template('delete.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)