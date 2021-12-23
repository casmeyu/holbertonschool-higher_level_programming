#!/usr/bin/python3
import hidden_4
import site
print(site.USER_SITE)
print(site.USER_BASE)
print(site.PREFIXES)

from modulefinder import ModuleFinder

finder = ModuleFinder()
finder.run_script("hidden_4.pyc")

print('Loaded modules:')
for name, mod in finder.modules.items():
    print('%s: ' % name, end='')
    print(','.join(list(mod.globalnames.keys())[:3]))
