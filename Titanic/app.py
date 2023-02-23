from flask import Flask,render_template,request
import pickle

app=Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET','POST'])
def home():
    result=''
    if (request.method=='POST'):
        pickled_model=pickle.load(open('./titanic.pkl','rb'))
        #getting input values from the user
        age=request.form['age']
        gender=request.form['gender']
        pclass=request.form['pclass']
        SibSp=request.form['SibSp']
        parch=request.form['parch']
        fare=request.form['fare']
        embarked=request.form['embarked']

        #making predictions using pickled model
        print(age,gender,pclass,SibSp,parch,fare,embarked)
        result_arr=pickled_model.predict([[int(pclass),int(gender),float(age),int(SibSp),int(parch),float(fare),int(embarked)]])
        
        if result_arr[0] == 1:
            result = "The Passenger Survived."
        elif result_arr[0]==0:
            result = "The Passenger didn't Survive."
        else:
            result="Error"
        return render_template('predict.html',result=result)
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)