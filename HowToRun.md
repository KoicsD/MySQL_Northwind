If you want to try my program, the easiest way is to use command-line:
* Create a directory named Resources, and copy the necessary files to it.
* Enter directory Resources in command line, and type:

```
ProjectRoot\Resources> set PYTHONPATH=..\PythonSource
ProjectRoot\Resources> python ..\PythonSource\main.py

```

If you want to use PyCharm:
* Make sure, this directory Resources is set as working directory in [run configurations](https://www.jetbrains.com/help/pycharm/2016.1/run-debug-configurations.html)
* Also make sure, PythonSource is marked as [source root](https://www.jetbrains.com/help/pycharm/2016.1/content-root.html)
* Then you can start my program, but my menu won't work properly in PyCharm's console.

[Here you can find how to set run configurations in PyCharm.](https://www.jetbrains.com/help/pycharm/2016.1/creating-and-editing-run-debug-configurations.html)  
[Here you can find how to configure content root in PyCharm.](https://www.jetbrains.com/help/idea/2016.1/configuring-content-roots.html)
