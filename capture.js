const Webcam = require("node-webcam");
const fs = require("fs");
const { mkdirp } = require('mkdirp')
const delayMilliseconds = 60000;

// Options for the webcam
const opts = {
    width: 1280,
    height: 720,
    quality: 100,
    delay: 0,
    saveShots: true,
    output: "jpeg",
    device: false,
    callbackReturn: "location",
    verbose: false
};

// Create a webcam instance
const webcam = Webcam.create(opts);

// Directory to store images
const dir = './captured_photos';

// Create directory if it doesn't exist
// return value is a Promise resolving to the first directory created
mkdirp(dir).then(made =>
  console.log(`made directories, starting with ${made}`)
)

// Function to capture an image
function captureImage() {
    const timestamp = Date.now();
    const filename = `${dir}/photo_${timestamp}.jpg`;

    webcam.capture(filename, function(err, data) {
        if (err) console.error(err);
        else console.log(`Image saved: ${filename}`);
    });
}

// Capture an image every x milliseconds.
setInterval(captureImage, delayMilliseconds);
