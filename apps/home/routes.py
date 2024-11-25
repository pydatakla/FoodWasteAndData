from apps.home import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from plotly.offline import plot
from flask import Markup

# Visualization dependences
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# @blueprint.route('/index')
# @login_required
# def index():
#     return render_template('pages/index.html', segment='index')

# Install necessary libraries if not already installed
# Load the data from the CSV file

# df = pd.read_csv('D:/PyData Kampala/FoodWaste/FoodWasteAndData/Data/African_data.csv')

# Since there's no continent column, we'll use the whole dataset
# and assume all countries are in Africa for this example.
# Replace this with your actual logic to identify African countries
# if you have other data or a different column indicating continent.

# africa_df = df

# Create the Choropleth map
# fig = go.Figure(data=go.Choropleth(
#     locations=africa_df['country'],
#     z=africa_df['loss_percentage'],
#     locationmode='country names',
#     colorscale='Oranges',
#     autocolorscale=False,
#     marker_line_color='darkgray',
#     marker_line_width=0.5,
#     colorbar_title='Percentage Loss',
# ))

# fig = fig.update_layout(
#     title_text='Percentage Loss in Africa', #Updated title to reflect data used
#     geo=dict(
#         showframe=False,
#         showcoastlines=False,
#         projection_type='equirectangular'
#     )
# )


# Visualization code
# Read csv
data = pd.read_csv('D:/PyData Kampala/FoodWaste/FoodWasteAndData/foodloss/data2_cleaned.csv')
# data.head(3)

import pycountry_convert as pc
def get_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        return continent_code
    except KeyError:
        return None

data['continent'] = data['country'].apply(get_continent)

africa_data = data[data['continent']=='AF'].reset_index(drop=True)

# East Africa
ea_data = africa_data.query("country == 'Burundi' or country == \
                            'Democratic Republic of the Congo' or country == \
                            'Kenya' or country == 'Rwanda' or country == \
                            'Somalia' or country == 'South Sudan' or \
                            country == 'Uganda' or country == \
                            'United Republic of Tanzania'").reset_index(drop=True)


#what are east africa's top five foods?
ea_top_five = ea_data.groupby('commodity')['loss_percentage'\
                                           ].count().sort_values(\
                                               ascending=False
                                               ).reset_index()


ea_data_top = ea_data.query("commodity == 'Maize (corn)' or commodity \
                            == 'Rice' or commodity == \
                            'Sorghum' or commodity == \
                            'Millet' or commodity \
                            == 'Wheat'"
                            ).reset_index(drop=True)

ea_data_grouped = ea_data.groupby('country')['loss_percentage'].mean(
            ).sort_values(ascending=False
                          ).reset_index(name='average_loss_percentage')

ea_data_top_grouped = ea_data_top.groupby('country')['loss_percentage'].mean(
    ).sort_values(ascending=False
                  ).reset_index(name='average_loss_percentage')

ea_data_top_grouped = ea_data_top.groupby('country')['loss_percentage'].mean(
            ).sort_values(ascending=False
                          ).reset_index(name='average_loss_percentage')

# Plots
# import geopandas as gpd
# world = gpd.read_file("D:/PyData Kampala/FoodWaste/FoodWasteAndData/foodloss/countries/ne_110m_admin_0_countries.shp")
# ea_data1 = ea_data_top_grouped.merge(world, left_on='country', \
#                                      right_on='SOVEREIGNT', how='left')
# geo_ea_data = gpd.GeoDataFrame(ea_data1, \
#                                geometry='geometry')

# # Visualize East Africa
# fig, ax = plt.subplots(1, 1, figsize=(12, 8))
# geo_ea_data.plot(
#     column='average_loss_percentage', 
#     cmap='YlGnBu', 
#     legend=True, 
#     legend_kwds={
#         'label': "Mean Loss Percentage",
#         'orientation': "vertical",
#         'shrink': 0.5,            
#         'pad': 0.02,              
#     },
#     ax=ax,
#     edgecolor='black'
# )

# ax.set_title('Average Wastage of Top Five Foods from East Africa (2000-2022)', fontsize=12, fontweight='bold')
# ax.axis('off')
# plt.savefig('eamap1.png', dpi=600, bbox_inches='tight')
# east_africaGeo = plt.show()

# #average wastage of the top five foods by east african countries through years
# top_foods_wastage = ea_data_top.groupby(['year', 'commodity'])\
#     ['loss_percentage'].mean(\
#         ).reset_index()
# # top_foods_wastage

# plt.figure(figsize=(12, 6))
# sns.lineplot(data=top_foods_wastage, 
#              x='year', 
#              y='loss_percentage', 
#              hue='commodity',
#              palette='Blues',
#              linewidth=2.0)
# plt.title('Average Wastage of Top Five Foods in East Africa from 2000 to 2022 ', fontsize=12, fontweight='bold')
# plt.xlabel('Year', fontsize=10, fontweight='bold')
# plt.ylabel('Average Loss Percentage (%)', fontsize=10, fontweight='bold')
# plt.legend(title='Commodity', fontsize=10)
# plt.tight_layout()
# plt.savefig('lineplot1.png', dpi=600, bbox_inches='tight')
# viz2 = plt.show()

# #activites that cause most wastage of the top five foods in east african countries
# top_foods_wastage_activity = ea_data_top.groupby('activity'\
#                                                  )['loss_percentage\
#                                                    '].count().sort_values(\
#                                                        ascending=False
#                                                        ).reset_index(name='count')

# viz3 = plt.figure(figsize=(10, 6))
# sns.barplot(data=top_foods_wastage_activity.head(), 
#             x='count', 
#             y='activity', 
#             hue='activity',
#             palette='Blues',
#             dodge=False,
#             legend=False)

# v3z3 = viz3.title('Activities Causing Most Wastage of Top 5 Foods in East Africa', 
#           fontsize=12, fontweight='bold')
# v3z3 = viz3.xlabel('Wastage Occurrences', fontsize=10, 
#            fontweight='bold')
# plt.ylabel('Activity', fontsize=10, 
#            fontweight='bold')
# v3z3 = viz3.gca().invert_yaxis()
# v3z3 = viz3.tight_layout()
# v3z3 = viz3.show()

@blueprint.route("/index/", methods=['POST', 'GET'])
@login_required
def index():
    # viz1Plot = visualize(east_africaGeo)
    # viz2Plot = visualize(viz2)
    # print(request.method)
    # if request.method == 'POST':
    #     continent = request.form['continents']
    #     print("Your Selection is", continent)
    #     return render_template('pages/index.html', viz = viz,
    #     data=[{'continents': 'Continent'}, {'continents': 'Africa'}, {'continents': 'Europe'}, {'continents': 'Asia'}, {'continents': 'South America'},
    #           {'continents': 'North America'}])

    # else:
    #     print("No Selection")
    #     return render_template('pages/index.html', viz = viz,
    #     data=[{'continents': 'Continent'}, {'continents': 'Africa'}, {'continents': 'Europe'}, {'continents': 'Asia'}, {'continents': 'South America'},
    #           {'continents': 'North America'}])

    return render_template('pages/index.html',
                        #    viz1=viz1Plot,
                        #    viz2=viz2Plot
                           )

def visualize(plot):
    # include_plotlyjs = True builds in the js library
    # output_type = 'div' outputs the html code


    # Markup directly renders the html code
    viz = Markup(plot)
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
