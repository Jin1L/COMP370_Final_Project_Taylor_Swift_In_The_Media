import csv, os, json

def main():
    path = os.path.join(os.path.dirname(__file__), '../data/taylor_swift_filtered_articles_500_oct_nov.csv')
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        popularity_index = header.index("popularity")

        popularity = {}
        # we have positive, negative, neutral
        popularity["positive"] = 0
        popularity["negative"] = 0
        popularity["neutral"] = 0

        for row in reader:
            popularity[row[popularity_index]] += 1

        # calculate percentages
        total = popularity["positive"] + popularity["negative"] + popularity["neutral"]
        popularity["positive"] = popularity["positive"] / total
        popularity["negative"] = popularity["negative"] / total
        popularity["neutral"] = popularity["neutral"] / total

        # write to json
        with open('popularity.json', 'w') as file:
            json.dump(popularity, file, indent=2)

if __name__ == '__main__':
    main()