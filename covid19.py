import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/09-19-2020.csv")
df = df[['Province_State','Confirmed']]
df = df.iloc[1:]
df.to_csv("CovidData.csv")