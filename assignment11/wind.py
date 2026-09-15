# Task 3: Interactive Visualizations with Plotly

import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')

# print haed and tail of the dataframe
print(df.head(10))
print(df.tail(10))


# Clean the data. You need to convert the 'strength' column to a float. 
# Use of str.replace() with regex is one way to do this, followed by type conversion.
print(df['strength'].unique())  # Check unique values in the 'strength' column before cleaning

# we see that the strength column has values like '0-1', '1-2' or '6+' 
# we convert these to just the first number, remove -+ and then convert to float.  

df['strength'] = df['strength'].str.replace(r'[-+].*$', '', regex=True).astype(float)

# print head and tail of the dataframe after cleaning
print(df.head(10))
print(df.tail(10))

# check the unique values in the 'strength' column after cleaning
print(df['strength'].unique())

# Create an interactive scatter plot of strength vs. frequency, with colors based on the direction.
fig = px.scatter(
    df, 
    x='strength', 
    y='frequency', 
    color='direction', 
    title='Wind Strength vs. Frequency'
)

fig.show()

# Save the HTML file
fig.write_html("wind.html", include_plotlyjs='cdn')