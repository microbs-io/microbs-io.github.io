# Standard packages
import binascii
import codecs
import copy
import datetime
import errno
import json
import os
import re
import shutil
import sys
from distutils.dir_util import copy_tree

# Third-party packages
import jinja2
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


META_DESCRIPTION_GENERIC = "microbs is an open source, vendor-inclusive framework to demo, test, or learn about microservices observability."
META_DESCRIPTION_GENERIC_SHORT = "Demo, test, or learn about microservices observability."

RE_NOTE_MESSAGE = (
    r'^\|([\!\?])' # |! or |?
    r'(.*)' # text
    r'$'
)

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader("templates"),
    variable_start_string = "{$",
    variable_end_string = "$}"
)

def plugin_message(md):

    def parse_message(inline, m, state):
        # ``inline`` is ``md.inline``, see below
        # ``m`` is matched regex item
        type = m.group(1)
        text = m.group(2)
        return 'message', 'warning' if type == '!' else 'info', text

    def render_html_message(type, text):
        md = mistune.create_markdown(renderer=MicrobsRenderer(), plugins=[plugin_message])
        return f'<div class="ui {type} message tiny">{md(text)}</div>'

    md.inline.register_rule('message', RE_NOTE_MESSAGE, parse_message)
    md.inline.rules.append('message')
    if md.renderer.NAME == 'html':
        md.renderer.register('message', render_html_message)

class MicrobsRenderer(mistune.HTMLRenderer):

    def block_code(self, code, lang):
        if not lang:
            return "\n<pre><code>%s</code></pre>\n" % mistune.escape(code)
        nocopy = False
        if lang.endswith(":nocopy"):
            lang = lang.split(":")[0]
            nocopy = True
        lexer = get_lexer_by_name(lang, stripall=True)
        id = "a%s" % binascii.hexlify(os.urandom(8))
        formatter = html.HtmlFormatter()
        formatted = highlight(code, lexer, formatter)
        if nocopy:
            formatted = """
            <div class="code">
              <code>
                <span id="%s">%s</span>
              </code>
            </div>
            """ % ( id, formatted )
        else:
            formatted = """
            <div class="code">
              <button class="ui labeled icon button teal tiny" data-clipboard-target="#%s">
                <i class="icon">
                  <span style="font-size:2rem;">&#x2398</span>
                </i>
                Copy to clipboard
               </button>
              <code>
                <span id="%s">%s</span>
              </code>
            </div>
            """ % ( id, id, formatted )
        return formatted

    def heading(self, text, level):
        out = "<h{} class='ui header{}'>{}</h{}>".format(level, ' dividing' if level == 3 else '', text, level)
        return out

    def image(self, src, alt='', title=None):
        out = """
        <a class="image-popup" href="{}" title="{}">
          <img src="{}" style="max-width:100%;" alt="{}"/>
        </a>
        """.format(src, alt, src, alt)
        return out

    def link(self, link, text, title):
        link = mistune.escape(link)
        if not text:
            return "<a name=\"%s\"></a>" % link
        out = "<a href=\"%s\"" % link
        if title:
            out += " title=\"%s\"" % mistune.escape(title, quote=True)
        if not link.startswith("/") and not link.startswith("#") and not link.startswith("https://microbs.io") and not link.startswith("http://microbs.io"):
            out += " onclick=\"to('%s', 'outbound');\"" % link
            out += " class=\"external\""
        elif link.startswith("#"):
            out += " onclick=\"to(window.location.pathname + '%s', 'internal');\"" % link
        out += ">%s</a>" % text
        return out

def fullpath(filename):
    return (os.path.dirname(os.path.abspath(__file__)) + filename).replace("\\", "/")

# Global markdown renderer
md = mistune.create_markdown(renderer=MicrobsRenderer(), plugins=[
    mistune.plugins.plugin_table,
    plugin_message
])

