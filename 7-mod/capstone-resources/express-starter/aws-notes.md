Frontend:

1. build out the splash page

```jsx
import React, { useState } from 'react';
import { updateUserThunk } from '../../redux/session';
import { useDispatch, useSelector } from 'react-redux';

const Splash = () => {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user)

  //image url to send to aws
  const [imgUrl, setImgUrl] = useState("");
  //telling us if we should show the image
  const [showUpload, setShowUpload] = useState(true);
  //img url we will load in react
  const [previewUrl, setPreviewUrl] = useState("");



  //function to get image from local

  const updateImage = async (e) => {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = (e) => {
      setPreviewUrl(reader.result);
    }
    setImgUrl(file);
    setShowUpload(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const img_url = imgUrl;
    const form = {img_url};
    const updateUser = await dispatch(updateUserThunk(user.id, form))
  }



  return (
    <div>
        <h1>Welcome</h1>
        <form onSubmit={handleSubmit}>
          <div>
            {showUpload && (
              <label htmlFor='file-upload'> Select From Computer
                <input
                  type='file'
                  id='file-upload'
                  name="img_url"
                  onChange={updateImage}
                  accept='.jpg, .jpeg, .png, .gif'
                  />
                </label>
            )}
            {!showUpload && (
              <div>
                <img
                  src={previewUrl}
                  alt="preview"
                />
                <button>Change Profile</button>
              </div>
            )}
          </div>
        </form>
    </div>
  );
}

export default Splash;


```

2. build out the navigation component

```jsx
import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { useSelector } from "react-redux";

function Navigation() {
  const user = useSelector((state) => state.session.user);


  return (
    <ul>
      <li>
        <NavLink to="/">Home</NavLink>
      </li>

      <li>
        <ProfileButton />
      </li>
      {user && (
        <li>
          {user.profileImg?
          <img
            src={user.profileImg}
            style={{height: "70px", width: '70px', borderRadius: "50%"}}
          />: null}
        </li>
      )}
    </ul>
  );
}

export default Navigation;

```

3. update csrfFetch to have multipart

```js
import Cookies from 'js-cookie';


export async function csrfFetch(url, options) {
    // set options.method to 'GET' if there is no method
    if (options) {
        options.method = options.method || 'GET';
        // set options.headers to an empty object if there is no headers
        options.headers = options.headers || {};

        // if the options.method is not 'GET', then set the "Content-Type" header to
        // "application/json", and set the "XSRF-TOKEN" header to the value of the
        // "XSRF-TOKEN" cookie
        if (options.method.toUpperCase() !== 'GET') {
            if(options.headers["Content-Type"] === "multipart/form-data"){
                delete options.headers["Content-Type"];
            }else {

                options.headers['Content-Type'] =
                options.headers['Content-Type'] || 'application/json';
            }
            options.headers['XSRF-Token'] = Cookies.get('XSRF-TOKEN');
        }
    }
    // call the default window's fetch with the url and the options passed in
    const res = await window.fetch(url, options);

    // if the response status code is 400 or above, then throw an error with the
    // error being the response
    if (res.status >= 400) throw res;

    // if the response status code is under 400, then return the response to the
    // next promise chain
    return res;
}

export function restoreCSRF() {
    return csrfFetch('/api/csrf/restore');
}

```


4. build redux thunk with aws formData and correct headers
```js
export const updateUserThunk = (userId, form) => async (dispatch) => {
    const { img_url } = form
    try{

        const formData = new FormData();

        formData.append('userId', userId)
        formData.append("image", img_url);

        const option = {
            method: "PUT",
            headers: { 'Content-Type': 'multipart/form-data' },
            body: formData
        }

        const response = await csrfFetch(`/api/users/${userId}/update`, option);
        if (response.ok) {
            const user = await response.json();
            dispatch(editUser(user));

        } else if (response.status < 500) {
            const data = await response.json();
            if (data.errors) {
                return data
            } else {
                throw new Error('An error occured. Please try again.')
            }
        }
        return response;
    } catch(e){
        return e
    }
}

```

