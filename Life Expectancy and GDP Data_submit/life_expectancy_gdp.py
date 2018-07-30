
# coding: utf-8

# # Introduction
# 
# For this project, you will act as a data researcher for the World Health Organization. You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)
# 

# ## Step 1. Import Python Modules

# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# ## Step 2 Prep The Data

# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# 
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Hint: Use `pd.read_csv()`
# 

# In[2]:


df = pd.read_csv("all_data.csv")
df.head()


# ## Step 3 Examine The Data

# The datasets are large and it may be easier to view the entire dataset locally on your computer. You can open the CSV files directly from the folder you downloaded for this project.
# 
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# What six countries are represented in the data?

# In[ ]:


#Chile, China, Germany, Mexico, United States and Zimbabwe


# What years are represented in the data?

# In[ ]:


#The data spans from 2000 to 2015


# ## Step 4 Tweak The DataFrame
# 
# Look at the column names of the DataFrame `df` using `.head()`. 

# In[3]:


df.columns


# What do you notice? The first two column names are one word each, and the third is five words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)). </font>

# In[4]:


df.rename(columns={ 'Life expectancy at birth (years)':'LEABY'}, inplace=True)


# Run `df.head()` again to check your new column name worked.

# In[5]:


df.head()


# ---

# ## Step 5 Bar Charts To Compare Average

# To take a first high level look at both datasets, create a bar chart for each DataFrame:
# 
# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 
# Remember to `plt.show()` your chart!

# In[6]:



fig, ax = plt.subplots(figsize=(10,10))
ax = sns.barplot(x="Country", y="GDP", data=df, palette="rocket")
plt.xlabel("Country", fontsize=14)
plt.ylabel("GDP", fontsize=14)
plt.title("Gross Domestic Product (GDP) Average by Country from 2000 to 2015", fontsize=14)
plt.savefig("GDPAverageByCountry_Barplot.png")
plt.show()


# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.
# Remember to `plt.show()` your chart!

# In[7]:


fig2, ax2 = plt.subplots(figsize=(10,10))
ax2 = sns.barplot(x="Country", y="LEABY", data=df, palette="rocket")
plt.xlabel("Country", fontsize=14)
plt.ylabel("LEABY", fontsize=14)
plt.title("Life Expectancy Average by Country from 2000 to 2015", fontsize=16)
plt.savefig("LEABYAverageByCountry_Barplot.png")
plt.show()


# What do you notice about the two bar charts? Do they look similar?

# In[ ]:


#The bar charts are drastically different, with most countries exhibiting a similar life expectancy range (with the exception of Zimbabwe)
#but most countries exhibiting a dramatic difference between their average GDP, with no country coming close to the USA's average. 


# ## Step 6. Violin Plots To Compare Life Expectancy Distributions 

# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# 
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# 1. Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 
# 2. Be sure to show your plot

# In[29]:


fig = plt.subplots(figsize=(15, 10)) 
ax = sns.violinplot(data=df, x="Country", y="LEABY", palette="muted", scale="count", inner="quartile")
#sns.set_style("whitegrid")
plt.xlabel("Country", fontsize=16)
plt.ylabel("LEABY", fontsize=16)
plt.title("Life Expectancy Distribution by Country between 2000 and 2015", fontsize=18)
plt.savefig("LEABYDistributionByCountry_Violinplot.png")
plt.show()


# What do you notice about this distribution? Which country's life expectancy has changed the most?
# 
# #Zimbabwe's life expectency has dramatically increased in comparison to the other countries, but also has the most dramatic range betweeen outliers.  The average age is somewhere around 48. 
# -The other countries have the majority of their distribution between 70 and 80, with Germany exhibitiong the highest distribution of ages 80 and older out of all of the countries displayed. 

# ## Step 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.
# 

# In[33]:


f, ax = plt.subplots(figsize=(10,10)) 
#sns.set_style("whitegrid")
colors=sns.cubehelix_palette(16, start=.5, rot=-.75)
ax = sns.barplot(x="Country",y="GDP", data=df, hue="Year", palette=colors)
plt.xticks(rotation=45)
plt.title("Total GDP by Country", fontsize=16)
plt.ylabel("GDP in Trillions of U.S. Dollars", fontsize=14)
plt.xlabel("Country",fontsize=14)
plt.savefig("TotalGDPByCountryAndYear_Barplot.png")
plt.show()


#extra grids for practice-->

