# calculer-clean
A varsity letter award point calculator website I built for my school.
This has been stripped of all potentially identifying information but is otherwise the same as the original.

The code in this project doesn't meet my quality standards as it was built in a very short timeframe but I think it should be shared anyways.
For better code, see https://github.com/TK421bsod/maximilian or https://github.com/TK421bsod/interessant.

## how it works
This site uses a crude component system for managing most page elements.
Components are Bootstrap rows containing 3 col-md-2 columns and a horizontal rule.
The page iterates through an array of components at runtime (`load` listener) and adds them to the `main-form` element.

To add new components, run generate_components.py and follow the instructions.
Then, add the generated JSON to the array `COMPONENTS` in index.html.
Reload, and your components should show up.
