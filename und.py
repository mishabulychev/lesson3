import csv

max_street = {}

with open ('data-398-2018-05-25.csv', 'r', encoding='cp1251') as file:
    fields = ['ID', 'Name', 'Longitude_WGS84', 'Latitude_WGS84', 'Street', 'AdmArea', 'District', 'RouteNumbers', 'StationName', 'Direction', 'Pavilion', 'OperatingOrgName', 'EntryState', 'global_id', 'geoData']
    reader = csv.DictReader(file, fields, delimiter=';')
    for row in reader:
        street_name = row['Street']
        if street_name in max_street: 
            max_street [street_name].append(row['Name'])
        else:
            max_street [street_name]=[ ]
print (max_street('Name'))

#print ('Количество остановок: ' + str(sum(1 for _ in file)))