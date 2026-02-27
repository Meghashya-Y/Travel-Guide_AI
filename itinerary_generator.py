def generate_itinerary(destination, days, interests):
    itinerary = f"🌍 Travel Itinerary for {destination}\n"
    itinerary += f"🗓 Duration: {days} days\n"
    itinerary += f"🎯 Interests: {interests}\n\n"

    for day in range(1, days + 1):
        itinerary += f"Day {day}:\n"
        itinerary += f"- Morning: Explore popular attractions in {destination}\n"
        itinerary += f"- Afternoon: Enjoy local food and cultural spots\n"
        itinerary += f"- Evening: Relax and explore nearby markets\n\n"

    itinerary += "✨ Travel Tips:\n"
    itinerary += "- Start early to avoid crowds\n"
    itinerary += "- Stay hydrated\n"
    itinerary += "- Try local cuisine\n"

    return itinerary


# -------- TEST THE FUNCTION --------
if __name__ == "__main__":
    destination = "Goa"
    days = 3
    interests = "Beaches, food, sightseeing"

    result = generate_itinerary(destination, days, interests)
    print(result)
