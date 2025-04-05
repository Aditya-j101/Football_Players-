import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.plotting import figure,show
from bokeh.models import HoverTool
dataframe = pd.read_csv('FIFA17_official_data.csv')
df1 = pd.DataFrame(dataframe , columns=['Name','Wage','Value'])#extract the columns from the database
def clean_currency(value):
    # Remove currency symbols and 'K' or 'M' for thousands or millions
    if 'K' in value:
        return int(float(value.replace('€', '').replace('K', '').replace(',', '').strip()) * 1000)
    elif 'M' in value:
        return int(float(value.replace('€', '').replace('M', '').replace(',', '').strip()) * 1000000)
    else:
        return int(value.replace('€', '').replace(',', '').strip())

# Apply the cleaning function to the Wage and Value columns
df1['Wage'] = df1['Wage'].apply(clean_currency)
df1['Value'] = df1['Value'].apply(clean_currency)

# Calculate the difference
df1['Difference'] = df1['Value'] - df1['Wage']
sort = df1.sort_values("Difference",ascending=False)

sns.set()
graph = sns.scatterplot(x='Wage',y='Value',data=df1)
# plt.title("Scatter Plot of Wage vs Value")  # Optional: Add a title for better understanding
# plt.xlabel("Wage")  # Label for x-axis
# plt.ylabel("Value")  # Label for y-axis
ToolTips = HoverTool(tooltips=[("Index",'$Index'),
('(Wage,Value)','(@Wage,@Value)'),
('Name','@Name')]
)

p = figure(title= 'Soccer17', x_axis_label='Wage', y_axis_label='Value' , tools=[ToolTips] )
p.circle('Wage' , 'Value' , size = 10 , source = df1)
show(p)