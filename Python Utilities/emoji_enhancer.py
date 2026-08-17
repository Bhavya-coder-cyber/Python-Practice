emoji_map = {
    "love": "❤️",
    "like": "👍",
    "dislike": "👎",
    "angry": "😡",
    "code": "💻",
    "happy": "😊",
    "music": "🎵",
    "food": "🍔",
}

message = input("Enter your message: ")
updated_words = []

for word in message.split():
    emoji = word.lower().strip(".,?")
    if emoji in emoji_map:
        updated_words.append(emoji_map.get(emoji) + " ")
    else:
        updated_words.append(word)

final_message = " ".join(updated_words)
print(final_message)