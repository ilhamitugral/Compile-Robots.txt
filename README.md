# Robots.txt Compiler
Formats the rules in robots.txt by formatting them. Tested on Python 3.

## How To Use?
Open `cmd` or `terminal` and execute this command;

```
compile_robots.py [website]
```

And this script returns; **allowed sites**, **disallowed sites** and **sitemaps**

`status`: Robots.txt status (str)\
`blacklist`: Disallowed sites. (list)\
`whitelist`: Allowed sites (list)

For Example:

```
python3 compile_robots.py https://github.com
```

And Result:
```python
{
    'status': 'success',
    'sitemap': [],
    'blacklist': ['/*/pulse', '/*/tree/', '/*/wiki*', '/gist/', '/*/forks', '/*/stars', '/*/download', '/*/revisions', '/*/issues/new', '/*/issues/search', '/*/commits/', '/*/commits/*?author', '/*/commits/*?path', '/*/branches', '/*/tags', '/*/contributors', '/*/comments', '/*/stargazers', '/*/archive/', '/*/blame/', '/*/watchers', '/*/network', '/*/graphs', '/*/raw/', '/*/compare/', '/*/cache/', '/.git/', '*/.git/', '/*.git$', '/search/advanced', '/search', '*/search', '/*q=', '/*.atom', '/ekansa/Open-Context-Data', '/ekansa/opencontext-*', '*/tarball/', '*/zipball/', '/*source=*', '/*ref_cta=*', '/*plan=*', '/*return_to=*', '/*ref_loc=*', '/*setup_organization=*', '/*source_repo=*', '/*ref_page=*', '/*referrer=*', '/*report=*', '/*author=*', '/*since=*', '/*until=*', '/*commits?author=*', '/*report-abuse?report=*', '/*tab=*', '/account-login', '/Explodingstuff/'],
    'whitelist': []
}
```

You can edit `compile_robots.py`.
For Example:
```python
robots = ["*", "Google-Bot"]
```
