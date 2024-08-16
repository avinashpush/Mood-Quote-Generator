import requests
import random

def get_mood():
	print("Running")
	available_moods = [
		"anger", "attitude", "beauty", "cool", "courage", "dating", "failure",
		"faith", "family", "fear", "funny", "good", "great", "happiness",
		"health", "imagination", "inspirational", "jealousy", "learning", "love",
		"patience", "peace", "poetry", "positive", "power", "relationship",
		"respect", "romantic", "sad", "smile", "strength", "success",
		"sympathy", "thankful", "truth", "wisdom", "favorite", "motivational",
		"life", "morning"
	]
	print("What kind of quote are you in the mood for? (Ex: happiness, motivational, sad, anger, etc): ")
	print("Type 'all' for the full list of moods OR Type 'random' for a random mood: ")
	mood = input().strip().lower()
	if mood == 'all':
		for m in available_moods:
			print(m)
		mood = input("What kind of quote are you in the mood for?: ")
	if mood == 'random':
		mood = random.choice(available_moods)
	if mood not in available_moods:
		print("Invalid mood. Please choose a mood from the list.")
		return None
	return mood

def get_quote(mood):
	if mood is None:
		return "No valid mood was provided"

	url = f'https://mood-based-quote-api.p.rapidapi.com/{mood}'

	headers = {
		"x-rapidapi-key": "fc31d7256amshf328c54f849f777p1bdd02jsn8b20b6817008",
		"x-rapidapi-host": "mood-based-quote-api.p.rapidapi.com"
	}
	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()

		data = response.json()



		if 'result' in data and isinstance(data['result'], list) and data['result']:
			quotes = []
			for quote in data['result']:
				if "quote" in quote and "author" in quote:
					quote_text = quote['quote']
					author = quote['author']
					formatted_quote = f'"{quote_text}" - {author}'
					quotes.append(formatted_quote)
			return random.choice(quotes)
		else:
			return "No quotes found for the mood"


	except requests.exceptions.RequestException as e:
		return f"Error: {e}"

def main():
	mood = get_mood()
	if mood:
		quote = get_quote(mood)
		print(f"Quote for {mood}: {quote}")

if __name__ == "__main__":
    main()


