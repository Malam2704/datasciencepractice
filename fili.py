import geopandas as gpd
import matplotlib.pyplot as plt

data = {
    'Country':  ["Afghanistan", "Algeria", "Azerbaijan", "Bahrain", "Bangladesh", "Benin", "Bosnia and Herzegovina", "Brunei", "Burkina Faso", "Chad", "Comoros", "Djibouti", "Egypt", "Eritrea", "Gambia", "Guinea", "Indonesia", "Iran", "Iraq", "Jordan", "Kazakhstan", "Kosovo", "Kuwait", "Kyrgyzstan", "Lebanon", "Libya", "Malaysia", "Mali", "Mauritania", "Morocco", "Niger", "Nigeria", "Oman", "Pakistan", "Palestine", "Qatar", "Saudi Arabia", "Senegal", "Sierra Leone", "Somalia", "Sudan", "Syria", "Tajikistan", "Tunisia", "Turkey", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Western Sahara", "Yemen"],
    'SentimentDifference': [-40, -20, 15, 20, 10, 20, 5, 10, 30, -5, 25, 15, -10, -15, 25, 20, 5, -60, -30, -10, 15, 40, 15, 10, -30, -25, 0, 10, 20, 10, 25, 0, 20, -20, -50, 20, 10, 30, 25, -20, -10, -50, 15, 15, -20, 0, 25, 15, 20, -40],
    'Latitude': [33.939110, 28.033886, 40.143105, 26.0667, 23.6850, 9.3077, 43.9159, 4.5353, 12.2383, 15.4542, -11.6455, 11.8251, 26.8206, 15.1794, 13.4432, 9.9456, -0.7893, 32.4279, 33.2232, 30.5852, 48.0196, 42.6026, 29.3759, 41.2044, 33.8547, 26.3351, 4.2105, 17.5707, 21.0079, 31.7917, 17.6078, 9.0820, 21.4735, 30.3753, 31.9522, 25.3548, 23.6345, 14.4974, 8.4606, 5.1521, 12.8628, 34.8021, 38.8610, 33.8869, 38.9637, 38.9697, 23.4241, 41.3775, 24.2155, 15.5527],
    'Longitude': [67.709953, 1.659626, 47.576927, 50.5577, 90.3563, 2.3158, 17.6791, 114.7277, -1.5616, 18.7322, 43.3333, 42.5903, 30.8025, 39.7823, -15.3101, -9.6966, 113.9213, 53.6880, 43.6793, 36.2384, 66.9237, 20.9020, 47.4818, 74.7661, 35.8623, 17.2283, 101.9758, -3.9962, -10.9408, -7.0926, 8.0817, 8.6753, 55.9754, 69.3451, 35.2332, 51.1839, 45.0792, -14.4524, -11.7799, 46.1996, 30.2176, 39.0560, 71.2761, 9.5375, 35.2433, 59.5563, 53.8478, 64.5853, -12.8858, 48.5164]
}


df = gpd.GeoDataFrame(data)

# Load the world map shape
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the world map with your data
world = world.merge(df, how="left", left_on="name", right_on="Country")

# Set up the colors for the map based on sentiment difference


def color_mapper(value):
    if value < -30:
        return '#8b0000'  # dark red
    elif -30 <= value < 0:
        return '#ff4500'  # red
    elif 0 <= value < 30:
        return '#adff2f'  # light green
    else:
        return '#008000'  # dark green


world['color'] = world['SentimentDifference'].apply(color_mapper)

# Plot the map
fig, ax = plt.subplots(figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1)
world.plot(ax=ax, color=world['color'], legend=True)
plt.title("Sentiment Difference Map")
plt.show()
