
        
       # Import modules 
       import os
       import csv

       # Specify file path
       file_path = os.path.join(directory, file_name)

       # Initialize variables
       month_year_list = []
       revenue_list = []
       tot_revenue = 0
       tot_change = 0
       change_max = ['', 0]
       cahnge_min = ['', 0]

       # Read csv data to gather date and revenue data
       with open(file_path, newline = '') as file in
            csvreader =csv.reader(file_in, delimiter = ',')
            next(csvreader, None)
            for row in csvreader:
            month_year = row[0]
            revenue = float(row[1])
            month_year_list.append(month_year)
            reneue_list.append(revenue)
            tot_revenue += revenue

      # loop through the list to calculate summary data
      tot_month = len(month_year_list)
      for i in range(1, len(month_year_list)):
      change_revenue_list[i] - revenue_list[i-1]
      tot_change += change
    if change > change_max[1]:
        change_max = [month_year_list[1], change]
    if change < change_min [1]:
        change_min = [month_year_list[1], change]
    change_average = tot_change / tot_month

        # store summary data in list
        line1 = 'Financial Analysis'
        line2 = '_' * 30
        line3 = 'Total Month: ' + str(tot_revenue)
        line4 = 'Total Revenue: $' + str(round(tot_revenue))
        line5 = 'Average Revenue change: $' + str(round(change_average))
        line6 = 'Greatest Increase in Revenue: ' + change_max[0] + ' ($' + str(round(change_max[1])) + ')'
        line7 = ' Greatest Decease in revenue: ' + change_min[0] + ' ($' + str(round(change_min[1])) + ')'
        summary = []
        summary.extend([line1, line2, line3, line4, line5, line6, line7])
   
      # Report summary data in terminal
       print('')
       print(file_name)
       for line in summary:
            print(line)
        print('')

      # write summary data into a text file
      output_file_path = file_name.split(',')[0] + '_output.txt'
      with open(output_file_path, 'w')as file_out:
           for line in summary:
            file_out.write(line + '\n')

     # Analyze test record using the define function
        directory = 'raw_data'
        file_name = ' budget_data_1.csv'
        main(directory, file_name)

     # Analyze test record using the define function
        directory = 'raw data'
        file_name = 'budget_data_2.csv'
        main(directory, file_nam