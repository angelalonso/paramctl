version = "0.053"
"""
Manage accepted parameters through a json file.

- The Json file should look like this:
{ "params": 
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

, where the amount of actions can be 1 to n, and the objects can but must not
  be the same for all actions, depending on how you define your functions.

"""
import paramctl.paramctl as pctl
