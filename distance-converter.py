print('Type a random distance')
distance=int(input())
print ('what units is the distance in mi or km')
start_units=input()
print('what is the tartget unit you want km or mi')
out_units=input()

#miles

if start_units == 'km':
    new_unit= 1.609/ distance
print(distance, 'in km is', new_unit,'.' )
if start_units == 'mi':
    new_unit= 1.609 * distance

print(distance, 'in mi is', new_unit,'.')
