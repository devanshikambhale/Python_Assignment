# Import a dataset of new recruitments in companies such as Microsoft, Google, Amazon, IBM, Deloitte, Capgemini, ATOS Origin, Amdocs etc.

# Generate & visualize reports of new recruitments using:

# a) Bar Chart
# b) Pie Chart
# c) Customize Pie Chart
# d) Doughnut Chart

# e) Compare the new recruitments in IBM & Amdocs using visualization.
import matplotlib.pyplot as plt

# recruitment data
company = ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "ATOS Origin", "Amdocs"]
recruit = [1800, 1600, 1500, 800, 1100, 2000, 800, 680]

# a) Bar Chart
plt.bar(company, recruit)
plt.title("New Recruitments in Companies")
plt.xlabel("Company Name")
plt.ylabel("No of Recruitments")
plt.xticks(rotation=45)
plt.show()

# b) Pie Chart
plt.pie(recruit, labels=company, autopct="%0.1f%%")
plt.title("Recruitment Pie Chart")
plt.show()

# c) Customize Pie Chart
explode = [0.2, 0, 0, 0, 0, 0.2, 0, 0]

plt.pie(recruit, labels=company, autopct="%0.1f%%", explode=explode, shadow=True, startangle=90)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(recruit, labels=company, autopct="%0.1f%%", startangle=90)

circle = plt.Circle((0, 0), 0.6, color="white")
plt.gca().add_artist(circle)

plt.title("Doughnut Chart")
plt.show()

# e) Compare IBM and Amdocs
ibm = recruit[3]
amdocs = recruit[7]

plt.bar(["IBM", "Amdocs"], [ibm, amdocs])
plt.title("IBM vs Amdocs Recruitment")
plt.xlabel("Company")
plt.ylabel("Recruitments")
plt.show()