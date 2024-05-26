import pandas as pd

df_circuits = pd.read_csv("data\\circuits.csv", sep = ",")
df_circuits.to_excel("data\\xlsx\\data.xlsx", sheet_name = "circuits", index = False)

df_constructor_results = pd.read_csv("data\\constructor_results.csv", sep = ",")
df_constructor_results.to_excel("data\\xlsx\\data.xlsx", sheet_name = "constructor_results", index = False)

df_constructor_standings = pd.read_csv("data\\constructor_standings.csv", sep = ",")
df_constructor_standings.to_excel("data\\xlsx\\data.xlsx", sheet_name = "constructor_standings", index = False)

df_constructors = pd.read_csv("data\\constructors.csv", sep = ",")
df_constructors.to_excel("data\\xlsx\\data.xlsx", sheet_name = "constructors", index = False)

df_driver_standings = pd.read_csv("data\\driver_standings.csv", sep = ",")
df_driver_standings.to_excel("data\\xlsx\\data.xlsx", sheet_name = "driver_standings", index = False)

df_drivers = pd.read_csv("data\\drivers.csv", sep = ",")
df_drivers.to_excel("data\\xlsx\\data.xlsx", sheet_name = "drivers", index = False)

df_lap_times = pd.read_csv("data\\lap_times.csv", sep = ",")
df_lap_times.to_excel("data\\xlsx\\data.xlsx", sheet_name = "lap_times", index = False)

df_pit_stops = pd.read_csv("data\\pit_stops.csv", sep = ",")
df_pit_stops.to_excel("data\\xlsx\\data.xlsx", sheet_name = "pit_stops", index = False)

df_qualifying = pd.read_csv("data\\qualifying.csv", sep = ",")
df_qualifying.to_excel("data\\xlsx\\data.xlsx", sheet_name = "qualifying", index = False)

df_races = pd.read_csv("data\\races.csv", sep = ",")
df_races.to_excel("data\\xlsx\\data.xlsx", sheet_name = "races", index = False)