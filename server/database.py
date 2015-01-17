from pymongo import MongoClient
import json, datetime

client = MongoClient()

db = client['vaccinfo']
schedule = db['schedule']
users = db['users']

# Return all the vaccines with week range for each
def getVaccines(week):
	result = []
	query = {"week_range.s": {"$lte": week}, "week_range.e": {"$gte": week}}
	projection = {"vaccines": 1, "week_range": 1, "_id": 0}
	cursor = schedule.find(query, projection)
	for doc in cursor:
		start_week = doc["week_range"]["s"]

		end_week = doc["week_range"]["e"]

		vaccines = doc["vaccines"]
		for vaccine in vaccines:
			vaccine = vaccine.encode("UTF-8")
			result_entry = {"vaccine": vaccine, "start_week": start_week, "end_week": end_week}
			result.append(result_entry)

	return result

# It register new user with phone number & date of birth
def register(phone, dob):
	#mydob = datetime.datetime.strptime('22081991', '%d%m%Y')
	data = {"phone": phone, "dob": dob}
	users.insert(data)

if __name__ == '__main__':
	pass