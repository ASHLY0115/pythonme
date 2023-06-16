import pandas as pd
dic ={"Reg No":["ABC123","ECH265","FET345","GMT734"],"Name":["Ganesh Kumar","John Mathew","Reena K","Adil M"],"Semester":["S8","S7","S6","S5"],"College":["ABC","ECH","FET","GMT"],"CGPA":[9.8,9.9,9.7,9.75]}
df = pd.DataFrame(dic)
#df.sort_values(by='CGPA'
#print(df.head(2))
df=df.sort_values(by='CGPA',ascending=False)
df.to_csv("Toppers1.csv")
