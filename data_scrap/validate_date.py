def validate_date(year, month, day):
	validate_year(year)
	validate_month(month)
	validate_day(day)

def validate_year(year):
	min_year = 1980
	max_year = 2019
	validate_in_range(year, min_year, max_year)

def validate_month(month):
	min_month = 1
	max_month = 12
	validate_in_range(month, min_month, max_month)

def validate_day(day):
	min_day = 1
	max_day = 30
	validate_in_range(day, min_day, max_day)

def validate_in_range(current, min, max):
	if(current < min or current > max):
		raise ValueError()