def markdown(filename, args):
    content = ""
    with open(fullpath(filename), "rb") as file:
        content = file.read().decode("utf8")
    markdownEnv = jinja2.Environment(
        loader = jinja2.BaseLoader(),
        variable_start_string = "{$",
        variable_end_string = "$}"
    )
    content = markdownEnv.from_string(content).render(**args)
    return md(content)

def render_page_docs_plugins(plugin_type=None):
    """
    Render the page for /docs/plugins if plugin_type=None,
    or render the page for /docs/plugins/{plugin_type} given a plugin_type.
    """
    content = ""
    if plugin_type is None:
        content += "# Plugins\n\n"
    else:
        content += "# {} plugins\n\n".format(plugin_type.title())
    # Render the plugins lists in a specific order.
    for _type in ( "kubernetes", "observability", "alerts" ):
        for i, (root, dirs, files) in enumerate(os.walk('./docs/plugins')):
            if i == 0:
                continue
            if not plugin_type or root.endswith("/{}".format(plugin_type)):
                type = root.split("/")[-1]
                if type != _type:
                    continue
                if plugin_type is None:
                    content += "## [{}](/docs/plugins/{})\n\n".format(type.title(), type)
                for file in sorted(files):
                    if file == "index.md" or not file.endswith(".md"):
                        continue
                    name = file.rsplit(".md", 1)[0]
                    content += "* [`{}`](/docs/plugins/{}/{})\n".format(name, type, name)
    return md(content)

def PAGES(args):
    return {
        "/": {
            "vars": {
                "title": "Microservices Observability",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "home": True
            }
        },
        "/docs": {
            "vars": {
                "title": "Documentation",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/index.md", args),
                "docs": True
            }
        },
        "/docs/overview": {
            "vars": {
                "title": "Overview",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/overview/index.md", args),
                "docs": True
            }
        },
        "/docs/overview/getting-started": {
            "vars": {
                "title": "Getting Started",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/overview/getting-started.md", args),
                "docs": True
            }
        },
        "/docs/overview/architecture": {
            "vars": {
                "title": "Architecture",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/overview/architecture.md", args),
                "docs": True
            }
        },
        "/docs/overview/concepts": {
            "vars": {
                "title": "Concepts",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/overview/concepts.md", args),
                "docs": True
            }
        },
        "/docs/usage": {
            "vars": {
                "title": "Usage",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/usage/index.md", args),
                "docs": True
            }
        },
        "/docs/usage/configuration": {
            "vars": {
                "title": "Configuration",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/usage/configuration.md", args),
                "docs": True
            }
        },
        "/docs/usage/cli": {
            "vars": {
                "title": "CLI",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/usage/cli.md", args),
                "docs": True
            }
        },
        "/docs/apps": {
            "vars": {
                "title": "Apps",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/apps/index.md", args),
                "docs": True
            }
        },
        "/docs/apps/ecommerce": {
            "vars": {
                "title": "ecommerce",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/apps/ecommerce.md", args),
                "docs": True
            }
        },
        "/docs/apps/templates": {
            "vars": {
                "title": "templates",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/apps/templates.md", args),
                "docs": True
            }
        },
        "/docs/plugins": {
            "vars": {
                "title": "Plugins",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": render_page_docs_plugins(),
                "docs": True
            }
        },
        "/docs/plugins/alerts": {
            "vars": {
                "title": "Alerts plugins",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": render_page_docs_plugins("alerts"),
                "docs": True
            }
        },
        "/docs/plugins/alerts/slack": {
            "vars": {
                "title": "slack plugin",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/plugins/alerts/slack.md", args),
                "docs": True
            }
        },
        "/docs/plugins/alerts/template": {
            "vars": {
                "title": "template plugin",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/plugins/alerts/template.md", args),
                "docs": True
            }
        },
        "/docs/plugins/kubernetes": {
            "vars": {
                "title": "Kubernetes plugins",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": render_page_docs_plugins("kubernetes"),
                "docs": True
            }
        },
        "/docs/plugins/kubernetes/gke": {
            "vars": {
                "title": "gke plugin",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/plugins/kubernetes/gke.md", args),
                "docs": True
            }
        },
        "/docs/plugins/kubernetes/kind": {
            "vars": {
                "title": "kind plugin",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/plugins/kubernetes/kind.md", args),
                "docs": True
            }
        },
        "/docs/plugins/kubernetes/minikube": {
            "vars": {
                "title": "minikube plugin",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/plugins/kubernetes/minikube.md", args),
                "docs": True
            }
        },
        "/docs/plugins/kubernetes/template": {
            "vars": {
                "title": "template plugin",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/plugins/kubernetes/template.md", args),
                "docs": True
            }
        },
        "/docs/plugins/observability": {
            "vars": {
                "title": "Observability plugins",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": render_page_docs_plugins("observability"),
                "docs": True
            }
        },
        "/docs/plugins/observability/elastic_cloud": {
            "vars": {
                "title": "elastic_cloud plugin",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/plugins/observability/elastic_cloud.md", args),
                "docs": True
            }
        },
        "/docs/plugins/observability/grafana_cloud": {
            "vars": {
                "title": "grafana_cloud plugin",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/plugins/observability/grafana_cloud.md", args),
                "docs": True
            }
        },
        "/docs/plugins/observability/template": {
            "vars": {
                "title": "template plugin",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/plugins/observability/template.md", args),
                "docs": True
            }
        },
        "/docs/development": {
            "vars": {
                "title": "Development",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/development/index.md", args),
                "docs": True
            }
        },
        "/docs/development/apps": {
            "vars": {
                "title": "App Development",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/development/apps.md", args),
                "docs": True
            }
        },
        "/docs/development/plugins": {
            "vars": {
                "title": "Plugin Development",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/development/plugins.md", args),
                "docs": True
            }
        },
        "/docs/development/versioning": {
            "vars": {
                "title": "Versioning",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/development/versioning.md", args),
                "docs": True
            }
        },
        "/docs/development/contributing": {
            "vars": {
                "title": "Contributing",
                "meta_description": META_DESCRIPTION_GENERIC,
                "meta_description_social": META_DESCRIPTION_GENERIC_SHORT,
                "content": markdown("/docs/development/contributing.md", args),
                "docs": True
            }
        }
    }

