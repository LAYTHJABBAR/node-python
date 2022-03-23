const express = require('express')
const { spawn } = require('child_process')
const app = express()
const port = 4000
app.use(express.urlencoded({extended: true}));
app.use(express.json())


app.get('/', (req, res) => {
  let dataToSend
  let largeDataSet = []
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
})

app.post('/data', (req,res) => {
 console.log(req.body)
  res.send({message: 'data posted'})
})

app.listen(port, () => {
  console.log(`App listening on port ${port}!`)
})
