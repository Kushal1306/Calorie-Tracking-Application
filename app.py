import psycopg2
import bcrypt
import os
# import matplotlib.pyplot as plt
from visual import generate_daily,generate_weekly,generate_monthly
from db import execute_query,execute_query2,execute_query3
from recommendation import recommend_text
from generate_combine import generate_data
from flask import Flask,jsonify,request,session,render_template,redirect,url_for,send_file

app = Flask(__name__, static_url_path='', static_folder='frontend/')
app.secret_key='abcdefg'

UPLOAD_FOLDER = 'static/uploads/'

@app.route('/')
def index():
    # if 'username' in session:
    #       return redirect(url_for('calorie'))
    if 'username' in session:
          username=session['username']
          return render_template('calorie.html',username=username)
    else:
         return render_template('login.html')

def hash_password(password):
      hashed_password=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
      return hashed_password

def check_password(password,hashed_password):
      
      return bcrypt.checkpw(password.encode('utf-8'),hashed_password)


def retrieve_userid(username,password):

      query="select userid from users where username= %s and  password= %s"
      values=(username,password)
      result=execute_query(query,values)
      print(result)
      if result:
            user_id=result[0]
            print(f"user id is {user_id}")
      else:
            print("invalid")
      session['userid']=user_id
    #   return user_id
     
      
      
@app.route('/login',methods=['GET','POST'])
def login():
      username=request.form['username']
      password=request.form['password']
      session['username']=username
    #   ha_password=hash_password(password)
      retrieve_userid(username,password)
      id=session['userid']
      query="select calories,meal_type,entry_date from calorie_entries where userid= %s order by entry_date DESC limit 3;"
      values=(id,)
      result=execute_query(query,values)
      print(result)
    

      return render_template('calorie.html',username=username,recent_data=result)

      
@app.route('/logout',methods=['GET','POST'])
def logout():
      #session.pop('username',None)
      session.clear()

      return render_template('login.html')
@app.route('/register',methods=['POST'])
def register():
      return render_template('register.html')

@app.route('/registration',methods=['POST'])
def regsiteration():
      
      username=request.form['username']
      password=request.form['password']

      query="insert into users(username,password) values(%s,%s)"
      values=(username,password)
      result=execute_query2(query,values)
  

      return render_template('login.html')

      
@app.route('/calorie')
def update_data():
      
      data={'message':'Your data'}
      return jsonify(data)

@app.route('/update_calories',methods=['POST'])
def calorie_update():
      calorie_amount=request.form['calories']
      Meal_Type=request.form['meal_type']
      date=request.form['date']
      username=session['username']
      userid=session['userid']

      query1="insert into calorie_entries (userid,calories,meal_type,entry_date) values(%s,%s,%s,%s)"
      values1=(userid,calorie_amount,Meal_Type,date)
      
      query2="select calories,meal_type,entry_date from calorie_entries where userid= %s order by entry_date DESC limit 7;"
      values2=(userid,)

      execute_query2(query1,values1)
      result1=execute_query(query2,values2)
      return render_template('calorie.html',username=username,recent_data=result1)
      
@app.route('/generate_report',methods=['POST'])
def generate_report():
      report_type=request.form['report_type']
      chart_type=request.form['chart_type']
      userid=session['userid']
      if report_type=='daily':
       
    #   query="select sum(calories) as total_sum, entry_date from calorie_entries where userid=%s group by entry_date order by entry_date DESC LIMIT 7"
            query="""SELECT SUM(calories) AS total_sum, 
       TO_CHAR(entry_date, 'DD-MM') AS entry_date
       FROM calorie_entries 
       WHERE userid=%s
       GROUP BY TO_CHAR(entry_date,'DD-MM'),entry_date
       ORDER BY TO_CHAR(entry_date,'MM-DD') DESC 
       LIMIT 7;"""
            values=(userid,)   
            result=execute_query(query,values)
            generate_daily(result,chart_type)
            image_path='/static/uploads/daily.png'
            return render_template('visual.html',image_src=image_path)
      elif report_type=='weekly':
            query="""SELECT AVG(calories) AS average_weekly_calories,
TO_CHAR(DATE_TRUNC('week', entry_date), 'DD-MM') AS start_of_week     
FROM calorie_entries
WHERE userid = 2
GROUP BY TO_CHAR(DATE_TRUNC('week', entry_date), 'DD-MM')
ORDER BY TO_DATE(TO_CHAR(DATE_TRUNC('week', entry_date), 'DD-MM'), 'DD-MM') DESC;

            
             """
            values=(userid,) 
            result=execute_query(query,values)
            generate_weekly(result,chart_type)
            image_path='/static/uploads/weekly.png'
            return render_template('visual.html',image_src=image_path)
      elif report_type=='monthly':
            query=""" SELECT AVG(calories) AS monthly_calories,
       TO_CHAR(DATE_TRUNC('month', entry_date), 'DD-MM') AS start_of_month 
              FROM calorie_entries
              WHERE userid = %s
              GROUP BY TO_CHAR(DATE_TRUNC('month', entry_date), 'DD-MM')
              ORDER BY start_of_month;
                   """
            values=(userid,)
            result=execute_query(query,values)
            generate_monthly(result,chart_type)
            image_path='/static/uploads/monthly.png'
            return render_template('visual.html',image_src=image_path)
      
@app.route('/generate_combined',methods=['POST'])
def generate_combined():
      userid=session['userid']
      chart_type=request.form['chart_type']
      file_type=request.form['file_type']

     
      generate_data(chart_type,userid)
      if file_type=='pdf':
            file_path2 = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\combined.pdf'
            return send_file(file_path2,as_attachment=True)
      elif file_type=='png':
            file_path = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\combined.png'
            return send_file(file_path,as_attachment=True)
      # elif file_type=='csv':
      #       query=f"select calories,meal_type,entry_date from calorie_entries where userid={id[0]} order by entry_date"
      #       execute_query3(query)
      #       file_path = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\output.csv'
      #       return send_file(file_path,as_attachment=True)


     
@app.route('/export_data',methods=['POST'])
def export_data():
      id=session['userid']
      print(id)
      query=f"select calories,meal_type,entry_date from calorie_entries where userid={id[0]} order by entry_date"
      execute_query3(query)
      file_path = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\output.csv'
      
      return send_file(file_path,as_attachment=True)

@app.route('/visualization',methods=['POST'])
def make_visualization():      

      return render_template('visual.html')
@app.route('/download_data',methods=['POST'])
def data():
      return render_template('download.html')

@app.route('/view_recommendations',methods=['POST'])   
def generating_recommendation():
      userid=session['userid']
      query="""SELECT SUM(calories) AS total_sum, 
       TO_CHAR(entry_date, 'DD-MM') AS entry_date
       FROM calorie_entries 
       WHERE userid=%s
       GROUP BY TO_CHAR(entry_date,'DD-MM'),entry_date
       ORDER BY TO_CHAR(entry_date,'MM-DD') DESC 
       LIMIT 15;
       """
      values=(userid,)   
      result=execute_query(query,values)
      print(result)
      text=recommend_text(result)
      recommendations_list = text.split('\n')
      recommendations_tuple = tuple(recommendations_list)
      recommendations_list = list(recommendations_list)
      return render_template('recommend.html',data=recommendations_list)



if __name__=='__main__':
    app.run(debug=True)



