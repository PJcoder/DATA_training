import pandas as pd

df = pd.read_csv('Czas pracy Patryk Janus Viper Wing - Styczeń 24.csv')

print(df.tail())
print(len(df))

text_to_write = "INSERT INTO czas_pracy (dzien,rozpoczecie,zakonczenie,przepracowane) \nVALUES "
save_file = 'SQL_upload_Styczeń.txt'

# Open a file in write mode ('w'). This will create the file if it doesn't exist.
# If the file does exist, it will be overwritten.
with open(save_file, 'w') as file:
    file.write(text_to_write)


for n in range(1,len(df)-1):
    text_to_write = "('" + df.iloc[n, 0] + "', '" 

    hour = df.iloc[n, 2]
    if "." in hour:
        new_hour = list(hour)
        new_hour[hour.find(".")]=":"

        text_to_write += ''.join(new_hour) 
        text_to_write += "0', '"
    else:
        text_to_write += df.iloc[n, 2]+ ":00', '"

    hour = df.iloc[n, 3]
    if "." in hour:
        new_hour = list(hour)
        new_hour[hour.find(".")]=":"

        text_to_write += ''.join(new_hour) 
        text_to_write += "0', '"
    else:
        text_to_write += df.iloc[n, 3]+ ":00', '"    
        
    text_to_write += df.iloc[n, 4] + "'),\n"

    with open(save_file, 'a') as file:
        file.write(text_to_write) 