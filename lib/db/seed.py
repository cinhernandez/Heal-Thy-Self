from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from random import random, randint, choice as rc

from models import Base, Festival, Add_To_Cart, Genre_Option, festival_genre_option

engine = create_engine('sqlite:///music_festivals.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# def add_to_carts(festivals, genre_options, session):
#     print("Deleting existing add to carts...")
#     session.query(Add_To_Cart).delete()
#     session.commit()

#     print("Adding to carts...")
#     add_to_carts = []
#     for i in range(30):
#         atc_genre_option = random.choice(genre_options)
#         atc_festivals = [random.choice(festivals) for i in range(15)]
#         add_to_cart = Add_To_Cart()
#         add_to_cart.festivals = []
#         add_to_cart.genre_id = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Assuming genre options are [1, 2, 3]
#         for festival in atc_festivals:
#             if festival not in atc_genre_option.festivals:
#                 atc_genre_option.festivals.append(festival)
#         add_to_carts.append(add_to_cart)

#     session.add_all(genre_options)
#     session.add_all(add_to_carts)
#     session.commit()


festival1 = Festival(name="Electric Zoo", date="September 3-5, 2023", location="New York, NY", price=300)
festival2 = Festival(name="Ultra", date="March 25-27, 2024", location="Miami, FL", price=400)
festival3 = Festival(name="EDC", date="May 22-24, 2024", location="Las Vegas, NV", price=500)
festival4 = Festival(name="Tomorrowland", date="August 27-29, 2023", location="Boom, Belgium", price=600)
festival5 = Festival(name="Electric Forest", date="June 23-26, 2023", location="Rothbury, MI", price=700)
festival6 = Festival(name="Bonnaroo", date="September 2-5, 2023", location="Manchester, TN", price=800)
festival7 = Festival(name="Coachella", date="April 15-17, 2024", location="Indio, CA", price=900)
festival8 = Festival(name="Lollapalooza", date="July 29-31, 2022", location="Chicago, IL", price=1000)
festival9 = Festival(name="Hard Summer", date="July 31-August 1, 2024", location="Fontana, CA", price=250)
festival10 = Festival(name="Beyond Wonderland", date="March 22-24, 2024", location="Las Vegas, NV", price=300)
festival11 = Festival(name="Escape", date="October 25-26, 2024", location="San Bernardino, CA", price=350)
festival12 = Festival(name="EDC Orlando", date="November 8-9, 2024", location="Orlando, FL", price=400)
festival13 = Festival(name="EDC Mexico", date="February 28-29, 2024", location="Mexico City, Mexico", price=450)
festival14 = Festival(name="Nocturnal Wonderland", date="September 13-14, 2024", location="San Bernardino, CA", price=500)
festival15 = Festival(name="Dreamstate", date="November 22-23, 2024", location="San Bernardino, CA", price=550)
festival16 = Festival(name="Countdown", date="December 30-31, 2024", location="San Bernardino, CA", price=600)
festival17 = Festival(name="Ultra Europe", date="July 12-14, 2024", location="Split, Croatia", price=650)
festival18 = Festival(name="Electric Love", date="July 4-6, 2024", location="Salzburg, Austria", price=700)
festival19 = Festival(name="Electric Zoo", date="September 3-5, 2024", location="New York, NY", price=750)
festival20 = Festival(name="Lightning in a Bottle", date="May 20-25, 2024", location="Bradley, CA", price=800)
festival21 = Festival(name="Creamfields", date="August 22-25, 2024", location="Daresbury, UK", price=850)
festival22 = Festival(name="Lost Lands", date="September 27-29, 2024", location="Thornville, OH", price=900)
festival23 = Festival(name="Groove Cruise", date="January 9-13, 2024", location="Miami, FL", price=450)
festival24 = Festival(name="Holy Ship", date="January 22-26, 2024", location="Miami, FL", price=500)
festival25 = Festival(name="CRSSD Festival", date="March 2-3, 2024", location="San Diego, CA", price=1050)
festival26 = Festival(name="Splash House", date="June 7-9, 2024", location="Palm Springs, CA", price=1100)
festival27 = Festival(name="Imagine Music Festival", date="September 20-22, 2024", location="Atlanta, GA", price=1150)
festival28 = Festival(name="Mysteryland", date="August 23-25, 2024", location="Haarlemmermeer, Netherlands", price=600)
festival29 = Festival(name="Sunset Music Festival", date="May 25-26, 2024", location="Tampa, FL", price=400)
festival30 = Festival(name="Untold Festival", date="August 1-4, 2024", location="Cluj-Napoca, Romania", price=500)

genre1 = Genre_Option(genre="House")
genre2 = Genre_Option(genre="Techno")
genre3 = Genre_Option(genre="Trance")
genre4 = Genre_Option(genre="Dubstep")
genre5 = Genre_Option(genre="Drum & Bass")
genre6 = Genre_Option(genre="Trap")
genre7 = Genre_Option(genre="Hardstyle")
genre8 = Genre_Option(genre="Future Bass")
genre9 = Genre_Option(genre="Progressive House")
genre10 = Genre_Option(genre="Tropical House")

festival1.genres.append(genre2)
festival2.genres.append(genre1)
festival3.genres.append(genre3)
festival4.genres.append(genre7)
festival5.genres.append(genre2)
festival6.genres.append(genre5)
festival7.genres.append(genre10)
festival8.genres.append(genre8)
festival9.genres.append(genre6)
festival10.genres.append(genre4)
festival11.genres.append(genre1)
festival12.genres.append(genre3)
festival13.genres.append(genre4)
festival14.genres.append(genre5)
festival15.genres.append(genre6)
festival16.genres.append(genre7)
festival17.genres.append(genre8)
festival18.genres.append(genre10)
festival19.genres.append(genre9)
festival20.genres.append(genre1)
festival21.genres.append(genre1)
festival22.genres.append(genre4)
festival23.genres.append(genre5)
festival24.genres.append(genre6)
festival25.genres.append(genre7)
festival26.genres.append(genre8)
festival27.genres.append(genre10)
festival28.genres.append(genre9)
festival29.genres.append(genre1)
festival30.genres.append(genre3)






session.add_all([festival1, festival2, festival3, festival4, festival5, festival6, festival7, festival8, festival9, festival10, festival11, festival12, festival13, festival14, festival15, festival16, festival17, festival18, festival19, festival20, festival21, festival22, festival23, festival24, festival25, festival26, festival27, festival28, festival29, festival30, genre1, genre2, genre3, genre4, genre5, genre6, genre7, genre8, genre9, genre10])
session.commit()


