from flask import Flask, render_template
from funcs import read_track_data, read_base_points

app = Flask(__name__)

@app.route('/')
def track():
    points = read_track_data()
    start_points, land_points = read_base_points()
    lat_lon = [[point[1], point[2]] for point in points]
    return render_template('index.html', lat_lon=lat_lon, start_points=start_points, land_points=land_points)

if __name__ == '__main__':
    app.run(debug=True)