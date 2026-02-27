import streamlit as st
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="My Smart Travel Planner",
    page_icon="✈️",
    layout="centered"
)

# ---------------- BACKGROUND ----------------
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .block-container {{
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            margin-top: 140px;
            background: rgba(0, 0, 0, 0.7);
            padding: 3rem;
            border-radius: 20px;
        }}

        h1, h2, h3, p, label {{
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("background.jpg")

# ---------------- TITLE ----------------
st.title("🌍 My Smart Travel Planner")
st.subheader("Complete State-wise Travel Planning")

# ---------------- STATE DATA ----------------
STATE_PLACES = {
 #---------------- ANDHRA PRADESH ----------------
"Andhra Pradesh": {
    "Tirupati": {
        "spots": ["Tirumala Temple", "Sri Kapileswara Temple", "Talakona Waterfalls", "Chandragiri Fort"],
        "food": ["Pulihora", "Laddu Prasadam", "Andhra Meals", "Dosa"],
        "stay": {
            "Budget": ["KVP Residency", "Hotel Bliss"],
            "Mid": ["Pai Viceroy", "Fortune Select"],
            "Luxury": ["Marasa Sarovar Premiere"]
        },
        "evening_activity": ["Evening Aarti at Temple", "Chandragiri Fort Sunset View", "Local Market Visit"]
    },
    "Visakhapatnam": {
        "spots": ["RK Beach", "Kailasagiri", "Submarine Museum", "Borra Caves"],
        "food": ["Fish Fry", "Prawn Curry", "Gongura Pickle", "Pootharekulu"],
        "stay": {
            "Budget": ["Treebo MVP", "Hotel Winsar"],
            "Mid": ["Novotel Vizag"],
            "Luxury": ["The Park Vizag"]
        },
        "evening_activity": ["RK Beach Sunset Walk", "Kailasagiri Night View", "Beachside Street Food"]
    },
    "Amaravati": {
        "spots": ["Amaravati Stupa", "Undavalli Caves", "Dhyana Buddha Statue"],
        "food": ["Andhra Thali", "Garelu", "Payasam"],
        "stay": {
            "Budget": ["Hotel Amaravati"],
            "Mid": ["Haritha Resort"],
            "Luxury": ["Vijayawada Marriott"]
        },
        "evening_activity": ["Dhyana Buddha Evening Illumination", "Krishna River Walk", "Local Handicraft Shopping"]
    },
    "Araku Valley": {
        "spots": ["Borra Caves", "Coffee Plantations", "Katiki Waterfalls"],
        "food": ["Bamboo Chicken", "Tribal Cuisine", "Fresh Coffee"],
        "stay": {
            "Budget": ["Haritha Resort"],
            "Mid": ["Casa Holiday Resort"],
            "Luxury": ["Premium Coffee Estate Stay"]
        },
        "evening_activity": ["Sunset at Viewpoint", "Tribal Cultural Dance Show", "Bonfire Night at Resort"]
    }
},


# ---------------- ARUNACHAL PRADESH ----------------
"Arunachal Pradesh": {
    "Tawang": {
        "spots": ["Tawang Monastery", "Sela Pass", "Madhuri Lake"],
        "food": ["Thukpa", "Momos", "Butter Tea"],
        "stay": {
            "Budget": ["Hotel Tawang Holiday"],
            "Mid": ["Tawang Inn"],
            "Luxury": ["Premium Mountain Resort"]
        },
        "evening_activity": ["Monastery Evening Prayer", "Sunset at Sela Pass", "Local Market Walk"]
    },
    "Ziro": {
        "spots": ["Ziro Valley", "Talley Valley Sanctuary"],
        "food": ["Smoked Pork", "Apong", "Local Rice Dishes"],
        "stay": {
            "Budget": ["Blue Pine Hotel"],
            "Mid": ["Ziro Palace Inn"],
            "Luxury": ["Eco Luxury Resort"]
        },
        "evening_activity": ["Valley Sunset View", "Traditional Apatani Cultural Show", "Bonfire Night"]
    },
    "Itanagar": {
        "spots": ["Ita Fort", "Ganga Lake"],
        "food": ["Momos", "Thukpa"],
        "stay": {
            "Budget": ["Hotel Arun Subansiri"],
            "Mid": ["Cygnett Inn"],
            "Luxury": ["Premium Resort"]
        },
        "evening_activity": ["Ganga Lake Sunset Walk", "Local Night Market Visit", "Cultural Dance Performance"]
    }
},

# ---------------- ASSAM ----------------
"Assam": {
    "Guwahati": {
        "spots": ["Kamakhya Temple", "Umananda Island", "Assam Zoo"],
        "food": ["Masor Tenga", "Pitha", "Assam Thali"],
        "stay": {
            "Budget": ["Hotel Rajmahal"],
            "Mid": ["Vivanta Guwahati"],
            "Luxury": ["Radisson Blu"]
        },
        "evening_activity": ["Brahmaputra River Sunset Cruise", "Kamakhya Temple Evening Aarti", "Fancy Bazaar Night Shopping"]
    },
    "Kaziranga National Park": {
        "spots": ["Jeep Safari", "Elephant Safari"],
        "food": ["Assamese Thali"],
        "stay": {
            "Budget": ["Nature Hunt Camp"],
            "Mid": ["Infinity Resort"],
            "Luxury": ["Diphlu River Lodge"]
        },
        "evening_activity": ["Sunset Nature Walk", "Campfire at Jungle Resort", "Traditional Bihu Dance Performance"]
    },
    "Majuli": {
        "spots": ["Majuli Island", "Satras"],
        "food": ["Fish Curry", "Rice Beer"],
        "stay": {
            "Budget": ["La Maison de Ananda"],
            "Mid": ["Okegiga Homes"],
            "Luxury": ["Premium Riverside Stay"]
        },
        "evening_activity": ["Brahmaputra Sunset View", "Satras Evening Prayer", "Cultural Folk Music Night"]
    }
},

# ---------------- BIHAR ----------------
"Bihar": {
    "Patna": {
        "spots": ["Golghar", "Patna Museum"],
        "food": ["Litti Chokha", "Thekua"],
        "stay": {
            "Budget": ["Hotel Patliputra"],
            "Mid": ["Hotel Maurya"],
            "Luxury": ["Lemon Tree Premier"]
        },
        "evening_activity": ["Ganga River Sunset View", "Golghar Evening Walk", "Local Street Food Trail"]
    },
    "Bodh Gaya": {
        "spots": ["Mahabodhi Temple", "Great Buddha Statue"],
        "food": ["Khaja", "North Indian Thali"],
        "stay": {
            "Budget": ["Hotel Taj Darbar"],
            "Mid": ["Bodhgaya Regency"],
            "Luxury": ["Marasa Sarovar"]
        },
        "evening_activity": ["Mahabodhi Temple Evening Prayer", "Meditation Session", "Monastery Cultural Visit"]
    },
    "Nalanda": {
        "spots": ["Nalanda University Ruins"],
        "food": ["Bihari Thali"],
        "stay": {
            "Budget": ["Nalanda Guest House"],
            "Mid": ["Rajgir Residency"],
            "Luxury": ["Premium Heritage Stay"]
        },
        "evening_activity": ["Nalanda Ruins Sunset View", "Heritage Walk", "Cultural Folk Performance"]
    }
},

# ---------------- CHHATTISGARH ----------------
"Chhattisgarh": {
    "Raipur": {
        "spots": ["Nandan Van Zoo", "Vivekananda Sarovar"],
        "food": ["Chana Samosa", "Faraa"],
        "stay": {
            "Budget": ["Hotel Meera"],
            "Mid": ["Courtyard Marriott"],
            "Luxury": ["Sayaji Hotel"]
        },
        "evening_activity": ["Vivekananda Sarovar Lake Walk", "Marine Drive Raipur Visit", "Local Street Food Exploration"]
    },
    "Jagdalpur": {
        "spots": ["Chitrakote Falls", "Kanger Valley Park"],
        "food": ["Tribal Cuisine"],
        "stay": {
            "Budget": ["Bastar Jungle Camp"],
            "Mid": ["Hotel Devansh Residency"],
            "Luxury": ["Premium Forest Resort"]
        },
        "evening_activity": ["Chitrakote Falls Sunset View", "Campfire at Jungle Resort", "Tribal Cultural Dance Show"]
    },
    "Chitrakote Falls": {
        "spots": ["Chitrakote Waterfalls"],
        "food": ["Local Tribal Dishes"],
        "stay": {
            "Budget": ["Tourism Guest House"],
            "Mid": ["Jagdalpur Hotel"],
            "Luxury": ["Luxury Jungle Stay"]
        },
        "evening_activity": ["Waterfall Sunset Photography", "Riverside Relaxation", "Bonfire Night Experience"]
    }
},

# ---------------- GOA ----------------
"Goa": {
    "Goa": {
        "spots": ["Baga Beach", "Calangute Beach", "Dudhsagar Falls"],
        "food": ["Fish Curry", "Bebinca", "Vindaloo"],
        "stay": {
            "Budget": ["Zostel Goa"],
            "Mid": ["Resort Rio"],
            "Luxury": ["Taj Exotica"]
        },
        "evening_activity": ["Beach Sunset Walk", "Beach Shack Dinner", "Night Beach Party"]
    },
    "Panaji": {
        "spots": ["Fontainhas", "Miramar Beach"],
        "food": ["Xacuti", "Sorpotel"],
        "stay": {
            "Budget": ["Hotel Palacio"],
            "Mid": ["Country Inn"],
            "Luxury": ["Grand Hyatt Goa"]
        },
        "evening_activity": ["Mandovi River Cruise", "Fontainhas Evening Walk", "Casino Night Experience"]
    },
    "Baga": {
        "spots": ["Baga Beach", "Tito’s Lane"],
        "food": ["Seafood Platter", "Goan Curry"],
        "stay": {
            "Budget": ["Roadhouse Hostel"],
            "Mid": ["La Calypso"],
            "Luxury": ["W Goa"]
        },
        "evening_activity": ["Baga Beach Sunset", "Tito’s Lane Nightlife", "Beach Club Party"]
    }
},

# ---------------- GUJARAT ----------------
"Gujarat": {
    "Ahmedabad": {
        "spots": ["Sabarmati Ashram", "Kankaria Lake", "Adalaj Stepwell"],
        "food": ["Dhokla", "Khandvi", "Gujarati Thali"],
        "stay": {
            "Budget": ["Hotel Accolade"],
            "Mid": ["Lemon Tree Hotel"],
            "Luxury": ["Hyatt Regency"]
        },
        "evening_activity": ["Kankaria Lake Night Walk", "Sabarmati Riverfront Visit", "Manek Chowk Street Food"]
    },
    "Statue of Unity": {
        "spots": ["Statue of Unity", "Valley of Flowers", "Sardar Sarovar Dam"],
        "food": ["Gujarati Thali", "Thepla"],
        "stay": {
            "Budget": ["Tent City Budget"],
            "Mid": ["Tent City Narmada"],
            "Luxury": ["Luxury Tent City"]
        },
        "evening_activity": ["Statue of Unity Light & Sound Show", "Sunset at Sardar Sarovar Dam", "Riverside Walk"]
    },
    "Rann of Kutch": {
        "spots": ["White Rann", "Kala Dungar", "Rann Utsav"],
        "food": ["Kutchi Dabeli", "Bajra Roti"],
        "stay": {
            "Budget": ["Dhordo Camps"],
            "Mid": ["Rann Riders"],
            "Luxury": ["Luxury Desert Camp"]
        },
        "evening_activity": ["White Rann Sunset View", "Rann Utsav Cultural Program", "Desert Stargazing"]
    },
    "Somnath": {
        "spots": ["Somnath Temple", "Triveni Sangam"],
        "food": ["Gujarati Thali"],
        "stay": {
            "Budget": ["Hotel Sun Plaza"],
            "Mid": ["Lords Inn"],
            "Luxury": ["The Fern Residency"]
        },
        "evening_activity": ["Somnath Temple Evening Aarti", "Light & Sound Show", "Beach Sunset Walk"]
    }
},

# ---------------- HIMACHAL PRADESH ----------------
"Himachal Pradesh": {
    "Shimla": {
        "spots": ["Mall Road", "Jakhoo Temple", "Kufri"],
        "food": ["Siddu", "Madra"],
        "stay": {
            "Budget": ["Hotel Willow Banks"],
            "Mid": ["Snow Valley Resort"],
            "Luxury": ["Oberoi Cecil"]
        },
        "evening_activity": ["Mall Road Evening Walk", "Ridge Sunset View", "Cafe Hopping"]
    },
    "Manali": {
        "spots": ["Solang Valley", "Rohtang Pass", "Hadimba Temple"],
        "food": ["Trout Fish", "Himachali Thali"],
        "stay": {
            "Budget": ["Zostel Manali"],
            "Mid": ["The Orchard Greens"],
            "Luxury": ["The Himalayan"]
        },
        "evening_activity": ["Old Manali Cafe Visit", "Bonfire Night", "Mall Road Shopping"]
    },
    "Dharamshala": {
        "spots": ["McLeodganj", "Bhagsu Waterfall"],
        "food": ["Thukpa", "Momos"],
        "stay": {
            "Budget": ["Backpackers Inn"],
            "Mid": ["Hotel Inclover"],
            "Luxury": ["Fortune Park"]
        },
        "evening_activity": ["McLeodganj Sunset View", "Monastery Evening Prayer", "Tibetan Market Walk"]
    },
    "Spiti Valley": {
        "spots": ["Key Monastery", "Chandratal Lake"],
        "food": ["Butter Tea", "Barley Bread"],
        "stay": {
            "Budget": ["Homestay"],
            "Mid": ["Spiti Valley Hotel"],
            "Luxury": ["Premium Eco Resort"]
        },
        "evening_activity": ["Mountain Sunset Photography", "Bonfire Under Stars", "Stargazing Experience"]
    }
},

# ---------------- KARNATAKA ----------------
"Karnataka": {
    "Bengaluru": {
        "spots": ["Lalbagh", "Cubbon Park", "Bangalore Palace"],
        "food": ["Masala Dosa", "Bisi Bele Bath"],
        "stay": {
            "Budget": ["Treebo Trend"],
            "Mid": ["The Chancery Pavilion"],
            "Luxury": ["Taj West End"]
        },
        "evening_activity": ["MG Road & Brigade Road Walk", "UB City Rooftop Dinner", "Indiranagar Pub Hopping"]
    },
    "Mysuru": {
        "spots": ["Mysore Palace", "Chamundi Hills"],
        "food": ["Mysore Pak", "Mysore Masala Dosa"],
        "stay": {
            "Budget": ["Hotel Roopa"],
            "Mid": ["Royal Orchid Metropole"],
            "Luxury": ["Radisson Blu"]
        },
        "evening_activity": ["Mysore Palace Illumination", "Devaraja Market Visit", "Brindavan Gardens Musical Fountain"]
    },
    "Hampi": {
        "spots": ["Virupaksha Temple", "Vittala Temple"],
        "food": ["South Indian Thali"],
        "stay": {
            "Budget": ["Gopi Guest House"],
            "Mid": ["Heritage Resort"],
            "Luxury": ["Evolve Back"]
        },
        "evening_activity": ["Matanga Hill Sunset", "Riverside Coracle Ride", "Heritage Walk Under Stars"]
    },
    "Coorg": {
        "spots": ["Abbey Falls", "Raja’s Seat"],
        "food": ["Pandi Curry", "Coorgi Kadambuttu"],
        "stay": {
            "Budget": ["Coorg Jungle Camp"],
            "Mid": ["Club Mahindra"],
            "Luxury": ["Taj Madikeri"]
        },
        "evening_activity": ["Raja’s Seat Sunset View", "Bonfire Night at Resort", "Coffee Plantation Walk"]
    }
},

# ---------------- KERALA ----------------
"Kerala": {
    "Munnar": {
        "spots": ["Tea Gardens", "Eravikulam National Park"],
        "food": ["Appam & Stew", "Kerala Sadya"],
        "stay": {
            "Budget": ["Green Ridge"],
            "Mid": ["Tea Valley Resort"],
            "Luxury": ["Blanket Hotel & Spa"]
        },
        "evening_activity": ["Tea Garden Sunset View", "Campfire Night", "Local Spice Market Visit"]
    },
    "Alleppey": {
        "spots": ["Backwaters", "Houseboat Ride"],
        "food": ["Karimeen Pollichathu"],
        "stay": {
            "Budget": ["Venice Castle"],
            "Mid": ["Houseboat Stay"],
            "Luxury": ["Lake Palace Resort"]
        },
        "evening_activity": ["Backwater Sunset Cruise", "Houseboat Candlelight Dinner", "Village Walk"]
    },
    "Kochi": {
        "spots": ["Fort Kochi", "Chinese Fishing Nets"],
        "food": ["Malabar Biryani"],
        "stay": {
            "Budget": ["Happy Camper Hostel"],
            "Mid": ["Casino Hotel"],
            "Luxury": ["Taj Malabar"]
        },
        "evening_activity": ["Kathakali Cultural Show", "Marine Drive Night Walk", "Fort Kochi Cafe Hopping"]
    },
    "Varkala": {
        "spots": ["Varkala Beach", "Cliff Walk"],
        "food": ["Seafood", "Kerala Thali"],
        "stay": {
            "Budget": ["Zostel Varkala"],
            "Mid": ["Palm Tree Heritage"],
            "Luxury": ["Gateway Varkala"]
        },
        "evening_activity": ["Cliff Sunset Walk", "Beachside Seafood Dinner", "Live Music at Cliff Cafes"]
    }
},

# ---------------- MAHARASHTRA ----------------
"Maharashtra": {
    "Mumbai": {
        "spots": ["Gateway of India", "Marine Drive", "Elephanta Caves"],
        "food": ["Vada Pav", "Pav Bhaji"],
        "stay": {
            "Budget": ["Hotel Residency"],
            "Mid": ["The Gordon House"],
            "Luxury": ["Taj Mahal Palace"]
        },
        "evening_activity": ["Marine Drive Night Walk", "Colaba Causeway Shopping", "Rooftop Dining Experience"]
    },
    "Pune": {
        "spots": ["Shaniwar Wada", "Sinhagad Fort"],
        "food": ["Misal Pav", "Mastani"],
        "stay": {
            "Budget": ["Hotel Sapna"],
            "Mid": ["Hyatt Pune"],
            "Luxury": ["JW Marriott"]
        },
        "evening_activity": ["Shaniwar Wada Light & Sound Show", "FC Road Food Walk", "Koregaon Park Cafe Visit"]
    },
    "Lonavala": {
        "spots": ["Tiger Point", "Bhushi Dam"],
        "food": ["Chikki"],
        "stay": {
            "Budget": ["Zostel Lonavala"],
            "Mid": ["Fariyas Resort"],
            "Luxury": ["Della Resorts"]
        },
        "evening_activity": ["Tiger Point Sunset View", "Lakeside Relaxation", "Resort Bonfire Night"]
    },
    "Ajanta & Ellora": {
        "spots": ["Ajanta Caves", "Ellora Caves"],
        "food": ["Maharashtrian Thali"],
        "stay": {
            "Budget": ["Hotel Kailas"],
            "Mid": ["Ambassador Ajanta"],
            "Luxury": ["Vivanta Aurangabad"]
        },
        "evening_activity": ["Ellora Caves Sunset View", "Heritage Walk", "Cultural Folk Performance"]
    }
},
}
# ---------------- DYNAMIC TRAVEL SYSTEM ----------------

PLACE_CATEGORY = {
    "Goa": "Beach",
    "Baga": "Beach",
    "Varkala": "Beach",
    "Munnar": "Hill",
    "Manali": "Hill",
    "Shimla": "Hill",
    "Coorg": "Hill",
    "Mumbai": "City",
    "Bengaluru": "City",
    "Ahmedabad": "City",
    "Tirupati": "Heritage",
    "Somnath": "Heritage",
    "Hampi": "Heritage",
    "Kaziranga National Park": "Wildlife",
    "Rann of Kutch": "Desert"
}

CATEGORY_COST = {
    "Beach": 1.2,
    "Hill": 1.1,
    "City": 1.3,
    "Heritage": 1.0,
    "Wildlife": 1.4,
    "Desert": 1.3
}

def generate_travel_data(place, travel_type):

    base_cost = {
        "Friends": 20000,
        "Family": 30000,
        "Solo": 15000
    }

    base_style = {
        "Friends": "Adventure, nightlife, group activities",
        "Family": "Comfort travel, sightseeing, cultural places",
        "Solo": "Self-exploration, nature & peaceful travel"
    }

    category = PLACE_CATEGORY.get(place, "City")
    multiplier = CATEGORY_COST.get(category, 1)

    adjusted_cost = int(base_cost[travel_type] * multiplier)

    essentials_by_category = {
        "Beach": ["Sunscreen", "Slippers", "Light clothes", "Sunglasses"],
        "Hill": ["Jacket", "Comfort shoes", "Thermal wear"],
        "City": ["Power bank", "Casual wear", "ID proof"],
        "Heritage": ["Comfort shoes", "Water bottle", "Camera"],
        "Wildlife": ["Binoculars", "Full sleeves", "First aid kit"],
        "Desert": ["Cap", "Sunglasses", "Water bottle"]
    }

    return {
        "cost": f"₹{adjusted_cost} – ₹{adjusted_cost + 15000}",
        "essentials": essentials_by_category.get(category, ["Basic travel items"]),
        "style": base_style[travel_type]
    }


# ---------------- ITINERARY FUNCTION ----------------
def generate_itinerary(state, place, days, travel_type):

    details = STATE_PLACES[state][place]
    trip = generate_travel_data(place, travel_type)


    spots = details["spots"]
    foods = details["food"]
    stay = details["stay"]

    itinerary = f"""
## 🌍 Complete Travel Plan

### 🗺 State: {state}
### 📍 Destination: {place}
### 👥 Travel Type: {travel_type}

### 💰 Estimated Cost:
{trip['cost']}

### 🎒 Essentials:
{', '.join(trip['essentials'])}

### ✨ Travel Style:
{trip['style']}

---

## 🏨 Recommended Stay

**Budget:** {', '.join(stay['Budget'])}  
**Mid-Range:** {', '.join(stay['Mid'])}  
**Luxury:** {', '.join(stay['Luxury'])}

---

## 🗓️ Day-wise Plan
"""

    spot_index = 0

    for day in range(1, days + 1):
        morning = spots[spot_index % len(spots)]
        afternoon = spots[(spot_index + 1) % len(spots)]
        evening = spots[(spot_index + 2) % len(spots)]
        food = foods[day % len(foods)]

        itinerary += f"""
### 🗓 Day {day}

🌅 Morning: Visit **{morning}**  
🍽 Lunch: Try **{food}**  
🏞 Afternoon: Explore **{afternoon}**  
🌇 Evening: Visit **{evening}**

---
"""
        spot_index += 3

    return itinerary

# ---------------- INPUTS ----------------
# ---------------- INPUTS ----------------

state_options = ["Select State"] + list(STATE_PLACES.keys())
state = st.selectbox("Select State", state_options)

if state == "Select State":
    place = st.selectbox("Select Place", ["Select Place"])
else:
    place_options = ["Select Place"] + list(STATE_PLACES[state].keys())
    place = st.selectbox("Select Place", place_options)

# ✅ DEFINE travel_type HERE
travel_type = st.selectbox("Traveling With", ["Select","Friends", "Family", "Solo"])

days = st.slider("Number of Days", 1, 20)


# ---------------- BUTTON ----------------
if st.button("Generate Travel Plan"):

    if state == "Select State" or place == "Select Place":
        st.error("Please select a valid State and Place.")
    else:
        plan = generate_itinerary(state, place, days,travel_type)
        st.success("Your Personalized Travel Plan")
        st.markdown(plan)

