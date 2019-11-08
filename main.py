from flask import Flask, render_template, request
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import re
import json

app = Flask(__name__)

def CleanString(strMessy):
	return re.sub( r'\W', ' ', strMessy )

@app.route("/")
def home():
	
	########################################
	# DROP DOWN DATE PICKER
	########################################
	
	# Create lists of months and years
	# These are hardcoded for now, but might be better queried from db (esp. years)
	vMonths = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ]
	vMonthSelected = ['']*len(vMonths)
	vYears = [ 2016, 2017, 2018, 2019 ]
	vYearSelected = ['']*len(vYears)
	
	# Get data from url query string
	iYear = int(request.args.get('year'))
	iMonth = int(request.args.get('month'))
	
	# Mark selected values according to query string
	vMonthSelected[iMonth-1] = "selected"
	vYearSelected[vYears.index(iYear)] = "selected"
	
	########################################
	# QUERY FOR BOOK DATA
	########################################
	psqlConn = psycopg2.connect("dbname=newtitles user=postgres password=postgres")
	psqlConn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
	psqlCursor = psqlConn.cursor()
	
	strSQL = 'SELECT "Category" FROM "Categories" ORDER BY "CategoryID";'
	psqlCursor.execute(strSQL)
	vCategories = [x[0] for x in psqlCursor.fetchall()]
	strSQL = 'SELECT "CategoryID" FROM "Categories" ORDER BY "CategoryID";'
	psqlCursor.execute(strSQL)
	vCatIDs = [x[0] for x in psqlCursor.fetchall()]
	# vCatIDs = [i[0] for i in vCatIDs]
	print(vCatIDs)
	
	vTitles = {}
	for iCatID, strCategory in zip(vCatIDs, vCategories):
		strSQL = 'SELECT * FROM "Books" WHERE "Month" = %i AND "Year" = %i AND "CategoryID" = %i;' % (iMonth,iYear,iCatID)
		psqlCursor.execute(strSQL)

		vCatTitles = psqlCursor.fetchall()
		for vCatTitle in vCatTitles:
			vCatTitle = list(vCatTitle)
			strTitle = vCatTitle[19]
			strTitle = re.findall( r'<a href="(.*?)"', vCatTitle[19])[0]
			print(strTitle)
			vCatTitle[19] = strTitle
			vCatTitle = tuple(vCatTitle)
		vTitles[strCategory] = vCatTitles
	
	########################################
	# LEAFLET MAP
	########################################
	strSQL = 'SELECT * FROM "Books" WHERE "Month" = %i AND "Year" = %i;' % (iMonth,iYear)
	psqlCursor.execute(strSQL)
	vBooks = psqlCursor.fetchall()
	vBooksJSON = []
	for vBook in vBooks:
		vBook = list(vBook)
		dBook = {}
		dBook["date"] = vBook[1]
		dBook["pleiades_id"] = vBook[3]
		# dBook["pleiades_name"] = vBook[4]
		# dBook["precision_code"] = vBook[7]
		dBook["precision"] = vBook[8]
		# dBook["region"] = vBook[9]
		# dBook["shelf_location"] = vBook[16]
		dBook["title"] = CleanString( vBook[13] )
		# dBook["imprint"] = vBook[14]
		# dBook["series"] = vBook[15]
		dBook["bsn"] = vBook[17]
		dBook["lat"] = vBook[25]
		dBook["location"] = CleanString( vBook[10] )
		dBook["lng"] = vBook[26]
		
		# dBook = (vBook[0], vBook[1])
		vBooksJSON.append(dBook)
	
	jsonBooks = json.dumps(vBooksJSON)

	########################################
	# CATEGORIZED BOOK LIST
	########################################
	
	
	psqlCursor.close()
	psqlConn.close()

	########################################
	# RENDER HTML
	########################################
	return render_template("home.html", 
				vMonths = zip( list(range(1,len(vMonths)+1)), vMonths, vMonthSelected ),
				vYears = zip( vYears, vYearSelected ),
				vCategories = vCategories,
				vTitles = vTitles,
				jsonBooks = jsonBooks )
	

	
if __name__ == "__main__":
	app.run(debug=True)














