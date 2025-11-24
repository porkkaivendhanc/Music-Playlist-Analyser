import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("music_playlist.csv")

# --- Calculations ---
average_duration = df["Duration"].mean()
most_common_genre = df["Genre"].mode()[0]
genre_counts = df["Genre"].value_counts()

# --- Bar Chart: Duration per Song ---
plt.figure(figsize=(10, 5))
plt.bar(df["Song name"], df["Duration"])
plt.xticks(rotation=45)
plt.title("Duration per Song")
plt.xlabel("Song")
plt.ylabel("Duration (seconds)")
plt.tight_layout()
plt.show()

# --- Bar Chart: Genre Distribution ---
plt.figure(figsize=(7, 5))
plt.bar(genre_counts.index, genre_counts.values)
plt.title("Genre Distribution")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Pie Chart: Genre Distribution ---
plt.figure(figsize=(6, 6))
plt.pie(genre_counts.values, labels=genre_counts.index, autopct='%1.1f%%')
plt.title("Genre Distribution (Pie Chart)")
plt.show()

# --- Insights ---
print("\n===== INSIGHTS =====")
print("1. Average song duration:", round(average_duration, 2), "seconds")
print("2. Most common genre:", most_common_genre)
print("3. You seem to prefer genres with the highest counts, showing your music taste pattern.")
