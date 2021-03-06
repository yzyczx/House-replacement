
# 使用初始时刻以及持续时间，推算数据点在各时间区间内的时间长度分布，并进行统计
def time_distribute_Cal(data):

    # 存储该类别数据在不同时间段的分布情况
    time_distribution = {'0-1': 0, '1-2': 0, '2-3': 0, '3-4': 0, '4-5': 0, '5-6': 0, '6-7': 0, '7-8': 0, '8-9': 0,
                         '9-10': 0, '10-11': 0, '11-12': 0, '12-13': 0, '13-14': 0, '14-15': 0, '15-16': 0, '16-17': 0,
                         '17-18': 0, '18-19': 0, '19-20': 0, '20-21': 0, '21-22': 0, '22-23': 0, '23-24': 0}

    for item in data:
        # 初始时刻及时间间隔
        hours = int(item[0][8:10])
        minutes = int(item[0][10:])
        durations = int(item[1])

        while durations > 0:

            if minutes + durations >= 60:
                store_key = str(hours % 24) + '-' + str((hours % 24) + 1)
                time_distribution[store_key] += (60 - minutes)

                hours += 1
                durations -= (60 - minutes)
                minutes = 0

            else:
                store_key = str(hours % 24) + '-' + str((hours % 24) + 1)
                time_distribution[store_key] += durations
                break

    return time_distribution