import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import unittest
import matplotlib as mpl
import matplotlib.ticker as mticker
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()



# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date", parse_dates=True)

# Clean data
df = df.loc[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12,6))

    plt.plot(df.index, df.value)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views '
                + df.index[0].strftime('%-m/%Y')
                + '-'
                + df.index[-1].strftime('%-m/%Y'))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month
    
    # Calculate the monthly average page views
    monthly_data = df_bar.groupby(['Year', 'Month'])['value'].mean().unstack()
    
    # Define month labels
    month_labels = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    monthly_data.plot(kind='bar', ax=ax, width=0.8)
    
    # Customize chart
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Average Daily Page Views per Month")
    ax.legend(title="Months", labels=month_labels)
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()

    df_box['Year'] = df_box.index.year
    df_box['Month'] = df_box.index.strftime('%b')
    df_box['Month_Num'] = df_box.index.month
    df_box = df_box.sort_values('Month_Num')

    fig, axes = plt.subplots(1, 2, figsize=(12,6))

    sns.boxplot(x = "Year", y = "value", data = df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='Month',y='value',data=df_box, ax=axes[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
