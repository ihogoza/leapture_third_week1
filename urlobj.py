from urlobject import URLObject

url = URLObject("https://github.com/zacharyvoase/urlobject?spam=eggs#foo")
print(url)
# https://github.com/zacharyvoase/urlobject?spam=eggs#foo
print(url.scheme)
# https
print(url.netloc)
# github.com
print(url.hostname)
# github.com
print(url.username, url.password)
# (None, None)
print(url.port)
# None
print(url.default_port)
# 443
print(url.path)
# /zacharyvoase/urlobject
print(url.query)
# spam=eggs
print(url.fragment)
# foo
print(url.with_scheme('http'))
print(url.with_netloc('example.com'))
print(url.with_auth('alice', '1234'))
print(url.with_path('/some_page'))
print(url.with_query('funtimes=yay'))
print(url.with_fragment('example'))
# For the query and fragment, without_ methods also exist:
print(url.without_query())
print(url.without_fragment())

# You can resolve relative URLs against a URLObject using relative():
print(url.relative('another-project'))
print(url.relative('?different-query-string'))
print(url.relative('#frag'))

# paths
print(url.path)
print(url.path.parent)
print(url.path.segments)
print(url.path.add_segment('subnode'))
print(url.path.root)

# Some of these are aliased on the URL itself:
print(url.parent)
print(url.add_path_segment('subnode'))
print(url.add_path('tree/urlobject2'))
print(url.root)
