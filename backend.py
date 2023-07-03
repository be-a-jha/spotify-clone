import csv
from flask import Flask, request, render_template

app = Flask(__name__)

def search_spotipy(file_path, query):
    results = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip the header row
        for row in reader:
            for value in row:
                if query.lower() in value.lower():
                    results.append(row)
                    break  # Found a match, no need to continue searching this row
    return results

@app.route("/search")
def search():
    file_path = 'C:/Users/be_a_jha/spotify/spotifydataset.csv'  # Update the file path
    query = request.args.get("query")  # Retrieve the search query from the request
    search_results = search_spotipy(file_path, query)  # Call the search function

    if len(search_results) > 0:
        return render_template("searchresult.html", results=search_results)
    else:
        return "No results found."

if __name__ == '__main__':
    app.run()
