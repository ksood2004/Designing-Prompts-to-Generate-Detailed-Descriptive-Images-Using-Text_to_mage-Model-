import pandas as pd
import matplotlib.pyplot as plt

def json_to_table(json_data):
    df = pd.DataFrame(json_data)
    return df

def generate_table_image(df, output_file):
    plt.figure(figsize=(10, 4))  
    ax = plt.subplot(111, frame_on=False)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    
    max_description_length = df['Description'].str.len().max()
    
    # Maximum width for the last column
    max_last_column_width = 0.9
    # Calculate last column width based on the length of the longest text
    last_column_width = min(max_last_column_width, max(0.2, max_description_length * 0.02))
    
    table = plt.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center',
                      colColours=['#ffffff'] * len(df.columns), cellColours=[['none']*len(df.columns) for _ in range(len(df))],
                      colWidths=[0.15]*3 + [last_column_width])
    
    for cell in table._cells:
        if cell[0] == 0:
            table._cells[cell].set_facecolor('none')
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    plt.savefig(output_file, transparent=True, bbox_inches='tight', pad_inches=0.05)
    plt.close()

json_data = {
    "Offer Provider": ["Flipkart", "Flipkart UPI", "Flipkart Axis Bank","HDFC Bank"],
    "Offer Amount": [12.650, 3249.75, 749.95, 1000],
    "Offer Type": ["Exchange", "UPI", "card", "credit card"],
    "Description": ["Buy with Exchange up to 12,650 off","25% Instant Discount for 1st Flipkart Order using Flipkart UPI","Cashback on Flipkart Axis Bank Card","1000 Off On HDFC Bank Credit Non EMI, Credit and Debit Card EMI Transactions"]
}

df = json_to_table(json_data)

output_file = "/Users/jarvis/pymycod/Samsung_prism/pics_data/table.png"
generate_table_image(df, output_file)
print("Table image saved as:", output_file)
