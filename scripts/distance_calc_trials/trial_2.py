#using batch processing

from geopy.distance import geodesic
from multiprocessing import Pool, cpu_count
import pandas as pd

def calculate_distances(primary_hospitals, secondary_hospitals, tertiary_hospitals):

  all_prim_to_sec = []
  all_sec_to_tert =[]

  for i, primary_hospital in primary_hospitals.iterrows():
      primary_to_sec = []
      for j, secondary_hospital in secondary_hospitals.iterrows():
          distance = geodesic(primary_hospital['lat_lng'].coords[0], secondary_hospital['lat_lng'].coords[0]).miles
          primary_to_sec.append(distance)

      if primary_to_sec:
        avg_distance = sum(primary_to_sec) / len(primary_to_sec)
        all_prim_to_sec.append(avg_distance)

  for s, secondary_hospital in secondary_hospitals.iterrows():
      sec_to_tert = []
      for t, tertiary_hospital in tertiary_hospitals.iterrows():
          distance = geodesic(secondary_hospital['lat_lng'].coords[0], tertiary_hospital['lat_lng'].coords[0]).miles
          sec_to_tert.append(distance)

      if sec_to_tert:
          avg_distance_tert = sum(sec_to_tert) / len(sec_to_tert)
          all_sec_to_tert.append(avg_distance_tert)

  return all_prim_to_sec, all_sec_to_tert

operational_hospitals = filtered_gdf[filtered_gdf['operation_status'] == 'Operational']
unique_states = operational_hospitals['state'].unique()

state_sec_distances = {}
state_tert_distances = {}

for state in unique_states:
    state_hospitals = operational_hospitals[operational_hospitals['state'] == state]
    primary_hospitals = state_hospitals[state_hospitals['facility_level'] == 'Primary']
    secondary_hospitals = state_hospitals[state_hospitals['facility_level'] == 'Secondary']
    tertiary_hospitals = state_hospitals[state_hospitals['facility_level'] == 'Tertiary']

    with Pool(cpu_count()) as pool:
        results = pool.apply(calculate_distances, args=(primary_hospitals, secondary_hospitals, tertiary_hospitals))

    state_sec_distances[state] = {k: v for result in results for k, v in result.items() if 'Primary' in k}
    state_tert_distances[state] = {k: v for result in results for k, v in result.items() if 'Secondary' in k}

print(state_sec_distances)
print(state_tert_distances)
