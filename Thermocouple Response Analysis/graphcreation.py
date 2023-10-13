import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataFrame = pd.read_excel("station2.xlsx")

time = np.array(dataFrame.time)
s1 = np.array(dataFrame.s1)
s2 = np.array(dataFrame.s2)
s3 = np.array(dataFrame.s3)
s4 = np.array(dataFrame.s4)

# print(dataFrame)
cold_hot = dataFrame.loc[701:1051]
time_cold_hot = np.array(cold_hot.time)
s1_cold_hot = np.array(cold_hot.s1)
s2_cold_hot = np.array(cold_hot.s2)
s3_cold_hot = np.array(cold_hot.s3)
s4_cold_hot = np.array(cold_hot.s4)


hot_cold = dataFrame.loc[1051:1332]
time_hot_cold = np.array(hot_cold.time)
s1_hot_cold = np.array(hot_cold.s1)
s2_hot_cold = np.array(hot_cold.s2)
s3_hot_cold = np.array(hot_cold.s3)
s4_hot_cold = np.array(hot_cold.s4)

# theta/theta init
s1_t_infinity = s1[350]
s2_t_infinity = s2[350]
s3_t_infinity = s3[350]
s4_t_infinity = s4[350]

s1_theta_i = s1_cold_hot[0] - s1_t_infinity
s2_theta_i = s2_cold_hot[0] - s2_t_infinity
s3_theta_i = s3_cold_hot[0] - s3_t_infinity
s4_theta_i = s4_cold_hot[0] - s4_t_infinity
s1_val = []
s2_val = []
s3_val = []
s4_val = []

s1_log = []
s2_log = []
s3_log = []
s4_log = []

for i in range(len(s1_cold_hot)):
    s1_val.append(((s1_cold_hot[i] - s1_t_infinity)/s1_theta_i))
    s2_val.append(((s2_cold_hot[i] - s2_t_infinity)/s2_theta_i))
    s3_val.append(((s3_cold_hot[i] - s3_t_infinity)/s3_theta_i))
    s4_val.append(((s4_cold_hot[i] - s4_t_infinity)/s4_theta_i))

    s1_log.append(np.log((s1_cold_hot[i] - s1_t_infinity)/s1_theta_i))
    s2_log.append(np.log((s2_cold_hot[i] - s2_t_infinity)/s2_theta_i))
    s3_log.append(np.log((s3_cold_hot[i] - s3_t_infinity)/s3_theta_i))
    s4_log.append(np.log((s4_cold_hot[i] - s4_t_infinity)/s4_theta_i))

df_new = pd.DataFrame({'time': time_cold_hot, 's1_log': s1_log,'s2_log':\
                        s2_log, 's3_log': s3_log, 's4_log': s4_log})

# df_new.to_csv('LN_Data.csv')

# i = 0
# time_ice_to_cold = []
# s1_ice_to_cold = []
# s2_ice_to_cold = []
# s3_ice_to_cold = []
# s4_ice_to_cold = []
# while time[i] > 200 and time[i] < 290:
#     time_ice_to_cold.append(time[i])
#     s1_ice_to_cold.append(s1[i])
#     s2_ice_to_cold.append(s2[i])
#     s3_ice_to_cold.append(s3[i])
#     s4_ice_to_cold.append(s4[i])
# i = 0
# time_hot_to_ice = []
# s1_hot_to_ice = []
# s2_hot_to_ice = []
# s3_hot_to_ice = []
# s4_hot_to_ice = []
# while time[i] > 200 and time[i] < 290:
#     time_hot_to_ice.append(time[i])
#     s1_hot_to_ice.append(s1[i])
#     s2_hot_to_ice.append(s2[i])
#     s3_hot_to_ice.append(s3[i])
#     s4_hot_to_ice.append(s4[i])

# Total Life Span

plt.figure()
plt.plot(time, s1, label = 's1')
plt.plot(time, s2, label = 's2')
plt.plot(time, s3, label = 's3')
plt.plot(time, s4, label = 's4')
plt.xlabel('Time [sec]')
plt.ylabel('Temperature[deg C]')
plt.title('Temperature vs Time')
plt.legend(['1/4" Beaded, Exposed Junction', '1/16"\
             Beaded, Exposed Junction', '1/4" Grounded\
             Junction', '1/4" Ungrounded Junction'],\
             loc = 'lower right', fontsize = 7)

# Ice to Hot

plt.figure()
plt.plot(time_cold_hot, s1_cold_hot, label = 's1')
plt.plot(time_cold_hot, s2_cold_hot, label = 's2')
plt.plot(time_cold_hot, s3_cold_hot, label = 's3')
plt.plot(time_cold_hot, s4_cold_hot, label = 's4')
plt.xlabel('Time [sec]')
plt.ylabel('Temperature[deg C]')
plt.title('Ice Water to Hot Water')
plt.legend(['1/4" Beaded, Exposed Junction', '1/16"\
             Beaded, Exposed Junction', '1/4" Grounded\
             Junction', '1/4" Ungrounded Junction'])

#Hot to Ice

plt.figure()
plt.plot(time_hot_cold, s1_hot_cold, label = 's1')
plt.plot(time_hot_cold, s2_hot_cold, label = 's2')
plt.plot(time_hot_cold, s3_hot_cold, label = 's3')
plt.plot(time_hot_cold, s4_hot_cold, label = 's4')
plt.xlabel('Time [sec]')
plt.ylabel('Temperature[deg C]')
plt.title('Hot Water to Cold Water')
plt.legend(['1/4" Beaded, Exposed Junction', '1/16"\
             Beaded, Exposed Junction', '1/4" Grounded\
             Junction', '1/4" Ungrounded Junction'])

#Theta/Theta I graph

plt.figure()
plt.plot(time_cold_hot, s1_val, label = 's1')
plt.plot(time_cold_hot, s2_val, label = 's2')
plt.plot(time_cold_hot, s3_val, label = 's3')
plt.plot(time_cold_hot, s4_val, label = 's4')

plt.xlabel('Time [sec]')
plt.ylabel('Theta/Theta init')
plt.title('Normalized Temperature vs Time')
plt.legend(['1/4" Beaded, Exposed Junction', '1/16"\
             Beaded, Exposed Junction', '1/4" Grounded\
             Junction', '1/4" Ungrounded Junction'])

# Log Theta/Theta init

plt.figure()
plt.plot(time_cold_hot, s1_log, label = 's1')
plt.plot(time_cold_hot, s2_log, label = 's2')
plt.plot(time_cold_hot, s3_log, label = 's3')
plt.plot(time_cold_hot, s4_log, label = 's4')

plt.xlabel('Time [sec]')
plt.ylabel('Ln(Theta/Theta init)')
plt.title('Natural Log Normalized Temperature vs Time')
plt.legend(['1/4" Beaded, Exposed Junction', '1/16"\
             Beaded, Exposed Junction', '1/4" Grounded\
             Junction', '1/4" Ungrounded Junction'])

plt.show()
