import matplotlib.pyplot as plt
import seaborn as sns
def showDistribution(df, cols, colors):
        for index in range(len(cols)):
            sns.displot(data=df, x=cols[index], color=colors[index], kde=True, height=4, aspect=2)
            plt.title(f'Distribution of '+cols[index]+' data volume', size=20, fontweight='bold')
            plt.show()
def box_plot(df,cols,title):            
    plt.figure(figsize=(12, 7))
    sns.boxplot(data = df, x=cols)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.show()