from flask import Flask, redirect, url_for, request, render_template
import MySQLdb

app = Flask(__name__)

#UNSUBSCRIPTION SERVICE #####################################################################

@app.route('/unsubscribePage')
def unsubscribePage():
      return render_template('unsubscribe.html')


@app.route('/unsubscribe', methods = ['POST', 'GET'])
def unsubscribe():
   if request.method == 'POST':
      user = request.form['nm'].lower().strip()
      return redirect(url_for('goodbye', name = user))
   else:
   		return("ERROR: ILLEGITIMATE ACCESS")


@app.route('/goodbye/<name>')
def goodbye(name):
   print("NAME: " + name)

   mydb = MySQLdb.connect(
      host="localhost",
      user="servermanager",
      passwd="potato",
      db="emailusers"
   )

   mycursor = mydb.cursor()
   mycursor.execute("DELETE FROM user WHERE email = \'" + name + "\';")
   mydb.commit()
   myresult = mycursor.fetchall()
   
   return render_template('goodbye.html', name = name)


#SUBSCRIPTION SERVICE #######################################################################

@app.route('/subscribePage')
def subscribePage():
      return render_template('subscribe.html')


@app.route('/subscribe', methods = ['POST', 'GET'])
def subscribe():
   if request.method == 'POST':
      user = request.form['nm'].lower().strip()
      return redirect(url_for('welcome', name = user))
   else:
   		return("ERROR: ILLEGITIMATE ACCESS")


@app.route('/welcome/<name>')
def welcome(name):
   print("NAME: " + name)

   mydb = MySQLdb.connect(
      host="localhost",
      user="servermanager",
      passwd="potato",
      db="emailusers"
   )

   mycursor = mydb.cursor()
   mycursor.execute("insert into user(email)  values (\"" + name + "\");")
   mydb.commit()
   myresult = mycursor.fetchall()

   return render_template('welcome.html', name = name)

if __name__ == '__main__':
   app.run(debug = True)