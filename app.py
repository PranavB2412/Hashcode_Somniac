from flask import Flask, render_template,url_for

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('landing_page.html')


@app.route('/profile')
def display_profile():
    return render_template('profile.html')


@app.route('/sleep_statistics')
def display_sleep_stats():
    return render_template('sleepStatistics.html')


@app.route('/recommendations')
def display_recommendations():
    return render_template('recommendations.html')


@app.route('/nap')
def display_nap():
    return render_template('nap.html')


if __name__=="__main__":
    app.run(debug=True)