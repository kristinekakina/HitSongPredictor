import os
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_bcrypt import generate_password_hash, check_password_hash
# from database import Users, House
from os import path
from werkzeug.utils import secure_filename
import pandas
# from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy import Table

# from flask import Flask, Session
# from flask.ext.session import Session
#
# SESSION_TYPE = 'memcache'
#
# app = Flask(__name__)
# sess = Session()
#
# app = Flask(__name__)
# app.secret_key = "bnvsdnvsfvdvkvnjvdvdkbvdsc"

#
# establish the connection with the engine object
# with engine.connect() as conn:
# Create the engine to connect to the inbuilt
# sqllite database\
engine = create_engine("sqlite+pysqlite:///:memory:")

# Read data from CSV which will be
# loaded as a dataframe object
data = pandas.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Kenya.csv')
data1 = pandas.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Naija.csv')

# print the sample of a dataframe
print(data.head())
print(data1.head())

# Write data into the table in sqllite database
data.to_sql('Track_data', engine)
data1.to_sql('Track_data1', engine)

with engine.connect() as conn:
    # let's select the column credit_history
    # from the data table
    result = conn.execute(text("SELECT track_id FROM Track_data"))
    result1 = conn.execute(text("SELECT album FROM Track_data1"))

# print the result
for row in result:
    print(row.track_id)
for row in result1:
    print(row.album)

# engine = create_engine('sqlite:////tmp/test.db')
metadata = MetaData(bind=engine)
users = Table('Track_data', metadata, autoload=True)
con = engine.connect()
# con.execute(users.insert(), name='admin', email='admin@localhost')
#
#
# with engine.connect() as conn:
#     # let's select the column credit_history
#     # from the data table
#     #     result3 = engine.execute('select * from Track_data where artist =="Nyashinski"').first()
#     result3 = engine.execute('select energy from Track_data where track_id =="run"').first()
#     result4 = engine.execute('select liveness from Track_data where track_id =="run"').first()
#     result5 = engine.execute('select danceability from Track_data where track_id =="run"').first()
#     result6 = engine.execute('select speechiness from Track_data where track_id =="run"').first()
#     # result7 = engine.execute('select speechiness from Track_data where speechiness >= 0.5').first()
#     print("The liveness is", result4)
#     print("The energy is", result3)
#     print("The danceability is", result5)
#     print("The speechiness is", result6)
#     # /////////////////////////////
#
#     result8 = engine.execute(
#         'select track_id =="2EISZ7FY6AkSP8ObzenBcB"  from Track_data where danceability >= 0.4').first()
#     result7 = engine.execute(
#         'select track_id =="2EISZ7FY6AkSP8ObzenBcB"  from Track_data where liveness >= 0.4').first()
#     result9 = engine.execute('select track_id =="2EISZ7FY6AkSP8ObzenBcB"  from Track_data where energy >= 0.4').first()
#     result10 = engine.execute(
#         'select track_id =="2EISZ7FY6AkSP8ObzenBcB"  from Track_data where speechiness >= 0.4').first()
#     # print the result
#     print(result8)
#     print(result7)
#     print(result9)
#     print(result10)
#     # variables = ["result7", "result3", "result5", "result6"]
#     for danceability in result8:
#         if danceability == 1:
#             print("danceability is good")
#         else:
#             print("danceability is bad",0)
#     for liveness in result7:
#         if liveness == 1:
#             print("liveness is good",1)
#         else:
#             print("liveness is bad",0)
#     for energy in result9:
#         if energy == 1:
#             print("energy is good",1)
#         else:
#             print("energy is bad",0)
#     for speechiness in result10:
#         if speechiness == 1:
#             print("speechiness is good",1)
#         else:
#             print("speechiness is bad",0)
#     sumation = danceability + liveness + energy + speechiness
#     if sumation == 2:
#         print("possibly")
#     elif sumation > 2:
#         print("hit")
#     else:
#         print("flop")
#
# # print the result


app = Flask(__name__)

app.debug = True


