# Importing

Terms

1. A **module** is simply Python code in a separate file.
2. A **package** is the path to a directory that contains modules, which is also a special type of module.
3. `__init__.py` is the default file for a package.
4. A **submodule** is another file in a module's folder.
5. A **function** is (obviously!) a function in a module.

More Simply

1. File == Module
2. Folder == Package
3. Folder with files in it == Module & Package
4. `__init__.py` == Main file in a folder (package)
5. `otherFiles.py` == Submodules

A single file is a module because a single file can contain everything we need a module to do.

It's often nice to organize large files into multiple smaller files

If you want all those files to act as a single module, put them in a folder with a `__init__.py`

- This is similar to how some of you managed components in React, or your store in Redux

  - Your store was made up of multiple smaller files, then an `index.js` collected those smaller file's functions
  - We only have to import the folder's name and the `index.js` gets imported

```js
// src/store/index.js
import sessionReducer from './session.js'; // These are submodules
import spotsReducer from './spots.js'; // These are submodules
import reviewsReducer from './reviews.js'; // These are submodules
import bookingsReducer from './bookings.js'; // These are submodules

const rootReducer = combineReducers(...)
const configureStore = () => ...

export default configureStore;
```

Here our `src/store/index.js` is acting as our `__init__.py`

Then inside your app's index.js

```js
// src/index.js
import configureStore from './store'; // This is a package & module

const store = configureStore();
```

Examples

1. `import <module>` - most basic
2. `import <package>.<subpackage>.<module>` - dot syntax
3. `from <package> import <module>` - one module in a package
4. `from <package> import <module>, <module>` - multiple modules or submodules in a package
5. `from . import <submodule>` - special case for module's **init**.py to get submodules in the same folder
6. `from <module> import <function>, <function>` - down to the function level
7. `from <package> import <module> as <altName>` - renaming to avoid confusion or conflict
