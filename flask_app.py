from flask import Flask, redirect, render_template, request, url_for
from covid_uk import covid_uk
import service
import service_charts
from db import DB
from update import Update

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/coviduk', methods=["GET", "POST"])
def coviduk():
    if request.method == 'GET':
        #current_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        update = service.get_nations_data()
        return render_template('covid.html', release_date=Update.release_date, update=update, comments=DB.comments)
    comment = service.create_comment(request)
    DB.comments.append(comment)
    return redirect(url_for('coviduk'))

# UK and nations group line charts start ------------------------
@app.route('/coviduk/charts/uk/newcases/groupline')
def groupline_uknewcases():
    line_labels = service_charts.get_labels_uk()
    line_labels.reverse()
    line_ukvalues = service_charts.get_values_uk_new_cases()
    line_ukvalues.reverse()
    line_envalues = service_charts.get_values_en_new_cases()
    line_envalues.reverse()
    line_scovalues = service_charts.get_values_sco_new_cases()
    line_scovalues.reverse()
    line_wavalues = service_charts.get_values_wa_new_cases()
    line_wavalues.reverse()
    line_nivalues = service_charts.get_values_ni_new_cases()
    line_nivalues.reverse()
    return render_template('charts_uk_new_cases_groupline.html',
                           title='New cases for the UK & all its nations',
                           labels=line_labels,
                           ukvalues=line_ukvalues,
                           envalues=line_envalues,
                           scovalues=line_scovalues,
                           wavalues=line_wavalues,
                           nivalues=line_nivalues)


@app.route('/coviduk/charts/uk/totalcases/groupline')
def groupline_uktotalcases():
    line_labels = service_charts.get_labels_uk()
    line_labels.reverse()
    line_ukvalues = service_charts.get_values_uk_total_cases()
    line_ukvalues.reverse()
    line_envalues = service_charts.get_values_en_total_cases()
    line_envalues.reverse()
    line_scovalues = service_charts.get_values_sco_total_cases()
    line_scovalues.reverse()
    line_wavalues = service_charts.get_values_wa_total_cases()
    line_wavalues.reverse()
    line_nivalues = service_charts.get_values_ni_total_cases()
    line_nivalues.reverse()
    return render_template('charts_uk_total_cases_groupline.html',
                           title='Total cases for the UK & all its nations',
                           labels=line_labels,
                           ukvalues=line_ukvalues,
                           envalues=line_envalues,
                           scovalues=line_scovalues,
                           wavalues=line_wavalues,
                           nivalues=line_nivalues)


@app.route('/coviduk/charts/uk/newdeaths/groupline')
def groupline_uknewdeaths():
    line_labels = service_charts.get_labels_uk()
    line_labels.reverse()
    line_ukvalues = service_charts.get_values_uk_new_deaths()
    line_ukvalues.reverse()
    line_envalues = service_charts.get_values_en_new_deaths()
    line_envalues.reverse()
    line_scovalues = service_charts.get_values_sco_new_deaths()
    line_scovalues.reverse()
    line_wavalues = service_charts.get_values_wa_new_deaths()
    line_wavalues.reverse()
    line_nivalues = service_charts.get_values_ni_new_deaths()
    line_nivalues.reverse()
    return render_template('charts_uk_new_deaths_groupline.html',
                           title='New deaths for the UK & all its nations',
                           labels=line_labels,
                           ukvalues=line_ukvalues,
                           envalues=line_envalues,
                           scovalues=line_scovalues,
                           wavalues=line_wavalues,
                           nivalues=line_nivalues)


@app.route('/coviduk/charts/uk/totaldeaths/groupline')
def groupline_uktotaldeaths():
    line_labels = service_charts.get_labels_uk()
    line_labels.reverse()
    line_ukvalues = service_charts.get_values_uk_total_deaths()
    line_ukvalues.reverse()
    line_envalues = service_charts.get_values_en_total_deaths()
    line_envalues.reverse()
    line_scovalues = service_charts.get_values_sco_total_deaths()
    line_scovalues.reverse()
    line_wavalues = service_charts.get_values_wa_total_deaths()
    line_wavalues.reverse()
    line_nivalues = service_charts.get_values_ni_total_deaths()
    line_nivalues.reverse()
    return render_template('charts_uk_total_deaths_groupline.html',
                           title='Total_deaths for the UK & all its nations',
                           labels=line_labels,
                           ukvalues=line_ukvalues,
                           envalues=line_envalues,
                           scovalues=line_scovalues,
                           wavalues=line_wavalues,
                           nivalues=line_nivalues)

# UK and nations group line charts end ------------------------