@app.route('/', methods=["POST", "GET"])
def url():
    if request.method == "POST":
        run = request.form["url"]
        # sqllite database\
        engine1 = create_engine("sqlite+pysqlite:///:memory:")

        # Read data from CSV which will be
        # loaded as a dataframe object
        data_kenya = pandas.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Kenya.csv')
        data_naija = pandas.read_csv(r'C:\Users\user\PycharmProjects\hitMusicPredictor\Naija.csv')

        # print the sample of a dataframe
        # print(data.head())
        # print(data1.head())

        # Write data into the table in sqllite database
        data_kenya.to_sql('Track_data', engine1)
        data_naija.to_sql('Track_data1', engine1)

        with engine1.connect() as CONN:

            # let's select the column credit_history
            # from the data table
            result = CONN.execute(text("SELECT track_id FROM Track_data"))
            result1 = CONN.execute(text("SELECT album FROM Track_data1"))
        # To test print the result
        # for row in result:
        #     print(row.track_id)
        # for row in result1:
        #     print(row.album)

        # /////////////////////////////////////

        # engine = create_engine('sqlite:////tmp/test.db')
        meta_data = MetaData(bind=engine1)
        users = Table('Track_data', meta_data, autoload=True)
        CONN = engine1.connect()
        # con.execute(users.insert(), name='admin', email='admin@localhost')

        with engine1.connect() as CONN:
            # let's select the column credit_history
            # from the data table
            #     result3 = engine.execute('select * from Track_data where artist =="Nyashinski"').first()
            result3 = engine1.execute('select energy from Track_data where track_id =="1QgM3SejXDyHkqt0guA4TX"').first()
            result4 = engine1.execute(
                'select liveness from Track_data where track_id =="1QgM3SejXDyHkqt0guA4TX"').first()
            result5 = engine1.execute(
                'select danceability from Track_data where track_id =="1QgM3SejXDyHkqt0guA4TX"').first()
            result6 = engine1.execute(
                'select speechiness from Track_data where track_id =="1QgM3SejXDyHkqt0guA4TX"').first()
            # result7 = engine.execute('select speechiness from Track_data where speechiness >= 0.5').first()
            print("The liveness is", result4)
            print("The energy is", result3)
            print("The danceability is", result5)
            print("The speechiness is", result6)
            # /////////////////////////////
            # with engine1.connect() as CONN:
            dancing = engine1.execute(
                    'select track_id =="1QgM3SejXDyHkqt0guA4TX" from Track_data where danceability >= 0.5').first()

            live = engine1.execute(
                    'select track_id =="1QgM3SejXDyHkqt0guA4TX"  from Track_data where liveness >= 0.4').first()
            energyopor = engine1.execute(
                    'select track_id =="1QgM3SejXDyHkqt0guA4TX"  from Track_data where energy >= 0.4').first()
            speech = engine1.execute(
                    'select track_id =="1QgM3SejXDyHkqt0guA4TX"  from Track_data where speechiness >= 0.4').first()
            # result11 = engine.execute(
            # 'SELECT @runs := run FROM Track_data WHERE track_id == runs  AND speechiness >0.4').first()

            # print the result
            print(dancing)
            print(live)
            print(energyopor)
            print(speech)
            # variables = ["result7", "result3", "result5", "result6"]
            for danceability in dancing:
                if danceability == 1:
                    print("danceability is good")
                else:
                    print("danceability is bad")
            for liveness in live:
                if liveness == 1:
                    print("liveness is good")
                else:
                    print("liveness is bad")
            for energy in energyopor:
                if energy == 1:
                    print("energy is good")
                else:
                    print("energy is bad")
            for speechiness in speech:
                if speechiness == 1:
                    print("speechiness is good")
                else:
                    print("speechiness is bad")
            total = danceability + liveness + energy + speechiness
            if total == 2:
                print("possibly")
            elif total > 2:
                print("hit")
            else:
                print("flop")

    return render_template("predictor.html")


if __name__ == '__main__':
    # app.config['SESSION_TYPE'] = 'memcached'
    # app.config['SECRET_KEY'] = 'super secret key'
    # sess = Session()
    app.debug = True
    app.run()
