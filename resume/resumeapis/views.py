
from django.shortcuts import render

class Template():

    def template1(request):
        context = {
            'name': 'Your Name',
            'email': 'yourname@example.com',
            'phone': '+1234567890',
            'linkedin': 'linkedin.com/in/yourprofile',
            'summary': 'A brief summary highlighting your key skills, experiences, and career objectives.',
            'experience': [
                {
                    'job_title': 'Job Title 1',
                    'company_name': 'Company Name 1',
                    'location': 'Location 1',
                    'start_date': 'Start Date 1',
                    'end_date': 'End Date 1',
                    'responsibilities': [
                        'Responsibility 1',
                        'Responsibility 2',
                    ]
                },
                {
                    'job_title': 'Job Title 2',
                    'company_name': 'Company Name 2',
                    'location': 'Location 2',
                    'start_date': 'Start Date 2',
                    'end_date': 'End Date 2',
                    'responsibilities': [
                        'Responsibility 1',
                        'Responsibility 2',
                    ]
                }
            ],
            'education': [
                {
                    'degree': 'Degree 1',
                    'university': 'University Name 1',
                    'location': 'Location 1',
                    'graduation_year': 'Graduation Year 1',
                    'achievements': 'Description of coursework or achievements.',
                },
                {
                    'degree': 'Degree 2',
                    'university': 'University Name 2',
                    'location': 'Location 2',
                    'graduation_year': 'Graduation Year 2',
                    'achievements': 'Description of coursework or achievements.',
                },
                {
                    'degree': 'Degree 3',
                    'university': 'University Name 3',
                    'location': 'Location 3',
                    'graduation_year': 'Graduation Year 3',
                    'achievements': 'Description of coursework or achievements.',
                }
            ],
            'skills': [
                'Skill 1',
                'Skill 2',
                'Skill 3'
            ]
        }
    
        return render(request, 'resume/template4.html', context)
