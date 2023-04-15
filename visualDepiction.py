import matplotlib.pyplot as plt

def buildPlot(x, y, topic, fromVal, toVal):
    plt.style.use('dark_background')

    colors = ['pink' if val < 0 else 'lightblue' if val == 0 else 'lightgreen' for val in y]

    # Create the scatter plot
    plt.scatter(x, y, c=colors)

    # Add a dashed line at y=0.0
    plt.axhline(y=0.0, color='gray', linestyle='--')

    # Set the labels and title
    plt.ylabel('Sentiment Polarity', color='white')

    plt.title("Sentiment Scores of the news regarding "+topic, color='white')
    if(fromVal == toVal):
        plt.suptitle('[' + str(fromVal) + ']', color='white', fontsize=8)
    else:
        plt.suptitle('[' + str(fromVal) + '] - ' + '[' + str(toVal) + ']', color='white', fontsize=8)

    # Show the plot
    plt.show()