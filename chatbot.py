# Cryptocurrency Advisor Chatbot

# Predefined crypto dataset
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

# Function to analyze and recommend cryptocurrencies
def crypto_advisor():
    print("Welcome to CryptoAdvisor! 🤖💰")
    print("I can help you analyze cryptocurrencies based on profitability and sustainability.")
    print("Available cryptocurrencies: Bitcoin, Ethereum, Cardano")
    print("You can ask questions like:")
    print("- Which crypto is trending up?")
    print("- What's the most sustainable coin?")
    print("- What should I buy for long-term growth?")
    print("- Which crypto is both profitable and sustainable?")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_query = input("You: ").lower()
        
        if user_query == 'quit':
            print("CryptoAdvisor: Happy investing! Remember to do your own research too. 🚀")
            break
            
        # Check for trending up cryptos
        elif any(word in user_query for word in ["trend", "rising", "going up"]):
            trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
            if trending:
                print(f"CryptoAdvisor: These cryptos are currently trending up: {', '.join(trending)} 📈")
                # Recommend the one with highest market cap among trending
                recommend = max(trending, key=lambda x: 1 if crypto_db[x]["market_cap"] == "high" else 0.5)
                print(f"  My top pick from these is {recommend} due to its strong market position.")
            else:
                print("CryptoAdvisor: No cryptocurrencies are currently showing a strong upward trend.")
                
        # Check for sustainability questions
        elif any(word in user_query for word in ["sustain", "eco", "green", "environment"]):
            recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
            score = crypto_db[recommend]["sustainability_score"]
            print(f"CryptoAdvisor: {recommend} is the most sustainable option with a score of {score*10}/10! 🌱")
            print(f"  It has {crypto_db[recommend]['energy_use']} energy consumption.")
            
        # Check for long-term growth
        elif any(word in user_query for word in ["long-term", "long term", "future", "growth"]):
            # Balance between sustainability and price trend
            scored_coins = []
            for coin in crypto_db:
                score = 0
                if crypto_db[coin]["price_trend"] == "rising":
                    score += 4
                elif crypto_db[coin]["price_trend"] == "stable":
                    score += 2
                
                if crypto_db[coin]["market_cap"] == "high":
                    score += 3
                elif crypto_db[coin]["market_cap"] == "medium":
                    score += 2
                
                score += crypto_db[coin]["sustainability_score"] * 3
                scored_coins.append((coin, score))
            
            if scored_coins:
                recommend = max(scored_coins, key=lambda x: x[1])[0]
                print(f"CryptoAdvisor: For long-term growth, consider {recommend}! 🚀")
                print(f"  It has a {'rising' if crypto_db[recommend]['price_trend'] == 'rising' else 'stable'} price trend,")
                print(f"  {crypto_db[recommend]['market_cap']} market cap, and")
                print(f"  a sustainability score of {crypto_db[recommend]['sustainability_score']*10}/10.")
                
        # Check for profitable and sustainable
        elif any(word in user_query for word in ["both", "profit and sustain", "balanced"]):
            profitable_sustainable = []
            for coin in crypto_db:
                if crypto_db[coin]["price_trend"] in ["rising", "stable"] and crypto_db[coin]["sustainability_score"] >= 0.6:
                    profitable_sustainable.append(coin)
            
            if profitable_sustainable:
                print("CryptoAdvisor: These cryptos balance profitability and sustainability:")
                for coin in profitable_sustainable:
                    print(f"  - {coin}: Trending {crypto_db[coin]['price_trend']}, Sustainability {crypto_db[coin]['sustainability_score']*10}/10")
            else:
                print("CryptoAdvisor: Currently no cryptos meet both strong profitability and sustainability criteria.")
                
        # General advice
        elif any(word in user_query for word in ["advice", "recommend", "suggest", "should i buy"]):
            print("CryptoAdvisor: Here's my general analysis:")
            print("1. For profitability (short-term):")
            profitable = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising"]
            if profitable:
                print(f"   - Trending up: {', '.join(profitable)}")
            else:
                print("   - No strong trends currently")
            
            print("\n2. For sustainability:")
            sustainable = sorted(crypto_db.items(), key=lambda x: x[1]["sustainability_score"], reverse=True)
            for coin, data in sustainable:
                print(f"   - {coin}: {data['sustainability_score']*10}/10")
            
            print("\nRemember: Crypto investments carry risk. Diversify and only invest what you can afford to lose.")
            
        else:
            print("CryptoAdvisor: I'm not sure I understand. Try asking about:")
            print("- Price trends")
            print("- Sustainability")
            print("- Long-term growth potential")
            print("- Balanced options")

# Start the chatbot
if __name__ == "__main__":
    crypto_advisor()