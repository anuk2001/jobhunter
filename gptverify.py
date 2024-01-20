import openai

base_prompt = """

I need your assistance in determining whether or not the following job description is well suited for someone who is looking for ENTRY-LEVEL software engineering, data analyst, data engineering, data science jobs. 

This person is going to be fresh graduate out of college (May 2024) with a Bachelor's in Computer Science and will have somewhere from 0 - 1 years of experience. This person is a U.S Citizen and does not require visa sponsorship. This person does not have an active security clearance.  Job descriptions requiring 2 years of experience can be considered 'YES' as well, but make sure to address all aspects of the job description. 

Assume the applicant has typical physical and technical aptitude. The applicant is knowledgeable with OOP principles, programming languages, software development tools and principles, web development, data analysis, database management, etc.

You are to answer with ONLY 'YES' if the job description is well-suited for the applicant, or ONLY 'NO' otherwise.

Job Description:
"""