f2, ax2 = plt.subplots(figsize=(10,10))
#sns.set_style("whitegrid")
df2 = df[df.Country == "Zimbabwe"]
ax2 = sns.barplot(x="Country", y="GDP", data=df2,hue="Year", palette=colors )
plt.title("Zimbabwe's Gross Domestic Product Totals by Year", fontsize=16)
plt.ylabel("Zimbabwe's GDP in Trillions of U.S. Dollars", fontsize=14)
plt.savefig("ZimbabweTotalGDPByYear_Barplot.png")
plt.show()

f4, ax4 = plt.subplots(figsize=(10,10))
#sns.set_style("whitegrid")
df4 = df[df.Country == "Zimbabwe"]
ax4 = sns.barplot(x="Country", y="LEABY", data=df4,hue="Year", palette=colors )
plt.title("Zimbabwe's Life Expectancy Average by Year", fontsize=16)
plt.ylabel("Zimbabwe's Life Expectancy Average", fontsize=14)
# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.1)
plt.savefig("ZimbabweTotalLEABYByYear_Barplot.png")
plt.show()

f3, ax3 = plt.subplots(figsize=(10,10))
#sns.set_style("whitegrid")
df3 = df[df.Country.isin(['Zimbabwe','Chile'])]
ax3 = sns.barplot(x="Country", y="GDP", data=df3,hue="Year" ,estimator=np.median, palette=colors)
plt.title("Comparison of the GDP in Chile vs Zimbabwe", fontsize=16)
plt.ylabel("Gross Domestic Product Totals in Trillions of U.S. Dollars", fontsize=14)
plt.xlabel("Country",fontsize=14)
plt.savefig("GDPinChileVSZimbabwe_Barplot.png")
plt.show()


# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`
# 

# In[12]:


f, ax = plt.subplots(figsize=(8,11)) 
#cmap = sns.cubehelix_palette(8, start=.5, rot=-.75)
#colors=sns.cubehelix_palette(16)
colors=sns.cubehelix_palette(16, start=.5, rot=-.75)
ax = sns.barplot(x="Country",y="LEABY", data=df, hue="Year",palette=colors )
plt.xticks(rotation=45)
plt.title("Life Expectancy Over Time by Country", fontsize=16)
plt.ylabel("Life Expectancy at Birth in Years", fontsize=14)
plt.xlabel("Country",fontsize=14)
# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.1)
plt.savefig("LEABYByCountryOverTime.png")
plt.show()

#just playing around a bit here
f2, ax2 = plt.subplots(figsize=(10,10))
sns.set_style=("whitegrid")
ax2 = sns.stripplot(x="Country", y="LEABY", data=df, palette=colors)
plt.xticks(rotation=45)
plt.title("Life Expectancy by Country", fontsize=16)
plt.savefig("LEABYByCountry_Stripplot.png")
plt.show()

#just playing around a bit here
f3, ax3 = plt.subplots(figsize=(10,10))
sns.set_style=("whitegrid")
ax3 = sns.stripplot(x="Year", y="LEABY",hue="Country", data=df, palette="rocket")
plt.xticks(rotation=45)
plt.title("Life Expectancy by Year and Country", fontsize=16)
plt.savefig("LEABYByYearAndCountry_Stripplot.png")
plt.show()


# What are your first impressions looking at the visualized data?
# 
# - Which countries' bars changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - How do countries compare to one another?
# - Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# - Can you think of any reasons that the data looks like this for particular countries?

# In[ ]:


# First impressions:
# 1. What countries' bars change the most?
#      Zimbabwe's life expectancy bars change the most, and is the only country that has a decrease and then a steep increase in
#      the average life expectancy years. China's GDP looks like it has the most dramatic change out of all of the countries
# 2. What years have biggest change? 

# 3. Least change in GDP over time:  

# 4. Countries compare to each other:
#        Its strange that Chile seems to have the current highest life expectency and yet has the second lowest GDP between all 
#        of the countries.
# 5. What do you think about the relationship between GDP and life expectancy? 
#        The years seem to all have a stable increase between them for all countries except Zimbabwe.  There are a few instances in
#        China and Mexico where the life expectancy drops and then climbs back up the next year.  Zimbabwe reached it's lowespt point 
#        for life expectancy in 2003, and from the chart that just shows Zimbabwe's data, it looks like 2004 was the lowest point for
#        GDP, which would show a correlation between a shorter life expectancy and a lower GDP within the country.
# 6. The data seems to be showing that the smaller, poorer countries are more significantly impacted by a lower average life expectancy.
#    Why is this? 
#       Because the best way to eliminate poverty is through economic growth. 
#       Poverty being one of the principle drivers of short lifespans, you would naturally expect to see life expectancy go up 
#       as GDP per capita increases.


# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose. In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# ## Step 8. Scatter Plots of GDP and Life Expectancy Data

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`. A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!
#     
# Since this may be the first time you've learned about FacetGrid, we have prepped a fill in the blank code snippet below. 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 

# In[14]:


# WORDBANK:
# "Year"
# "Country" 
# "GDP" 
# "LEABY" 
# plt.scatter


# Uncomment the code below and fill in the blanks
g = sns.FacetGrid(df, col="Year", hue="Country", col_wrap=4, size=2)
g = (g.map(plt.scatter,"GDP","LEABY", edgecolor="w").add_legend())
#g = (g.map(plt.plot, "Year", "LEABY").add_legend())

plt.savefig("GDPAndLEABYFacteGrid_Scatterplot.png")
plt.show()


# + Which country moves the most along the X axis over the years?
# + Which country moves the most along the Y axis over the years?
# + Is this surprising?
# + Do you think these scatter plots are easy to read? Maybe there's a way to plot that! 

# In[64]:


# 1. it looks like China might move the most across the X axis; It also looks like the United States moves quite a bit across 
#    the x-axis.
# 2. Most of the countries stay between the 70 and 80 year range on the y-axis; the only country that has dramatic movement
#    across the y-axis is Zimbabwe.
# 3. Not surprising, based off of the other chart's data the United States had the biggest GDP growth, and Zimbabwe had the
#    most dramatic swing for life expectancy in the 15-year span.
# 4. I think this is difficult to read with all of the years on a seperate graph, and it would be easier to visualize the 
#    movement of the data points across the years if the graph was in a different format.


# ## Step 9. Line Plots for Life Expectancy

# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph. A few other things have to change as well. So we have created a different codesnippets with fill in the blanks.  that makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.
# 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 
# 

# In[15]:


# WORDBANK:
# plt.plot
# "LEABY"
# "Year"
# "Country"


# Uncomment the code below and fill in the blanks
g2 = sns.FacetGrid(df, col="Country", palette="tab20c", col_wrap=3, size=4, )
g2 = (g2.map(plt.plot, "Year", "LEABY").add_legend())

plt.savefig("LEABYByCountry_FacetGrid.png")


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
#     zimbabwe is the only country that has a significant decline and then a dramatic increase in life expectancy
# - What years are there the biggest changes in the data?
#     it looks like between 200 and 2005 showed the biggest changes for *most* countries, although mexico stays pretty flat to the
#     75 line during this time
# - Which country has had the least change in life expectancy over time? 
#     mexico?
# - Can you think of any reasons that the data looks like this for particular countries?

# ## Step 10. Line Plots for GDP

# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# 
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis. Change the color on your own! Be sure to show your plot.
# 

# In[16]:


g3 = sns.FacetGrid(df, col="Country", col_wrap=3, size=4)
#sns.set_style("whitegrid")
g3 = (g3.map(plt.plot, "Year", "GDP").add_legend())
plt.savefig("GDPByCountry_FacetGrid.png")
plt.show()


# In[27]:


df["LEABY"].groupby(df['Country']).mean().round(2)


# Which countries have the highest and lowest GDP?

# In[ ]:


#This set of graphs makes it obvious that the United States has the highest GDP out of all of the countries, and Zimbabwe 
#has the lowest GDP; you can't see any movement in the line for Zimbabwe, it looks like it has flatlined, just because the 
#increase is so small in comparison to the other countries


# Which countries have the highest and lowest life expectancy?

# In[ ]:


#Germany has the highest life expectancy, and Zimbabwe, although much improved over the last decade and a half, still has the
#lowest life expectancy of all the countries. 


# ## Step 11 Researching Data Context 

# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# In[ ]:


#also what happened to Zimbabwe that caused the life expectancy to drop around 2003-2004
#what happened to china in the past 10 years that increased the GDP so drastically? 
#You can see the dip in the United State's GDP around the time of the recession in 2009


# ## Step 12 Create Blog Post

# Use the content you have created in this Jupyter notebook to create a blog post reflecting on this data.
# Include the following visuals in your blogpost:
# 
# 1. The violin plot of the life expectancy distribution by country
# 2. The facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
# 3. The facet grid of line graphs mapping GDP by country
# 4. The facet grid of line graphs mapping Life Expectancy by country
# 
# 
# We encourage you to spend some time customizing the color and style of your plots! Remember to use `plt.savefig("filename.png")` to save your figures as a `.png` file.
# 
# When authoring your blog post, here are a few guiding questions to guide your research and writing:
# + How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?
# + What would have helped make the project data more reliable? What were the limitations of the dataset?
# + Which graphs better illustrate different relationships??
