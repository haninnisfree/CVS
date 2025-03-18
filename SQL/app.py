from flask import Flask,render_template,redirect
from fetchall import query_with_fetchall
from insertData import insert_book
from updateData import update_product
from deleteData import delete_product
from config import read_config

app = Flask(__name__)

@app.route('/')
def index():
  datas = query_with_fetchall()
  return render_template('list.html',datas=datas)

@app.route('/insert/<itemcode>/<name>/<price>/<quantity>/<date>')
def insert(itemcode,name,price,quantity,date):
  insert_book(itemcode,name,price,quantity,date)
  return redirect('/')

@app.route('/update/<itemcode>/<name>')
def update(itemcode,name):
  affected_rows = update_book(itemcode, name)
  print(f'Number of affected rows: {affected_rows}')
  return redirect('/')

@app.route('/delete/<itemcode>')
def delete(itemcode):
  affected_rows = delete_book(itemcode)
  print(f'Number of affected rows: {affected_rows}')
  return redirect('/')

if  __name__ == '__main__':  
    app.run(debug=True)