# individual bar charts
# UK charts start ----------------------------------------
@app.route('/coviduk/charts/uk/newcases/bar')
def bar_uknewcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_uk_new_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_uk_new_cases_bar.html',
                           title='COVID19, new cases in the UK',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

@app.route('/coviduk/charts/uk/totalcases/bar')
def bar_uktotalcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_uk_total_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_uk_total_cases_bar.html',
                           title='COVID19, total cases in the UK',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/uk/newdeaths/bar')
def bar_uknewdeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_uk_new_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_uk_new_deaths_bar.html',
                           title='COVID19, new deaths in the UK',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/uk/totaldeaths/bar')
def bar_uktotaldeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_uk_total_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_uk_total_deaths_bar.html',
                           title='COVID19, total deaths in the UK',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

# UK charts end ----------------------------------------


# ENGLAND charts start ----------------------------------------
@app.route('/coviduk/charts/en/newcases/bar')
def bar_ennewcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_en_new_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_en_new_cases_bar.html',
                           title='COVID19, new cases in England',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

@app.route('/coviduk/charts/en/totalcases/bar')
def bar_entotalcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_en_total_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_en_total_cases_bar.html',
                           title='COVID19, total cases in England',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/en/newdeaths/bar')
def bar_ennewdeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_en_new_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_en_new_deaths_bar.html',
                           title='COVID19, new deaths in England',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/en/totaldeaths/bar')
def bar_entotaldeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_en_total_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_en_total_deaths_bar.html',
                           title='COVID19, total deaths in England',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

# ENGLAND charts end ----------------------------------------


# SCOTLAND charts start ----------------------------------------
@app.route('/coviduk/charts/sco/newcases/bar')
def bar_sconewcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_sco_new_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_sco_new_cases_bar.html',
                           title='COVID19, new cases in Scotland',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

@app.route('/coviduk/charts/sco/totalcases/bar')
def bar_scototalcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_sco_total_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_sco_total_cases_bar.html',
                           title='COVID19, total cases in Scotland',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/sco/newdeaths/bar')
def bar_sconewdeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_sco_new_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_sco_new_deaths_bar.html',
                           title='COVID19, new deaths in Scotland',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/sco/totaldeaths/bar')
def bar_scototaldeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_sco_total_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_sco_total_deaths_bar.html',
                           title='COVID19, total deaths in Scotland',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

# SCOTLAND charts end ----------------------------------------


# WALES charts start ----------------------------------------
@app.route('/coviduk/charts/wa/newcases/bar')
def bar_wanewcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_wa_new_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_wa_new_cases_bar.html',
                           title='COVID19, new cases in Wales',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

@app.route('/coviduk/charts/wa/totalcases/bar')
def bar_watotalcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_wa_total_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_wa_total_cases_bar.html',
                           title='COVID19, total cases in Wales',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/wa/newdeaths/bar')
def bar_wanewdeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_wa_new_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_wa_new_deaths_bar.html',
                           title='COVID19, new deaths in Wales',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/wa/totaldeaths/bar')
def bar_watotaldeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_wa_total_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_wa_total_deaths_bar.html',
                           title='COVID19, total deaths in Wales',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

# WALES charts end ----------------------------------------


# NI charts start ----------------------------------------
@app.route('/coviduk/charts/ni/newcases/bar')
def bar_ninewcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_ni_new_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_ni_new_cases_bar.html',
                           title='COVID19, new cases in Northern Ireland',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

@app.route('/coviduk/charts/ni/totalcases/bar')
def bar_nitotalcases():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_ni_total_cases()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_ni_total_cases_bar.html',
                           title='COVID19, total cases in Northern Ireland',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/ni/newdeaths/bar')
def bar_ninewdeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_ni_new_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_ni_new_deaths_bar.html',
                           title='COVID19, new deaths in Northern Ireland',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)


@app.route('/coviduk/charts/ni/totaldeaths/bar')
def bar_nitotaldeaths():
    bar_back_colours = service_charts.get_back_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_border_colours = service_charts.get_border_colours_bar(service_charts.FIRST_SUN, service_charts.REPEAT)
    bar_labels = service_charts.get_labels_uk()
    bar_labels.reverse()
    bar_values = service_charts.get_values_ni_total_deaths()
    bar_values.reverse()
    max_value = max(bar_values)
    print('inside app')
    return render_template('charts_ni_total_deaths_bar.html',
                           title='COVID19, total deaths in Northern Ireland',
                           max=max_value,
                           back_colours=bar_back_colours,
                           border_colours=bar_border_colours,
                           labels=bar_labels,
                           values=bar_values)

# NI charts end ----------------------------------------



