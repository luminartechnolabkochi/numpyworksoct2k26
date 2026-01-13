"""
# 1️⃣ Total Passengers & Columns
    # print(data.shape)

2️⃣ Survival Analysis
    
    survived = data[:,1].astype(int)
    np.sum(survived)           # total survived
    np.mean(survived) * 100    # survival rate %

3️⃣ Gender-based Survival

    male_survival = survived[data[:,3] == "male"]
    female_survival = survived[data[:,3] == "female"]
    np.mean(male_survival) * 100
    np.mean(female_survival) * 100

4️⃣ Class-wise Survival

    for cls in ['1','2','3']:
        cls_data = survived[data[:,2] == cls]
        print(cls, np.mean(cls_data) * 100)


5️⃣ Age Statistics

    age = data[:,4].astype(float)

    np.mean(age)
    np.max(age)
    np.min(age)

6️⃣ Fare Analysis

    fare = data[:,5].astype(float)
    np.mean(fare)
    np.max(fare)
    np.min(fare)

7️⃣ Passengers Above Age 50

    data[age > 50]

8️⃣ Conditional Logic (np.where)

    fare_category = np.where(fare > 50, "High", "Low")
    fare_category

9️⃣ Sorting by Fare (Descending)
    
    data[np.argsort(fare)[::-1]]

🔟 Unique Embarkation Points

    np.unique(data[:,6], return_counts=True)

"""