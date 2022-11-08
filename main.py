import pandas as pd
import matplotlib.pyplot as plt

zip_codes = pd.read_csv("finalassignment.csv", usecols=["zip_code"])
bottles = pd.read_csv("finalassignment.csv", usecols=["sold_bottles"])
store_num = pd.read_csv("finalassignment.csv", usecols=["store_number"])

myzip_codes = list(zip_codes["zip_code"])
mybottles = list(bottles["sold_bottles"])
my_store_num = list(store_num["store_number"])

tot_sum = sum(mybottles)
percentage = []
for num in mybottles:
    percentage.append(round(num * 100 / tot_sum, 2))

plt.title("Bottles Sold")
plt.xlabel('Zip Code')
plt.ylabel("Bottles Sold")

plt.scatter(myzip_codes, mybottles)
plt.show()

plt.title("Bottles Sold")
plt.xlabel('Store Number')
plt.ylabel("Percentage %")

plt.scatter(store_num, percentage)
plt.show()
