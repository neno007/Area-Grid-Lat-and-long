start_long = float(input('input longitude for lower coner :\n'))
start_lat = float(input('input latitude for lower coner :\n'))
final_long = float(input('input longitude for higher coner :\n'))
final_lat = float(input('input latitude for higher coner :\n'))
interval = float(input('put the space interval in KM :\n'))
interval = interval * 0.01

lat_points = []
long_points = []

while start_lat <= final_lat:
    lat_points.append(start_lat)
    start_lat = start_lat + interval

while start_long <= final_long:
    long_points.append(start_long)
    start_long = start_long + interval

grid= []
for x in lat_points:
    for y in long_points:
        grid.append((x,',', y))
print(grid)

f = open('grid.csv', 'w')
for t in grid:
    line = ' '.join(str(x) for x in t)
    f.write(line + '\n')
f.close()
