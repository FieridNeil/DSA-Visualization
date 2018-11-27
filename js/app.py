from flask import Flask, render_template
from algos import *
app = Flask(__name__)
app.debug = True

v = VectorLog(0,0)
for i in range(10):
    v.add_back(i)

print(v)
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/selection_sort/')
def selection_sort():
    return render_template('selection_sort.html')

@app.route('/selection_sort/<data>')
def do_selection_sort(data):
    return render_template('selection_sort.html', func = in_place_selection_sort, data=v)

if __name__ == '__main__':
    app.run()
