# ⏱️ `simpler_timer`: a simple interactive-first timer for all your Python timekeeping needs 
# ❗️ TL;DR - for the impatient...
```py
from simpler_timer import SimplerTimer
timer = SimplerTimer()
timer.end()
```
Simple as that. Batteries included - no dependencies required. 🔋

# ⬇️ Installation
Simply `pip install`
```sh
$ pip install simpler_timer
```

For development version
```sh
$ git clone https://github.com/prince-ravi-leow/simpler_timer.git && cd simpler_timer/
$ pip install -e .
```

# ⚡️ Simple usage
Say you want to time a simple operation. 

First, import:
```py
from simpler_timer import SimplerTimer
```
Simply create a `SimplerTimer` object, run your operation(s), and call `.end()` to stop the timer and return elapsed time in seconds.

From there, use the `.report()` method to print a nicely formatted timestamp.
```py 
>>> timer = SimplerTimer()
>>> some_operation()
>>> some_other_operation()
>>> timer.end()
0:00:15.005237
>>> timer.report()
Elapsed time (H:MM:SS.ff): 0:00:15.005237
```

Want to recall the non-formatted time in seconds? *Easy*:
```py
>>> elapsed_time = timer.recall()
>>> elapsed_time
15.005237
```

# 🍬 Other goodies
## Monitor timer status / progress
Use `.status` attribute or Boolean evaluation with `.is_active()` method:
```py
>>> timer = SimplerTimer()
>>> timer.is_active()
True
>>> timer.end()
>>> timer.status
'Inactive'
```
Get progress readout of active timer:

```py
>>> timer.start()
>>> timer.progress()
2.3714890480041504
>>> timer.progress()
5.502876043319702
>>> timer.progress()
13.753906011581421
```
## Pause / resume
Does what it says on the tin:
```py
>>> timer = SimpleTimer()
>>> timer.pause()
>>> timer.is_active()
True
>>> timer.resume()
>>> timer.status
'Active (resumed)'
```
> *Note that pausing/resuming affects `.status` attribute, but `.is_active()` evaluates as `True`.*
## Timestamps for humans
Tired of reporting execution times with a bazillion decimal places?

Worry no more - use `strip = True` to purge those pesky trailing digits with extreme prejudice.
```py
>>> timer.end()
31.928856
>>> timer.report(strip = True)
'Elapsed time (H:MM:SS): 0:00:31'
>>> timer.timestamp(strip = True)
0:00:31
```
> *Currently only works for inactive timer with `.report()` and `.timestamp()` methods*.

# ⛔️ What this tool is *not* (...or more specifically what it *is*)
This is *not* a command line utility.

I originally designed the `SimplerTimer` class for use in Python scripts / pipelines, where execution time could be calculated and reported in 2 short, ultra-readable statements. However, it tends to work great for interactive sessions, as having a single 'timer' object saves the headache of having to keep track of multiple intermediate variables. 

While it's great for use within scripts and interactive sessions, this tool does not support being run FROM a CLI - and it most likely never will. Reason for this, is that the most simple and reliable version of this already exists in the the UNIX utility [`/usr/bin/time`](https://medium.com/hackernoon/usr-bin-time-not-the-command-you-think-you-know-34ac03e55cc3). If you want a proper **benchmarking** tool, Python's own [`timeit`](https://docs.python.org/3/library/timeit.html) will serve you well - and works both in interactive sessions, and as a command line utility. 

Honourable mention to `PowerShell` [`Measure-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/measure-command?view=powershell-7.4) for our Windows friends.

🐣 *Pssst - as an easter-egg, I've included the function that inspired this project: `simplerer_timer()`. This is an ultra-stripped down implementation, if all you want is a timer that starts, stops and reports elapsed time (inspect docstrings for usage)* 
