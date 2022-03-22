const { spawn } = require('child_process')

const getData = (req, res) => {
    console.log(req.params)
    let dataToSend
    let largeDataSet = [];
    const  pc  = require('child_process');
    // spawn new child process to call the python script
    const python = spawn('python3', ['script3.py'])
  
    // collect data from script
    python.stdout.on('data', function (data) {
      console.log('Pipe data from python script ...')
      //dataToSend =  data;
      largeDataSet.push(data)
    })
  
    // in close event we are sure that stream is from child process is closed
    python.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`)
      // send data to browser
      res.send(largeDataSet.join(''))
    })
  }

  export default {getData}