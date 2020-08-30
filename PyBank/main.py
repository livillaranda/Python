# Import packages
import os
import csv

# Read data file
bd_path = os.path.join("Resources", "budget_data.csv")
    #"C:/Users/livil/Desktop/PREWORK_LIV/Homework/Python-Challenge/PyBank/Resources/budget_data.csv")

# Read with CSV function
with open(bd_path) as csvfile:
    bd_read = csv.reader(csvfile, delimiter=',')

    # Read Header
    next(bd_read)

    # Assign Variables
    row_count = 0
    total_sum = 0
    changes = []
    previous = 0
    inc_change = [" ", 999999]
    dec_change = [" ", 0]

    # For Loop
    for row in bd_read:
        
        # Count Months
        row_count += 1
        
        # Sum of Profits/Losses
        total_sum = total_sum + int(row[1])

        # Calculate Difference Between 
        # Profit/Loss Amount from the Following Amount
        difference = int(row[1]) - previous
        
        # Store Changes into 'Changes' List
        changes.append(difference)

        # Replace 'previous' in Difference Formula to Move Down the Row
        previous = int(row[1])

        # To Find Greatest Increase
        if difference > inc_change[1]:
            inc_change[1] = difference
            inc_change[0] = row[0]

        # To Find Greatest Decrease
        if difference < dec_change[1]:
            dec_change[1] = difference
            dec_change[0] = row[0]

    # Average of *Changes* in Profits/Losses
    average = sum(changes[1:]) / (len(changes) - 1)
    
    # Finding Greatest Increase
    greatest = max(changes)

    # Finding Greatest Decrease
    least = min(changes)

    # Formatting Outputs
    total_sum = '${:,.0f}'.format(total_sum)
    average = '${:,.2f}'.format(average)
    inc_change[1] = '${:,.0f}'.format(inc_change[1])
    dec_change[1] = '${:,.0f}'.format(dec_change[1])

                      
    
    # Summary of Analysis
    print("Financial Analysis")
    print("-" *30)
    print("Total Months: " + str(row_count))
    print("Total: " + total_sum)
    print("Average Change: " + average)
    print("Greatest Increase in Profits: " + inc_change[0], inc_change[1])
    print("Greatest Decrease in Profits: " + dec_change[0], dec_change[1])
    
    # Write CSV file output
    output_path = os.path.join("Analysis", "Final_Analysis.csv")

    # Open the file using "write" mode
    with open(output_path, 'w') as csvfile:

        # Start csv.writer
        csvwriter = csv.writer(csvfile)

        # 'Rewrite' Summary into file
        csvwriter.writerow(["Financial Analysis"])
        csvwriter.writerow(["-" *30])
        csvwriter.writerow(["Total Months: " + str(row_count)])
        csvwriter.writerow(["Total: " + total_sum])
        csvwriter.writerow(["Average Change: " + average])
        csvwriter.writerow(["Greatest Increase in Profits: " + inc_change[0], inc_change[1]])
        csvwriter.writerow(["Greatest Decrease in Profits: " + dec_change[0], dec_change[1]])