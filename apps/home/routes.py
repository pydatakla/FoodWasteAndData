from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from plotly.offline import plot
from flask import Markup
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# @blueprint.route('/index')
# @login_required
# def index():
#     return render_template('pages/index.html', segment='index')

# Install necessary libraries if not already installed
# Load the data from the CSV file

df = pd.read_csv('D:/PyData Kampala/FoodWaste/FoodWasteAndData/Data/African_data.csv')

# Since there's no continent column, we'll use the whole dataset
# and assume all countries are in Africa for this example.
# Replace this with your actual logic to identify African countries
# if you have other data or a different column indicating continent.

africa_df = df

# Create the Choropleth map
fig = go.Figure(data=go.Choropleth(
    locations=africa_df['country'],
    z=africa_df['loss_percentage'],
    locationmode='country names',
    colorscale='Oranges',
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title='Percentage Loss',
))

fig = fig.update_layout(
    title_text='Percentage Loss in Africa', #Updated title to reflect data used
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    )
)

@blueprint.route("/index/", methods=['POST', 'GET'])
@login_required
def index():
    viz = visualize()
    print(request.method)
    if request.method == 'POST':
        continent = request.form['continents']
        print("Your Selection is", continent)
        return render_template('pages/index.html', viz = viz,
        data=[{'continents': 'Continent'}, {'continents': 'Africa'}, {'continents': 'Europe'}, {'continents': 'Asia'}, {'continents': 'South America'},
              {'continents': 'North America'}])

    else:
        print("No Selection")
        return render_template('pages/index.html', viz = viz,
        data=[{'continents': 'Continent'}, {'continents': 'Africa'}, {'continents': 'Europe'}, {'continents': 'Asia'}, {'continents': 'South America'},
              {'continents': 'North America'}])

def visualize():
    # include_plotlyjs = True builds in the js library
    # output_type = 'div' outputs the html code
    viz = plot(fig, include_plotlyjs = True, output_type = 'div')

    # Markup directly renders the html code
    viz = Markup(viz)
    return viz


@blueprint.route('/typography')
@login_required
def typography():
    return render_template('pages/typography.html')

@blueprint.route('/color')
@login_required
def color():
    return render_template('pages/color.html')

@blueprint.route('/icon-tabler')
@login_required
def icon_tabler():
    return render_template('pages/icon-tabler.html')

@blueprint.route('/sample-page')
@login_required
def sample_page():
    return render_template('pages/sample-page.html')  

@blueprint.route('/accounts/password-reset/')
def password_reset():
    return render_template('accounts/password_reset.html')

@blueprint.route('/accounts/password-reset-done/')
def password_reset_done():
    return render_template('accounts/password_reset_done.html')

@blueprint.route('/accounts/password-reset-confirm/')
def password_reset_confirm():
    return render_template('accounts/password_reset_confirm.html')

@blueprint.route('/accounts/password-reset-complete/')
def password_reset_complete():
    return render_template('accounts/password_reset_complete.html')

@blueprint.route('/accounts/password-change/')
def password_change():
    return render_template('accounts/password_change.html')

@blueprint.route('/accounts/password-change-done/')
def password_change_done():
    return render_template('accounts/password_change_done.html')

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
