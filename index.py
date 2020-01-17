from yattag import Doc


class PersonalPage:

    def __init__(self,
                 name,
                 google_track_url,
                 links, ):
        self.name = name
        self.google_track_url = google_track_url
        self.links = links

    def get_html(self):
        doc, tag, text = Doc().tagtext()
        with tag('html', lang="en"):
            self._generate_head(doc, tag, text)
            self._generate_body(doc, tag, text)
        result = doc.getvalue()
        return result

    def _generate_body(self, doc, tag, text):
        with tag('body'):
            params = ['width:100%', 'max-width:800px', 'border:0px',
                      'border-spacing:0px', 'border-collapse:separate',
                      'margin-right:auto', 'margin-left:auto']
            style = ';'.join(params)
            with tag('table', style=style):
                with tag('tbody'):
                    with tag('tr', style="padding:0px"):
                        with tag('td', style="padding:0px"):
                            self._get_introduction(tag, text)
                            self._get_interests(tag, text)
                            self._get_projects(doc, tag, text)
                            self._get_acknowledgement(doc, tag, text)

    def _get_introduction(self, tag, text):
        params = ['width:100%', 'border:0px', 'border-spacing:0px',
                  'border-collapse:separate', 'margin-right:auto',
                  'margin-left:auto']
        style = ';'.join(params)
        with tag('table', style=style):
            with tag('tbody'):
                with tag('tr', style="padding:0px"):
                    params = ['padding:2.5%', 'width:63%',
                              'vertical-align:middle']
                    style = ';'.join(params)
                    self._get_description(style, tag, text)
                    self._get_profile_image(tag)

    def _get_description(self, style, tag, text):
        with tag('td', style=style):
            with tag('p', style="text-align:center"):
                with tag('name'):
                    text(self.name)
            with tag('p'):
                text("I work as a Data Scientist at ")
                with tag('a', href="https://www.cencosud.com/"):
                    text("Cencosud")
            with tag('p'):
                text(
                    "I did my bachelors and MSc in electrical engineering in ")
                with tag('a', href="http://ingenieria.uchile.cl/"):
                    text("Universidad de Chile")
                text(". I have worked in image segmentation, computer vision")
                text(", LIDAR processing/point cloud segmentation,")
                text(" time series forecasting.")
            self._get_links(tag, text)

    def _get_profile_image(self, tag):
        with tag('td', style="padding:2.5%;width:40%;max-width:40%"):
            with tag('a', href="data/sebastian_cepeda.jpg"):
                author_image = "data/sebastian_cepeda.jpg"
                with tag('a', href=f"{author_image}"):
                    with tag('img',
                             style="width:100%;max-width:100%",
                             alt="Profile image",
                             src=f"{author_image}",
                             klass="hoverZoomLink"):
                        pass

    def _get_links(self, tag, text):
        slatch = "    /    "
        with tag('p', style="text-align:center"):
            for i in range(len(self.links) - 1):
                name, url = self.links[i]
                with tag('a', href=url):
                    text(name)
                text(slatch)
            if len(self.links) > 1:
                name, url = self.links[-1]
                with tag('a', href=url):
                    text(name)

    def _get_interests(self, tag, text):
        with tag('table',
                 style="width:100%;border:0px;border-spacing:0px;border"
                       "-collapse:separate;margin-right:auto;margin-left"
                       ":auto;"):
            with tag('tbody'):
                with tag('tr'):
                    with tag('td', style="padding:20px;width:100%;vertical"
                                         "-align:middle"):
                        self._get_interests_description(tag, text)

    def _get_interests_description(self, tag, text):
        with tag('heading'):
            text("Interests and projects")
        with tag('p'):
            text("My interests are computer vision, machine learning, "
                 "natural language processing, reinforcement learning and "
                 "software development.")

    def _get_projects(self, doc, tag, text):
        with tag('table',
                 style="width:100%;border:0px;border-spacing:0px;border"
                       "-collapse:separate;margin-right:auto;margin-left"
                       ":auto;"):
            with tag('tbody'):
                self._get_bvs_project(doc, tag, text)

    def _get_bvs_project(self, doc, tag, text):
        project_id = "bvs"
        with tag('tr', onmouseout=f"{project_id}_stop()",
                 onmouseover=f"{project_id}_start()"):
            with tag('td', style="padding:20px;width:25%;"
                                 "vertical-align:middle"):
                with tag('div', klass="one"):
                    with tag('div', klass="two", id=project_id):
                        with tag('img',
                                 src='data/blood_vessels_segmentation_after.png'):
                            pass
                    with tag('img',
                             src='data/blood_vessels_segmentation_before.png'):
                        pass
                self._get_mouse_over_js(project_id, tag, text)
            with tag('td',
                     style="padding:20px;width:75%;vertical-align:middle"):
                with tag('a',
                         href="http://repositorio.uchile.cl/handle/2250/138129"):
                    with tag('b'):
                        text("Blood vessels segmentation in retinal images")
                doc.stag('br')
                doc.stag('br')

    def _get_mouse_over_js(self, project_id, tag, text):
        with tag('script', type="text/javascript"):
            txt = f"function {project_id}_start()" \
                  f"{{document.getElementById('{project_id}')." \
                  f"style.opacity = '1';}} " \
                  f"function {project_id}_stop()" \
                  f"{{document.getElementById('{project_id}').style" \
                  f".opacity = '0';}}" \
                  f"{project_id}_stop()"
            text(txt)

    def _get_acknowledgement(self, doc, tag, text):
        with tag('table',
                 style="width:100%;border:0px;border-spacing:0px;border"
                       "-collapse:separate;margin-right:auto;margin-left"
                       ":auto;"):
            with tag('tbody'):
                with tag('tr'):
                    with tag('td', style="padding:0px"):
                        doc.stag('br')
                        with tag('p',
                                 style="text-align:right;font-size:small;"):
                            text("Code of this page is ")
                            with tag('a',
                                     href="https://github.com/sebastiancepeda/sebastiancepeda.github.io"):
                                text("in github")
                            text(", based on ")
                            with tag('a', href="https://jonbarron.info/"):
                                text("Jon Barron's site")
                            with tag('a',
                                     href="https://github.com/jonbarron/jonbarron_website"):
                                text("(source code)")
                        doc.stag('br')

    def _generate_head(self, doc, tag, text):
        with tag('head'):
            doc.asis(
                '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')
            doc.asis(f'<script async src="{self.google_track_url}"></script>')
            with tag('script'):
                text(self._get_google_tracker_js())
            with tag('title'):
                text(self.name)
            with tag('meta', name="author", content=self.name):
                pass
            with tag('meta', name="viewport",
                     content="width=device-width, initial-scale=1"):
                pass
            with tag('link', rel="stylesheet", type="text/css",
                     href="stylesheet.css"):
                pass
            with tag('link', rel="icon", type="image/png",
                     href="images/seal_icon.png"):
                pass

    def _get_google_tracker_js(self):
        result = "window.dataLayer = window.dataLayer || [];\
                function gtag()\
                {\
                    dataLayer.push(arguments);\
                }\
                gtag('js', new Date());\
                gtag('config', 'UA-153089899-1');"
        return result


if __name__ == "__main__":
    links = [
        ("Email", "mailto:sebastian.cepeda.fuentealba@gmail.com"),
        ('CV',
         "https://docs.google.com/document/d/1pmh6-pwJh98fTAS6WTCZ4L4SEyRNJc3GHv0oRNhewG8/export?format=pdf"),
        ('LinkedIn', "https://www.linkedin.com/in/sebastiancepeda/"),
        ('Google Scholar',
         "https://scholar.google.com/citations?hl=en&user=1ArDfoUAAAAJ"),
    ]
    p = PersonalPage(name="Sebastian Cepeda",
                     google_track_url="https://www.googletagmanager.com/gtag/js?id=UA-153089899-1",
                     links=links,
                     )
    html = p.get_html()
    with open("index.html", "w") as text_file:
        text_file.write(html)
