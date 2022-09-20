'''
Each element in 'schedule' is an array such that schedule[i][j] represents meeting jth of employee ith. Each meeting is in the format [start_time, end_time]. Time is measured by the number of minutes since midnight. Start and end times do not exceed 24 * 60.

Find the earliest time you can schedule a meeting with length 'length' where all employees are available. If no time blocks suit everyone, return -1

Example:
schedules = [ [[60,150], [180,240]],
			  [[0,210], [360,420]] ]
solution (schedules, length) = 240
'''

'''
put all meetings among all employees in a list
sort list by start time
create a new list for merged intervals, put the first interval in
loop through all remaining intervals
	if start time of curr interval < end time of the last interval in merged list
 		end time of interval in merged list = max() of 2 end times
   else
   		append curr interval into merged list
loop through merged list
	first interval: compare start time with beginning of day
 	last interval: compare end time with end of day
  	others: compare end time with start time of next

Time: O(nlogn + n + n) = O(nlogn) due to sorting
Space: O(n)
'''

def solution(schedules, length):
	all = []
	for meetings_of_i in schedules:
		all += meetings_of_i
	
	all = sorted(all, key=lambda x:x[0])
	merged = [all[0]]
	for mtg in all[1:]:
		if mtg[0] < merged[-1][1]:
			merged[-1][1] = max(mtg[1], merged[-1][1])
		else:
			merged.append(mtg)

	if merged[0][0] >= length:
		return 0
	for i in range(len(merged)-1):
		if merged[i+1][0] - merged[i][1] >= length:
			return merged[i][1]
	if 24*60 - merged[-1][1] >= length:
		return merged[-1][1]


	
	
	# for i, emp in enumerate(schedules):
	# 	for j, itv in enumerate(schedules[i]):
	# 		if len(merged) == 0:
	# 			merged.append(itv)
	# 		else:
	# 			for k, m_itv in enumerate(merged):
	# 				es = itv[0]
	# 				ee = itv[1]
	# 				ms = m_itv[0]
	# 				me = m_itv[1]
	# 				if es < ms and ee < ms:
	# 					continue
	# 				else:
	# 					m_itv[0] = min(es, ms)
	# 					m_itv[1] = max(ee, me)
	

				
