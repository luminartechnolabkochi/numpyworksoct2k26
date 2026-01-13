
import numpy as np

data = np.genfromtxt("fileworks\\titanic_case_study\\passenger_data.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")

# total number of passengers
print(f"total number of passengers {data.shape}")

# survival analysis

# total number of survivals

survived_unsurvived=data[:,1].astype("int")

survived=survived_unsurvived[survived_unsurvived==1]

print(f" total number of survived {survived.size}")

survival_rate=( survived.size/ survived_unsurvived.size)*100

print(f"survival rate={survival_rate}")

# total number of death

death = survived_unsurvived[survived_unsurvived==0]

print(f"unsurvived count{death.size}")

death_rate= (death.size/survived_unsurvived.size)*100

print(f"death rate{death_rate}")

#gender analysys
genders = data[:,3]

male_count = genders[genders=="male"].size

print(f"male count",male_count)

female_count = genders[genders=="female"].size

print(f"female count{female_count}")

survived_males=data[(data[:,3]=="male")&(data[:,1].astype("int")==1)]

survived_male_count = survived_males[:,0].size

print(f"survived males{survived_males}")

male_survival_rate = (survived_male_count/male_count)*100

print(f"male survival rate{male_survival_rate}")
# total number of males 
# total number females
# male survival rate
# female survival rate

# age analysis
# max(age)
# min(age)
ages = data[:,4].astype("int")
print(f"minum age{np.min(ages)}")
print(f"maximum age{np.max(ages)}")
print(f"average age{np.mean(ages)}")

# fare analysis

fares = data[:,-2].astype("float")

print(f"max fare{np.max(fares)}")
print(f"min fare{np.min(fares)}")
print(f"avg fare{np.mean(fares)}")

# sort

# np.argsort()

print(data[np.argsort(data[:,-2].astype("float"))])