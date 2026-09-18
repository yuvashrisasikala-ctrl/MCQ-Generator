import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="SkyCast AI",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ SkyCast")
st.caption("Your simple weather forecast dashboard")

# -------------------------------
# Weather API
# -------------------------------

def find_city(city):

    response = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        },
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        return None

    return data["results"][0]


def fetch_forecast(latitude, longitude):

    response = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "daily": (
                "temperature_2m_max,"
                "temperature_2m_min,"
                "precipitation_probability_max"
            ),
            "forecast_days": 5,
            "timezone": "auto"
        },
        timeout=10
    )

    response.raise_for_status()

    return response.json()


# -------------------------------
# User Interface
# -------------------------------

st.sidebar.header("📍 Search Location")

city = st.sidebar.text_input(
    "Enter city",
    "Chennai"
)

search = st.sidebar.button(
    "Search Weather"
)

if search:

    try:

        with st.spinner("Finding location..."):

            location = find_city(city)

        if location is None:

            st.error("City not found. Try another name.")

        else:

            latitude = location["latitude"]
            longitude = location["longitude"]

            with st.spinner("Loading forecast..."):

                data = fetch_forecast(
                    latitude,
                    longitude
                )

            daily = data["daily"]

            city_name = location["name"]
            country = location.get("country", "")

            st.header(
                f"🌍 {city_name}, {country}"
            )

            # -------------------------------
            # Forecast DataFrame
            # -------------------------------

            forecast = pd.DataFrame({

                "Date": daily["time"],

                "Maximum Temperature (°C)":
                    daily["temperature_2m_max"],

                "Minimum Temperature (°C)":
                    daily["temperature_2m_min"],

                "Rain Probability (%)":
                    daily["precipitation_probability_max"]

            })

            # -------------------------------
            # Today's Weather
            # -------------------------------

            st.subheader("☀️ Today's Forecast")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Maximum",
                    f"{forecast.iloc[0, 1]} °C"
                )

            with col2:

                st.metric(
                    "Minimum",
                    f"{forecast.iloc[0, 2]} °C"
                )

            with col3:

                st.metric(
                    "Rain Probability",
                    f"{forecast.iloc[0, 3]}%"
                )

            # -------------------------------
            # Temperature Chart
            # -------------------------------

            st.subheader("📊 5-Day Temperature Chart")

            chart_data = forecast.set_index("Date")[
                [
                    "Maximum Temperature (°C)",
                    "Minimum Temperature (°C)"
                ]
            ]

            st.line_chart(chart_data)

            # -------------------------------
            # Forecast Table
            # -------------------------------

            st.subheader("📅 Upcoming Forecast")

            st.dataframe(
                forecast,
                use_container_width=True,
                hide_index=True
            )

            # -------------------------------
            # Recommendation
            # -------------------------------

            st.subheader("💡 Weather Advice")

            rain = forecast.iloc[0, 3]
            maximum = forecast.iloc[0, 1]

            if rain >= 60:

                st.info(
                    "🌧️ Rain may be likely today. "
                    "Consider carrying an umbrella."
                )

            elif maximum >= 35:

                st.info(
                    "☀️ High temperatures are expected. "
                    "Stay hydrated and seek shade when needed."
                )

            else:

                st.success(
                    "🌤️ Check the forecast before planning "
                    "your outdoor activities."
                )

    except requests.RequestException:

        st.error(
            "Unable to connect to the weather service."
        )

    except Exception as error:

        st.error(
            f"Something went wrong: {error}"
        )

else:

    st.info(
        "👈 Enter a city name and click Search Weather."
    )