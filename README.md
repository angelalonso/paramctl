# paramctl
A Python library to match positional parameters based on a json file

When integrated properly to your script, you should be able to trigger actions like this:  
```script.py action object extra_parameter_1 extra_parameter_n```

## Installation
```pip3 install paramctl```

## Requirements
This thing obviously needs json. 

## How does it work
You will need a Json file to define the accepted actions and objects  

The Json file should look like this:
```{ "params": 
    {"action1":
      { "object_a": {
        "help": "Description for what action1 does to object_a",
        "action": "the_name_of_your_function_for_action1_on_object_a"
        },
        "object_b": {
        "help": "Description for what action1 does to object_b",
        "action": "the_name_of_your_function_for_action1_on_object_b"
        }
      },
     "action2":
      { "object_a": {
        "help": "Description for what action2 does to object_a",
        "action": "the_name_of_your_function_for_action2_on_object_a"
        },
        "object_y": {
        "help": "Description for what action2 does to object_y",
        "action": "the_name_of_your_function_for_action2_on_object_y"
        }
      }
  }
}
```
, where the amount of actions is -sort-of- unlimited, and any object can but does not have to
  belong under several actions.  


On your python code (e.g.: myscript.py) add the following:
```
import paramctl

params = paramctl.ParameterMap("parametermap.json") # or whatever you call your json file
try:
    print(globals()[function[0]](function[1:]))
except KeyError:
    print("No function available like " + " ".join(function[:]))

```
, finally, create the functions defined on the json file (under "action") like this: 
```
def get_nodes(*argv):
    ...
```
...and manage the arguments passed (as a tuple) as you please.
