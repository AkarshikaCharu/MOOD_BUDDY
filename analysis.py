import random


def get_greeting(username):
    """Returns a random warm greeting upon login."""
    greetings = [
        f"Hi {username}! I've been waiting for you. ✨ How is your soul feeling today?",
        f"Welcome back, {username}. ☕ The world can be a lot, but you're safe here. What's on your mind?",
        f"There you are! 👋 I'm so glad you stopped by. Tell me everything."
    ]
    return random.choice(greetings)


def get_static_response(text):
    """Static logic for conversational responses based on keywords."""
    text = text.lower()

    if any(word in text for word in ["tired", "exhausted", "drain", "sleepy", "burnout"]):
        return "I hear you... that kind of tired is so heavy. I'm just glad you're here with me. No pressure to do anything but just be. ☕"

    if any(word in text for word in ["sad", "hurt", "cry", "upset", "lonely"]):
        return "I'm so sorry things feel this way. I'm right here, and I'm listening to every word. You aren't alone in this. 🫂"

    if any(word in text for word in ["irritated", "annoyed", "mad", "rude", "angry", "hate"]):
        return "I hear the frustration in your voice. It's valid to feel that way. Want to vent more about it? I'm a safe vault. 🕊️"

    if any(word in text for word in ["happy", "good", "great", "excited", "amazing"]):
        return "That's wonderful to hear! ✨ It makes me smile knowing things are looking up for you. Tell me more!"

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "Hey! I'm so happy to see your message. How has your day been treating you?"

    # Default fallback responses
    return random.choice([
        "That makes a lot of sense. I'm following you...",
        "I'm listening. Thank you for sharing that with me.",
        "I see. How does that make you feel overall?",
        "I'm right here. Go on, tell me more."
    ])


def get_mood_analysis(messages):
    """
    Scans chat history to provide a detailed summary report.
    Calculates mood distribution and word count.
    """
    user_messages = [m['content'].lower() for m in messages if m['role'] == 'user']
    history_text = " ".join(user_messages)

    if not user_messages or len(history_text) < 15:
        return "### 📊 Analysis Pending\n\nWe haven't talked much yet today. Share a bit more of your thoughts with me so I can give you a deeper look into your mood! ✨"

    # Define keyword groups
    mood_map = {
        "Exhausted/Overwhelmed": ["tired", "exhausted", "drain", "sleepy", "busy", "work", "stress"],
        "Sad/Sensitive": ["sad", "hurt", "cry", "upset", "miss", "lonely", "bad"],
        "Frustrated/Heated": ["annoyed", "angry", "mad", "hate", "rude", "boss", "irritated"],
        "Positive/Peaceful": ["good", "happy", "great", "better", "peace", "love", "thanks", "smile"]
    }

    # Calculate counts
    counts = {mood: sum(history_text.count(word) for word in words) for mood, words in mood_map.items()}

    # Determine primary vibe
    primary_mood = max(counts, key=counts.get)

    # If no keywords matched, default to 'Reflective'
    if counts[primary_mood] == 0:
        primary_mood = "Reflective/Quiet"

    # Calculate word count for "Energy Spent"
    word_count = len(history_text.split())

    # Build the report string
    report = f"""
    ## 📊 Your Personal Mood Report
    ---
    **Current Primary Vibe:** {primary_mood}

    **Words Shared:** {word_count}

    **Buddy's Observation:**
    Looking back at our conversation, you've used {word_count} words to express yourself. It seems like you are currently leaning into a **{primary_mood.split('/')[0]}** state of mind. 

    Whether you're feeling high or low, I want you to know that your feelings are valid. You've done a great job opening up today. 

    ---
    *Keep talking to me to refine this analysis!* 🕊️
    """
    return report