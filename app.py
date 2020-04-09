from flask import Flask, json, render_template
from covid import Covid
from datetime import datetime

app = Flask(__name__)
covid = Covid()

results = covid.get_data()

# countries = covid-visualizer.list_countries()
# italy_cases = covid-visualizer.get_status_by_country_name("italy")

d = datetime.now()
date = d.date()
hour = d.hour
minute = d.minute
second = d.second
time = str(hour) + "." + str(minute) + "." + str(second)
date = str(date) + '(' + time + ')'
# print(date)


@app.route('/')
def hello_world():
    # print(results)
    return render_template('covid.html', results=results, date=date)


if __name__ == '__main__':
    app.run()