def wipe_build_dir():
    filepath = fullpath("/build")
    print("Wiping build directory: {}".format(filepath))
    return shutil.rmtree(filepath)

def copy_assets_dir():
    filepath_from = fullpath("/assets")
    filepath_to = fullpath("/build")
    print("Copying assets from: {}".format(filepath_from))
    return copy_tree(filepath_from, filepath_to)

def write_page(uri_path, content):
    filepath = fullpath("/build" + uri_path + "/index.html")
    # Ensure any subdirectories are created
    try:
        os.makedirs(os.path.dirname(filepath))
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise
    print("Writing file: {}".format(filepath))
    with codecs.open(filepath, "wb", "utf-8") as file:
        file.write(content)

def build_page(uri_path, page, args={}):
    template = env.get_template(page.get("template", "base.html"))
    vars = copy.deepcopy(page["vars"])
    vars.update(args)
    vars.update({ "now": datetime.datetime.utcnow() })
    vars['path'] = uri_path
    return env.get_template(template).render(**vars)

def build_pages(pages, args={}):
    for uri_path, page in pages.items():
        print("Building page: {}".format(uri_path))
        content = build_page(uri_path, page, args)
        write_page(uri_path, content)

def build(args={}):
    pages = PAGES(args)
    wipe_build_dir()
    copy_assets_dir()
    build_pages(pages, args)

if __name__ == "__main__":
    args = {}
    args["test"] = False
    for arg in sys.argv[1:]:
        if arg == "--test":
            args["test"] = True
    print(args)
    build(args)
