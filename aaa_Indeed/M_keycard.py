'''
1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
Medium

LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.

Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".

Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.

Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.

 

Example 1:

Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]

Output: ["daniel"]
Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").

Example 2:

Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"]
keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]

Output: ["bob"]
Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").

Constraints:

1 <= keyName.length, keyTime.length <= 105
keyName.length == keyTime.length
keyTime[i] is in the format "HH:MM".
[keyName[i], keyTime[i]] is unique.
1 <= keyName[i].length <= 10
keyName[i] contains only lowercase English letters.
'''

'''
*U
within hour period here just means the times are within 60 minutes of each other

The problem states '... in a single day', so we don't need to worry about the transition from 23:59 to 00:00

*M
Array + dict

*P
loop through the arrays
populate a dict:
	key = name
	value = list of key times

Since key times are not sorted in chronological order in the keyTime array, we have to sort them first

loop through items in dict
sort keytimes list
each person can only be added to the alert list if they have 3 or more key times, and after sorting, key time[i] is within 60 minutes of key time[i-2]

time: O(nlogn) (because in the worst case, we have to sort n elements either in key time list or the output list)
space: O(n) (in the worst case, need to store n in the output)


*I
*R
*E

'''

def alertNames(keyName, keyTime):

	def isWithinHour(t1, t2):
		h1 = int(t1[0:2])
		h2 = int(t2[0:2])
		m1 = int(t1[3:])
		m2 = int(t2[3:])

		d = (h2 - h1) * 60 + m2 - m1

		if d>60:
			return False

		return True
	
	output = []
	key_times = {}
	
	for i in range(len(keyName)):
		name = keyName[i]
		time = keyTime[i]

		if name in key_times:
			key_times[name].append(time)
		else:
			key_times[name] = [time]
		
	for name, times in key_times.items():
		if len(times) >= 3:
			sorted_times = sorted(times)
			
			for i, t in enumerate(sorted_times):
				if i>=2 and isWithinHour(sorted_times[i-2], t):
					output.append(name)
					break
					
	return sorted(output)
