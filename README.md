# FoodWasteAndData
# Title
Development of a Food Waste Dashboard for EAC countries

## Introduction
Today, the world faces uncertainty about food security largely due to food wastage along the whole food supply chain. 
Over a third of all food produced (around 2.5 billion tons) is lost or wasted yearly. One year of this occurs in the food production stage. Boston Consulting
Group (BCG) estimates this wasted food is worth $230 billion.

Researchers estimate the lost food calories from food waste amount to roughly 24% of the total available food
calories. To put this in perspective, the UN reports that about a third of the global population, mostly in developing countries
and low-income countries, didn't have enough access to food in 2020, an increase of 320 million people from the previous year.

According to UCU Mukono, food wastage makes up 65-79% of solid waste in landfills in Uganda, causing environmental and health problems.
Globally, the problem is predicted to increase, causing higher global food insecurity.

## Description
This project seeks to create a data tool to address Global Food Insecurity  through;
<ul>
<li>Analysis of World Datasets on Food Demand and Wastage in Africa</li>
<li>Visualize World Food Waste and Demand Data</li>
<li>Predict food demands and waste in Africa</li>
</ul>

## Core Features
<ul>
<li> Analysis and Visualization of Food Demand and Waste Data</li>
<li> Food Demand and Waste Predictions</li>
</ul>

## Scope
This project shall address Africa Food Insecurity through the mitigation of Food Waste
at the following levels.
<ul>
<li>Regional level (for example, East Africa, Southern Africa, etc) </li>
<li>Country level (for example Uganda, Kenya, Democratic Republic of Congo, Sudan, etc) </li>
</ul>


# Submission
## Summary of Data Sources

The dataset provides insights into food loss across various commodities, regions, and supply stages. It includes detailed records highlighting the extent, causes, and stages of food loss. The data was obtained from the website of the Food and Agriculture Organization of the United Nations ([FAO](https://www.fao.org/platform-food-loss-waste/flw-data/en/))

## General Information
- **Total Records**: 25,416
- **Number of Columns**: 18

## Key Attributes
1. **m49_code and country**: Numerical and textual identifiers for countries, which help in classifying data by region and location.
2. **cpc_code and commodity**: Codes and names of food commodities, such as "Rice, milled."
3. **year**: Indicates the year of data collection, enabling trends over time.
4. **loss_percentage and loss_quantity**: Provides quantitative measures of food loss, showing the percentage and actual quantity lost.
5. **activity and food_supply_stage**: Describes the specific supply chain stages (e.g., storage) where losses occurred and the activities linked to these losses.
6. **method_data_collection and reference**: Specifies the data collection methods used (e.g., controlled experiments) and references to sources, providing context to the data's reliability.
7. **Other Columns**: Includes region, cause_of_loss, treatment, sample_size, URL, and notes. These provide further detail on the context, causes (e.g., rodents), and methods of treatment for the loss (e.g., trapping vs. no trapping).

## Sample Data
- **Example**: For the commodity "Rice, milled" in Myanmar, 2015, the dataset records varying loss percentages, such as 1.78% and 11.77%.
- **Food Supply Stage**: Loss typically occurs during storage.
- **Cause of Loss**: Commonly attributed to rodents, with treatments like "trapping" or "no trapping."
- **Data Collection Method**: Mostly based on controlled experiments.

## Data Completeness
- **Missing Values**: Some columns, like loss_quantity, treatment, and cause_of_loss, contain missing data.
- **Core Columns**: Columns such as country, commodity, year, and loss_percentage are fully populated, ensuring consistency in the analysis of food loss trends.

---

## Methods
The dataset relies on various methods for data collection, with "controlled experiments" frequently mentioned. This suggests a structured approach to gathering data, where variables are managed to ensure accurate measurements of food loss. However, given that some columns have missing values, further data imputation or cleaning might be necessary for comprehensive analysis.

## Data Cleaning
Out of the 18 columns in the dataset, only six(country, cpc_code, commodity, loss_percentage, activity, and food_supply_stage) were maintained, as these were the only ones relevant to our study. The rest were dropped. 
The column of activity and food_supply_stage had a few random missing entries, which were filled with the keyword 'Not Recorded'. This helped us to maintain the dataset without null values and thus keep all the rows without deleting them.

## Data Transformation
On the cleaned dataset, the column for the continent was appended to allow identification of the countries by their continents and thus filter out for the African data, which made it easy to locate East African countries.

## Justification for Data Selection and Use
This dataset is valuable for understanding food loss patterns globally and at a regional level. It enables the identification of key factors influencing loss (such as storage conditions) and can inform strategies to reduce food waste. Quantitative data (loss percentage) and qualitative information (activity) provide a holistic view of food loss dynamics. 

Given its extensive records and detailed attributes, the dataset is suitable for both regional and global analyses of food waste reduction initiatives, making it a critical resource for policymakers, researchers, and industry stakeholders focused on improving food security and sustainability.

## Key Insights
- **Variation in Loss**: There is considerable variation in food loss percentages across different commodities. Understanding the reasons behind this variation can help target specific interventions.
- **Stage-Specific Losses**: Storage is a critical stage for food loss, indicating better storage solutions to minimize waste.
- **Prevalence of Rodents**: Rodent-related losses are a significant cause across many commodities, pointing to the importance of pest control measures.
- **Data Gaps**: Missing values in certain columns highlight areas where data collection could be improved, particularly for causes and treatments.

</ul>


