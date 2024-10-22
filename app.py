import streamlit as st

# The HTML template is stored directly as a string
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{NAME}}'s Portfolio</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        header {
            background: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        header h1 {
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        header p {
            font-size: 1.2em;
        }
        section {
            margin: 20px 0;
            padding: 20px;
            background: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #333;
            font-size: 2em;
            border-bottom: 2px solid #333;
            padding-bottom: 5px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            background: #f4f4f4;
            margin-bottom: 10px;
            padding: 10px;
            border-left: 5px solid #333;
        }
        footer {
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background: #333;
            color: #fff;
        }
    </style>
</head>
<body>

    <header>
        <h1>{{NAME}}</h1>
        <p>{{BIO}}</p>
    </header>

    <section>
        <h2>Skills</h2>
        <ul>
            {{SKILLS}}
        </ul>
    </section>

    <section>
        <h2>Projects</h2>
        <ul>
            {{PROJECTS}}
        </ul>
    </section>

    <footer>
        <p>Portfolio created using Streamlit | {{NAME}}'s Portfolio</p>
    </footer>

</body>
</html>
"""

# Title of the app
st.title("Portfolio Creator App")

# Input fields for user details
name = st.text_input("Enter your full name:")
bio = st.text_area("Write a short bio about yourself:")
skills = st.text_area("List your skills (separated by commas):")
projects = st.text_area("List your projects (one per line):")

# Generate portfolio button
if st.button("Create Portfolio"):
    if name and bio and skills and projects:
        # Process skills and projects into HTML list items
        skills_list = ''.join([f'<li>{skill.strip()}</li>' for skill in skills.split(',')])
        projects_list = ''.join([f'<li>{project.strip()}</li>' for project in projects.split('\n')])

        # Replace placeholders in the template
        filled_content = html_template.replace("{{NAME}}", name)\
                                      .replace("{{BIO}}", bio)\
                                      .replace("{{SKILLS}}", skills_list)\
                                      .replace("{{PROJECTS}}", projects_list)

        # Display the generated portfolio content directly in the Streamlit app
        st.markdown(filled_content, unsafe_allow_html=True)
        
        # Inform the user of successful creation
        st.success("Portfolio created successfully!")
    else:
        st.error("Please fill in all fields!")
