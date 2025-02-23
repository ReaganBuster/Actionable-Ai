import os
from dotenv import load_dotenv
from ai_engine import Ai_engine
from mail_hander.mail_report import MailReport
from utils import utils
from data.database import engine, CurrentReport
from sqlalchemy.orm import sessionmaker
import streamlit as st

load_dotenv()
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

apikey = os.getenv('openai-apikey')
sender = os.getenv('sender_email')
receiver = os.getenv('receiver_email')
credentials = os.getenv('password')

goal = utils.fetch_goal()
review_data = utils.fetch_reviews()
business_data = utils.fetch_business_data()

if __name__ == "__main__":
    ai_engine = Ai_engine(apiKey=apikey, goal=goal, reviews=review_data, business_data=business_data)
    report = ai_engine.query_online_model()
   
    current_report = CurrentReport(report=report)
    session.add(current_report)
    session.commit()
    
    st.title("Actionable AI")
    st.subheader("AI Engine for generating business reports")
    st.write(report)