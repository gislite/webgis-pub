from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))


def get_html_title(html_file):
    uu = BeautifulSoup(open(html_file), 'lxml')
    return uu.title.text


def render_html(tmpl, outfile, **kwargs):
    template = env.get_template(tmpl)
    output_from_parsed_template = template.render(kwargs)

    # to save the results
    with open(outfile, "w") as fh:
        fh.write(output_from_parsed_template)


if __name__ == '__main__':
    get_html_title('templates/03_projman_Project-management/03_outou.jinja2')
