const express = require('express');
const app = express();
const path = require('path');

app.use('/css', express.static('assets/css'));
app.use('/pics', express.static('assets/images'));
app.use('/js', express.static('assets/scripts'));


app.get('/spots', (req, res) => {
res.json({"Spots": ["Disney World", "Spot 2", "Spot 3"]});
})

// app.use(express.static('./'));



const port = 5000;
app.listen(port, () => console.log('Server is listening on port', port));




// app.get('/test', (req, res) => {
//     res.status(201).sendFile(path.join(__dirname, 'assets/images/hello.png'));
// });

// //* Solution to practice below :)
// app.use('/stylesheets', express.static('assets/css'));

// //! Step 2
// // app.use('/', express.static('assets'));

// //! Step 3
// app.use(express.static('assets/scripts'));

// //! Step Bonus
// //? URL: /stickers/hello.png
// // app.use('/stickers', express.static('assets/images'));
// //? URL: /sticker
// app.use('/sticker', express.static('assets/images/hello.png'));
