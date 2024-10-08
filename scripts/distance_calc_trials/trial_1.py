from geopy.distance import geodesic
from itertools import combinations

operational_hospitals = filtered_gdf[filtered_gdf['operation_status'] == 'Operational']
unique_states = operational_hospitals['state'].unique()

state_sec_distances = {}
state_tert_distances ={}

for state in unique_states:
    state_hospitals = operational_hospitals[operational_hospitals['state'] == state]
    prim_distances = []
    sec_distances=[]

    primary_hospitals = state_hospitals[state_hospitals['facility_level'] == 'Primary']
    secondary_hospitals = state_hospitals[state_hospitals["facility_level"]== 'Secondary']
    tertiary_hospitals = state_hospitals[state_hospitals["facility_level"]== 'Tertiary']

    for i in range(len(primary_hospitals)):
      primary_to_sec = []

      for j in range(len(secondary_hospitals)):
        hospital1 = primary_hospitals.iloc[i]
        hospital2 = secondary_hospitals.iloc[j]
        dist = geodesic(hospital1['lat_lng'].coords[0], hospital2['lat_lng'].coords[0]).miles
        distance = (dist/60) * 60
        primary_to_sec.append(distance)

      if primary_to_sec:
          avg_distance = sum(primary_to_sec) / len(primary_to_sec)
          prim_distances.append(avg_distance)

    for s in range(len(secondary_hospitals)):
      sec_to_tertiary = []

      for t in range(len(tertiary_hospitals)):
        sec_hosp = secondary_hospitals.iloc[s]
        tert_hosp = tertiary_hospitals.iloc[t]
        dist = geodesic (sec_hosp["lat_lng"].coords[0], tert_hosp["lat_lng"].coords[0]).miles
        distance = (dist/60) * 60
        sec_to_tertiary.append(distance)

      if sec_to_tertiary:
        avg_distance = sum(sec_to_tertiary)/ len(sec_to_tertiary)
        sec_distances.append(avg_distance)

    if prim_distances:
        median_distance = sorted(prim_distances)[len(prim_distances) // 2]
        state_sec_distances[state] = {'avg_distance_to_sec': sum(prim_distances) / len(prim_distances),
                                  'median_distance_to_sec': median_distance}

    if sec_distances:
        median_distance = sorted(sec_distances)[len(sec_distances) // 2]
        state_tert_distances[state] = {'avg_distance_to_tert': sum(sec_distances) / len(sec_distances),
                                  'median_distance_to_tert': median_distance}

print(state_sec_distances)


