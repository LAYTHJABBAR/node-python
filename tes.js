const { spawn } = require('child_process')

const python = spawn('python3', ['script4.py', 1])

// collect data from script
python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...', data)
  //dataToSend =  data;

})