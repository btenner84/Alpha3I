from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('main', __name__)

# This list will store all reports
reports = []

@bp.route('/')
def base():
    return render_template('home.html')
    
@bp.route('/research_topic_input', methods=['GET', 'POST'])
def research_topic_input():
    if request.method == 'POST':
        title = request.form.get('title')
        industry = request.form.get('industry')
        date = request.form.get('date')
        context = request.form.get('context')
        source_base = request.form.get('source_base')

        # Handle the Sources and Questions
        sources = []
        questions = request.form.getlist('question')

        # Get the number of sources from the form data
        source_count = int(request.form.get('sourceCount', 0))

        # Loop over each source and store its details
        for i in range(1, source_count + 1):
            source_name = request.form.get(f'sourceName{i}')
            email = request.form.get(f'email{i}')
            phone = request.form.get(f'phone{i}')
            job_title = request.form.get(f'jobTitle{i}')
            organization = request.form.get(f'organization{i}')

            sources.append({
                'source_name': source_name,
                'email': email,
                'phone': phone,
                'job_title': job_title,
                'organization': organization,
            })

        # Store the report in the reports list
        reports.append({
            'title': title,
            'industry': industry,
            'date': date,
            'context': context,
            'source_base': source_base,
            'sources': sources,
            'questions': questions,
        })

        return redirect(url_for('main.research_reports'))

    return render_template('research_topic_input.html')

@bp.route('/research_reports')
def research_reports():
    # Pass the reports list to the template
    return render_template('research_reports.html', reports=reports)