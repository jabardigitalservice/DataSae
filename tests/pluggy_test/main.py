import pluggy
# from datasae.datasource.google import GoogleSheet

hookspec = pluggy.HookspecMarker("datasae-data-quality-framework")
hookimpl = pluggy.HookimplMarker("datasae-data-quality-framework")


@hookspec
def myhook(self, arg1, arg2):
    """My special little hook that you can customize."""


@hookimpl
def myhook_change(arg1, arg2):
    print("inside Plugin_1.myhook()")
    return arg1 + arg2


# create a manager and add the spec
pm = pluggy.PluginManager("myhook")
pm.add_hookspecs(myhook)
# register plugins
pm.register(myhook_change())
# call our `myhook` hook
results = pm.hook.myhook(arg1=1, arg2=2)
print(results)
