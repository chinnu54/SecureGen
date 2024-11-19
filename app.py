from flask import Flask,render_template,request,Response
from Generate_Password import GeneratePassword

app=Flask(__name__)
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/submit',methods=["Get","Post"])
def submit():
    if request.method == 'POST':
        try:
            # Retrieve form data
            n_letters = int(request.form.get('letters', 0))
            n_numbers = int(request.form.get('digits', 0))
            n_special_characters = int(request.form.get('specialChars', 0))

            # Ensure no negative values are entered
            if n_letters < 0 or n_numbers < 0 or n_special_characters < 0:
                return render_template('index.html', error="Please enter non-negative values!")

            # Generate password
            password = GeneratePassword(n_letters, n_numbers, n_special_characters)
            # output(password)
            # Home()
            return render_template('index.html', password=password)

        except ValueError:
            return render_template('index.html', error="Please enter valid integer values.")
    
    return render_template('index.html')
# def output(password):
#     return render_template('index.html', password=password)
# app.run(port=3001,debug=True)
if __name__=='__main__':
    app.run(port=3000,debug=True)