Backend:

1. Install: aws-sdk and multer
```sh
npm install aws-sdk multer
```
2. Make awsS3.js file (copy and paste)

```js
const AWS = require("aws-sdk");
// name of your bucket here
const NAME_OF_BUCKET = process.env.AWS_BUCKET_NAME
const multer = require("multer");

//  make sure to set environment variables in production for:
//  AWS_ACCESS_KEY_ID
//  AWS_SECRET_ACCESS_KEY
//  and aws will automatically use those environment variables

const s3 = new AWS.S3({ apiVersion: "2006-03-01" });

// --------------------------- Public UPLOAD ------------------------

const singlePublicFileUpload = async (file) => {
    const { originalname, mimetype, buffer } = await file;
    const path = require("path");
    // name of the file in your S3 bucket will be the date in ms plus the extension name
    const Key = new Date().getTime().toString() + path.extname(originalname);
    const uploadParams = {
        Bucket: NAME_OF_BUCKET,
        Key,
        Body: buffer,
        ACL: "public-read",
    };
    const result = await s3.upload(uploadParams).promise();

    // save the name of the file in your bucket as the key in your database to retrieve for later
    return result.Location;
};

const multiplePublicFileUpload = async (files) => {
    return await Promise.all(
        files.map((file) => {
            return singlePublicFileUpload(file);
        })
    );
};

// --------------------------- Prviate UPLOAD ------------------------

const singlePrivateFileUpload = async (file) => {
    const { originalname, mimetype, buffer } = await file;
    const path = require("path");
    // name of the file in your S3 bucket will be the date in ms plus the extension name
    const Key = new Date().getTime().toString() + path.extname(originalname);
    const uploadParams = {
        Bucket: NAME_OF_BUCKET,
        Key,
        Body: buffer,
    };
    const result = await s3.upload(uploadParams).promise();

    // save the name of the file in your bucket as the key in your database to retrieve for later
    return result.Key;
};

const multiplePrivateFileUpload = async (files) => {
    return await Promise.all(
        files.map((file) => {
            return singlePrivateFileUpload(file);
        })
    );
};

const retrievePrivateFile = (key) => {
    let fileUrl;
    if (key) {
        fileUrl = s3.getSignedUrl("getObject", {
            Bucket: NAME_OF_BUCKET,
            Key: key,
        });
    }
    return fileUrl || key;
};

// --------------------------- Storage ------------------------

const storage = multer.memoryStorage({
    destination: function (req, file, callback) {
        callback(null, "");
    },
});

const singleMulterUpload = (nameOfKey) => //'image' comes in
    multer({ storage: storage }).single(nameOfKey);
const multipleMulterUpload = (nameOfKey) =>
    multer({ storage: storage }).array(nameOfKey);

module.exports = {
    s3,
    singlePublicFileUpload,
    multiplePublicFileUpload,
    singlePrivateFileUpload,
    multiplePrivateFileUpload,
    retrievePrivateFile,
    singleMulterUpload,
    multipleMulterUpload,
};

```

3. complete AWS set up online
    - get AWS user API key and use it in .env
    - make a bucket and use the name in .env
    - get AWS user secret key and add it to .env

4. Make route using aws middleware:


```js
router.put('/:id/update', singleMulterUpload('image'), async (req, res, next) => {
    try{
        const {userId} = req.body;
        let user;

        if(userId){
            user = await User.findByPk(userId);
        } else{
            throw new Error("No user founder with that id")
        }

        let imgUrl;

        if(req.file){
            imgUrl = await singlePublicFileUpload(req.file); //converts data from form
        }
        user.profileImg = imgUrl;
        await user.save();
        return res.json(user)

    }catch(e){
        next(e)
    }

})


```

note: notice we have to pass in a string of what the name of our file in formData is, and then pass it into aws middleware to parse for us. Then we can use `singlePublicFileUpload` to upload 1 image to aws


Frontend (again)

1. Complete Action type
2. Make a reducer


Enjoy 😄
