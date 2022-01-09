from flask import Flask, render_template, request, session, request, redirect, g, url_for, flash
import pickle
from forms import LoginForm
import numpy as np
import folium
import os , smtplib
from flask_mail import Mail, Message

model = pickle.load(open('modelBM.pkl', 'rb'))
fraudmodel = pickle.load(open('fraudmodel.pkl', 'rb'))

app = Flask(__name__)

mail = Mail(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/dashboard")
def dashboard():
    map = folium.Map(
        location=[34.6113892, 8.7590835]
    )
    folium.Marker(
        location=[36.8008325, 10.1554105],
        popup="The first state ",
        tooltip="Tunis"
    ).add_to(map)
    folium.Marker(
        location=[34.7555058, 10.6612224],
        popup="The second state",
        tooltip="Sfax"
    ).add_to(map)
    folium.Marker(
        location=[36.8688529, 10.1353404],
        popup="The third state",
        tooltip="Ariana"
    ).add_to(map)
    folium.Marker(
        location=[35.8283295, 10.5830349],
        popup="The fourth state",
        tooltip="Sousse"
    ).add_to(map)
    folium.Marker(
        location=[36.7464825, 10.2171373],
        popup="The fifth state",
        tooltip="Ben Arous"
    ).add_to(map)
    folium.Marker(
        location=[36.4523901, 10.6803222],
        popup="The sixth state",
        tooltip="Nabeul"
    ).add_to(map)
    folium.Marker(
        location=[35.7542668, 10.7754201],
        popup="The seventh state",
        tooltip="Monastir"
    ).add_to(map)
    folium.Marker(
        location=[33.8892778, 10.0851486],
        popup="The eighth state",
        tooltip="Gabes"
    ).add_to(map)
    map.save('templates/map.html')
    sinsitredata = [
        ("Ariana", 14943),
        ("Tunis", 34962),
        ("Gabes", 2786),
        ("Sfax", 16399),
        ("Monastir", 5309),
        ("Sousse", 11380),
        ("Nabeul", 6475),
        ("Ben Arous", 8085)
    ]
    labels = [row[0] for row in sinsitredata]
    values = [row[1] for row in sinsitredata]

    typepolicedata=[
        ("Individuel",99.52),
        ("Flotte",0.48)
    ]
    types = [row[0] for row in typepolicedata]
    poucentagetype = [row[1] for row in typepolicedata]

    naturepolicedata = [
        ("Renouvelable", 88.7),
        ("Temporaire", 11.3)
    ]
    naturepolice = [row[0] for row in naturepolicedata]
    poucentagenaturepolice = [row[1] for row in naturepolicedata]

    numaccidentdata = [
        ("0",930433),("1",118743),("2",23092),("3",4988),("4",1087),("5 a 9",963)
    ]
    numaccident = [row[0] for row in numaccidentdata]
    countnumaccident = [row[1] for row in numaccidentdata]

    avicompagniedata = [
        ("AMI", 149), ("Maghrbeia", 58), ("Star", 134),("Astree", 30), ("Hayett", 7), ("COMAR", 109),
        ("MAE", 67), ("Zitouna", 59), ("Carte",42),("Llyod",42),  ("GAT assurance", 98),("At-takafulia", 32)

    ]
    nomassurance = [row[0] for row in avicompagniedata]
    rateassurance = [row[1] for row in avicompagniedata]

    clientperclassdata = [
        ("1", 302941), ("2", 150012), ("3", 204003), ("4", 172279), ("5", 85303), ("6", 45436), ("7", 11043), ("8", 99917),
        ("9", 7587), ("10", 600), ("11", 185)
    ]
    classeBM = [row[0] for row in clientperclassdata]
    nombreperclass = [row[1] for row in clientperclassdata]

    puissancefiscaldata = [
        ("4", 218998), ("5", 311777), ("6", 142271), ("7", 120484), ("8", 89501), ("9", 33204), ("10 ..", 163071)
    ]
    pfiscal = [row[0] for row in puissancefiscaldata]
    numberperpf = [row[1] for row in puissancefiscaldata]

    codeusagedata = [
        ("Privé et professionnel", 716780), ("Agricole1 véhicule dont le PTC < 3500 kg", 97865),
        ("Agricole 2 véhicule dont le PTC > 3500 kg", 14331)
        , ("Agricole Tracteur et Moissonneuse Batteuse", 25892),
        ("Utilitaire 1 véhicule dont le PTC < 3500 kg", 160104), ("Utilitaire 2 véhicule dont le PTC > 3500 kg", 8742)
        , ("Transport public de marchandise", 4066), ("Transport public de voyageurs", 33),
        ("Transport privé de personnes", 859),
        ("Taxi", 30243), ("Auto-Ecole", 3043), ("Louage", 8006), ("Transport Rural", 5535),
        ("Agences de Voyage et Hôtels", 74),
        ("Location", 1298), ("Engin de Chantiers", 2247), ("autres usages (Ambulance / Corbillard...)", 188)
    ]
    cdusage = [row[0] for row in codeusagedata]
    cdusagedata = [row[1] for row in codeusagedata]





    return render_template('dashboard-crm.html', labels=labels, values=values,types=types,poucentagetype=poucentagetype,
                         naturepolice=naturepolice,poucentagenaturepolice=poucentagenaturepolice,
                           numaccident=numaccident,countnumaccident=countnumaccident,
                           nomassurance=nomassurance,rateassurance=rateassurance,
                           classeBM=classeBM,nombreperclass=nombreperclass,
                           pfiscal=pfiscal,numberperpf=numberperpf,cdusage=cdusage,cdusagedata=cdusagedata);


@app.route('/map')
def map():
    return render_template('map.html')


@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotpassword.html')


@app.route('/mailingpassword', methods=['GET', 'POST'])
def mailingpassword():
    to = request.form['email']
    message="Password is amine"
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("amine.mbarki2013@gmail.com","Farcry42013")
    server.sendmail("amine.mbarki2013@gmail.com",to,message)

    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def login():
    error =None
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data != "amine@esprit.com" or form.password.data != 'amine':
            error_statement = "Wrong Credentials"
            return render_template('login.html', title='Login', form=form, error_statement=error_statement)
        if form.email.data == 'amine@esprit.com' and form.password.data == 'amine':
            flash('You have been logged in!', 'success')
            return redirect(url_for('dashboard'))
        else:
            error
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/predictfraudpage')
def predictfraudpage():
    return render_template('predictfraud.html', title='predection model')

@app.route('/predict', methods=['POST'])
def predict():
    codeUsage = request.form['codeUsage']
    coefBonusMalus = request.form['coefBonusMalus']
    codeMarque = request.form['codeMarque']
    puissanceFiscal = request.form['puissanceFiscal']
    energie = request.form['energie']
    codeCompagnie = request.form['codeCompagnie']
    codeAgence = request.form['codeAgence']
    typeIntermediaire = request.form['typeIntermediaire']
    naturePolice = request.form['naturePolice']
    typePolice = request.form['typePolice']
    Etat_Police = request.form['Etat_Police']
    num_accidents = request.form['num_accidents']

    arr=np.array([[codeUsage,coefBonusMalus,codeMarque,puissanceFiscal,energie,codeCompagnie,codeAgence,typeIntermediaire,naturePolice,typePolice,Etat_Police,num_accidents]])
    pred=model.predict(arr)


    return render_template('predict.html', prediction_text='BonusMalus class should be  {}'.format(pred));


@app.route('/predictfraud', methods=['POST'])
def predictfraud():
    codeUsage = request.form['codeUsage']
    classeBonusMalus = request.form['classeBonusMalus']
    codeMarque = request.form['codeMarque']
    puissanceFiscal = request.form['puissanceFiscal']
    energie = request.form['energie']
    codeCompagnie = request.form['codeCompagnie']
    codeAgence = request.form['codeAgence']
    typeIntermediaire = request.form['typeIntermediaire']
    naturePolice = request.form['naturePolice']
    typePolice = request.form['typePolice']
    Etat_Police = request.form['Etat_Police']
    num_accidents = request.form['num_accidents']

    arr=np.array([[codeUsage,classeBonusMalus,codeMarque,puissanceFiscal,energie,codeCompagnie,codeAgence,typeIntermediaire,naturePolice,typePolice,Etat_Police,num_accidents]])
    pred=fraudmodel.predict(arr)


    return render_template('predictfraud.html', prediction_text=pred);

@app.route('/predictclasseBM')
def predictclasseBM():


    return render_template('predictclasseBM.html');

@app.route('/ClientBMclass', methods=['POST'])
def ClientBMclass():
    codeUsage = request.form['codeUsage']
    import random
    number_list = [100,80,90,70,200,120,150,140,160,170,250,300,350]
    coefBonusMalus = random.choice(number_list)
    codeMarque = request.form['codeMarque']
    puissanceFiscal = request.form['puissanceFiscal']
    energie = request.form['energie']
    typeIntermediaire = request.form['typeIntermediaire']
    naturePolice = request.form['naturePolice']
    typePolice = request.form['typePolice']
    Etat_Police = request.form['Etat_Police']
    num_accidents = request.form['num_accidents']

    arr=np.array([[coefBonusMalus,codeMarque,puissanceFiscal,energie,typeIntermediaire,naturePolice,typePolice,Etat_Police,num_accidents]])
    pred=model.predict(arr)


    return render_template('predictclasseBM.html', prediction_text=pred);



if __name__ == '__main__':
    app.run()
