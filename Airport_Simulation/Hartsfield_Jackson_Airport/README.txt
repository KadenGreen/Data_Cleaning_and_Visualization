Additional information of given data sets:

-----flights.csv-----
year - year of flight
month - numerical month of flight
day - numerical day of flight
day_of_week - 1=sunday, 2=monday, 3=tuesday, ... , 7=saturday
airline - two letter code of the airline carrying the flight
flight_number - unique number given to each flight for air traffic coordination
tail_number - unique number given to a plane, similar to a liscense plate
origin_airport - airport the plane takes off at
destination_airport - airport the planes is attempting to land at
scheduled_departure - time plane is intended to depart
departure_time - actual time plane departs
departure_delay - departure_time minus scheduled_departure (in minutes)
taxi_out - time from departure to wheels off
wheels_off - time of plane take off
scheduled_time - planned time from wheels off to wheels on
air_time - time from wheels off to wheels on (flight time)
distance - distance flown from origin airport to destination airport in miles
wheels_on - time of plane landing
taxi_in - time from plane landing to arrival at gate
scheduled_arrival - estimated time of plane arrival
arrival_time - actual time of arrival 
arrival_delay - arrival_time minus scheduled_arrival
diverted - 0=not diverted, 1=diverted elsewhere
canceled - 0=not canceled, 1=canceled
cancellation_reason - A=maintenance problem B=incliment weather C=under capacity D=other
Air_system_delay - Delay caused by air traffic when trying to land
security_delay - Delay caused by airport security
airline_delay - Delay caused by airline at gate
late_aircraft_delay - delay due to aircraft falling behind schedule in previous flights (causes no fee to either airport or airline)
weather_delay - delay caused by incliment weather

-----flights_test_size.csv-----
The same as flights.csv, but only the first 10,000 rows
Will allow you to develop the code to clean/analyze the data without having long waits on large operations(especially imports and exports of the csv)

-----airports.csv-----
IATA_CODE - 3 character code given to each airport
AIRPORT - full name of airport
CITY - city airport is located in
STATE - state airport is located in
COUNTRY - country airport is located in
LATITUDE - geographical latitude coordinate of airport
LONGITUDE - geographical longitude coordinate of airport
BASE GATE COST - cost to an airline for a flight to use an airport gate
AIRLINE DELAY FEE - fee cost per minute in dollars an airline pays the airport for delays it causes (applys only to outbound)
AIR SYSTEM DELAY FEE / MIN - fee cost per minute in dollars an airport pays to a respective flight's airline from air system delays (applys only to inbound planes)
SECURITY DELAY FEE / MIN - fee cost per minute in dollars an airport pays to a respective flight's airline from security delays (applys only to outbound planes)


-----planes.csv-----
TAIL NUMBER - unique number given to a plane, similar to a liscense plate
PASSENGER CAPACITY - max passanger capacity of the plane
FUEL COST/MILE - cost of fuel per mile of flight
BASE COST/FLIGHT - cost of crew, maintenece, and other costs not including the airport gate rental or fuel
