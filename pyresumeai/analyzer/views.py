from django.shortcuts import render
from django.views.generic import TemplateView

class Test(TemplateView):
    template_name="analyzer.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file="""🧑‍💻 Responsibilities
Develop web applications and APIs using Python and relevant frameworks (especially Django or Flask)

Work with databases such as PostgreSQL and MongoDB

Integrate DevOps tools like Docker and GitLab CI/CD

Write tests and participate in code reviews to improve code quality and security

Take part in agile software development processes within the team

✅ Required Qualifications
At least 2 years of professional experience in Python software development

Hands-on knowledge of Django or Flask

Experience designing and consuming RESTful APIs

Familiarity with version control systems (preferably Git)

A team player with a solution-oriented mindset and eagerness to learn

💡 Preferred Qualifications
Familiarity with frontend technologies (React, Vue.js)

Project experience with cloud platforms (AWS, Azure, GCP)

Strong English communication skills

🎁 What We Offer
Competitive salary and performance bonuses

Technical training and career development support

Flexible working hours and remote work opportunities

A dynamic and supportive team environment"""
        context['items'] = [line.strip() for line in file.split("\n") if line.strip()]
        return context
    
