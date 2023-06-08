def find_farthest_orbit(orbits):
    list_of_elliptical_orbits = [i for i in orbits if i[0] != i[1]]
    list_of_areas = [i[0] * i[1] for i in list_of_elliptical_orbits]
    max_area_index = list_of_areas.index(max(list_of_areas))
    return list_of_elliptical_orbits[max_area_index]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))




# def find_farthest_orbit(orbits):
#     return max(orbits, key=lambda x: x[0] * x[1] if x[0] != x[1] else -1)

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))





# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# list1  = []
# result = 0
# for i in orbits:
#     a,b = i
#     if a == b:
#         a = 0
#         b = 0
#     s = a * b
#     if result < s :
#         result = s
#         list1  = a, b
# print(*list1)
