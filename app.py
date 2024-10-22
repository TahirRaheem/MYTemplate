import streamlit as st

# The new HTML template matching the design in the image
html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{NAME}}'s Portfolio</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 70%;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }
        header {
            background-color: #44aacc;
            padding: 30px;
            text-align: center;
            color: white;
        }
        header h1 {
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        header img {
            border-radius: 50%;
            margin-bottom: 15px;
            width: 120px;
            height: 120px;
            object-fit: cover;
        }
        header p {
            font-size: 1em;
        }
        .left-column {
            float: left;
            width: 30%;
            padding: 15px;
        }
        .right-column {
            float: left;
            width: 70%;
            padding: 15px;
        }
        h2 {
            font-size: 1.4em;
            color: #44aacc;
            border-bottom: 2px solid #44aacc;
            margin-bottom: 15px;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        ul li {
            background-color: #e6f7ff;
            margin-bottom: 10px;
            padding: 10px;
            border-left: 5px solid #44aacc;
        }
        footer {
            clear: both;
            text-align: center;
            padding: 20px;
            background-color: #44aacc;
            color: white;
            margin-top: 30px;
        }
        .contact-info {
            text-align: right;
        }
        .contact-info p {
            margin: 0;
        }
        .personal-info, .skills, .certifications {
            margin-bottom: 20px;
        }
        .personal-info p, .skills ul, .certifications ul {
            margin-bottom: 5px;
        }
    </style>
</head>
<body>

<div class="container">
    <header>
        <img src="{{IMAGE}}" alt="Profile Picture">
        <h1>{{NAME}}</h1>
        <div class="contact-info">
            <p>{{PHONE}}</p>
            <p>{{EMAIL}}</p>
            <p>{{ADDRESS}}</p>
        </div>
    </header>

    <div class="left-column">
        <div class="skills">
            <h2>Core Competencies</h2>
            <ul>
                {{SKILLS}}
            </ul>
        </div>

        <div class="certifications">
            <h2>Certifications</h2>
            <ul>
                {{CERTIFICATIONS}}
            </ul>
        </div>

        <div class="personal-info">
            <h2>Personal Details</h2>
            <p>Date of Birth: {{DOB}}</p>
            <p>Languages: {{LANGUAGES}}</p>
        </div>
    </div>

    <div class="right-column">
        <div class="profile-objective">
            <h2>Profile Objective</h2>
            <p>{{PROFILE_OBJECTIVE}}</p>
        </div>

        <div class="education">
            <h2>Education & Credentials</h2>
            <p>{{EDUCATION}}</p>
        </div>

        <div class="projects">
            <h2>Projects</h2>
            <p>{{PROJECTS}}</p>
        </div>
    </div>

    <footer>
        <p>Portfolio created by {{NAME}} | Streamlit App</p>
    </footer>
</div>

</body>
</html>
'''

# Title of the app
st.title("Portfolio Creator App")

# Input fields for user details
name = st.text_input("Enter your full name:")
phone = st.text_input("Enter your phone number:")
email = st.text_input("Enter your email:")
address = st.text_input("Enter your address:")
dob = st.text_input("Enter your date of birth:")
languages = st.text_input("Enter the languages you speak:")
profile_objective = st.text_area("Write a short bio about yourself:")
skills = st.text_area("List your skills (separated by commas):")
certifications = st.text_area("List your certifications (separated by commas):")
education = st.text_area("Provide your education details:")
projects = st.text_area("Provide details of your projects:")
image_url = st.text_input("Provide a link to your profile picture:")

# Generate portfolio button
if st.button("Create Portfolio"):
    if name and phone and email and address and profile_objective and skills and certifications and education and projects:
        # Process input data into HTML-friendly format
        skills_list = ''.join([f'<li>{skill.strip()}</li>' for skill in skills.split(',')])
        certifications_list = ''.join([f'<li>{cert.strip()}</li>' for cert in certifications.split(',')])

        # Replace placeholders in the template
        filled_content = html_template.replace("{{NAME}}", name)\
                                      .replace("{{PHONE}}", phone)\
                                      .replace("{{EMAIL}}", email)\
                                      .replace("{{ADDRESS}}", address)\
                                      .replace("{{DOB}}", dob)\
                                      .replace("{{LANGUAGES}}", languages)\
                                      .replace("{{PROFILE_OBJECTIVE}}", profile_objective)\
                                      .replace("{{SKILLS}}", skills_list)\
                                      .replace("{{CERTIFICATIONS}}", certifications_list)\
                                      .replace("{{EDUCATION}}", education)\
                                      .replace("{{PROJECTS}}", projects)\
                                      .replace("{{IMAGE}}", image_url)

        # Display the generated portfolio content directly in the Streamlit app
        st.markdown(filled_content, unsafe_allow_html=True)
        
        st.success("Portfolio created successfully!")
    else:
        st.error("Please fill in all fields!")
