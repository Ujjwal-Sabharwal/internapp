import joblib
import pandas as pd



def predict_mood(academic,age,gender,family_income,family_members,subject,factor,dependancy,adequate_support,future_goal):
    values = {"Male": 1, "Female": 0,
              'Under Graduate': 4, 'Professional': 3, 'Post Graduate': 2, 'Senior Secondary': 1,
              'Working Professionals': 0,
              "21-25 Yrs.": 2, "More than 25 Yrs.": 1, "Less than 20 Yrs. ": 0,
              'Your own decision': 4, 'Family/Society': 3, 'Friends/Peer group': 2, 'Subject Matter Expert (SME)': 1,
              'Teachers': 0,
              'Personal Interest': 3, 'Career Prospects': 2, 'Parental Expectations': 1, 'Academic Performance': 0,
              "Previous Students' Experiences": 4, 'Academic Advisors': 3, 'Online Resources': 2,
              'Friends and Peers': 1, 'Family Members': 0,
              "No": 0, "Yes": 1, "Not Sure": 0,
              'Recent Trends': 4, 'Hobbies/interest areas': 3, 'Financial Stability': 2, 'Career Preferences': 1,
              'Family Professional Goals': 0}
    # Get input values from the user
    # academic = input("Enter academic level : ")
    # age = input("Enter age : ")
    # gender = input("Enter gender : ")
    # family_income = int(input("Enter family income : "))
    # family_members = int(input("Enter number of family members : "))
    # subject = input("Enter who influence your subject selection : ")
    # factor = input("Enter factor influencing decision : ")
    # dependancy = input("Enter dependency : ")
    # adequate_support = input("Enter adequate support : ")
    # future_goal = input("Enter what decide future goal : ")

    # Create a DataFrame for the user input
    user_data = pd.DataFrame(
        [[values[academic], values[age], values[gender], family_income, family_members, values[subject], values[factor],
          values[dependancy], values[adequate_support], values[future_goal]]],
        columns=['DGIF_1\n(Academic Level)', 'DGIF_2\n(Age)',
                 'DGIF_3\n(Gender)', 'DGIF_4\n(Family Income)',
                 'DGIF_5 \n(No. of Family Members)',
                 'BIF_1 (Who influence your decision in subject selection)',
                 'BIF_2 (Factor influencing decision)', 'SGIF_1 (Dependency)',
                 'IAIF_1\n(Adequate support and guidance )',
                 'ESIF_2\n(What Decide Future Goal)']
    )

    # Load the trained model
    model = joblib.load('mood_prediction.pkl')

    # print(user_data)
    # Make prediction
    prediction = model.predict(user_data)

    if prediction == 1:
        return "Positive"
    else:
        return "Negative"

