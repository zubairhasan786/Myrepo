import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Zubair Hasan , Software Engineer
##### *Resume* 
''')

image = Image.open('dp.jpg')
st.image(image, width=150)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- I am a self-motivated and competent software engineer with expertise in web and software development. I am proficient in developing, maintaining, and configuring operating systems, application software, system management tools, and software solutions as well as analyzing and determining system needs and recommending solutions. I am skilled in designing, upgrading, and testing software and software requirements.  
- I am capable of writing testable, well-designed, and effective code. I have a technical understanding of database design, development, ERD, store procedure, views, and jobs. I possess profound knowledge of web applications and programming languages and strong experience in relational databases i.e. SQL Server, and MYSQL.
- My excellent analytical skills enable me to organize and process specifications/requirements in conformity with technical needs, identify issues, and provide suggestions for resolution. I have extraordinary communication, interpersonal, and problem-solving skills. I am willing to perform in a challenging environment with the ability to learn and adopt advanced technologies.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="#" target="_blank">Zubair Hasan</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Bachelor In** (Software Engineering), *University of Sargodha*, Pakistan',
'2014-2018')
st.markdown('''
- GPA: `3.89`
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Web Developer**, Glixen Technalogy, Pakistan',
'2020-2022')
st.markdown('''
- Generating WordPress themes and plugins,Good hands in WordPress and woo commerce ,Troubleshooting content issues.
- Strong fundamental knowledge of JavaScript, JQuery,
  HTML, Ajax, XHTML&CSS, Website Security (Malware detection and rectification),Proficient understanding of code versioning tools, such
  as Git.
- Monitoring the performance of the live website,Back up files from Web sites to local directories for
  recovery, Designing, Website Maintenance and managing the website back-end including database and server
  integration.
- Meeting with clients to discuss website design and function.
''')

txt('**Web Developer**, OCAnalytica, Based in USA',
'2019-2020')

st.markdown('''
- Generating WordPress themes and plugins,Good hands in WordPress and woo commerce ,Troubleshooting content issues.
- Strong fundamental knowledge of JavaScript, JQuery,
  HTML, Ajax, XHTML&CSS, Website Security (Malware detection and rectification),Proficient understanding of code versioning tools, such
  as Git.
- Monitoring the performance of the live website,Back up files from Web sites to local directories for
  recovery, Designing, Website Maintenance and managing the website back-end including database and server
  integration.
''')

txt('**Web Internee**, Jump Solutions, pakistan',
'2018')
st.markdown('''
- Website Development Team member simple and intuitive interactions and experiences,Development of project concepts and maintain optimal workflow
- Involved in Database Development and Design.
- Worked with senior developer to manage large, complex projects for corporate clients.
''')
#####################


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `Php`,`Reactjs`, `Node js`,`Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Wordpress', '`Elementor`,`Woocommerce`,`ACF`,`WP bakery`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/zubair-hasan-software-engineer')
